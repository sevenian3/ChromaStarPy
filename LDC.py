# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:58:43 2017

@author: ishort
"""

def ldc(numLams, lambdaScale, numThetas, cosTheta, contIntens):

    ldc = [0.0 for i in range(numLams)]

    #double epsilon, meanEpsilon, y;

    for iL in range(numLams):

        #//System.out.println("lambdaScale[iL] " + lambdaScale[iL]);
        meanEpsilon = 0.0 #//initialize accumulator

        for iT in range(1, numThetas):

            y = contIntens[iL][iT]/contIntens[iL][0]
            epsilon = (y - 1.0) / (cosTheta[1][iT] - 1.0)
            #//System.out.println("cosTheta[1][iT] " + cosTheta[1][iT] + " epsilon " + epsilon);
            meanEpsilon += epsilon  

        #} //iT theta loop

        ldc[iL] = meanEpsilon / numThetas

    #} //iL lambda loop  

    return ldc

#}  //end method ldc 