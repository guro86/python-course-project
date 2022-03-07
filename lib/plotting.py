#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:37:07 2022

@author: robertgc
"""

import matplotlib.pyplot as plt

def validation_plot(test,pred):
    
    f, ax = plt.subplots()
    
    ax.plot(test, pred, 'r+')
    
    ax.set_xlabel('Test samples')
    ax.set_ylabel('Predicted test samples')
    
    return f, ax