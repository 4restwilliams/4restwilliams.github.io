---
layout: post
title: Optimization of Slope Units
tags: ["landscape analysis", "slope units"]
categories: figures
comments: false
---

The [r.slopeunits](http://geomorphology.irpi.cnr.it/tools/slope-units) algorithim is a tool for automatically delineating hillsides (slope units) and provides a real-world unit for measuring landscape parameters such as slope or aspect. The algorithim results vary however based on two key input parameters: circular variance and minimum slope unit area. To determine the best combination of inputs, we use an objective function to measure the performance of many different combinations. The graph below plots the runs of r.slopeunits with different minimum area/circular variance against their optimization function score.
{% include plotly/surface.html %}
Based on this graph, we can tell that a circular variance of 0.2 and minimum area of 1500 m<sup>2</sup> provide us with the highest optimization function score, and thus, the best delineation of hillsides!