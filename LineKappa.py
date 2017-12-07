# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:03:52 2017

@author: Ian
"""

"""// Assumes CRD, LTE, ???
// Input parameters:
// lam0 - line centre wavelength in nm
// logNl - log_10 column density of absorbers in lower E-level, l (cm^-2)
// logFlu - log_10 oscillator strength (unitless)
// chiL - energy of lower atomic E-level of b-b transition in eV
// chiI - ground state ionization energy to niext higher stage in (ev)
    //   
//     * PROBLEM: line kappaL values converted to mass extinction by division by rho() are 
// * not consistent with fake Kramer's Law based scaling of kappa_Ros with g.
    //*   Try leaving kappaLs as linear extinctions and converting the scaled kappa_Ros back to linear units
// * with solar rho() in LineTau2
    //
// Also needs atsmopheric structure information:
// numDeps
// tauRos structure
// temp structure 
// rho structure
// Level population now computed in LevelPops.levelPops()"""

import math
import numpy
import Useful
import ToolBox

def lineKap(lam0In, logNums, logFluIn, linePoints, lineProf,
            numDeps, zScale, tauRos, temp, rho, logFudgeTune):

    logE10 = math.log(10.0) #//natural log of 10
    
    c = Useful.c()
    logC = Useful.logC()
    k = Useful.k()
    logK = Useful.logK()
    logH = Useful.logH()
    logEe = Useful.logEe()
    logMe = Useful.logMe()

    ln10 = math.log(10.0)
    logE = math.log10(math.e) #// for debug output
    log2pi = math.log(2.0 * math.pi)
    log2 = math.log(2.0)

    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)
    #//double logNl = logNlIn * ln10;  // Convert to base e
    logFlu = logFluIn * ln10 #// Convert to base e
    logKScale = math.log10(zScale)

    #//chiI = chiI * Useful.eV;  // Convert lower E-level from eV to ergs
    #//double boltzFacI = chiI / k; // Pre-factor for exponent of excitation Boltzmann factor
    #//double logSahaFac = log2 + (3.0/2.0) * ( log2pi + logMe + logK - 2.0*logH);
    #//chiL = chiL * Useful.eV;  // Convert lower E-level from eV to ergs
    #//double boltzFac = chiL / k; // Pre-factor for exponent of excitation Boltzmann factor
    numPoints = len(linePoints[0])
    #//System.out.println("LineKappa: numPoints: " + numPoints);

    #double logPreFac;
    #//This converts f_lu to a volume extinction coefficient per particle - Rutten, p. 23
    logPreFac = logFlu + math.log(math.pi) + 2.0 * logEe - logMe - logC
    #//System.out.println("LINEKAPPA: logPreFac " + logPreFac);

    #//Assume wavelength, lambda, is constant throughout line profile for purpose
    #// of computing the stimulated emission correction
    #double logExpFac;
    logExpFac = logH + logC - logK - logLam0
    #//System.out.println("LINEKAPPA: logExpFac " + logExpFac);

    #// int refRhoIndx = TauPoint.tauPoint(numDeps, tauRos, 1.0);
    #// double refLogRho = rho[1][refRhoIndx];
    #//System.out.println("LINEKAPPA: refRhoIndx, refRho " + refRhoIndx + " " + logE*refRho);
    #// return a 2D numPoints x numDeps array of monochromatic *LINE* extinction line profiles
    
    logKappaL = [ [ 0.0 for i in range(numDeps)] for j in range(numPoints) ]
    #double num, logNum, logExpFac2, expFac, stimEm, logStimEm, logSaha, saha, logIonFrac;
    #double logNe;

    for id in range(numDeps):

        logExpFac2 = logExpFac - temp[1][id]
        expFac = -1.0 * math.exp(logExpFac2)

        stimEm = 1.0 - math.exp(expFac)
        logStimEm = math.log(stimEm)

        logNum = logNums[id]

        #//if (id == refRhoIndx) {
        #//    System.out.println("LINEKAPPA: logStimEm " + logE*logStimEm);
        #//}
        for il in range(numPoints):

            #// From Radiative Transfer in Stellar Atmospheres (Rutten), p.31
            #// This is a *volume* co-efficient ("alpha_lambda") in cm^-1:
            logKappaL[il][id] = logPreFac + logStimEm + logNum + math.log(lineProf[il][id])
            #//if (id == 36) {
            #//    System.out.println("il " + il + " logNum " + logE*logNum + " Math.log(lineProf[il][id]) " + logE*Math.log(lineProf[il][id]));
            #////    //System.out.println("logPreFac " + logPreFac + " logStimEm " + logStimEm);
            #//}
            #//System.out.println("LINEKAPPA: id, il " + id + " " + il + " logKappaL " + logE * logKappaL[il][id]);

            #//Convert to mass co-efficient in g/cm^2:                
            #// This direct approach won't work - is not consistent with fake Kramer's law scaling of Kapp_Ros with g instead of rho
            logKappaL[il][id] = logKappaL[il][id] - rho[1][id]
            #//Try something:
            #//
            #// **********************
            #//  Opacity problem #2 
            #//
            #//Line opacity needs to be enhanced by same factor as the conitnuum opacity
            #//  - related to Opacity problem #1 (logFudgeTune in GrayStarServer3.java) - ??
            #//
            logKappaL[il][id] = logKappaL[il][id] + logE10*logFudgeTune

            #//if (id == 12) {
            #//  System.out.println("LINEKAPPA: id, il " + id + " " + il + " logKappaL " + logE * logKappaL[il][id]
            #//   + " logPreFac " + logE*logPreFac + " logStimEm " + logE*logStimEm + " logNum " + logE*logNum 
            #//  + " log(lineProf[il]) " + logE*Math.log(lineProf[il][id]) + " rho[1][id] " + logE * rho[1][id]);
            #// }
            #//if (id == refRhoIndx-45) {
            #//    System.out.println("LINEKAPPA: id, il " + id + " " + il + " logKappaL " + logE*logKappaL[il][id]
            #//    + " logPreFac " + logE*logPreFac + " logStimEm " + logE*logStimEm + " logNum " + logE*logNum + " logRho " + logE*rho[1][id] 
            #//    + " log(lineProf[1]) " + logE*Math.log(lineProf[1][il]) );
            #//}
        #} // il - lambda loop

    #} // id - depth loop

    return logKappaL

#}

#//Create total extinction throughout line profile:
def lineTotalKap(linePoints, logKappaL, numDeps, kappa, 
                 numLams, lambdaScale):

    logE = math.log10(math.e) #// for debug output
    numPoints = len(linePoints)

    #// return a 2D numPoints x numDeps array of monochromatic *TOTAL* extinction line profiles
    logTotKappa = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    #double kappaL, logKappaC;

    #//Interpolate continuum opacity onto onto line-blanketed opacity lambda array:
    #//
    kappaC = [0.0 for i in range(numLams)]
    kappaC2 = [0.0 for i in range(numPoints)]
    kappa2 = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    for id in range(1, numDeps):
        for il in range(numLams):
            kappaC[il] = kappa[il][id]
           
        #kappaC2 = ToolBox.interpolV(kappaC, lambdaScale, linePoints);
        kappaC2 = numpy.interp(linePoints, lambdaScale, kappaC);
        for il in range(numPoints):
            kappa2[il][id] = kappaC2[il]
                 

    for id in range(numDeps):
        for il in range(numPoints):
            #//Both kappaL and kappa (continuum) are *mass* extinction (cm^2/g) at thsi point: 
            #//logKappaC = kappa[1][id];
            #//kappaL = Math.exp(logKappaL[il][id]) + Math.exp(logKappaC);
            kappaL = math.exp(logKappaL[il][id]) + math.exp(kappa2[il][id])
            logTotKappa[il][id] = math.log(kappaL)
            #//logTotKappa[il][id] = kappa[1][id];   //test - no line opacity
            #//if (id == 12) {
            #//    System.out.println("il " + il + " linePoints[0][il] " + 1.0e7*linePoints[0][il] + " logTotKappa[il][id] " + logE*logTotKappa[il][id] + " logKappaL[il][id] " + logE*logKappaL[il][id] + " kappa[1][id] " + logE*kappa[1][id]);
            #//    }
                
        #}
    #}

    return logTotKappa
