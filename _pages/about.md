---
permalink: /
title: "Energy Systems Researcher"
description: "Energy systems research combining power systems and macro-energy systems modeling to study industrial demand flexibility and energy infrastructure."
author_profile: true
redirect_from: 
  - /about/
  - /about.html

impact_row:
  - title: "Nature Energy"
    excerpt: "**Cover Article (2026).** Industrial overcapacity and product inventories as a source of seasonal grid flexibility."
    url: "https://www.nature.com/articles/s41560-026-02073-y"
    btn_label: "Read the paper"
    btn_class: "btn--primary"
  - title: "Industrial Implementation"
    excerpt: "**US$4 million/year** in estimated operating-cost savings from coordinating manufacturing load, battery storage, and solar generation."
    url: "/projects/industrial-energy-management/"
    btn_label: "View the project"
    btn_class: "btn--primary"
  - title: "Open-Source Modeling"
    excerpt: "Implemented models of aluminum, ammonia, and methanol production in MacroEnergy.jl, an open-source framework for optimizing large, multi-sector energy systems."
    url: "https://github.com/macroenergy/MacroEnergy.jl"
    btn_label: "View the code"
    btn_class: "btn--primary"

research_areas:
  - title: "Physically Grounded and Scalable Modeling"
    excerpt: "Optimization methods that represent industrial production constraints while remaining tractable for power-system planning and operations."
  - title: "Large Loads and Energy Infrastructure Planning"
    excerpt: "Co-optimizing production capacity, inventories, facility locations, computing workloads, and operating schedules with generation, storage, and grid investments."
  - title: "Markets and Institutions for Demand Flexibility"
    excerpt: "Procurement mechanisms, contracts, and electricity markets that compensate firms for the capital, inventory, and operating costs of providing flexibility."
---

**Power Systems and Macro-Energy Systems Modeling for Industrial Demand Flexibility and Energy Infrastructure**

I am currently a Postdoctoral Research Scientist in the Department of Earth and Environmental Engineering at Columbia University, working with [Prof. Bolun Xu](https://www.engineering.columbia.edu/faculty-staff/directory/bolun-xu). I received my Ph.D. in Electrical Engineering from Tsinghua University, advised by [Prof. Chongqing Kang](https://www.eea.tsinghua.edu.cn/en/faculties/cqkang.htm). Before joining Columbia, I held research appointments at The Hong Kong Polytechnic University, where I worked with [Dr. Ziqing Zhu](https://www.polyu.edu.hk/eee/people/academic-staff-and-teaching-staff/dr-zhu-ziqing) and [Prof. Siqi Bu](https://www.polyu.edu.hk/eee/people/academic-staff-and-teaching-staff/prof-bu-siqi), and Princeton University’s Andlinger Center for Energy and the Environment, where I worked with [Prof. Jesse Jenkins](https://mae.princeton.edu/people/jesse-jenkins).

**Contact**<br>
Mudd 1038G, 500 W 120th St, New York, NY 10027<br>
Tel: +1 (609) 436-8628<br>
Email: rl3763@columbia.edu

My research examines how energy infrastructure and the systems it serves can be co-designed to enable a reliable and affordable transition to clean energy. Grounded in power systems, optimization, and electricity markets, I focus particularly on the interaction between electricity infrastructure and flexible industrial demand. I combine macro-energy systems optimization, engineering models of industrial processes, and empirical analysis of smart-meter data to develop physically grounded, scalable representations of demand flexibility and assess its value to energy-system planning and operations.

[Explore Research Projects]({{ base_path }}/projects/){: .btn .btn--primary }
[Download CV]({{ base_path }}/files/CV_Ruike_Lyu.pdf){: .btn .btn--inverse }
[Email Me](mailto:{{ site.author.email }}){: .btn }

## Selected Impact

{% include feature_row id="impact_row" %}

## Current Research

{% include feature_row id="research_areas" %}

## Research Vision

My broader vision is to build a **demand flexibility economy** in which large energy users adapt their operations and investments to renewable electricity availability while earning predictable returns for the flexibility they provide.

## Latest News

<ul>
{% for item in site.data.news limit:6 %}
  <li><strong>[{{ item.date }}]</strong> {{ item.text | markdownify | remove: "<p>" | remove: "</p>" }} <a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{{ item.link_label }}</a>.</li>
{% endfor %}
</ul>
