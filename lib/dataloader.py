#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:57:35 2022

@author: robertgc
"""

#Import pickle 
import pickle 

#Defining a function that returns train and test data 
#assuming it is stored as a list in a file
def dataloader(fname):    
    
    #Opening the file
    with open(fname,'rb') as file:    
        #Loading the data
        Xtrain,Xtest,ytrain,ytest = pickle.load(file)
        
    #Returning the data
    return Xtrain,Xtest,ytrain,ytest