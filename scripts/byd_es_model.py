"""Illustrative model of the BYD behind-the-meter battery project.

Everything here is synthetic and normalized, so no project data is disclosed:
  * plant load = 1.0 (a flat load with small synthetic fluctuations),
  * battery = 4 hours of plant load, charge <= 0.5, discharge <= 2/3,
  * prices are relative to the flat time-of-use tier (= 1.0).

Three strategies are compared on one representative day for each month type:
  static   - the original operating rule: fixed time blocks, reserve held all year;
  dynamic  - the simplified rules proposed to operators (reserve only in Jul-Aug,
             extra critical-peak discharge, use the optional blocks);
  optimal  - a day-ahead linear program that minimizes the electricity bill,
             including the demand charge, with perfect load forecasts.

Run:  python scripts/byd_es_model.py
Writes assets/js/byd-es-data.js, used by the project page.
"""

import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

DT = 0.25                    # hours per slot
T = 96                       # 15-minute slots per day
HOURS = np.arange(T) * DT

E_MAX = 4.0                  # battery energy, in hours of plant load
P_CH = 0.5                   # charge limit (x plant load)
P_DIS = 2 / 3                # discharge limit (x plant load)
P_DIS_CRIT = 1.0             # allowed discharge in critical-peak hours
ETA = 0.94                   # one-way efficiency
STATIC_RESERVE = 0.20 * E_MAX
SUMMER_RESERVE = 0.17 * E_MAX

PRICE = {"valley": 0.48, "flat": 1.0, "peak": 1.5, "critical": 1.77}
PRICE_VOLUME = 0.16          # per-kWh network charge
DEMAND_PER_DAY = 1.58        # monthly demand charge spread over one day

MONTHS = {
    "other": {"label": "Spring and autumn", "critical": False, "summer": False},
    "winter": {"label": "Winter (critical peak)", "critical": True, "summer": False},
    "summer": {"label": "July and August", "critical": True, "summer": True},
}


def tier(h, critical):
    if h < 8:
        return "valley"
    if h < 11 or 17 <= h < 20 or h >= 22:
        return "flat"
    if critical and 12 <= h < 14:
        return "critical"
    return "peak"


def synthetic_load(seed=7):
    """Flat plant load with mild noise and short dips at shift changes."""
    rng = np.random.default_rng(seed)
    load = 0.97 + 0.02 * rng.standard_normal(T)
    for start in (7.5, 15.5, 23.5):
        load[(HOURS >= start) & (HOURS < start + 0.5)] -= 0.12
    return np.clip(load, 0.8, 1.0)


def discharge_limit(h, month, strategy):
    if strategy != "static" and month["critical"] and 12 <= h < 14:
        return P_DIS_CRIT
    return P_DIS


def reserve(month, strategy):
    if strategy == "static":
        return STATIC_RESERVE
    return SUMMER_RESERVE if month["summer"] else 0.0


def run_rules(month, strategy):
    floor = reserve(month, strategy)
    soc = E_MAX / 2
    for _ in range(4):                       # repeat until the day is periodic
        p, s = np.zeros(T), np.zeros(T + 1)
        s[0] = soc
        for t, h in enumerate(HOURS):
            if strategy == "static":
                charge = h < 8 or 17 <= h < 20
                discharge = 11 <= h < 17 or 20 <= h < 22
            else:
                charge = h < 11 or 17 <= h < 20
                discharge = 11 <= h < 17 or h >= 20
            if charge:
                p[t] = max(0.0, min(P_CH, (E_MAX - soc) / (ETA * DT)))
                soc += ETA * p[t] * DT
            elif discharge:
                lim = discharge_limit(h, month, strategy)
                p[t] = -max(0.0, min(lim, (soc - floor) * ETA / DT))
                soc += p[t] / ETA * DT
            s[t + 1] = soc
    return p, s


def run_optimal(month, load):
    """LP: variables [p_ch(T), p_dis(T), soc(T+1), peak]."""
    floor = reserve(month, "optimal")
    price = np.array([PRICE[tier(h, month["critical"])] for h in HOURS])
    n = 3 * T + 2
    ich, idis, isoc, ipk = 0, T, 2 * T, 3 * T + 1

    c = np.zeros(n)
    c[ich:ich + T] = (price + PRICE_VOLUME) * DT + 1e-4
    c[idis:idis + T] = -(price + PRICE_VOLUME) * DT + 1e-4
    c[ipk] = DEMAND_PER_DAY

    a_eq, b_eq = [], []
    for t in range(T):                       # state-of-charge balance
        row = np.zeros(n)
        row[isoc + t + 1], row[isoc + t] = 1, -1
        row[ich + t], row[idis + t] = -ETA * DT, DT / ETA
        a_eq.append(row)
        b_eq.append(0)
    row = np.zeros(n)                        # end the day where it started
    row[isoc], row[isoc + T] = 1, -1
    a_eq.append(row)
    b_eq.append(0)

    a_ub, b_ub = [], []
    for t in range(T):                       # peak >= net load
        row = np.zeros(n)
        row[ich + t], row[idis + t], row[ipk] = 1, -1, -1
        a_ub.append(row)
        b_ub.append(-load[t])

    bounds = ([(0, P_CH)] * T
              + [(0, discharge_limit(h, month, "optimal")) for h in HOURS]
              + [(floor, E_MAX)] * (T + 1) + [(0, None)])
    res = linprog(c, A_ub=a_ub, b_ub=b_ub, A_eq=a_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    assert res.status == 0, res.message
    x = res.x
    return x[ich:ich + T] - x[idis:idis + T], x[isoc:isoc + T + 1]


def bill(month, load, p):
    price = np.array([PRICE[tier(h, month["critical"])] for h in HOURS])
    net = load + p
    energy = float(np.sum(price * net) * DT)
    volume = float(np.sum(net) * DT * PRICE_VOLUME)
    demand = float(net.max() * DEMAND_PER_DAY)
    return {"energy": energy, "volume": volume, "demand": demand,
            "total": energy + volume + demand}


def main():
    load = synthetic_load()
    out = {"hours": HOURS.tolist(), "load": np.round(load, 4).tolist(),
           "E_max": E_MAX, "months": {}}
    for key, month in MONTHS.items():
        base = bill(month, load, np.zeros(T))
        entry = {"label": month["label"],
                 "tiers": [tier(h, month["critical"]) for h in HOURS],
                 "strategies": {}}
        results = {
            "static": run_rules(month, "static"),
            "dynamic": run_rules(month, "dynamic"),
            "optimal": run_optimal(month, load),
        }
        static_saving = base["total"] - bill(month, load, results["static"][0])["total"]
        for name, (p, s) in results.items():
            b = bill(month, load, p)
            discharged = float(-np.sum(np.minimum(p, 0)) * DT / ETA)
            entry["strategies"][name] = {
                "power": np.round(p, 4).tolist(),
                "soc": np.round(s / E_MAX, 4).tolist(),
                "reserve": reserve(month, name) / E_MAX,
                "cycles": round(discharged / E_MAX, 3),
                "saving_index": round(100 * (base["total"] - b["total"]) / static_saving, 1),
                "peak": round(float((load + p).max()), 3),
                "bill_change": {k: round(100 * (b[k] - base[k]) / base["total"], 2)
                                for k in ("energy", "volume", "demand", "total")},
            }
        out["months"][key] = entry

    target = Path(__file__).resolve().parents[1] / "assets" / "js" / "byd-es-data.js"
    target.write_text("// Generated by scripts/byd_es_model.py. Synthetic, normalized data.\n"
                      "window.BYD_ES_DATA = " + json.dumps(out, separators=(",", ":")) + ";\n")
    for key, entry in out["months"].items():
        for name, r in entry["strategies"].items():
            print(f"{key:7s} {name:8s} idx={r['saving_index']:6.1f} cyc={r['cycles']:.3f} "
                  f"peak={r['peak']:.3f} bill={r['bill_change']}")
    print("wrote", target)


if __name__ == "__main__":
    main()
