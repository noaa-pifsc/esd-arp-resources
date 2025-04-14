---
title: "Access Data"
permalink: /accessdata/
layout: splash
excerpt: "Our data is typically organized by <b>region</b> and <b>site type</b>, such as random versus permanent (fixed) sites. Accordingly, raw data must be analyzed in the specified manner for each methodology.  See options for data access below."
header:
  overlay_color: "#C2D9E3"
  overlay_filter: "0.4"
  overlay_image:  /assets/images/accessdata-banner.jpg
  # overlay_filter: linear-gradient(rgba(0, 133, 202, 0.38), rgba(0, 48, 135, 0.6))

  #overlay_filter: linear-gradient(rgba(0, 0, 0, 0.4), rgba(255, 255, 255, 0.41))
  caption: "Photo credit: NOAA Fisheries"
  actions:
   - label: "Browse Metadata"
     url: /metadata_catalog/
feature_row2:
- image_path: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmcO5tHXjtN5CEzy1KMGDeVuLNn52DYvVttw&s
  alt: "coris image"
  title: "NOAA CoRIS"
  excerpt: "Access our data on NOAA Coral Reef Information Systems (CoRIS)."
  buttons:
  - url: "https://www.coris.noaa.gov/"
    btn_label: "Go to CoRIS"
    btn_class: "btn--primary"
feature_row3:
- image_path: https://www.pacioos.hawaii.edu/wp-content/uploads/2016/06/PacIOOS-logo-stacked-small.jpg
  alt: "pacioos image"
  title: "PacIOOS"
  excerpt: "Access our data and related tools in the Projects section."
  buttons:
  - url: "https://www.pacioos.hawaii.edu/"
    btn_label: "Go to PacIOOS"
    btn_class: "btn--primary"
feature_row4:
- image_path: https://www.pmel.noaa.gov/ocs/sites/default/files/thumbnails/image/ERDDAP_Data_Access.png
  alt: "errdap image"
  title: "CRCP ERRDAP"
  excerpt: "Go to tabledap to see CRCP datsets or use the video tutorial provided."
  buttons:
  - url: "https://www.ncei.noaa.gov/erddap/index.html"
    btn_label: "Go to CRCP ERRDAP"
    btn_class: "btn--primary"
---


<style>
/* Custom Button Style */
/* Style the custom button */
.custom-button {
  background-color:  #90DFE3;  /* Remove background */
  color: rgb(255, 255, 255);                 /* Inherit the text color */
  /*border: 2px solid #00797F;      /* Add a border */
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
  background-color: #005E5E;      /* Light background color on hover */
  border-color:rgb(84, 86, 87);          /* Darker border color on hover */
  color:rgb(255, 255, 255);                 /* Change text color on hover */
  text-decoration: none;  
}


</style>
# Visualize NCRMP Random Site Data via  <a href ="https://ncrmp.coralreef.noaa.gov/">NOAA Data Viz Tool</a> / NOAA GeoPlatform
- Browse by dashboard type to view and download data. For caveats and more on the NCRMP program, including surveys in the Atlantic <a href = " https://noaa.hub.arcgis.com/pages/4976333fbf884f26b2fdc9ac51a20576" target = "_blank">here</a>.<br><i>Note: this only includes <b>random</b> site data.</i>

<br>
# Raw Data via NCEI / Described on InPort
- Raw data is archived with NCEI within Collections and can be searched using <a href ="https://data.noaa.gov/onestop/">NOAA's OneStop Platform</a>.
- NCRMP data is typically submitted by mission, and each dataset will have a specific landing page with NCEI. To access links for all missions for a given datastream, refer to the InPort metadata record.
- When searching data, note the distinction for site type and region. For example fixed-site imagery is described separately from random site imagery for each distinct region. For convenience, Ecosystem Sciences Division InPort metadata can be browsed here: [Browse Available ESD Metadata]({{ site.url }}/metadata_catalog/){: .custom-button} or you may browse within the InPort <a href = "https://www.fisheries.noaa.gov/inport/item/2712" target ="_blank">PIFSC CREP Metadata Portfolio</a>. 
- For inquires on how to best work with NCRMP data and sampling design please contact <a href = "mailto:nmfs.pic.credinfo@noaa.gov">nmfs.pic.credinfo@noaa.gov</a>.
<br>

<div style="display: flex; gap: 1rem; align-items: flex-start; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 250px;">
<img src="{{ '/assets/images/Methods-Island-Scale-Surveys-PIFSC.png' | relative_url }}" alt="Fixed vs Random Site Island Scale" style="width: 100%;">
    <p><em>Diagram illustrating fixed versus random site locations for a given hypothetical island. Credit: NOAA Fisheries</em></p>
  </div>
  <div style="flex: 1; min-width: 250px;">
    <img src="https://www.fisheries.noaa.gov/s3//styles/media_750_x500/s3/2024-06/1138x720-Pacific-Islands-Region-map-Fisheries-PIFSC.png?itok=5oaDDT8f" alt="Pacific Island Regions" style="width: 100%;">
    <p><em>Data may be organized into Hawaiian Archipelago, Mariana Archipelago, American Samoa, and Pacific Heritage Islands Marine National Monument (formerly Pacific Remote Island Areas). Credit: NOAA Fisheries</em></p>
  </div>
</div>

<br>

# SfM/Photogrammetry Imagery via Google Cloud Bucket (NODD)
- Due to the size of structure-from-motion (SfM) imagery, raw imagery as well as products are available via our <a href= "https://console.cloud.google.com/storage/browser/nmfs_odp_pifsc/PIFSC/ESD/ARP/Photogrammetric%20Imagery" target ="_blank">Google Cloud Bucket</a>. Raw imagery is archived with NCEI and available on the <a href ="https://www.ncei.noaa.gov/access/ocean-exploration/video/" target = "_blank"> OER Portal</a>.
- For assistance and tools on how to adopt a similar strategy at your institution, contact the Data Services Team at <a href = "mailto:nmfs.pic.credinfo@noaa.gov">nmfs.pic.credinfo@noaa.gov</a>.


<br>

# R Processing Scripts
-  Our data is still being updated into public-ready form and will become available on <a href = "https://github.com/noaa-pifsc" target = "_blank">PIFSC github</a>.


<br>
# Public Tools
See our PIFSC github for python-based tools to assist with processing imagery for NODD, imagery validation, etc.
<br>

***

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="left" %}
{% include feature_row id="feature_row4" type="left" %}