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




