---
layout: page
permalink: /publications/
title: publications
active: publications
description: Publications by categories in reversed chronological order. 
years: [2017, 2015, 2014, 2013,2012,2011]
---

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
