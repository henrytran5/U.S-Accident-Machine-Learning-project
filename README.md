●U.S Accident dataset

Content:

The data collected is a countrywide car accident dataset, which covers 49 states of the USA. The accident data are collected from February 2016 to June 2020. including two APIs which provide streaming traffic event data. These APIs broadcast traffic events captured by a variety of entities such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road-networks. Currently, there are about 3.5 million accident records in this dataset\
Purpose:

Based on the insight of dataset, we can work on data analytics process by Python, R language, Tableau, and Power BI to answer the following questions:
+ What is the trend of number of accidents from USA?
By breaking down this data by severity of the accident as the capture below, we can see:

- The grey line indicates the total of accidents which are increase year by year
- The orange indicates the accidents with severity 2 (Medium) which have the same trend.
- The remaining have the small proportion and not much change over the year.
+ What is city having the highest number of accidents?
+ How is the distribution of accident by severity?
+ How about the weather impact on the severity of accident?

Apply Statistical model and Machine Learning:

Finally, we apply Machine Learning model to predict the severity of accident base on the condition of weather, the actual weather at the time of accidents like temperature, wind direction, sunrise, sunset, ...\
Two statistical models will be applied are Logistic Regression and Random Forest. The AUC will be used to determine the accuracy of the model and based on this AUC; we can decide whether we can use this model to detect the severity of the accidents.\
The predictive results can be used to make it easier for the police to grasp the situation to allocate reasonable human resources to solve problems.\

The dataset contains 3,500,000 rows and 48 attributes (columns).\
Attributes are severity_map, start time, end time, start latitude, start longitude, distance, city, state, street, county, weather stamptime, zipcode, temperature, humidity, wind, pressure, visibility, wind speed, weather condition, traffic claiming, traffic signal, sunset sunrise, etc.\
\
ELT process: Extract- Load-Transform dataset.\
Extract: After collect raw dataset from many source locations, we will extract data as dataset can consist of many data types and come from virtually any structured or unstructured source.\
Load: the transformed data is moved from the staging area into a data storage area, or between many storing software.\
Transform: data is to change values to new values for the purport of analytics process.\ 
•	Filtering, cleansing, de-duplicating, validating and authenticating the data.\
•	Performing calculations, translations, data analysis or summaries based on the raw data.\ 
•	Removing, encrypting, hiding, or otherwise protecting data.\
•	Formatting the data into tables or joined tables based on the schema deployed\
         - Find outliers, anomaly detection, missing values, duplicate values, histogram, bar charts, line charts.\
         - Find accuracies, AUC values, ROC curves based on the target attribute to making decisions.\
         - Quantitative analyst for statistical models.\
         - Building, developing, and maintaining statistical models for whole dataset in Python and R language.\

Apply Statistical model and Machine Learning:

- Using statistical models as Random Forest, Logistics based on 47 attributes and 1 target attribute of the severity of Accident (severity_map coloumn) with the classification goal is to predict the severity and the police can save time to assess and allocate reasonable human resources to solve problems.
