# Pima-Indians-Diabetes-Analysis

This aim of this project is to predict whether a patient has diabetes based on various diagnostic measures. The dataset is originall from the National Institute of Diabetes and Digestive and Kidney Diseases. I came across this dataset on Kaggle, and further information regarding the context of the data can be found by opening the link below. 

https://www.kaggle.com/uciml/pima-indians-diabetes-database/download

Further insight into the data itself and understanding of its applications were obtained by going through the following research paper: 'Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus'

It can be accessed via this link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2245318/pdf/procascamc00018-0276.pdf

## Introduction

The goal of this project was to predict the onset of diabetes based on health metrics. The patients are all females 
that are atleast 21 years old. The metric provided in the dataset are: 

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)
- Outcome: Class variable (0 or 1)

## Data Exploration

The data was explored using different methods to obtain a sense of how the data is **distributed** and **correlated** with the presence of diabetes and with other features. Data visualizations such as **histograms**, **pair plots**, and **heat maps** helped obtain a statistical understanding of the data. 

During this stage, it was found that were were 0 values for many of the features for which a value of 0 was not possible. These inconsistencies were addressed to ensure the data was being interpreted properly and so that the values did not skew the statistical summary of the data (mean, median, distribution, etc.). 

Heatmap <br>
![alt tag](https://github.com/ShaktiB/Pima-Indians-Diabetes-Project/blob/master/Data%20Visualizations/heatmap.jpg)

## Data Preparation

The 0 values in the dataset were replaced with mean/median values based on the data distribution. The data was also scaled using the **RobustScaler**, which scales the data using the 25th and 75th percetiles. Scaling is an important step in **preprocessing** data as many algorithms (especially ones that use distance SVM, k-Means, etc.) require data to be on the same scale. This prevents certain features from having more "meaning" (bigger impact) during the learning process simply because they consist of bigger values compared to other features. 

Prior to implementation of machine learning algorithms, the data was split into **training**, **validaton**, and **test** sets. The validation set was used to evaluate the model and tune its hyperparamters. The test data was used at the end to compare each model's performance on new data which was *unseen* by the models. 

Ex: The **K** value in the k-NN model was tested to find the optimal value. <br>
![alt tag](https://github.com/ShaktiB/Pima-Indians-Diabetes-Project/blob/master/Data%20Visualizations/knnModelTuning.jpg)

## Machine Learning

The models used in this project are **SVM**, **Logistic Regression**, **k-NN**, and **Random Forests**. Models such as SVM and Logistic Regression were penalized for misclassification to help account for the imbalance in data (500 non-diabetic records, and only 278 diabetic records). 

### Model Evaluation 

The project problem is a classification problem, hence **Sensitivity**, **Specificity**, **AUCROC (Area Under the Curve of ROC)**, and **Accuracy** were used to evaluate the models' performance. Accuracy was the least important metric in this case due to the imbalane in data. For example, if a model's classification accuracy was 90% it would not be a valid representation of a *good* model if: 90/100 data points belonged to Class 1, 10/100 data points belonged to Class 2, and the model completely missclassified all of the Class 2 data points. In such a scenario, even though the accuracy is 90%, the model is unabl to accurately classify Class 2 data. 





 
