#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:26:01 2022


@author: robertgc
"""

from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.gaussian_process.kernels import RBF
import numpy as np

class gp_ensamble():
    
    def __init__(self,**kwargs):
        
        #Get the instances from kwargs
        self.Xtrain = kwargs.get('Xtrain',None)
        self.ytrain = kwargs.get('ytrain',None)
        
        #Gps and dimensions
        self.gps = None 
        self.dims = None
        
    def predict(self,X):
        
        gps = self.gps 
        
        return np.column_stack([gp.predict(X) for gp in gps])
    
    def fit(self):
        
        #Get training data 
        Xtrain = self.Xtrain
        ytrain = self.ytrain
        
        #Calc dimensions of inpu
        dims = Xtrain.shape[-1]
        
        #Store dimensions 
        self.dims = dims
        
        #A list of one gp per output dimension
        gps = [self._factory() for i in range(ytrain.shape[-1])]
        
        #Loop and fit dimension specific gps
        for i,gp in enumerate(gps): 
            gp.fit(
                Xtrain,
                ytrain.iloc[:,i]
                )
        
        #Store trained gps
        self.gps = gps
    
    #Internal factory function to create a local gaussian process
    def _factory(self):
        
        #Get fimenstions 
        dims = self.dims 
        
        #Create kernel
        kernel = 1 * RBF(length_scale=np.ones(dims))
                
        #Create gp
        gp = GPR(
            kernel = kernel,
            normalize_y=True
            )
        
        #return gp
        return gp
