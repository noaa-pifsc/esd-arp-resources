---
title: "Access Data"
permalink: /accessdata/
layout: splash
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

---
# Under Construction
# Caveats
### Our data is split into fixed site versus random site surveys. 
Our random sites follow a stratified-random sampling design (StRS), meaning they can only be meaningfully analyzed at island and regional levels.

# Raw data via NCEI
Our raw data is archived with NCEI within Collections, and is described with the InPort metadata catalog.

# R processing scripts
Our data is still being converted into public-ready form and will become available on PIFSC github

# SfM imagery via Google Cloud bucket (NODD)
### Due to the size of structure-from-motion (SfM) imagery, we have made our raw imagery as well as products available via Google Cloud Bucket. Raw imagery is also archived on NCEI OER Portal.
For assistance and tools on how to adopt a similar strategy at your institution, contact the Data Services Team at nmfs.pic.credinfo@noaa.gov

# Public Tools
See our PIFSC github for python-based tools to assist with processing imagery for NODD, imagery validation, etc.

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="left" %}