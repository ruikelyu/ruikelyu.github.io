---
title: "indflex: Industrial Demand Flexibility Toolkit"
excerpt: "Open models and interactive demos of my PhD work on industrial demand flexibility: from production-process models to grid decisions."
collection: portfolio
order: 1
permalink: /projects/industrial-flexibility-modeling/
teaser: /images/indflex/crtn_gantt.png
teaser_alt: "Gantt charts of three steelmaking heats scheduled by the RTN and cRTN models"
category_label: "Modeling"
---

<link rel="stylesheet" href="{{ '/assets/css/indflex.css' | relative_url }}">

**Industrial demand flexibility: from process models to grid decisions.** [indflex](https://github.com/ruikelyu/indflex) is the open-source toolkit of my PhD thesis. It turns each step of the work into a Python implementation, checked against the original paper code, and an interactive notebook that runs in seconds to a few minutes. Each step below has a two-minute video, an interactive demo precomputed with the toolkit (it runs in your browser), and a notebook.

## The problem

Industrial demand flexibility is governed by material flows, task sequences, inventories, and discrete operating requirements. Simplified load models are tractable in power-system studies but can misrepresent these constraints, while detailed production-scheduling models are often too computationally intensive for system planning and real-time operation. A grid operator also rarely knows a factory's parameters: it sees only meter data.

## The chain

<div class="ifx-chain">
  <a href="#process-models"><b>1. Process models</b>STN and LSTN for continuous processes; RTN and cRTN for batch processes</a>
  <a href="#parameter-identification"><b>2. Parameter identification</b>Learn a factory's private parameters from hourly meter data</a>
  <a href="#dimension-reduction"><b>3. Dimension reduction</b>Replace a detailed model with a few numbers</a>
  <a href="#virtual-power-plant"><b>4. Virtual power plant</b>Bid for regulation, then split the signal in milliseconds</a>
</div>

## 1. Process models {#process-models}

{% include youtube.html id="wMm-IgvIvhM" title="LSTN explainer" %}

**Continuous processes.** A State-Task Network (STN) schedules each machine's operating mode with binary variables. Market intervals are much longer than mode switches, so the **LSTN** instead decides *how long* each machine spends in each mode within the hour. The binaries disappear and the scheduling problem becomes a linear program. Pick a day:

<div id="ifx-lstn" class="ifx"></div>

The LSTN's cost is a lower bound on the STN's and is within 1% on every day of July 2022. Because it is an LP, it scales to fleets of factories:

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/lstn_scaling.png' | relative_url }}" alt="Solve time of STN and LSTN versus the number of factories">
  <figcaption>Solve time with the free HiGHS solver: the STN reaches a 30 s limit at 5 factories; the LSTN schedules 200 in about 10 s.</figcaption>
</figure>

{% include youtube.html id="RATnHWVbLwY" title="cRTN explainer" %}

**Batch processes.** Steelmaking processes discrete *heats* that cannot be interrupted once melting starts. The conventional Resource-Task Network (RTN) models every task for every heat, and rounds task durations up to whole time slots. The **continuous RTN (cRTN)** tracks the *progress* of one shared task per stage, so a heat can finish in the middle of a slot and the model does not grow with the number of heats. The example below is the one-furnace case of the paper: two heats, flexible melting power.

<div id="ifx-crtn" class="ifx"></div>

In scenario 2, the RTN must finish the second heat at a slot boundary, so it runs into an expensive hour. The cRTN melts both heats at high power in three cheap hours.

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/crtn_structure.png' | relative_url }}" alt="RTN needs eight per-heat lines for two heats; cRTN needs four shared lines">
  <figcaption>The same two heats as each model sees them: the RTN needs a set of tasks and resources per heat (8 lines); the cRTN needs one shared set (4 lines), whatever the production target.</figcaption>
</figure>

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/crtn_gantt.png' | relative_url }}" alt="Gantt charts of three heats through EAF, AOD, LF and CC for RTN and cRTN">
  <figcaption>A steelmaking line (EAF → AOD → LF → CC) with three heats. In the paper (8 heats, 5-minute slots), the cRTN cuts the mean solution time from 156.7 to 17.1 minutes (−89%).</figcaption>
</figure>

## 2. Parameter identification {#parameter-identification}

{% include youtube.html id="gpxkEAigneE" title="PSI explainer" %}

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/psi_meter_data.png' | relative_url }}" alt="Load disaggregation needs a high-frequency trace; the grid has 24 hourly readings a day; the plant's stage powers, buffers, production target and number of stages are unknown">
  <figcaption>What identification has to work with. Load-disaggregation methods (NILM) need high-frequency traces; a grid operator has 24 hourly readings a day, and the plant's parameters are private. The top trace is illustrative; the hourly data are the steel-powder test case of the thesis.</figcaption>
</figure>

**Production scheduling identification (PSI)** assumes a factory minimizes its electricity cost and asks which plant parameters make that optimal schedule reproduce its meter data. The optimality conditions of the plant's scheduling problem become constraints of an *inverse* optimization problem, and the private parameters become its decision variables. Below, a two-machine plant is identified from **one day** of meter data in a single solve, and the identified model then predicts how the plant would respond to a demand-response event. Move the event:

<div id="ifx-psi" class="ifx"></div>

The identified model recovers the rated powers and the daily output exactly, so its predicted response matches the true plant's. For real plants with many days of data, PSI cycles through the days and averages the estimates.

## 3. Dimension reduction {#dimension-reduction}

{% include youtube.html id="ClJwRWYXZfI" title="D3R explainer" %}

A grid model cannot carry a detailed process model, with its binaries, for every factory. **Data-driven dimension reduction (D3R)** learns an *adjustable load fleet*: a few loads with power and daily-energy limits (four numbers each), whose optimal response to prices mimics the detailed model's. It is trained by inverse optimization on the detailed model's responses. Here, a one-load fleet is fitted to three days of a cement plant and checked on ten unseen days:

<div id="ifx-d3r" class="ifx"></div>

For a steelmaking plant, the paper replaces **10,208 integer variables with 24 continuous ones** at 3.6% error on test days. These are errors in optimal response, not feasibility guarantees: the detailed model turns the reduced model's decision into an executable schedule.

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/d3r_approximations.png' | relative_url }}" alt="Inner, outer and least-error box approximations of a rounded feasible region">
  <figcaption>Three ways to approximate a plant's feasible region with a simple box. The inner box leaves out feasible operation (gray); the outer box allows operation the plant cannot deliver (red); the least-error box has the smallest worst-case boundary distance and both kinds of error. D3R takes the least-error view, measured on optimal responses.</figcaption>
</figure>

## 4. Virtual power plant {#virtual-power-plant}

{% include youtube.html id="dFsv5i7JZIM" title="Virtual power plant explainer" %}

A virtual power plant pools EVs, storage, air conditioning, industrial production stages and PV, and sells energy and frequency regulation. Every half hour it solves a bidding LP. When the grid operator then sends a regulation signal every two seconds, it must split the requested power among its resources at once. The bidding LP's dual variables price each resource's stored energy, which turns the split into a **merit order**: fill the cheapest power segments first. That is optimal, and takes milliseconds instead of an LP solve. Press play to follow the first hour:

<div id="ifx-vpp" class="ifx"></div>

<figure class="ifx-figure">
  <img src="{{ '/images/indflex/vpp_cube.png' | relative_url }}" alt="A cube of 24 hours by 20 scenarios by 10,000 resources collapses, through shadow prices, into one column of resources sorted by cost and filled up to the signal">
  <figcaption>Why the split is fast. The bidding problem spans 24 hours, 20 regulation-signal scenarios and 10,000 resources (more than 20 million constraints). Its shadow prices fold the future hours and scenarios into each resource's cost, so every 2 seconds the dispatch only sorts resources by cost and fills up to the signal. In the thesis tests, this takes about 3 ms for a fleet of 15,000 EVs.</figcaption>
</figure>

## Try it yourself

Every step has a notebook that runs in the browser on Google Colab, with nothing to install, and a two-minute explainer video:

| Step | Notebook | Video |
|---|---|---|
| STN vs. LSTN | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruikelyu/indflex/blob/main/notebooks/01_stn_vs_lstn.ipynb) | [YouTube](https://youtu.be/wMm-IgvIvhM) |
| RTN vs. cRTN | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruikelyu/indflex/blob/main/notebooks/02_rtn_vs_crtn.ipynb) | [YouTube](https://youtu.be/RATnHWVbLwY) · [Bilibili](https://www.bilibili.com/video/BV1cdurzbEgi) |
| PSI (needs a Gurobi license) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruikelyu/indflex/blob/main/notebooks/03_psi.ipynb) | [YouTube](https://youtu.be/gpxkEAigneE) · [Bilibili](https://www.bilibili.com/video/BV1bXQDYcE8Y) |
| D3R | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruikelyu/indflex/blob/main/notebooks/04_d3r.ipynb) | [YouTube](https://youtu.be/ClJwRWYXZfI) · [Bilibili](https://www.bilibili.com/video/BV1JFQ1YwEsK) |
| VPP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruikelyu/indflex/blob/main/notebooks/05_vpp.ipynb) | [YouTube](https://youtu.be/dFsv5i7JZIM) · [Bilibili](https://www.bilibili.com/video/BV1CpQDYDE67) |

The [toolkit's documentation](https://github.com/ruikelyu/indflex/tree/main/docs) explains each step, what it can and cannot claim, and how it was checked against the original paper code.

## Papers and open-source resources

- R. Lyu et al., [LSTN: A Linear Model of Industrial Production Process for Demand Response](https://www.researchgate.net/publication/377827063_LSTN_A_Linear_Model_of_Industrial_Production_Process_for_Demand_Response), IEEE ISGT Europe, 2023 · [Slides](https://github.com/ruikelyu/indflex/releases/tag/slides-lstn-isgt2023)
- R. Lyu et al., [Efficient Scheduling of Discrete Industrial Processes through Continuous Modeling](https://ieeexplore.ieee.org/document/11082423), IEEE Transactions on Smart Grid · [Code](https://github.com/ruikelyu/Efficient-Scheduling-of-Discrete-Industrial-Processes)
- R. Lyu et al., [Production Scheduling Identification](https://ieeexplore.ieee.org/document/10769532), IEEE Transactions on Smart Grid, 2025 · [Code](https://github.com/ruikelyu/Production-Scheduling-Identification)
- R. Lyu et al., [Data-Driven Dimension Reduction for Industrial Load Modeling](https://ieeexplore.ieee.org/document/10902053), IEEE Transactions on Smart Grid, 2025 · [Code](https://github.com/ruikelyu/Data-Driven-Dimension-Reduction)
- Q. Chen, R. Lyu et al., [Real-Time Operation Strategy of Virtual Power Plants With Optimal Power Disaggregation Among Heterogeneous Resources](https://doi.org/10.1016/j.apenergy.2024.122876), Applied Energy, 2024 · [Code](https://github.com/ruikelyu/Real-time-operation-strategy-of-virtual-power-plants)
- **Toolkit:** [github.com/ruikelyu/indflex](https://github.com/ruikelyu/indflex). This body of work formed the methodological core of my Ph.D. dissertation, and its open-source implementations have received more than 200 GitHub stars.

To cite the toolkit, please cite the thesis:

```bibtex
@phdthesis{lyu2026industrial,
  author = {Ruike Lyu},
  title  = {Industrial Load Modeling and Optimization for Market-Based Interaction with Power Systems},
  school = {Tsinghua University},
  year   = {2026},
  month  = jun
}
```

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="{{ '/assets/js/indflex-demos-data.js' | relative_url }}"></script>
<script src="{{ '/assets/js/indflex-demos.js' | relative_url }}"></script>
