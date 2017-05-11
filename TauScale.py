# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:46:06 2017

Create the standard optical depth scale sampling the model vertically - interpreted as the
Rosseland optical depth scale
Uniformly spaced in log(tau)

@author: ishort
"""

import math

def tauScale(numDeps, log10MinDepth, log10MaxDepth):
    
    """Create the standard optical depth scale sampling the model vertically - interpreted as the
Rosseland optical depth scale
Uniformly spaced in log(tau)"""
    
    #//log_10 Rosseland optical depth scale  
    #double tauRos[][] = new double[2][numDeps];
    tauRos = [ [ 0.0 for i in range(numDeps) ] for j in range(2)] 
        
    #// Construct the log ROsseland optical depth scale:
    #// Try equal spacing in log depth
        
    ln10 = math.log(10.0)
        
#//        double log10MinDepth = -4.5;
#//        double log10MaxDepth = 1.5;
        
    logMinDepth = log10MinDepth * ln10
    logMaxDepth = log10MaxDepth * ln10;
        
    deltaLogTau = (logMaxDepth - logMinDepth)/(numDeps - 1.0);
        
    ii = 0.0
    for i in range(numDeps):
            
        ii = float(i)
        tauRos[1][i] = logMinDepth + ii*deltaLogTau
        tauRos[0][i] = math.exp(tauRos[1][i])
        #//System.out.println("i: " + i + " absTauDiff[1][i] " + tauRos[1][i] + " tauRos[0][i] " + tauRos[0][i]);
        
        
    return tauRos
        

