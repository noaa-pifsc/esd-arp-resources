---
layout: survey_template
title: "Survey template"
permalink: /surveys/test_survey

header:
  overlay_color: "#000"
survey_type: survey type
description: "Add a description here"
feature_row2:
  - image_path: "assets/images/default-sop.jpg"
    alt: "sops"
    title: "SOPs"
    excerpt: "Standard operating Procedures detailing methods"
    url: "https://example.com/sops"
    btn_label: "Download"
    btn_class: "btn--primary"
feature_row3:
  - image_path: "assets/images/default-datasheets.jpg"
    alt: "data sheets"
    title: "Data Sheets"
    excerpt: "Details about data sheets"
feature_row4:
- image_path: "assets/images/default-rawdata.jpg"
  alt: "access raw data"
  title: "Access Raw data"
  excerpt: "Browse raw data for datastream"
  url: #test-link
  btn_label: "Placeholder"
  btn_class: "btn--primary"
feature_row5:
- image_path: "assets/images/default-rcode.jpg"
  alt: "R code"
  title: "R code for processing data"
  excerpt: "See our team scripts for processing raw data"
  url: #test-link
  btn_label: "Placeholder"
  btn_class: "btn--primary"
sidebar:
  nav: "docs"
---

{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="right" %}
{% include feature_row id="feature_row4" type="left" %}
{% include feature_row id="feature_row5" type="right" %}
