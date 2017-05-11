# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:33:44 2017

Create the wavelength grid that samples the overall spectral energy distribution

@author: ishort
"""

import math

def lamgrid(numLams, lamSetup):
    
    lambdaScale = []
    logLambda = 0.0
    
    #// Space lambdas logarithmically:
    logLam1 = math.log10(lamSetup[0])
    logLam2 = math.log10(lamSetup[1])
    delta = ( logLam2 - logLam1 ) / numLams
    
    ii = 0.0
    
    for i in range(numLams):
        ii = float(i);
        logLambda = logLam1 + ( ii * delta );
        lambdaScale.append(math.pow(10.0, logLambda))
        
    return lambdaScale;
