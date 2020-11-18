---
layout: post
title: Regression Analysis
tags: ["landscape analysis"]
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
This transformation standarizes the distributions of the covariates, and allows the regression coefficients to be used as an assesment of variable importance. Once standardization was complete, a 10-fold cross-validation and a L1 (LASSO) regularization (lamnda=5) was used to train the model and asses its performance.

## Comparison of Regression Flavors
After the first iteration of the logistic regression analysis, I investigated two different alterations to the framework of the regression: limiting the analysis to the Rangitikei Supergroup (Whanganui Basin Sediments), and basing association of the covariates with the landslides one their boundaries directly, instead of their associated SLUs. The result accuracies of these approaches (represented by AUC) are shown below.
{% include plotly/20201116_study_comparison.html %}

These boxplots represent the range of AUC values obtained from 10 cross-validated regressions for each of 10 negative sample sets (100 total regressions) for planar rock slides and rotational rock slides. Overall, there was not a large difference between models that included the full dataset and the models that were constrained to the Rangitikei Supergroup. The use of SLUs however did reduce the accuracy of the models. Since the non-bedrock relationships are clearer in the Rangitikei Supergroup resricted models, and using SLUs worsened the regression, all following analyses are restricted to the Rangitikei Supergroup and do not use SLUs to aggregate the data.

## Variation of the Negative Sample Set
At the last meeting, Hugh mentioned that differents sets of negative sample should be tested to determine if the choice of the negative sample set was affecting the accuracy of analysis. To test this, I created 10 negative sample sets and compared the variation in AUC values between the negative sample sets to the internal variation in AUC that results from the cross-validation analysis.
{% include plotly/20201116_auc_cv_v_negatives.html %}

These boxplots show that the variation in AUC caused by negative sample selection is much less than the variation caused by the cross-validation process, suggesting that negative sample selection has a small impact on the analysis.

## Addition of New Covariates
Several new covariates were also added to the analysis. These include six classes that reference Rantikei Supergroup members, the percent of forest cover, Distance to river (Strahler Order 3 and above), Stream Power Index, and maximum elevation. Maximum elevation ended up being highly correlated with the standard deviation of the elevation and was ultimately removed. The correlation coefficient for each set of covariates can be found below.
{% include plotly/20201116_correlation.html %}

Interestingly, Slope and Bedding Alignment is weakly correlated with many covariates, even those unrelated to slope and bedding attitude. Additionally, forest cover and the Rangitikei Supergroup members were ultimeately removed from the analysis because they added little to the model and obscured some important relationships.

## Rock Planar Slide and Rock Rotational Slide Regressions
Per Sam's suggestion, I split the regression analysis by landslide type. This has yielded interesting results for each slide type. The graph below shows the average coefficent values for Rock Planar Slides
{% include plotly/20201116_coeff_planar_sub.html %}

And this graph displays the results for Rock Rotational Slides
{% include plotly/20201116_coeff_rotational_sub.html %}

Splitting the regression provides us with interesting into the differing mechanisms between these features. For example, Slope and Bedding Alignment is an important factor for planar, but not rotational slides, and River Incision is more important for rotational slides. Additionally, concave curvatures are important for identifying rotational slides, but not for planar slides.
