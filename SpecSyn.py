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
    lineKap2 = 1.0e-99 #//initialization

    #//int numCnt = lambdaScale.length;
    #//int numLine = lineLambdas.length - 1;
    kappa1D = [0.0 for i in range(numNow)]
    lineKap1D = [0.0 for i in range(numPoints)]
    #//System.out.println("iL   masterLams    logMasterKappa");
    for iD in range(numDeps):

        #//Extract 1D *linear* opacity vectors for interpol()
        for k in range(numNow):
            kappa1D[k] = math.exp(logMasterKaps[k][iD]) #//now wavelength dependent 
            

        for k in range(numPoints):
            lineKap1D[k] = math.exp(listLogKappaL[k][iD])
            #//     if (iD%10 == 1){
            #//        System.out.println("iD " + iD + " k " + k + " listLineLambdas " + listLineLambdas[k] + " lineKap1D " + lineKap1D[k]);
            #//     }
            

        #//Interpolate continuum and line opacity onto master lambda scale, and add them lambda-wise:
        for iL in range(numTot):
            kappa2 = ToolBox.interpol(masterLams, kappa1D, masterLamsOut[iL])
            lineKap2 = 1.0e-49 #//re-initialization
            if ( (masterLamsOut[iL] >= listLineLambdas[0]) and (masterLamsOut[iL] <= listLineLambdas[numPoints-1]) ):
                
                lineKap2 = ToolBox.interpol(listLineLambdas, lineKap1D, masterLamsOut[iL])
                if (lineKap2 <= 0.0):
                    lineKap2 = 1.0e-49
                #//lineKap2 = 1.0e-99;  //test
                
            #//test lineKap2 = 1.0e-99;  //test
            #// if (iD%10 == 1){
            #//   System.out.println("iD " + iD + " iL " + iL + " masterLamsOut " + masterLamsOut[iL] + " kappa2 " + kappa2 + " lineKap2 " + lineKap2);
            #//}
            totKap = kappa2 + lineKap2
            logMasterKapsOut[iL][iD] = math.log(totKap)
            #//if (iD == 36) {
            #//    System.out.format("%02d   %12.8e   %12.8f%n", iL, masterLams[iL], logE * logMasterKappa[iL][iD]);
            #//}
        #} iL loop
    #}  iD loop 

    return logMasterKapsOut;
#}
    