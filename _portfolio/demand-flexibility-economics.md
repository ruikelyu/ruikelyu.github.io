---
title: "Valuing Demand Flexibility"
excerpt: "Comparing demand-side flexibility with energy storage while accounting for the capital and operating costs borne by flexibility providers."
collection: portfolio
order: 3
permalink: /projects/valuing-demand-flexibility/
teaser: /images/valuing/lcpe_by_period.png
teaser_alt: "Levelized cost of shifting electricity with a battery and with aluminum smelting, by flexibility period"
category_label: "Economics & Markets"
---

<figure>
  <img src="{{ '/images/valuing/lcpe_by_period.png' | relative_url }}" alt="Levelized cost per kWh shifted versus flexibility period: the battery's cost rises from hourly to seasonal, aluminum smelting's falls">
  <figcaption>Cost of shifting one kWh as the flexibility period grows from a day to a year. A battery cycles less often, so its cost per kWh rises; an aluminum smelter spreads its restart cost over a longer period, so its cost falls. The dotted line is the value to the power system.</figcaption>
</figure>

## The problem

Demand flexibility can reduce generation, storage, and grid investment, but it is not costless. Firms may need spare equipment capacity, inventories, working capital, or operational changes to shift electricity use. Power-system models often quantify the value of flexibility without representing these consumer-side costs.

## What I am developing

I developed a life-cycle cost framework that compares industrial and data-center load shifting with energy storage across timescales. The framework accounts for both the infrastructure costs avoided by power systems and the capital and operating costs borne by flexibility providers.

<figure>
  <img src="{{ '/images/valuing/storage_vs_load_shifting.png' | relative_url }}" alt="Storage charges at low prices and discharges at high prices; load shifting runs added capacity at low prices and draws down product inventory at high prices">
  <figcaption>Storage moves electricity and pays for power and energy capacity. Load shifting moves output and pays for added production capacity, product inventory, and restarts.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/valuing/lcpe_hourly_seasonal.png' | relative_url }}" alt="Levelized cost per kWh shifted for storage technologies and new production capacity, for a daily and an annual cycle">
  <figcaption>Levelized cost per kWh shifted for a daily cycle (left) and an annual cycle (right), log scale. Batteries are cheapest for daily shifting; aluminum smelting is cheapest for seasonal shifting. At the price spread studied (dashed line), most options cost more than the value they create.</figcaption>
</figure>

This work supports a broader research agenda on a **demand flexibility economy**: defining flexibility as a dependable service and designing utility procurement, bilateral contracts, and organized markets that translate its system value into stable incentives for firms.

## Current outputs and next steps

- [Do We Still Need Demand Flexibility as Batteries Become Cheaper? A Levelized Cost Perspective](https://arxiv.org/abs/2608.07348), manuscript under review
- “Demand flexibility must account for consumer-side capital costs,” commentary under review

The next stage links system-level avoided costs with firm-level investment models to compare availability payments, performance payments, contract duration, and verification requirements for seasonal and other forms of large-load flexibility.
