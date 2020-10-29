---
layout: post
title: Covariate Importance
tags: ["landscape analysis", "slope units"]
categories: figures
comments: false
---

## Regression Overview
Logistic regressions are commonly used to predict the presence or absence of features, which makes them well suited for the creation of landslide susceptibility models. In addition, logistic regressions are used to determine the importance of the covariates included in the model. The discussion below details my use of a logistic regression analysis to determine which landslide susceptibility factors influence the occurence of deep-seated landslides in the North Island of New Zealand.

First, a note on methods. For this analysis, a balanced dataset of roughly 1000 landslide occurences and 1000 landslide absences was used to train\test the logistic regression model, and 15 susceptibility factors were used as the explanatory variables. Before use in the model, these explanatory variables were first standardized using the formula:
<div align="center">
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=Standarized&space;Value&space;=&space;\frac{Value-Mean}{Standard&space;Deviation}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?Standarized&space;Value&space;=&space;\frac{Value-Mean}{Standard&space;Deviation}" title="Standarized Value = \frac{Value-Mean}{Standard Deviation}" /></a>
<br>
</div>
This transformation standarizes the distributions of the covariates, and allows the regression coefficients to be used as an assesment of variable importance. Once standardization was complete, a 10-fold cross-validation and a L1 (LASSO) regularization (lamnda=5) was used to train the model and asses its performance. Overall the cross-validated regressions produced an average AUC of 0.85 and a classification accuracy of 77%.

## Model Coefficients and Significance
The regression identified six significant susceptibility factors (see figure below):
1. Presence of Whanganui Basin sandstones and mudstones (Whanganui Basin)
2. Slope (Slope)
3. The amount of alignment between bedding attitude and slope attitude (Slope and Bedding Alignment)
4. The amount of valley incision (Incision)
5. The roughness of the terrain (Elevation (STD))
6. Concave hillslopes (Profile Curvature)

Overall the absolute values of the regression coefficients also decreased in this order, with the presence of Rangitikei Supergroup bedrock being much more influential than the other factors. The charts below are interactive so feel free to explore them!
{% include plotly/lr_coefficient.html %}

## Jacknife Regresions
In addition to coefficent magnitude, coviariate importance can also be assessed using jacknife regressions. This procedure looks at value of a model's AUC when each coviariate is used inidividually, and when all covariates except one are used. In the former case, high AUCs point to important variables and in the latter case the opposite is true.
{% include plotly/lr_jth.html %}
{% include plotly/lr_allbutjth.html %}
My interpretaion of this data is that the significant landslide susceptibility factors identifed in this analysis can broadly be put into three groups. The most influential group includes only the bedrock geology covariate and is associated with the long-term strength of terrain. The medium influential group contains slope, bedding alignment, and incison, and is associated with current to recent-past landscape evolution. And finally, the least influential group includes profile curvature and surface roughness, which do not cause landslide occurrence, but rather increase as a result.

## Principal Components Analysis
Using a PCA analysis of the significant covariates, no discernible differences between the three major landslide classes was found.
{% include plotly/lr_pca.html %}
Likewise, landslide size does not appear to effectively group the PCA resluts.
{% include plotly/lr_pca_size.html %}