---
permalink: /about/
layout: splash
title: "About us"
header: 
 overlay_color: "#000"
 overlay_filter: "0.3"
 overlay_image: https://www.fisheries.noaa.gov/s3//2024-08/4032x2268-NCRMP-crew-Hawaii-Fisheries-PIFSC.jpg
 actions:
    - label: "Read more about the ESD"
      url: "https://www.fisheries.noaa.gov/pacific-islands/ecosystems/surveying-vast-pacific-ocean"
 caption: "2024 NCRMP Main Hawaiian Islands Team"
excerpt: "The ARP team is composed of 20-30 folks from various backgrounds, divided into technicians, coordinators, analysts, lead scientists, project managers, operations, and data managers/app developers."
intro:  
- excerpt:"Read more about where we survey and how to contact us below."
feature_row2:
- image_path: https://www.fisheries.noaa.gov/s3/styles/full_width/s3/dam-migration/pifsc.png?itok=SmTJPyV8
  alt: "survey area image"
  title: "Survey area"
  excerpt: "We survey the Pacific Islands Regions inlcuding the Hawaiian Archipelago, the Mariana Archipelago, American Samoa, and Pacific Remote Island Areas.  We conduct multidisciplinary research and monitoring of shallow-water coral reef ecosystems with some of our datastreams starting as early as 2013. Projects include: the National Coral Reef Monitoring Program (NCRMP), Land-based sources of polllution (LBSP), and more. Because humans are a key part of the ecosystem, the PIFSC science center's research outside of our program includes the social, cultural, and economic aspects of fishery and resource management decisions."
  url: "https://www.fisheries.noaa.gov/region/pacific-islands"
  btn_label: "Learn More"
  btn_class: "btn--primary"
feature_row3:
- image_path: "/assets/images/rainbow_marianas.jpg"
  alt: "contact image"
  title: "Contact us"
  excerpt: "This website is maintained by the Data Services Team(nmfs.pic.credinfo@noaa.gov) on a PIFSC github repository using minimal-mistakes jekyll theme."
  url: "mailto:nmfs.pic.credinfo@noaa.gov"
  btn_label: "Email Us"
  btn_class: "btn--primary"
---
{% include feature_row id="intro" type="center" %}
{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}