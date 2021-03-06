#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:10:26 2022

@author: robertgc
"""

#Modules
from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.gaussian_process.kernels import RBF
import numpy as np
import matplotlib.pyplot as plt
from lib import dataloader

Xtrain,Xtest,ytrain,ytest = dataloader('data.p')

#One gp
gp = GPR(
    kernel=1*RBF(
        length_scale=np.ones(4),
        ),
    )

#Fit the gp
gp.fit(Xtrain,ytrain)

#A new plot
plt.figure(0)

#Set title of plot
plt.title("Validation plot using one gp")

plt.xlabel('Test samples')
plt.ylabel('Predicted test samples')

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
            length_scale = np.ones(4),
            ),
        normalize_y = True
        )

#A list of one gp per output dimension
gps = [factory() for i in range(ytrain.shape[-1])]

#Fit the gps for each dimension 
for i,gp in enumerate(gps): 
    gp.fit(
        Xtrain,
        ytrain.iloc[:,i]
        )

#Another figure
plt.figure(1)    

#Set title of plot
plt.title("Validation plot using several gps")

#Validation plot
for i,gp in enumerate(gps): 
    plt.plot(
        ytest.iloc[:,i],
        gp.predict(Xtest),
        '+'
        )

plt.xlabel('Test samples')
plt.ylabel('Predicted test samples')

plt.show()
    
    
'''
    Conclusion, overall accuracy is improved but there are several outliers 
    that we might reduce with more training data. 
'''