# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:28:55 2021

@author: 40100123
"""

import numpy as np
import pandas as pd
import os
import argparse
import joblib

from azureml.core.run import Run
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset


data = TabularDatasetFactory.from_delimited_files(path="https://raw.githubusercontent.com/NAMU2NI/Capstone_Project/main/payer_level_features.csv")

def one_hot_encode(data,list_columns,drop_original_columns=True):    
    #Reset index
    data=data.reset_index(drop=True)
    for current_column in list_columns:
        #print("One Hot Encoding : "+current_column+"\n"+"nunique : "+str(data[current_column].nunique()))
        #display(data.groupby(current_column).size().sort_values(ascending=False))
        
        current_data=pd.get_dummies(data[current_column])
        current_data=current_data.add_prefix(current_column+'_')
        #Merging
        data=pd.merge(data,current_data,left_index=True,right_index=True)
        #print("----------------------------------------")
    #deleting raw columns
    if(drop_original_columns):
        data=data.drop(list_columns,axis=1)
    
    #Returning data frame
    return(data)



def clean_data(data):
    
    x_df = data.to_pandas_dataframe().dropna()
    # Clean and one hot encode data
    categorical_cols = ['Payment Term', 'Payment Behavior Status']
    x_df=one_hot_encode(x_df,categorical_cols,drop_original_columns=True)
    y_df = x_df.pop("FLAG_BAD_DEBT")

    return x_df,y_df

x, y = clean_data(data)  


x_train, x_test, y_train, y_test = train_test_split(
         x, y, test_size=0.33, random_state=42)

## Removing the variables which are not required 

x_train = x_train.drop(['Payer', 'Bankruptcy month'], axis=1)
x_test = x_test.drop(['Payer', 'Bankruptcy month'], axis=1)

y_train = y_train.astype('category')
y_test = y_test.astype('category')

## Building a Random forest Model 


run = Run.get_context()

def main():

    #Add arguments to script 
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators',type=int,default=100,help="The number of trees in the forest")
    parser.add_argument('--max_depth',type=int,default=1.0,help="The maximum depth of the tree")
    parser.add_argument('--max_features',type=float,default=100,help="The number of features to consider when looking for the best split")
    parser.add_argument('--n_jobs',type=int,default=100,help="The The number of jobs to run in parallel")

    
    args = parser.parse_args()

    run.log("# of trees:", np.int(args.n_estimators))
    run.log("depth of trees:", np.int(args.max_depth))
    run.log("# of features for best split :", np.float(args.max_features))
    run.log("# of Jobs to run parallel :", np.int(args.n_jobs))

    model = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth,max_features=args.max_features,
    n_jobs=args.n_jobs).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    os.makedirs('./outputs', exist_ok=True)
    joblib.dump(value=model, filename = './outputs/bkt-model-Hyp.joblib')


if __name__ == '__main__':
    main()










