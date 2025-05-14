---
title: Outreach Links
layout: splash
permalink: /outreach/
excerpt: "More about our program and links to outreach for past missions."
header:
  overlay_color: "#000"
  overlay_filter: linear-gradient(rgba(3, 3, 3, 0.5), rgba(255, 255, 255, 0.5))
  overlay_image: https://www.fisheries.noaa.gov/s3//2024-10/1243x1580-Birds-Aina-PMNM-Fisheries_PIFSC.png
  caption: "He aliʻi ka ʻāina, he kauā ke kanaka. The land is a chief; man is its servant.  (‘Ōlelo No‘eau #531)<br>Out in Papahānaumokuākea this ʻōlelo noʻeau is brought to life as we enter into spaces where ʻāina (land and sea) has no need for kanaka but it is us kanaka that need ʻāina. <br>Reinforcing the importance for monitoring to ensure ʻāina and kanaka can live. Credit: NOAA Fisheries/A. Nālani Olguin (2024 NCRMP Permit #PMNM-2024-001)"
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
    <img src="{{ '/assets/images/2023_storymap.png' | relative_url }}" alt="2023 storymap screenshot" style="max-width: 100%; height: auto;">
    <i>Snapshot of 2023 storymap for mission to American Samoa</i>
  </div>
</div>

