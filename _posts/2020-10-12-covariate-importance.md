---
layout: post
title: Covariate Importance
tags: ["landscape analysis", "slope units"]
categories: figures
comments: false
---

## Regression Overview
Logistic regression is commonly used to model to predict the presence or absence of features, which makes it well suited for the creation of landslide susceptibility models. In addition, logistic regression can be used to determine the importance of landslide susceptibility factors. The discussion below details my use of a logistic regression to determine the importance of landslide susceptibility for deep-seated landslides in the North Island.

First, a note on methods. For this analysis, a balanced dataset of roughly 1000 landslide occurences and 1000 landslide absences were used to train\test the logistic regression model, and 15 susceptibility factors were used as the explanatory variables. Before use in the model, these explanatory variables were first standardized using the formula:
<div align="center">
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=Standarized&space;Value&space;=&space;\frac{Value-Mean}{Standard&space;Deviation}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Standarized&space;Value&space;=&space;\frac{Value-Mean}{Standard&space;Deviation}" title="Standarized Value = \frac{Value-Mean}{Standard Deviation}" /></a>
<br>
</div>
This transformation standarizes the distributions of the covariates, and allows the regression coefficients to be used as an assesment of variable importance. Once standardization was complete a 10-fold cross-validation and an L1 (LASSO) regularization (lamnda=5) was used to train the model and asses its performance. Overall the cross-validated regressions produced an average AUC of 0.85 and a classification accuracy of 77%.

## Model Coefficients and Significance
The regression identified six significant susceptibility factors (see figure below):
1. Presence of Rangitikei Supergroup sandstones and mudstones (rangitikei)
2. Slope (slope)
3. The amount of alignment between bedding attitude and slope attitude (tobia)
4. The amount of valley incision (incision)
5. The roughness of the terrain (std_elev)
6. Concave hillslopes (profc)

Overall the absolute values of the regression coefficients also decreased in this order, with the presence of Rangitikei Supergroup bedrock being much more influential than the other factors. The charts below are interactive so feel free to explore them!
{% include plotly/lr_coefficient.html %}

## Jacknife Regresions
In addition coefficent magnitude, coviariate importance can also be assessed using jacknife regressions. This procedure looks at value of the model's AUC when each coviariate is used inidividually, and when all covariates except one are used. In the former case, high AUCs point to importance variables and in the latter case the opposite is true.
{% include plotly/lr_jth.html %}
{% include plotly/lr_allbutjth.html %}
My interpretaion is that this analysi points to three groups of significant covariates which also fit neatly into susceptibility factor categories. The most influential group includes only the bedrock geology covariate and is associated with the long-term strength of terrain. The medium influential group contains slope, bedding alignment, and incison, and is associated with current to recent-past landscape evolution. And finally, the least influential group includes profile curvature and surface roughness, which do not cause landslide occurrence, but rather increase as a result.