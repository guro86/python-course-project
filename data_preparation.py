#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:05:07 2022

@author: robertgc
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

#import y_data 
y_data = pd.read_csv('raw_data/tu_data.csv')
y_data = y_data.pivot_table(
    columns='name',
    values = 'fgr',
    index = 'case',
)

#import x_data
x_data = pd.read_csv(
    'raw_data/calibration_samples.csv', 
    index_col=0
    )

#X and y data
#Use a fixed seed for reproducability
Xtrain,Xtest,ytrain,ytest = train_test_split(
    x_data,
    y_data,
    random_state= 19953
    )

#Put the data in a dict for storage
data = [Xtrain,Xtest,ytrain,ytest]

#Dump the pre-processed data to a file
with open('data.p','wb') as file:
    pickle.dump(
        data,
        file
        )