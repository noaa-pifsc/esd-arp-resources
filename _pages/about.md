---
title: "About us"
layout: splash
permalink: /about/
header: 
 overlay_color: "#000"
 overlay_filter: "0.3"
 overlay_image: https://www.fisheries.noaa.gov/s3//2024-08/4032x2268-NCRMP-crew-Hawaii-Fisheries-PIFSC.jpg
 actions:
    - label: "Read more about the ESD"
      url: "https://www.fisheries.noaa.gov/pacific-islands/ecosystems/surveying-vast-pacific-ocean"
 caption: "2024 NCRMP Main Hawaiian Islands Team"
excerpt: "Our specific ARP team is composed of 20-30 folks from various backgrounds, divided into technicians, coordinators, analysts, lead scientists, project managers, operations, and data managers/app developers."
intro:  
- excerpt:"Read more about where we survey and how to contact us below."
feature_row2:
- image_path: https://www.fisheries.noaa.gov/s3/styles/full_width/s3/dam-migration/pifsc.png?itok=SmTJPyV8
  alt: "survey area image"
  title: "Survey area"
  excerpt: "Pacific Islands regions surveyed since 2013.We conduct multidisciplinary research, monitoring, and analysis of coral reef ecosystems in the Hawaiian Archipelago, the Mariana Archipelago, American Samoa, and Pacific Remote Island Areas. Projects include: the National Coral Reef Monitoring Program (NCRMP), Land-based sources of polllution (LBSP), and more. Because humans are a key part of the ecosystem, the PIFSC science center's research outside of our program includes the social, cultural, and economic aspects of fishery and resource management decisions."
  url: "https://www.fisheries.noaa.gov/region/pacific-islands"
  btn_label: "Learn More"
  btn_class: "btn--primary"
feature_row3:
- image_path: /assets/images/rainbow_marianas.jpg
  alt: "contact image"
  title: "Contact us"
  excerpt: "This website is maintained by the Data Services Team on a PIFSC github repository using minimal-mistakes jekyll theme. For questions, feel free to email us at: nmfs.pic.credinfo@noaa.gov"
  url: "mailto:nmfs.pic.credinfo@noaa.gov"
  btn_label: "Email Us"
  btn_class: "btn--primary"


---
{% include feature_row id="intro" type="center" %}
{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}