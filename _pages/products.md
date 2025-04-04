---
title: "Products"
permalink: /products/
layout: splash
excerpt: "Tools that allow users to interact with our data as well as products developed by the Ecosystem Sciences Division (ESD)."
header:
  overlay_color: "#323C46"
  overlay_filter: "0.75" 
  # overlay_filter: linear-gradient(rgba(2, 2, 2, 0.81), rgba(255, 255, 255, 0.75),rgba(2, 2, 2, 0.81))
  overlay_image:  /assets/images/ncrmp_data_viz_snap.png
  caption: "NCRMP Pacific Fish Dashboard Screenshot"
  actions:
    - label: "Search Reports & Publications"
      url: /publications/
feature_row2:
- image_path: /assets/images/ncrmp_data_viz_dashboard.png
  image_caption: "Dashboard Screenshot 2024"  
  alt: "NCRMP viz tool dashboard screenshot"
  title: "NCRMP Visualization Tool"
  excerpt: "Interact with our random site data such as benthic cover and fish diversity and biomass by selecting a Pacific dashboard."
  buttons:
  - url: https://ncrmp.coralreef.noaa.gov/
    btn_label: "Go to Landing Page"
    btn_class: "btn--primary"
 # target: "_blank"

feature_row3:
- image_path: https://github.com/MichaelAkridge-NOAA/ncei_eds_codespace/raw/main/docs/02.png
  image_caption: "EDS Screenshot 2024"  
  alt: "environmental data summary codespaces screenshot"
  title: "Environmental Data Summary (EDS)"
  excerpt: Use this codespace to run your own EDS models. Access original repository <a href ="https://github.com/krtanaka/ncei_eds" target ="_blank">here</a>.
  buttons:
  - url: https://github.com/MichaelAkridge-NOAA/ncei_eds_codespace
    btn_label: "EDS Codespace"
    btn_class: "btn--primary"  
 # target: "_blank"

feature_row4:
- image_path: assets/images/pacioos-eco-geospatial-tool.png
  image_caption: "PACIOOS Screeshot 2024"  
  alt: "pacioos amsm coral reef drivers tool screenshot"
  title: "Eco-geospatial Tool American Samoa"
  excerpt: "PACIOOS hosted American Samoa Coral Reef Ecosystem Drivers tool from data gathered by the Ecosystem Sciences Division (ESD)."
  buttons:
  - url: https://www.pacioos.hawaii.edu/projects/coral-drivers-amsam/#data
    btn_label: "Go to PacIOOS Page"
    btn_class: "btn--primary"
 # target: "_blank"

feature_row5:
- image_path:  assets/images/amsm_data_project_tool_screenshot.png
  image_caption: "Dashboard Screenshot 2024"  
  alt: "american samoa data project tool screenshot"
  title: "American Samoa Data Dashboard"
  excerpt: "This R Shiny dashboard provides information on American Samoa coral reef monitoring programs, data collection methods, and site-specific location data. Benthic cover, coral reef fish surveys, and environmental data can easily be displayed in interactive ways to support and inform American Samoa coral reef stewardship."
  buttons:
  - url: https://connect.fisheries.noaa.gov/american_samoa_data_integration/
    btn_label: "Explore "
    btn_class: "btn--primary"
 # target: "_blank"

---
{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}
{% include feature_row id="feature_row4" type="left" %}
{% include feature_row id="feature_row5" type="right" %}
