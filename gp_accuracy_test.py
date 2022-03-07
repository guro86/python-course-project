#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:10:26 2022

@author: robertgc
"""

#Modules
from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.gaussian_process.kernels import RBF
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#import y_data 
y_data = pd.read_csv('tu_data.csv')
y_data = y_data.pivot_table(
    columns='name',
    values = 'fgr',
    index = 'case',
)

#import x_data
x_data = pd.read_csv(
    'calibration_samples.csv', 
    index_col=0
    )

#X and y data
Xtrain,Xtest,ytrain,ytest = train_test_split(
    x_data,
    y_data,
    random_state= 19953
    ) 

#One gp
gp = GPR(
    kernel=1*RBF(
        length_scale=np.ones(4),
        ),
    normalize_y=True
    )

#Fit the gp
gp.fit(Xtrain,ytrain)

#Validation plot
plt.plot(
    ytest,
    gp.predict(Xtest),
    'o'
    )

#%%Several gps mihgt imporve accuracy
#Since the hyper parameters can be dimension specific

#a factory function that returns a GP
def factory():
    return GPR(
        kernel = 1 * RBF(
            length_scale = np.ones(4)
            )
        )

#A list of one gp per output dimension
gps = [factory() for i in range(ytrain.shape[-1])]

#Fit the gps for each dimension 
for i,gp in enumerate(gps): 
    gp.fit(
        Xtrain,
        ytrain.iloc[:,i]
        )
    
#Validation plot
for i,gp in enumerate(gps): 
    plt.plot(
        ytest.iloc[:,i],
        gp.predict(Xtest),
        '+'
        )
    
'''
    Conclusion, overall accuracy is improved but there are several outliers 
    that we might reduce with more training data. 
'''