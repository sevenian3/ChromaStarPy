# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:58:43 2017

@author: ishort
"""

    #JB#
import numpy as np
from sklearn.metrics import r2_score

#returns the "experimental" data
#takes a coefficent episilon(lambda) and a cosine value.

def func(coeff,ctheta):
    return(1-coeff+coeff*ctheta)

#returns the mean^2 "experimental" value
def meansq(mean,val):
    return((val-mean)**2)
    
#returns the mean^2 "real" value
def residsq(mean,funVal):
    return((funVal-mean)**2)

#an array of epsilon values to try for each function
epi=np.linspace(0,1,num=750)#can increase to get a better solution, but 750 seems fine
    #JB#
    
    
def ldc(numLams, lambdaScale, numThetas, cosTheta, contIntens):

    ldc = [0.0 for i in range(numLams)]

    #double epsilon, meanEpsilon, y;

    for iL in range(numLams):

        #//System.out.println("lambdaScale[iL] " + lambdaScale[iL]);
        #meanEpsilon = 0.0 #//initialize accumulator
        
        
        
        
        #JB#
        #a list to hold all of the R^2 values
        R2=[]
        
        #loop through all the episilons to find the one that best fits the data
        for epiI in epi:
            
            #hold values for a particular lambda model
            currentY=[]
            currentMeansq=0
            currentResidsq=0    
            intensities=[]
                
            for iT in range(1, numThetas-1):
            
                #consider this to be the "real" data of the function
                I=contIntens[iL][iT]
                I0=contIntens[iL][0]
                y = I/I0
                intensities.append(y)

                #get the "experimental" values with the current coefficent
                currentY.append(func(epiI,cosTheta[1][iT]))
            
            
            for k in range(0,len(currentY),1):
                
                #get mean^2 and residuals for current data set
                currentMeansq+=(meansq(np.mean(currentY),currentY[k]))
                currentResidsq+=(residsq(np.mean(intensities),intensities[k]))
            
            #store the R^2 value to see how well it fits the data set
            R2.append(r2_score(currentY,intensities))
            
        #pick the best LDC with the best R^2 and use that LDC
        ldc[iL] = epi[R2.index(max(R2))]

            #JB#
            
                #epsilon = (y - 1.0) / (cosTheta[1][iT] - 1.0)
                #//System.out.println("cosTheta[1][iT] " + cosTheta[1][iT] + " epsilon " + epsilon);
                #meanEpsilon += epsilon  

        #} //iT theta loop

            #ldc[iL] = meanEpsilon / numThetas

    #} //iL lambda loop  

    return ldc

#}  //end method ldc 