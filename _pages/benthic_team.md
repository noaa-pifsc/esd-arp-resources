---
title: "Benthic Surveys"
permalink: /benthic-surveys/
layout: splash
excerpt:  We monitor the benthos using various survey methods since the year 2000. In addition to NCRMP baseline surveys, we investigate coral bleaching events, support coral restoration, and track impacts of land-based sources of pollution. We rely on both imaging surveys and data recorded by divers <i>in situ</i> to collect benthic cover, coral demography, structural complexity, and corallivory data.
# "We monitor the benthos of coral reef ecosystems in the Hawaiian Archipelago, Mariana Archipelago, American samoa, and the Pacific Remote Island Areas since 2000."
header:
  overlay_color: "#323C46"
  overlay_image: https://media.fisheries.noaa.gov/2023-04/4000X3000-Fans-DTP-PIFSC.JPG
  caption: "Photo credit: Damaris Torres-Pulliza/NOAA"
  overlay_filter: "0.5"
  #overlay_filter: linear-gradient(rgba(15, 15, 15, 0.5), rgba(235, 150, 221, 0.36))

feature_row2:
- image_path: https://media.fisheries.noaa.gov/2023-04/500x391-coral-faces-DTP-PIFSC.gif
  image_caption: "2023 NCRMP. Credit: NOAA Fisheries/Damaris Torres-Pulliza"
  alt: "coral taxa and symbionts"
  title: "What do we survey"
  excerpt: We collect benthic data of shallow coral reef ecosystems (up to 100 ft). This means identifying, counting, and sizing different organisms on the seafloor. We conduct <b>coral demography</b> surveys (coral composition & condition of adults and juveniles), as well as <b>benthic cover</b> surveys (cover of algae, CCA, hard coral, and other taxa).  Read more on  benthic cover in the NCRMP Data Viz Tool <a href = "https://ncrmp.coralreef.noaa.gov/pages/ncrmp-data#BenthicSection" target= "_blank">documentation</a>.
  url: https://www.fisheries.noaa.gov/pacific-islands/ecosystems/coral-health-and-threats-pacific-islands
  btn_label: "More on Coral Health & Threats"
  btn_class: "btn--primary"
feature_row3:
- image_path: https://www.fisheries.noaa.gov/s3//2024-07/5472x3648-NCRMP-diver-Maui-Fisheries-PIFSC.JPG
  image_caption: "Diver collecting SfM imagery. Credit: NOAA Fisheries/Lori Luers"
  alt: "diver conducting SfM survey"
  title: "How do we survey"
  excerpt:  As of 2023, we mainly use image-based surveys to collect benthic observations. Divers collect both <b>photogrammetry models</b>, stitching together thousands of images of a site, as well as <b>photoquadrat</b> imagery, relying on “unstitched” single images of a site. Using photogrammetry we can build 3D models of the coral reef and extract data, including coral demographic data (measured by divers in situ before 2024). The photoquadrat imagery is annotated with the AI tool CoralNet to provide estimates of benthic cover. We conduct surveys at both fixed and random sites; random sites allow us to provide geographically comprehensive estimates of data for an island or region, whereas fixed sites allow us to compare changes in the benthos over time at the same site, such as growth of specific coral colonies. We utilize machine-learning and also develop CoralNet Classifiers such as the <a href = "https://doi.org/10.25923/d0re-9y93" target ="_blank">semi-automated CoralNet Bleaching Classifier</a>.
feature_row4:
- image_path: https://media.fisheries.noaa.gov/2022-05/3977X2379-20220519-DTP-surveys-n-COTS-PIFSC.JPG
  image_caption: "Diver assesses coral predation. Credit: NOAA Fisheries"
  alt: "diver conducts coral demography survey and detects COTS predation"
  title: "What do we measure"
  excerpt: Our benthic cover raw data includes <b>CoralNet point annotations</b>, produced with the identification of benthic taxa under random points on photoquadrat imagery. The coral demographic data includes <b>identification, counts, and sizes of juvenile and adult hard coral colonies</b>, with conditions for adult hard corals (disease, bleaching, etc.). For example, in this photo, a diver is noting the stark white patch on the coral colony left from predation by crown-of-thorns seastars.
  url: #test-link
  btn_label: "Placeholder"
  btn_class: "btn--primary"
feature_row5:
- image_path: https://media.fisheries.noaa.gov/2022-05/4000X2782-TG6C-consulting-PIFSC.JPG
  image_caption: "2022 MA NCRMP: Divers deliberate. Credit: NOAA Fisheries"
  alt: "training materials"
  title: "Training materials"
  excerpt: Photogrammetry training and other community resources are available on <a href ="https://www.lai-network.org/" target = "_blank">LAI-NETWORK</a>. To correctly identify coral species as well as their condition, such as causes of predation, our coral experts undergo thorough training. To mitigate diver biases, we routinely run and analyze our data for potential diver biases and have regular discussions to normalize our data and surveys. Please contact us for access to more training materials.
  url: #test-link
  btn_label: "Placeholder"
  btn_class: "btn--primary"

---

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}
{% include feature_row id="feature_row4" type="left" %}
{% include feature_row id="feature_row5" type="right" %}


## Why do we survey
By revisiting these regions since 2000, and with a stable, stratified random survey design since 2013, we can monitor and see how coral reef ecosystems are changing over time such as higher or lower coral cover, or coral recruitment or loss. We produce technical memoranda for policy makers that provide a summary of the status of coral reefs and inform management decisions. We can also integrate our benthic data with our fish and oceanographic data to investigate patterns in ecosystem shifts.

## GitHub Repository
Currently we are working on making our scripts, such as one to summarize CoralNet data, public. Please contact us if you would like access.

## Access Data
<ul>
<li>
Under <a href= "{{ site.baseurl }}/products/">Products</a> you can visualize and access our data using the NCRMP Visualization tool. </li>
<li>Go to <a href = "/sops/">Methods</a> to see access for specific datasets. </li>
<li>For raw data, our data is organized in NCEI collections and also described in our NCRMP  <a href = "https://www.fisheries.noaa.gov/inport/item/28844" target ="_blank">InPort metadata catalog</a>, organized by region.</li>
<li>Access SfM imagery with <a href = "https://console.cloud.google.com/storage/browser/nmfs_odp_pifsc/PIFSC/ESD/ARP/Photogrammetric%20Imagery" target ="_blank">NODD Google Cloud bucket</a>, or make a request through the <a href ="https://www.ncei.noaa.gov/access/ocean-exploration/video/" target = "_blank">OER Portal</a>.</li>
</ul>

## Contact
<ul>
<li>Principal Investigator: Thomas Oliver <a href="mailto:thomas.oliver@noaa.gov"> (thomas.oliver@noaa.gov)</a></li>
<li>Data Services Team: <a href="mailto:nmfs.pic.credinfo@noaa.gov">nmfs.pic.credinfo@noaa.gov</a></li>
</ul>