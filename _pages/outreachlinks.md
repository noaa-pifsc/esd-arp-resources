---
title: Outreach Links
layout: splash
permalink: /outreach/
excerpt: "More about our program and links to outreach for past missions."
header:
  overlay_color: "#000"
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  overlay_image: 
---
<div>
<h2>Browse links below</h2>

<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div style="width: 50%;">
<ul>
{% for link in site.data.links %}
    <li><a href = "{{ link.URL}}" target="_blank">{{ link.Topic}}</a></li>
{% endfor %}
</ul>
  </div>
  <div style="width: 50%; text-align: right;">
    <!-- Right side: Image -->
    <img src="/assets/images/2023_storymap.png" alt="2023 storymap screenshot" style="max-width: 100%; height: auto;">
    <i>Snapshot of 2023 storymap for mission to American Samoa</i>
  </div>
</div>