---
title: "Access Data"
permalink: /accessdata/
layout: single
excerpt: "How and where to access our data."
header:
  overlay_color: "#000"
  overlay_image:  /assets/images/accessdata-banner.jpg
  overlay_filter: linear-gradient(rgba(0, 0, 0, 0.4), rgba(255, 255, 255, 0.41))
  caption: "Photo credit: NOAA/NMFS"
feature_row2:
- image_path: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmcO5tHXjtN5CEzy1KMGDeVuLNn52DYvVttw&s
  alt: "coris image"
  title: "NOAA CoRIS"
  excerpt: "Access our data on NOAA Coral Reef Information Systems (CoRIS)"
  buttons:
  - url: "https://www.coris.noaa.gov/"
    btn_label: "Go to CoRIS"
    btn_class: "btn--primary"
feature_row3:
- image_path: https://www.pacioos.hawaii.edu/wp-content/uploads/2016/06/PacIOOS-logo-stacked-small.jpg
  alt: "pacioos image"
  title: "PacIOOS"
  excerpt: "Access our data and related tools in the Projects section "
  buttons:
  - url: "https://www.pacioos.hawaii.edu/"
    btn_label: "Go to PacIOOS"
    btn_class: "btn--primary"
feature_row4:
- image_path: https://www.pmel.noaa.gov/ocs/sites/default/files/thumbnails/image/ERDDAP_Data_Access.png
  alt: "errdap image"
  title: "CRCP ERRDAP"
  excerpt: "Go to tabledap to see CRCP datsets or use the video tutorial provided"
  buttons:
  - url: "https://www.ncei.noaa.gov/erddap/index.html"
    btn_label: "Go to CRCP ERRDAP"
    btn_class: "btn--primary"
sidebar:
  nav: "docs"
---


<style>
/* Custom Button Style */
/* Style the custom button */
.custom-button {
  background-color: transparent;  /* Remove background */
  color: inherit;                 /* Inherit the text color */
  border: 2px solid rgb(84, 86, 87);      /* Add a border */
  text-decoration: none;          /* Remove underline or other text decorations */
  padding: 10px;              /* Smaller padding for a smaller button */
  font-size: 16px;                /* Smaller font size */
  font-weight: bold;              /* Make text bold */
  border-radius: 5px;             /* Rounded corners */
  display: inline-block;          /* Ensure the button is inline with other elements */
  cursor: pointer;               /* Pointer cursor on hover */
  transition: all 0.3s ease;      /* Smooth transition for hover effect */
}

/* Optional: Hover effect for the custom button */
.custom-button:hover {
  background-color:rgba(44, 44, 44, 0.82);      /* Light background color on hover */
  border-color:rgb(84, 86, 87);          /* Darker border color on hover */
  color:rgb(255, 255, 255);                 /* Change text color on hover */
}


</style>

# Working with Our Data 
Our data is typically organized by fixed versus random site surveys, as well as by region. For example, fixed-site imagery is described separately from random site imagery for each distinct region.  Accordingly, raw data should only be analyzed in the specific manner described per methodology.<br><br>
[Browse Ecosystem Sciences Division Data](/metadata_catalog/){: .custom-button}
<br><br>
![FixedVsRandomSiteIslandScale](/assets/images/Methods-Island-Scale-Surveys-PIFSC.png)
*Diagram illustrating fixed versus random site locations for a given hypothetical island. Credit: NOAA Fisheries*
<br>

## Visualize NCRMP random site data via  <a href ="https://ncrmp.coralreef.noaa.gov/">NOAA Data Viz Tool</a> / NOAA GeoPlatform
- Browse by dashboard type to view and download data. For caveats and more on the NCRMP program, including surveys in the Atlantic <a href = " https://noaa.hub.arcgis.com/pages/4976333fbf884f26b2fdc9ac51a20576" target = "_blank">here</a>.<br><i>Note: this only includes <b>random</b> site data.</i>

## Raw data via NCEI
- Our raw data is archived with NCEI within Collections, and is described within the InPort <a href = "https://www.fisheries.noaa.gov/inport/item/2712" target ="_blank">PIFSC CREP Metadata Portfolio</a>. Go to methods page for survey specific details.

## R processing scripts
-  Our data is still being updated into public-ready form and will become available on <a href = "https://github.com/noaa-pifsc" target = "_blank">PIFSC github</a>.

## SfM imagery via Google Cloud bucket (NODD)
- Due to the size of structure-from-motion (SfM) imagery, raw imagery as well as products are available via our <a href= "https://console.cloud.google.com/storage/browser/nmfs_odp_pifsc/PIFSC/ESD/ARP/Photogrammetric%20Imagery" target ="_blank">Google Cloud Bucket</a>. Raw imagery is archived with NCEI and available on the <a href ="https://www.ncei.noaa.gov/access/ocean-exploration/video/" target = "_blank"> OER Portal</a>.
- For assistance and tools on how to adopt a similar strategy at your institution, contact the Data Services Team at <a href = "mailto:nmfs.pic.credinfo@noaa.gov">nmfs.pic.credinfo@noaa.gov</a>.</p>

## Public Tools
See our PIFSC github for python-based tools to assist with processing imagery for NODD, imagery validation, etc.

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="left" %}
{% include feature_row id="feature_row4" type="left" %}