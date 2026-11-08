---
title: "Industrial Energy Management System Implementation"
excerpt: "An implemented optimization strategy coordinating a 60 MW manufacturing load, a 60 MW/240 MWh battery, and 10 MW of solar generation."
collection: portfolio
order: 4
permalink: /projects/industrial-energy-management/
redirect_from:
  - /portfolio/portfolio-1/
teaser: /images/port1.jpg
teaser_alt: "Ruike Lyu discussing the industrial energy-management system with on-site engineers"
category_label: "Implementation"
---

<link rel="stylesheet" href="{{ '/assets/css/byd-es.css' | relative_url }}">

<figure class="byd-es-figure">
  <img src="{{ '/images/port1.jpg' | relative_url }}" alt="Ruike Lyu and an on-site engineer reviewing the monitoring screens in the control room">
  <figcaption>Reviewing the system's operating data with an on-site engineer in the control room.</figcaption>
</figure>

## The problem

Large manufacturing facilities increasingly combine complex production loads with on-site generation and battery storage. Coordinating these resources requires an operating strategy that can reduce electricity costs without disrupting production.

## What I implemented

As implementation lead, I developed and implemented an optimization strategy for a BYD battery manufacturing plant in Chongqing. The system coordinated:

- a 60 MW manufacturing load;
- a 60 MW/240 MWh battery energy storage system; and
- 10 MW of solar generation.

The work was conducted with the State Power Investment Corporation and the manufacturing plant, linking production operations with the scheduling of distributed energy resources.

<figure class="byd-es-figure">
  <img src="{{ '/images/byd-es/system.svg' | relative_url }}" alt="Diagram of the grid, revenue meter, plant load, battery, and rooftop solar behind the meter">
</figure>

A two-minute explainer of the project (all charts use a synthetic plant):

{% include youtube.html id="x0Zmy_rP5Uo" title="Scheduling a battery behind a factory's meter" %}

## Why the operating problem is hard

The battery sits behind the plant's revenue meter, so it is never scheduled on its own: every kilowatt it charges or discharges adds to or subtracts from the plant's load, and the plant pays for the combined result. The savings are shared between the plant and the battery operator. The time-of-use tariff alone would say "fill the battery in every valley, empty it in every peak", which allows about two cycles a day. Several other pressures pull the schedule in different directions:

<table class="byd-es-table byd-es-table--text">
  <thead>
    <tr><th>Pressure</th><th>What it asks of the battery</th><th>Why it conflicts</th></tr>
  </thead>
  <tbody>
    <tr><td>Time-of-use prices</td><td>Charge fully when power is cheap; discharge fully when it is expensive</td><td>This is the source of value, and every other pressure limits it</td></tr>
    <tr><td>Demand charge</td><td>Do not charge too hard on top of the plant's load</td><td>The month's single highest 15-minute demand sets this charge. Charging at full power during the valley creates a new peak, and one careless interval costs about a week of arbitrage savings</td></tr>
    <tr><td>Outage and load-shedding risk</td><td>Hold energy in reserve during the summer and winter peak seasons, when the grid may curtail supply</td><td>Reserved energy cannot earn arbitrage savings, so the question is how much to hold, and in which months</td></tr>
    <tr><td>Fluctuating plant load</td><td>Leave headroom for load swings, and follow the load when possible</td><td>The same charging power that is harmless at average load can set a new monthly peak during a load spike</td></tr>
    <tr><td>Power-quality alarms</td><td>Keep charging and discharging well below the battery's rating</td><td>The plant's alarm thresholds, not the battery, cap the power, so a full cycle takes more hours</td></tr>
    <tr><td>Manual operation</td><td>Run on rules that on-site staff can follow</td><td>An optimal schedule is useful only if operators can carry it out reliably every day</td></tr>
  </tbody>
</table>

The optimization therefore treats the battery and the plant as one system. It minimizes the plant's total bill, including both energy and demand charges, subject to the reserve requirement, the alarm limits, and the plant's load.

## What the optimization changed

Analysis of meter data showed that the original operating rule held the summer backup reserve **all year**. That energy sat idle every night, so the battery completed only about 82% of its designed daily cycling. The optimized strategy kept the same safety limits but made the operating rules depend on the month:

- **July and August:** keep the backup reserve, as before.
- **All other months:** release the reserve and discharge fully during peak hours.
- **Critical-peak months:** discharge harder during the two critical-peak hours, top up in the morning shoulder if the battery is not full, and keep discharging late in the evening if energy remains.

The explorer below reproduces this logic on an **illustrative model**. It uses a synthetic plant whose average load is 1.0, a 4-hour battery, and prices relative to the flat tariff tier. No project data is shown. The full model is open source in [industrial-bess-scheduling](https://github.com/ruikelyu/industrial-bess-scheduling) (see [below](#open-source-code)). "Full optimization" solves a day-ahead linear program that also minimizes the demand charge, assuming a perfect load forecast.

<div id="byd-es-explorer" class="byd-es"></div>

Two patterns stand out. Outside summer, the simplified rules use almost the whole battery every day; under the original rule, about a fifth of it sits idle at midnight. And the full optimization adds little beyond the simplified rules: because the plant's load is so steady, most of the value can be captured with a rulebook that operators can follow by hand.

## Results

Using the plant's measured load for a winter month, the strategies change the monthly electricity bill as follows (percent of the bill without a battery):

<table class="byd-es-table">
  <thead>
    <tr><th>Bill component</th><th>Original rule</th><th>Simplified rules</th><th>Full optimization</th></tr>
  </thead>
  <tbody>
    <tr><td>Energy charges</td><td>−11.6%</td><td>−14.0%</td><td>−14.0%</td></tr>
    <tr><td>Demand charge</td><td>+2.7%</td><td>+2.7%</td><td>+2.1%</td></tr>
    <tr><td>Per-kWh network charge</td><td>+0.3%</td><td>+0.5%</td><td>+0.5%</td></tr>
    <tr><td>Total bill</td><td>−8.5%</td><td>−10.8%</td><td>−11.4%</td></tr>
  </tbody>
</table>

- The simplified rules raise the battery's savings by **about 27%** relative to the original rule, with no new hardware, software, or forecasting.
- Full optimization raises them by **about 35%**. The extra gain comes from tracking the load to limit the demand-charge increase that battery charging causes.
- The payback period of the battery investment shortens by roughly **20%**, from about ten years to about eight.

Extrapolated from the month analyzed, the improved strategies were projected to save an additional **US$1.3–1.7 million per year** compared with the original operating rule.

## Open-source code

The optimization and operator rules are available as a Python package, [industrial-bess-scheduling](https://github.com/ruikelyu/industrial-bess-scheduling). It includes:

- the monthly linear program, with energy, network, and demand charges, the outage reserve, and alarm and import limits;
- the operator rulebooks;
- a load generator calibrated to aggregate statistics of the plant's metered load, so the analysis can be reproduced without the original data; and
- a walkthrough notebook, tests, and reproducible figures.

## Research connection

The project also revealed an important physical limit: when production equipment is already highly utilized, short-term rescheduling alone provides limited flexibility. That observation helped motivate my subsequent research on spare production capacity, inventories, and seasonal industrial flexibility.

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="{{ '/assets/js/byd-es-data.js' | relative_url }}"></script>
<script src="{{ '/assets/js/byd-es-explorer.js' | relative_url }}"></script>
