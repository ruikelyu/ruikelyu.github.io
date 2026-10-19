---
title: "Industrial Production Process Modeling: Improving Computational Efficiency While Maintaining Accuracy"
collection: publications
category: manuscripts
permalink: /publication/2023-industrial-load-modeling
excerpt: 'Developing linearized models of industrial production processes to improve computational efficiency while maintaining model accuracy'
date: 2023-10-25
venue: 'IEEE Transactions on Smart Grid/ISGT EU 2023'
paperurl: 'https://ieeexplore.ieee.org/document/10408608'
# header:
#   teaser: /images/pub1.png
---

![Industrial production process modeling](/images/pub1.png)

## Research Overview

My research in this area focuses on developing efficient mathematical models to describe energy flows and material conversions in industrial production processes. The goal is to create models that maintain accuracy while being computationally efficient enough for practical applications in energy management and grid interaction.

## The Challenge

Conventional models like State-Task Networks (STN) and Resource-Task Networks (RTN) describe industrial production processes using numerous integer or binary variables. This creates significant computational challenges:

- A single plant with 10 devices operating over 24 hours results in 240 variables
- At 15-minute resolution, this increases to thousands of variables
- When these are integer variables, the problem becomes NP-hard to solve
- Industrial-scale applications become computationally infeasible

## Our Solution

My contribution in this area is linearizing most parts of these models using advanced mathematical techniques that:

1. Greatly reduce model complexity
2. Increase computational feasibility
3. Maintain model accuracy

The results demonstrate that our linearized models maintain high accuracy while accelerating computation by more than 20 times compared to conventional approaches.

## Key Publications

### Linear STN Model

Our first approach focused on the State-Task Network model, creating a "Linear STN" that significantly reduces computational complexity through strategic linearization techniques. This work was published as a conference paper:

[LSTN-Paper](https://ieeexplore.ieee.org/document/10408608)

### Continuous RTN Model

Building on our STN work, we developed a "Continuous RTN" model that applies similar principles to the more complex Resource-Task Network framework. A systematic reconstruction of the Resource-Task Network (RTN) model – the first in over three decades since its inception. We've achieved at least a 10x speedup while maintaining accuracy. For those in steelmaking and beyond who have worked with RTN, we invite you to explore our new model:

[cRTN-Paper](https://ieeexplore.ieee.org/document/11082423)

## Open-Source Implementation

We have established GitHub repositories containing both the conventional models and our improved versions:

[Link to STN/RTN models repository](https://github.com/ruikelyu/Industrial-User-Modeling-Toolkit)

These repositories include implementation details, example data, and documentation to help other researchers apply our methods to their own industrial modeling problems.

## Impact and Applications

The dramatically improved computational efficiency of our models enables:

- Real-time optimization of industrial energy consumption
- Better integration of industrial loads in demand response programs
- More effective participation of industrial users in electricity markets
- Faster economic dispatch and market clearing with industrial load consideration

By making these complex models more tractable, we open the door to better coordination between industrial operations and power system needs.

