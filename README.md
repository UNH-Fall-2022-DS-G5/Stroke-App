Introduction

Stroke is a medical emergency that can lead to instant death if prompt treatment is not available at the right time. There are many factors that cause a stroke. Based on a Kaggle data containing healthcare stroke data information, this project will predict how likely is a person to get a stroke.
The goal of this project was to identify variables that have a crucial impact on stroke patient types. The association between the different forms of stroke and several covariates, such as age, sex, hypertension level, heart diseases, marital status, smoking status along with several other features effecting the probability to increase the stroke, was examined using the logistic regression model.
The parameters were estimated using maximum likelihood estimation. When compared to stroke patients who do not have a history of diseases, those with a history of diseases had a 60% lower chance of suffering a hemorrhagic stroke. In other words, those with a history of disorders are more likely to experience a non-hemorrhagic stroke. Patients with stroke who don't have normal blood sugar levels are more likely to experience hemorrhagic strokes by a factor of two than stroke patients who do.
Blood sugar levels and a history of illnesses were elements that strongly influenced the various forms of stroke. With 5.8 million fatal instances per year, stroke is the second biggest cause of mortality after heart disease. 10% of all fatalities worldwide were due to strokes. Strokes affect adults under the age of 70 in 40% of cases.
Two-thirds of those who suffer from the estimated 15 million new acute strokes each year reside in emerging nations with poor and moderate incomes. There are hemorrhagic and non-hemorrhagic stroke variants. Non-hemorrhagic stroke is a kind of stroke that happens when a blood artery in the brain is blocked. According to estimates, non-hemorrhagic strokes account for more than 80% of stroke cases globally.

LITERATURE REVIEW
Heart disease comes in a variety of forms, and each one has unique signs, causes, and treatments. Some people's health can be significantly improved by making lifestyle modifications and taking medications. The most frequent type of heart condition is coronary artery disease (CAD). Your coronary arteries, which carry blood to your heart, may become blocked if you have CAD.
This may result in less blood flowing to your heart muscle, depriving it of the oxygen it requires. Atherosclerosis, often known as hardening of the arteries, is the condition that typically leads to the disease's onset. Chest pain is a symptom of coronary heart disease, and it can also cause a heart attack.
Some features that may affect a person’s probability to get a stroke are:
• Age
• Gender
• Genetics
• Obesity
• Smoking
• Stress
Heart disease: Your heart doesn't pump blood as efficiently as it should to meet your body's needs if you have heart failure. The most common cause is coronary artery disease, but other illnesses such thyroid disease, hypertension, cardiomyopathy, and others can also contribute to it. A small blood vessel known as the ductus arteriosus does not always close properly upon birth in some infants.
Heart is put under strain because of some blood returning to the pulmonary artery when this occurs. This can be treated surgically, through a procedure, or sometimes with medication. To prevent such possibilities this project enables a prediction model which predicts the possibility of having a heart stroke by taking in various inputs such as the above-mentioned features.
A data set has been cleaned and analyzed to which logistic regression is applied. Logistic regression is a regression analysis suitable when the dependent variable is binary. Like all regression analysis, logistic regression is predictive analysis.
Logistic regression is used to describe data and describe the relationship between a dependent binary variable and one or more independent variables at the nominal, ordinal, interval, or ratio level. Many people have tried to perform the analysis using different datasets and algorithms such as linear regression, kmeans, and all other supervised learning algorithms which are possible and suitable.
Scientists and engineers have also performed logistic regression which has been proved to be the most suitable method to predict the stroke that can occur depending on the various features available in the data set.
However, the main difference between their work and ours is the dataset, which plays a major role in our project. The dataset was cleaned using various data cleaning processes and was made available, because of which the accuracy of the model has been increased. All the details will be explained in the next coming sections.

Methodology

This research will consider using Logistic regression to predict the case of an individual based on features that were selected after training the data and discovering variables that have significant effect on whether an individual has stroke syndrome or not. Logistic regression was selected amongst other classification algorithms because of the dichotomous nature of the outcome variable.
With this adopted method of analysis, we will be able to determine the factors that have significant association with whether an individual is suffering from stroke or not. Prior to model building, dependencies within the independent variables will be reduced using correlation analysis to ensure all predictors are not highly correlated with each other.
Features with corresponding p-values that is less than 0.05 will be considered to have significant effect with whether an individual has stroke or not, and at the end, the predicting ability of the model will be evaluated by visualizing a confusion matrix, obtaining the evaluated model performance score and also, visualizing the ROC curve.
Data for the research was sourced from Kargle. It entails 12 health-related attributes. Series of data cleaning processes will be applied on the data to boost the prediction performance of the model. The original data downloaded from the website appears to be imbalanced as a result of disproportionate cases of individuals with stroke disease in relation with individuals with no stroke disease syndrome.

Results

Figure 1

Figure 2

Figure 3

Figure 4

Table 1

Table 2

Figure 5

Table 6

Discussion
Results from our analysis as revealed that out of 1070 participants who were randomly selected from the sample, bar chart has revealed that there exists more cases of individuals without stroke disease syndrome. The results can be visualized using a bar char as displayed in figure 1 below

In order to visualize the gender distribution, a bar-chart will be adopted to see number of males and females involved in the research. From our analysis, results have shown that (n=619) male and (n=451) respondents participated in the research. Further analysis which visualizes the average age of the respondents with respect to gender and whether they are facing stroke challenges or not is displayed below with error bars. The graph has shown that, the average age of men and women who have stroke challenges is between the age of 65 and 70. This prompts that age is probably a significant factor that predicts stroke prevalence the graphs as shown that it is prevalent among people of older age. See figure 3

The graph shown below also reveals the age distribution of respondents that were involved in the research as it shows that the distribution is slightly skewed to the left. Analytically, this means the sample has more older participants than the younger ones.

Correlation analysis was conducted to investigate the features that significantly affects the stroke prevalence and also ensure that the assumption of multicollinearity is properly maintained to take care of linear dependencies amongst the predictors. Although non of the variables is highly correlated with stroke prevalence and, however, features that exhibit higher correlation with stroke prevalence were selected. See correlation matrix below:

Results have shown that age(r=0.4869), hypertension(r=0.2349) heart disease (r=0.2560) and glucose levels (r=0.2324) all have weak but are relatively highly correlated with stroke prevalence.
See table 1

Model Training

In this section, we try to train out model to take the features to a second phase of selection. This time around, we are using our inferential knowledge in statistics to select suitable features that have corresponding p-values less than 0.05. The logit model built for this approach has revealed that age (b=0.8452, p<0.01), heart disease (b=0.2379, p<0.05) and average glucose level (b=0.1670, p ≅ 0.05 appears to have significant effect on whether an individual has stroke disease or not. Because the coefficient for age is positive, it means that higher age increases the odds of getting stroke. Our model shows that age has a coefficient value of 0.8452 which can be converted to an odd ratio = 2.238 which means a unit increase in age increases the odd of getting stroke by 2.238. Similarly, results from the analysis revealed a coefficient of 0.238 with an equivalent odd-ratio = 1.2685 which tells that individual who have hypertension are 1.239 times the odd of developing stroke disease than those that do not have hypertension and lastly, the model suggests that a unit increase in the average glucose level in the body can increase the odd of getting stroke by = 1.1818. The training accuracy of the model are 83.17% which is relatively high and tells that the model has learned the patterns in the dataset well enough. Testing the model with an unseen data resulted in a 78.82% model performance. By this we can say the model is quite good and will perform well for prediction. See table 1 for figures

Model evaluation

in order to be confident about the performance of the model, we will be needing to evaluate the logistic model. For this reason, the specificity and sensitivity analysis will be carried through the ROC curve will be used to evaluate the model and also confusion matrix will be used to know the counts of individual stroke cases that were correctly predicted.
Results from the analysis have shown that that the model is not making random guess for prediction as the ROC curve reveals a curve that that is relatively close to the top of the graph with a total area = 0.68 under the curve. This is an indication that that the model is good. See figure 5

Confusion matrix shown below has revealed that 216 observed data points for individuals who actually suffer from stroke disease were correctly predicted while 21 were wrongly predicted. Furthermore, results showed that 47 observed data points were wrongly predicted for individuals who suffer stroke disease and 37 were correctly predicted. See figure 6

Conclusion
The world would be a better place to live in if young adults can be aware of the old age illnesses. In this case study, stroke, which may occur based combination of numerous factors. This research has been able to identify a number of factors that seem to cause stroke disease which arguably, mostly occurs among people of old age. Based on the outputs obtained from the analysis, age appears to be standout as a major contributing factor to stroke risk. Since growing old is inevitable, it is believed that other contributing factor can be manipulated by human. Taking for example, one may consider to reduce their level of blood pressure after series of consultations and prescription of drugs from doctors. Our model will be contributing to the communities in the United States and beyond, as it will be published to reach the people who have access to the internet to consume the model built from this research, by inputting the limited features the model has identified to be linked with stroke risk human body system: (Age, level of hypertension and glucose level) which will enable them predict the odds of having the stroke illness in the coming future.  
Researchers who are interested in this area of study can go further to dig more factors that can improve the model and may also consider using interaction between predictors to see examine their interaction effect with the odds of stroke risk.
