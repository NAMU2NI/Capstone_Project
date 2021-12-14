# Capstone_Project

## Write a short introduction to your project.
In this project ,  i will be using both Hyperdrive and AutoML API from Azure ML to build this project to predict  whether an Account (Point of Contact/Customer) will go Bankrupt or not. I will not only the predict the model , i will also compare the results of Hyperparameter tuning model and Automl model and the best model out of them will be deployed as web service. After the deployment , we have used Rest API and SDK to predict its outcome. 

![image](https://user-images.githubusercontent.com/92014201/146041981-31b30b6b-5215-4f46-8f54-4c148ad1bba1.png)


### Business Context of the problem statement  

This is very important because a Customer get a lot of products from the beverage Manufacturer. In order to do faster transactions , beverage manufacturer gives credit limit and Payment terms for its customers. But when the Customer goes bankrupt , the money which is in Credit will be lost to the beverage manufacturer so it is very much essential to the BM (beverage manufacturer) to set up the right credit limit and revise the credit limit often and also when we know in advance or if we are able to predict a customer going bankrupt than the BM can take necessary actions by reducing the credit limit or change the payment patterns for those customers so that the BM does not lose any money. Considering the COIVD era , there are lot of small customers went bankrtupt so it is very much essentail for any business to have this model which predicts the whether the customer will go bankrupt or not. Risk Exposure of the BM will be reduced by taking proactive actions based out of the predictive model. 


## Project Set Up and Installation
For this project , i have used my own Azure subscription. The data for this collated from various data sources from the external site which talks about how good is a customer financial status and internal data like BM's sales order and buying pattern for all the different pocs are studied with the detailed explorary analysis and than merged togother into single dataset for the prediction. 

In order to make this as a professional project , the various data sources of Internal data and external data has to be queried into the Data bricks and the pipeline has to be created and the refresh of the model has to take place once in a month or once in 2 months to understand the risky customers. By this visibility , Risk team can review the accounts who are under the risk zone and also can understand the movements of the risky pocs in the form of trend.  Based on these visibility , BM's can take necessary actions to mitigate the risk. 


## Dataset
As explained above ,the dataset used above is a combination of internal and external data due to the limiation of the projects i do not want deep dive in the formation of the various features which were created in the model. Basically most of hte features for the data were created based on the business knowledge and discussion wiht the SME's/ 

Various features were collated for the model were aggregated at POC level , each row in the excel corresponds to one POC and it has 41 columns in total. Column name "FLAG_BAD_DEBT" corresponds to the Target column which tells whether a POC has gone bankrupt in the past or not. Objective for the Machine learning model is to study those Bankrupt POCs and Not a Bankrupty POC in detail using hte other 39 features and than simulate the same for the new data to get the Bankrupt POCs 

Data 	Details 
Payer	Customer ID which gets beverages from the Manufacturer

Bankruptcy month	Month on which the Customer in the history has gone bankrupt 

FLAG_BAD_DEBT	Target variable , 0 indicates no bankruptcy , 1 indicates bankruptcy 

POCs	Number of outlets one customer has 

Rent	Rent which is paid by the customer to the company 

Average Receivables	Whats the average receivables Manufacturer gets from the customer 

Average Overdue	Whats the average due amount from the customer 

Payment Term Days	Agreed Payment term days between Customer and Manufacturer 

Payment Behavior Status	Based on the historical payments done by the customer , Manufacturer have clustered the data 

Credit Limit	Credit amount assigned by the Manufacturer to customer 

Std Dev AR	Standard deviation of the Average receivables 

Max Credit Utilization	Max ratio of the Recievables to the Credit limit 

Avg Credit Utilization	Avg ratio of the Recievables to the Credit limit 

fb_rating	Ratings of the consumers to the particular POC , data scrapped from FB 

![image](https://user-images.githubusercontent.com/92014201/145835634-fe9be912-419a-480c-93e0-5ea4c91150de.png)



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

Below screenshot shows the confusion metrics in which the Overall Accuracy has dropped to 86% but Recall Accuracy has increased to 75% which means that the False Negatives are minimum , here in one of the child runs there is a Sampling has happened hence there is more positives than we see here in the below screenshot. 

![image] ![image](https://user-images.githubusercontent.com/92014201/145675615-bb2708bd-a39d-4a58-b235-701a0f97cdbe.png)



Model showing the current run status in the Model 
![image](https://user-images.githubusercontent.com/92014201/145675698-68e6c7cd-2e0c-4dd4-9983-45be2e46a2e1.png)

![image](https://user-images.githubusercontent.com/92014201/145675712-7a08b87e-978f-451d-b72a-a10c7dad1b40.png)


#### Screenshot of the details of the best model with its run id:
![image](https://user-images.githubusercontent.com/92014201/146045852-11cee8df-91c6-405d-b6be-2bb98b62fcde.png)
![image](https://user-images.githubusercontent.com/92014201/146046502-7f412b8b-2347-4bf9-9549-dc2fda8dbccf.png)

Iteration 26 , shows the best model with the accuracy of 70% with Voting Ensemble as the best model in the above figure 

##### The screen below shows that run has been completed and shows the VotingEnsemble as a best model

![image](https://user-images.githubusercontent.com/92014201/146046718-c61cdae7-4c6b-4a5a-91e6-4a32940c5d9f.png)

##### The below screen shows the parameters of the train model:

![image](https://user-images.githubusercontent.com/92014201/146046979-f2681fab-ca10-42c9-9f07-3fc164567435.png)


##### The below screen shows metrics details of the VotingEnsemble

![image](https://user-images.githubusercontent.com/92014201/146047122-608f37f6-ea1c-4425-9e2d-a426fe901599.png)

##### The screen below shows the environment dependencies:

![image](https://user-images.githubusercontent.com/92014201/146047323-ed117854-6cee-46a8-97cd-430584431122.png)


## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

In Hyperparameter tuning , we selected Random forest model , because ensemble model accuracy is always better than one model. For tuning RF model, we used below parameters : 

#### Parameter Sampling 

n_estimators : number of trees in the forest : used a discrete hyperparameters "Choice" it tries select the discrete values specified. in the current model depth of the trees were given a choice between 100 , 150 ,200,250,300 

max_depth : The maximum depth of the tree. here again a discrete choice function is used with the below options 7,14,21,28,35,42

max_features : The number of features to consider when looking for the best split: used a continous distribution hyperparameter space in the model numbers between 0.25 and 0.50 are unifomrly selected for multiple iterations 

#### Early Termination Policy 
 Bandit Early termination policy it helps to eliminate the runs early if hte accuracy is not improving for a  model. 

#### Primary Metric Accuracy 
Recall is used as the primary metric in the model , since the objective was to minimize the False Negatives and to maximize the Recall accuracy. Recall Accuracy have been mentioned as the Primary metric and is used in the model. 

#### Max Concurrent runs 
specified as 4 which means Maximum number of runs that can run concurrently. If not specified, all runs launch in parallel 

#### Max Total runs
Specified as 20 , maximum number of models created to train the model with the above iterations 

In the current below model , shows the 20 iterations which were trained by iterating on the various Hyper parameter tuning techniques 

![image](https://user-images.githubusercontent.com/92014201/144847989-7656e380-9ba7-4c45-b022-d399605a6010.png)

Below figure shows the various Hyperparameter tuning factors and its corresponding accuracy , in the below case all the 20 iteration had the same accuracy of 25% 

![image](https://user-images.githubusercontent.com/92014201/144848147-13daac01-9ace-42f8-8395-faed6af2ab4c.png)


Conculsion : There were no best model from Hyperparameter tuning , all the model had same accuracy as shown in the above model. Hence for Deployment the Model from the Automl was used to deploy the model. 

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

### Model Register 
Best Model was from the Auto ML which had an accuracy 74% so this model was identified and regsitered for the Deployment. 
Model was registered from the local file , in the below screenshot PKL file of hte model was downloaded into the local file. 
Than the Model was Registered with the Model Name and Model Path where the PKL file is locaated 

![image](https://user-images.githubusercontent.com/92014201/145519050-0071bc47-04ef-47b6-987f-e7f912a47419.png)

### Entry Script 
An Entry script receives data submitted to a deployed web service and passes it to the model. It then returns the model's response to the client. The script is specific to your model.

Loading the Model using the function init() and running hte model using run () function - this entry script is used in the deployment 
![image](https://user-images.githubusercontent.com/92014201/145519622-f8c68d7d-9c55-4ae8-8f99-343c9201e632.png)

### Inference Configuration 

An inference configuration describes the Docker container and files to use when initializing your web service. The inference configuration below screenshot specifies that the machine learning deployment will use the file autoscore.py in the ./source_dir directory to process incoming requests and that it will use the Docker image with the Python packages specified in the project_environment environment.

![image](https://user-images.githubusercontent.com/92014201/145519950-e1b62f6d-7687-4cc3-9cb7-386356cb461b.png)

### Deployment Configuration 

A deployment configuration specifies the amount of memory and cores your webservice needs in order to run. It also provides configuration details of the underlying webservice. 

### Deployment 

Model is deployment with the above configuration 

![image](https://user-images.githubusercontent.com/92014201/145520213-81310799-2c45-4cc0-b805-666d5bc2a722.png)

Querying with a Sample Input 

2 data points from the Model is chosen as a Input one with a Bad Debt and another one without a Bad Debt , these 2 inputs are passed into the Model to check the predictions 
to the end point. Final Prediction of the Model is shown in the below image for 0 and 1. Model has correctly classified the output as 0 and 1. 

![image](https://user-images.githubusercontent.com/92014201/145520359-69d7ce20-2787-491c-9ad3-b1cdcca3f63b.png)

### Deployed Model as End point 

Status showing Healthy 
 
![image](https://user-images.githubusercontent.com/92014201/145675756-32603e56-054b-4c45-887f-9d5fe351c991.png)

### Query the endpoint with a sample input

For querying the endpoint, we used the REST call by importing the requests Here are the steps with REST call:

a) Store the scoring uri and primary key
b) Create the header with key "Content-Type" and value "application/json" and set the Authorization with Bearer token
c) Create the sample input and post to the requests. Here is the sample input:

when considering the sample input , i assisgned the values based on the feature importance such that the model predicts 2 different classes Bankrupt and Not a Bankrupt.In the first case , the variables which were chosen such that Credit limit , Fb ratings are extreme so that the first sample predicts the Bankrupt class. 

![image](https://user-images.githubusercontent.com/92014201/145675803-caa5227d-98c9-46a7-91c4-06fa8cf3b942.png)

## Screen Cast of the Project 

https://www.youtube.com/watch?v=ebIWI5L63E8

## Improvement of this project in the future 

The best model had an FN accuracy of 72%  , we need to focus on how to improve this accuracy to reach 100% so that in the prediction all the customer which goes bankrupt are being predicted. At the same time , final recommendation can be in terms of probability apart from the prediction class  of 1 and 0. This proboablites will help is interms of confidence of taking a specific decision. For the business user , apart from the probablites of the prediction model dashboard which gives a clear visibility of a certain behaviour of the customers at a longer trend should be made available so that there is more transparecny in the analysis and it gives much visibility on the Predictions. 


