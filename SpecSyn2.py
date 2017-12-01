# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:03:30 2017

@author: ishort
"""

#/**
# *
# * Create master kappa_lambda(lambda) and tau_lambda(lambda) for
# * FormalSoln.formalSoln()
# *
# * @author Ian
# */

import math
import ToolBox
#plotting:
import matplotlib
import pylab
import numpy

def masterLambda(numLams, numMaster, numNow, masterLams, numPoints, listLineLambdas):
        
    """//Merge continuum and line wavelength scales - for one line
//This expects *pure* line opacity - no continuum opacity pre-added!"""
    
    #//int numCnt = lambdaScale.length;
    #//skip the last wavelength point in the line lambda grid - it holds the line centre wavelength
    #//int numLine = lineLambdas.length - 1;

    numTot = numNow + numPoints #//current dynamic total

    #//System.out.println("numCnt " + numCnt + " numLine " + numLine + " numTot " + numTot);
    """/*
         for (int i = 0; i < numCnt; i++) {
         System.out.println("i " + i + " lambdaScale[i] " + lambdaScale[i]);
         }
         for (int i = 0; i < numLine; i++) {
         System.out.println("i " + i + " lineLambdas[i] " + lineLambdas[i]);
         }
         */ """
    #//Row 0 is merged lambda scale
    #//Row 1 is log of *total* (line plus continuum kappa
    masterLamsOut = [0.0 for i in range(numTot)]

    #// Merge wavelengths into a sorted master list
    #//initialize with first continuum lambda:
    lastLam = masterLams[0]
    masterLamsOut[0] = masterLams[0]
    nextCntPtr = 1
    nextLinePtr = 0
    for iL in range(1, numTot):
        if (nextCntPtr < numNow):
            #//System.out.println("nextCntPtr " + nextCntPtr + " lambdaScale[nextCntPtr] " + lambdaScale[nextCntPtr]);
            #//System.out.println("nextLinePtr " + nextLinePtr + " lineLambdas[nextLinePtr] " + lineLambdas[nextLinePtr]);
            if ((masterLams[nextCntPtr] <= listLineLambdas[nextLinePtr])
            or (nextLinePtr >= numPoints - 1)):
                #//Next point is a continuum point:
                masterLamsOut[iL] = masterLams[nextCntPtr]
                nextCntPtr+=1

            elif ((listLineLambdas[nextLinePtr] < masterLams[nextCntPtr])
                        and (nextLinePtr < numPoints - 1)):
                #//Next point is a line point:
                masterLamsOut[iL] = listLineLambdas[nextLinePtr]
                nextLinePtr+=1            
            
            #//System.out.println("iL " + iL + " masterLamsOut[iL] " + masterLamsOut[iL]);
    #} //iL loop
    #//Make sure final wavelength point in masterLams is secured:
    masterLamsOut[numTot-1] = masterLams[numNow-1]

    return masterLamsOut
#}

def masterKappa(numDeps, numLams, numMaster, numNow, masterLams, masterLamsOut, logMasterKaps, \
                numPoints, listLineLambdas, listLogKappaL):
#//                                          
    logE = math.log10(math.e) #// for debug output

    #//int numLams = masterLams.length;
    numTot = numNow + numPoints
        
    logMasterKapsOut = [ [ 0.0 for i in range(numDeps) ] for j in range(numTot) ]
    #//double[][] kappa2 = new double[2][numTot];
    #//double[][] lineKap2 = new double[2][numTot];
    #double kappa2, lineKap2, totKap;
    #lineKap2 = 1.0e-99 #//initialization
    #logLineKap2 = -49.0 #//initialization
    logKappa2 = [0.0 for i in range(numTot)]
    logLineKap2 = [-49.0 for i in range(numTot)]
    #//int numCnt = lambdaScale.length;
    #//int numLine = lineLambdas.length - 1;
    #kappa1D = [0.0 for i in range(numNow)]
    logKappa1D = [0.0 for i in range(numNow)]
    #thisMasterLams = [0.0 for i in range(numNow)]
    #lineKap1D = [0.0 for i in range(numPoints)]
    logLineKap1D = [0.0 for i in range(numPoints)]
    #//System.out.println("iL   masterLams    logMasterKappa");
    #print("numNow ", numNow, " numPoints ", numPoints)
    #print("iD ", iD, " len(masterLams) ", len(masterLams), " len(logKappa1D) ", len(logKappa1D))           
    
    #for k in range(numNow):
    #    thisMasterLams[k] = masterLams[k]
    thisMasterLams = [ masterLams[k] for k in range(numNow) ]
        
    for iD in range(numDeps):

        #//Extract 1D *linear* opacity vectors for interpol()
        #for k in range(numNow):
        #    #kappa1D[k] = math.exp(logMasterKaps[k][iD]) #//now wavelength dependent 
        #    logKappa1D[k] = logMasterKaps[k][iD] #//now wavelength dependent
        logKappa1D = [ logMasterKaps[k][iD] for k in range(numNow) ]

        #for k in range(numPoints):
        #    #lineKap1D[k] = math.exp(listLogKappaL[k][iD])
        #    logLineKap1D[k] = listLogKappaL[k][iD]
            #//     if (iD%10 == 1){
            #//        System.out.println("iD " + iD + " k " + k + " listLineLambdas " + listLineLambdas[k] + " lineKap1D " + lineKap1D[k]);
            #//     }
        logLineKap1D = [ listLogKappaL[k][iD] for k in range(numPoints) ]    

        #//Interpolate continuum and line opacity onto master lambda scale, and add them lambda-wise:
        #for iL in range(numTot):
        #    logLineKap2[iL] = -49.0 #//re-initialization
        logLineKap2 = [ -49.0 for iL in range(numTot) ]
 
        logKappa2 = numpy.interp(masterLamsOut, thisMasterLams, logKappa1D)
        logLineKap2 = numpy.interp(masterLamsOut, listLineLambdas, logLineKap1D)
        for iL in range(numTot):
            totKap = math.exp(logKappa2[iL]) + math.exp(logLineKap2[iL])
            logMasterKapsOut[iL][iD] = math.log(totKap)
        #logMasterKapsOut[:][iD] =\
        #[ math.log(math.exp(logKappa2[iL]) + math.exp(logLineKap2[iL])) for iL in range(numTot) ]
        
    #}  iD loop 
    #pylab.plot(masterLamsOut, [logMasterKaps[i][12] for i in range(numTot)]) 
    #pylab.plot(masterLamsOut, [logMasterKaps[i][12] for i in range(numTot)], '.')      

    return logMasterKapsOut;
#}
    