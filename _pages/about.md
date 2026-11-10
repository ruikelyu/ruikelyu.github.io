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
    excerpt: "**US$1.3–1.7 million/year** in projected additional savings over the original operating rule, from coordinating manufacturing load, battery storage, and solar generation."
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
    excerpt: "Optimization methods that represent industrial production constraints while remaining tractable for power-system planning and operations. Open-source in **indflex**, with interactive demos."
    url: "/projects/industrial-flexibility-modeling/"
    btn_label: "Explore the toolkit"
    btn_class: "btn--primary"
  - title: "Large Loads and Energy Infrastructure Planning"
    excerpt: "Co-optimizing production capacity, inventories, facility locations, computing workloads, and operating schedules with generation, storage, and grid investments."
    url: "/projects/seasonal-industrial-flexibility/"
    btn_label: "View the project"
    btn_class: "btn--primary"
  - title: "Markets and Institutions for Demand Flexibility"
    excerpt: "Procurement mechanisms, contracts, and electricity markets that compensate firms for the capital, inventory, and operating costs of providing flexibility."
    url: "/projects/valuing-demand-flexibility/"
    btn_label: "View the project"
    btn_class: "btn--primary"
---

**Power Systems and Macro-Energy Systems Modeling for Industrial Demand Flexibility and Energy Infrastructure**

I am a postdoc at Columbia University, working with [Bolun Xu](https://www.engineering.columbia.edu/faculty-staff/directory/bolun-xu). I obtained my PhD in Electrical Engineering from Tsinghua University, advised by [Chongqing Kang](https://www.eea.tsinghua.edu.cn/en/faculties/cqkang.htm), where I was also mentored by [Hongye Guo](https://www.eea.tsinghua.edu.cn/en/faculties/hy_guo.htm). I was a graduate student researcher at Princeton University, working with [Jesse Jenkins](https://mae.princeton.edu/people/jesse-jenkins), and a research associate at The Hong Kong Polytechnic University, working with [Ziqing Zhu](https://www.polyu.edu.hk/eee/people/academic-staff-and-teaching-staff/dr-zhu-ziqing) and [Siqi Bu](https://www.polyu.edu.hk/eee/people/academic-staff-and-teaching-staff/prof-bu-siqi).

My research studies how power systems and flexible industrial demand can be planned and operated together, so that the clean-energy transition stays reliable and affordable.

[Explore Research Projects]({{ base_path }}/projects/){: .btn .btn--primary }
[Download CV]({{ base_path }}/files/CV_Ruike_Lyu.pdf){: .btn .btn--inverse }
[Email Me](mailto:{{ site.author.email }}){: .btn .btn--inverse }

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
