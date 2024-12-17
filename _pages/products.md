---
title: "Products"
permalink: /products/
layout: splash
excerpt: "Tools that allow users to interact with our data as well as products developed by the Ecosystem Sciences Division (ESD)"
header:
  overlay_color: "#000"
  overlay_filter: linear-gradient(rgba(95, 253, 253, 0.5), rgba(8, 8, 8, 0.9))
  overlay_image: /assets/images/ncrmp_data_viz_snap.png
  caption: "NCRMP Pacific Fish Dashboard Screenshot"

feature_row2:
- image_path: /assets/images/ncrmp_data_viz_dashboard.png
  alt: "ncrmp vis tool"
  title: "NCRMP Visualization Tool"
  excerpt: "Interact with our random site data such as benthic cover and fish diversity and biomass"
  url: https://ncrmp.coralreef.noaa.gov/
  btn_label: "Go to Landing Page"
  btn_class: "btn--primary"
  target: "_blank"
feature_row3:
- image_path: https://github.com/MichaelAkridge-NOAA/ncei_eds_codespace/raw/main/docs/02.png
  alt: "environmental data summary"
  title: "Environmental Data Summary (EDS)"
  excerpt: Use this codespace to run your own EDS models. Access original repository <a href ="https://github.com/krtanaka/ncei_eds" target ="_blank">here</a>.
  url: https://github.com/MichaelAkridge-NOAA/ncei_eds_codespace
  btn_label: "EDS Codespace"
  btn_class: "btn--primary"  
  target: "_blank"

feature_row4:
- image_path: assets/images/pacioos-eco-geospatial-tool.png
  alt: "pacioos amsm coral reef drivers"
  title: "Eco-geospatial tool American Samoa"
  excerpt: "PACIOOS hosted American Samoa Coral Reef Ecosystem Drivers tool from data gathered by the Ecosystem Sciences Division (ESD)"
  url: https://www.pacioos.hawaii.edu/projects/coral-drivers-amsam/#data
  btn_label: "Go to PacIOOS Page"
  btn_class: "btn--primary"
  target: "_blank"

feature_row5:
- image_path: https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg
  alt: "shiny app"
  title: "Shiny App"
  excerpt: "Placeholder for Juliette's shiny app"
  url: #test-link
  btn_label: "Placeholder"
  btn_class: "btn--primary"
  target: "_blank"

---
{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}
{% include feature_row id="feature_row4" type="left" %}
{% include feature_row id="feature_row5" type="right" %}
