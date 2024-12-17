---
title: "Access Data"
permalink: /accessdata/
layout: single
excerpt: "How and where to access our NCRMP data."
header:
  overlay_image: https://www.fisheries.noaa.gov/s3//2024-07/640x480-Sette-NCRMP-Fisheries-PIFSC.jpg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: NOAA/NMFS"
feature_row2:
- image_path: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmcO5tHXjtN5CEzy1KMGDeVuLNn52DYvVttw&s
  alt: "coris image"
  title: "NOAA CoRIS"
  excerpt: "Access our data on NOAA Coral Reef Information Systems (CoRIS)"
  url: "https://www.coris.noaa.gov/"
  btn_label: "Go to CoRIS"
  btn_class: "btn--primary"
feature_row3:
- image_path: https://www.pacioos.hawaii.edu/wp-content/uploads/2016/06/PacIOOS-logo-stacked-small.jpg
  alt: "pacioos image"
  title: "PacIOOS"
  excerpt: "Access our data and related tools in the Projects section "
  url: "https://www.pacioos.hawaii.edu/"
  btn_label: "Go to PacIOOS"
  btn_class: "btn--primary"
feature_row4:
- image_path: https://www.pmel.noaa.gov/ocs/sites/default/files/thumbnails/image/ERDDAP_Data_Access.png
  alt: "errdap image"
  title: "CRCP ERRDAP"
  excerpt: "Go to tabledap to see CRCP datsets or use the video tutorial provided"
  url: "https://www.ncei.noaa.gov/erddap/index.html"
  btn_label: "Go to CRCP ERRDAP"
  btn_class: "btn--primary"
sidebar:
  nav: "docs"
---
# Caveats
### Our data is split into fixed site versus random site surveys. 
Our random sites follow a stratified-random sampling design (StRS), meaning they can only be meaningfully analyzed at island and regional levels.
# Data via NOAA GeoPlatform
View data, caveats, and more on the NCRMP program including surveys in the Atlantic <a href = " https://noaa.hub.arcgis.com/pages/4976333fbf884f26b2fdc9ac51a20576" target = "_blank">here</a>

# Raw data via NCEI
Our raw data is archived with NCEI within Collections, and is described within the InPort metadata catalog <a href = "https://www.fisheries.noaa.gov/inport/item/2712" target = "_blank">CREP library</a>.

# R processing scripts
Our data is still being converted into public-ready form and will become available on <a href = "https://github.com/noaa-pifsc" target = "_blank">PIFSC github</a>.

# SfM imagery via Google Cloud bucket (NODD)
<p>Due to the size of structure-from-motion (SfM) imagery, raw imagery as well as products are available via our <a href= "https://console.cloud.google.com/storage/browser/nmfs_odp_pifsc/PIFSC/ESD/ARP/Photogrammetric%20Imagery" target ="_blank">Google Cloud Bucket</a>. Raw imagery is archived with NCEI and available on the <a href ="https://www.ncei.noaa.gov/access/ocean-exploration/video/" target = "_blank"> OER Portal</a>.
<br>
For assistance and tools on how to adopt a similar strategy at your institution, contact the Data Services Team at <a href = "mailto:nmfs.pic.credinfo@noaa.gov">nmfs.pic.credinfo@noaa.gov</a>.</p>

# Public Tools
See our PIFSC github for python-based tools to assist with processing imagery for NODD, imagery validation, etc.

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="left" %}
{% include feature_row id="feature_row4" type="left" %}