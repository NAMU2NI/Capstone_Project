# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:28:55 2021

@author: 40100123
"""

import numpy as np
import pandas as pd
import os
from datetime import datetime

data = pd.read_csv('payer_level_features.csv')



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
    
    
    # Clean and one hot encode data
    x_df = data.dropna()
    x_df['Bankruptcy month'] = x_df['Bankruptcy month'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    categorical_cols = ['Payment Term', 'Payment Behavior Status']
    x_df=one_hot_encode(x_df,categorical_cols,drop_original_columns=True)
    y_df = x_df.pop("FLAG_BAD_DEBT")

    return x_df,y_df

x, y = clean_data(data)    
