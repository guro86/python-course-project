#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:26:52 2022

@author: robertgc
"""

from lib import gp_ensamble
from lib import dataloader
from lib.plotting import validation_plot

Xtrain,Xtest,ytrain,ytest = dataloader('data.p')

gp_regressor = gp_ensamble(
    Xtrain = Xtrain,
    ytrain = ytrain
    )

gp_regressor.fit()

#%%

%%time
pred = gp_regressor.predict(Xtest)


#%%
validation_plot(ytest,pred)


'''
    To do: improve the evaluation time from ms to us by writing an alternative 
    predict method.
'''