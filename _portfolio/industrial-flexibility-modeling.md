---
title: "Industrial Flexibility Modeling Toolkit"
excerpt: "Physically grounded, computationally tractable models for representing industrial production in power-system planning and operations."
collection: portfolio
order: 1
permalink: /projects/industrial-flexibility-modeling/
teaser: /images/pub1.png
teaser_alt: "Diagram of the industrial production-process modeling framework"
category_label: "Modeling"
---

![Industrial production-process modeling framework](/images/pub1.png)

## The problem

Industrial demand flexibility is governed by material flows, task sequences, inventories, and discrete operating requirements. Simplified load models are tractable in power-system studies but can misrepresent these constraints, while detailed production-scheduling models are often too computationally intensive for system planning and real-time operation.

## What I developed

I developed a connected modeling toolkit that makes physically grounded industrial-load models usable in power-system applications:

- a continuous Resource Task Network that represents material flows and production tasks with far fewer binary variables;
- an inverse optimization method that infers plant scheduling parameters from smart-meter and electricity-price data;
- a data-driven reduction method that converts detailed industrial constraints into compact models for system-scale studies; and
- real-time coordination methods that connect these models with virtual-power-plant operation.

## Key result

In a steelmaking case, the reduced model replaced **10,208 integer variables with 48 continuous variables** while reproducing the detailed model's optimal load profiles with a normalized RMSE of **3.9%** on test data. This body of work formed the methodological core of my Ph.D. dissertation, and its open-source implementations have received more than 200 GitHub stars.

## Papers and open-source resources

- [Efficient Scheduling of Discrete Industrial Processes through Continuous Modeling](https://ieeexplore.ieee.org/document/11082423)
- [Production Scheduling Identification](https://ieeexplore.ieee.org/document/10769532) · [Code](https://github.com/ruikelyu/Production-Scheduling-Identification)
- [Data-Driven Dimension Reduction for Industrial Load Modeling](https://ieeexplore.ieee.org/document/10902053) · [Code](https://github.com/ruikelyu/Data-Driven-Dimension-Reduction)
- [Industrial User Modeling Toolkit](https://github.com/ruikelyu/Industrial-User-Modeling-Toolkit)
