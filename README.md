# Capstone_Project

## Write a short introduction to your project.
In this project , i am going to leverage Azure to predict whether an Account (Point of Contact/Customer) will go Bankrupt or not. This is very important because a Customer get a lot of products from the beverage Manufacturer. In order to do faster transactions , beverage manufacturer gives credit limit and Payment terms for its customers. But when the Customer goes bankrupt , the money which is in Credit will be lost to the beverage manufacturer so it is very much essential to the BM (beverage manufacturer) to set up the right credit limit and revise the credit limit often and also when we know in advance or if we are able to predict a customer going bankrupt than the BM can take necessary actions by reducing the credit limit or change the payment patterns for those customers so that the BM does not lose any money. Considering the COIVD era , there are lot of small customers went bankrtupt so it is very much essentail for any business to have this model which predicts the whether the customer will go bankrupt or not. Risk Exposure of the BM will be reduced by taking proactive actions based out of the predictive model. 


## Project Set Up and Installation
For this project , i have used my own Azure subscription. The data for this collated from various data sources from the external site which talks about how good is a customer financial status and internal data like BM's sales order and buying pattern for all the different pocs are studied with the detailed explorary analysis and than merged togother into single dataset for the prediction. 

In order to make this as a professional project , the various data sources of Internal data and external data has to be queried into the Data bricks and the pipeline has to be created and the refresh of the model has to take place once in a month or once in 2 months to understand the risky customers. By this visibility , Risk team can review the accounts who are under the risk zone and also can understand the movements of the risky pocs in the form of trend.  Based on these visibility , BM's can take necessary actions to mitigate the risk. 


## Dataset
As explained above ,the dataset used above is a combination of internal and external data due to the limiation of the projects i do not want deep dive in the formation of the various features which were created in the model. Basically most of hte features for the data were created based on the business knowledge and discussion wiht the SME's/ 

Various features were collated for the model were aggregated at POC level , each row in the excel corresponds to one POC and it has 41 columns in total. Column name "FLAG_BAD_DEBT" corresponds to the Target column which tells whether a POC has gone bankrupt in the past or not. Objective for the Machine learning model is to study those Bankrupt POCs and Not a Bankrupty POC in detail using hte other 39 features and than simulate the same for the new data to get the Bankrupt POCs 

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
As discussed in the above previous steps , Objective is predict the Bankrupt POCs which will help the BM to mitigates its risk exposure. Several features were built like Standard devaiation of Account receivables , Average credit utlization based on the detailed understanding of the data. 



### Access
*TODO*: Explain how you are accessing the data in your workspace.
I have accessed the data using 2 ways : 
1)  Data has uploaded into the Github and accessed in azure through Raw github user content
2)  Data has been direcly uploaded as a part of folder in the Azure drive and than directly read that file as pd.read csv , but the problem with this method , azure does not process any of the data as a data table so it has be converted as a Tabular file

Hence the first method was preferred than the second method and data set is also registed in the dataset. below is the screenshot of the same. 

![image](https://user-images.githubusercontent.com/92014201/144088136-30414ed6-345a-410d-8f5a-a0f112e2922d.png)


## Automated ML  
Automl config class is way of leveraging the SDK to automate ML , Below are the different parameters which have been used in my model : 

Task Type : Classification , here in this problem we would like to predict whether an account will go bankrupt or not 

training dataset : POC Dataset , data which has all the features except the POC ID and hte bankruptcy month 

label column : Target column which specifies whether a POC has gone bankrupt or not 

enable_early_stopping : Whether to enable early termination if the score is not improving in the short term 

featurization: hether featurization step should be done automatically or not , in this project i have set it to auto which i would need to have more features in the model 

max_concurrent_iterations: Represents the maximum number of iterations that would be executed in parallel 

primary_metric: norm_macro_recall - since in the current project , focus is more on the preventing the FN , rather than the overall Accuracy Recall Maximization function has been used 

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

## First Iteration : 
Automl model was run with the Primary metric : AUC Weighted , below is the screenshot of the name 

![image](https://user-images.githubusercontent.com/92014201/144278323-e04bf573-3215-4bfc-94ee-c8115a1d4732.png)

Problem with this model is that it really gives a very good overall accuracy , but when you look into the False Negative it is very high. For the current problem which we are trying to solve the False Negatives have to minimum , because if there is account in Actual bankrupt but the prediction says it is not a bankrupt is more critical because BM (beverage Manufacurer) will be losing the money which was given in credit if the pro active actions were not taken.  

On the other hand , for False Positives which means Model predicts they are bankrupt customers and finally they are not bankrupt so it does not have any financial impact to the company. But while the False Negative will have Financial impact hence importance of the model should be focused more on reducing the False Negatives. 

But in the below confusion matrix , even though we have an overall accuracy of 99.3% , the Recall is 0 because there are not True Positives in the below conufusion metrics. 
Hence the Primary metric was changed for the second iteration to minimized the False Negatives , meaning the focus should to increase the Recall. 
![image](https://user-images.githubusercontent.com/92014201/144278032-b2c2c7d2-4eda-456a-877d-e1ef75768c80.png)


## Second Iteration : 
As discussed in the above  , primary metric was changed from "AUC WEIGHTED" to "NORM_MACRO_RECALL" , to improve the Recall accuracy, Below are the details which shows the completed status of the Auto Ml and also the confusion matrix for this model. 

Screenshot of the Model showing , "NORM_MACRO_RECALL" as a primiary metric and its corresponding accuracy 
![image](https://user-images.githubusercontent.com/92014201/144283199-80ce26c0-2fc8-4111-bb8d-48f494d948f8.png)

Below screenshot shows the confusion metrics in which the Overall Accuracy has dropped to 94% but Recall Accuracy has increased to 82% which means that the False Negatives are minimum , here in this case it is only 5. And also the True Postives have improved to 23 right predictions.  
![image](https://user-images.githubusercontent.com/92014201/144283941-28f5dbd0-b308-4f0d-9628-d047afb6766b.png) 

Model showing the current run status in the Model 
![image](https://user-images.githubusercontent.com/92014201/144284614-feaac719-9596-4c17-98b2-6c109c742d04.png)


