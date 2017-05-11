# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:33:20 2017

@author: Ian
"""

import math
import Useful

"""
/* This might be the wrong approach - using the *local* monochromatic continuum optical depth and extinction 
 * scale for reference at each wavelength - the alternative is to use a universal tau and kappa scale
 * for reference, like Rosseland tau and kappa (or those at 500 nm)*/"""

def tauLambda(numMaster, masterLams, logKappaL,
            numDeps, logKappaRef, tauRef, logTotalFudge): 
 
    """/* This version is for computing the monochromatic optical depth distribution from a line blanketed 
 * and a continuum monochromatic extinction distribution */
/* logTauCont is the optical depth scale corresponding to the continuum extinction logKappa*/"""

    #//No monochromatic optical depth can be less than the Rosseland optical depth,
    #// so prevent zero tau_lambda values by setting each tau_lambda(lambda) at the 
    #//top of the atmosphere to the tau_Ross value at the top 
    #// - prevents trying to take a log of zero!
    logE = math.log10(math.e) #// for debug output
    logE10 = math.log(10.0)
    minTauL = tauRef[0][0]
    minLogTauL = tauRef[1][0]

    #//int numPoints = linePoints[0].length;
    logTauL = [ [ 0.0 for i in range(numDeps) ] for j in range(numMaster) ]
    #double tau1, tau2, delta, tauL, thisTau, lastTau,
    #            integ, logKapRat, lastLogKapRat, kapTot;

    #//Interpolate continuum opacity and corresponding optical depth scale onto onto line-blanketed opacity lambda array:
    #//
    """#/*
    logKappaC = [0.0 for i in range(numLams)]
    logKappaC2 = [0.0 for i in range(numMaster)]
    logKappa2 = [ [ 0.0 for i in range(numDeps) ] for j in range(numMaster) ]
    logTauC = [0.0 for i in range(numLams)]
    logTauC2 = [0.0 for in range(numMaster)]
    logTau2 = [ [ 0.0 for i in range(numDeps) ] for j in range(numMaster) ]
    for id in range(numDeps):
        for il in range(numLams):
            logKappaC[il] = logKappa[il][id]
            logTauC[il] = logTauCont[il][id]
           
        logKappaC2 = ToolBox.interpolV(logKappaC, lambdaScale, masterLams); 
        logTauC2 = ToolBox.interpolV(logTauC, lambdaScale, masterLams);
        for il in range(numMaster): 
            logKappa2[il][id] = logKappaC2[il]
            logTau2[il][id] = logTauC2[il]
           
        
  */"""
    for il in range(numMaster):

        tau1 = minTauL #//initialize accumulator
        logTauL[il][0] = minLogTauL #// Set upper boundary TauL           

        #//System.out.println("LineTau: minTauL: " + minTauL);
        #//Trapezoid method: first integrand:
        #//total extinction co-efficient
        #//// With local monochromatic optical depth scale as reference scale:
        #//lastLogKapRat = logKappaL[il][0] - logKappa2[il][0];
        #//With Rosseland optical depth scale as reference scale:
        #//lastLogKapRat = Math.log(kapTot) - kappaRef[1][0];
        lastLogKapRat = logKappaL[il][0] - logKappaRef[1][0]
        lastLogKapRat = lastLogKapRat + logE10*logTotalFudge
        for id in range(1, numDeps):

            #// With local monochromatic optical depth scale as reference scale:
            #//thisTau = Math.exp(logTau2[il][id]);
            #//lastTau = Math.exp(logTau2[il][id - 1]);
            #////With Rosseland optical depth scale as reference scale:
            thisTau = tauRef[0][id]
            lastTau = tauRef[0][id-1]
            #//
            delta = thisTau - lastTau
            #// With local monochromatic optical depth scale as reference scale:
            #//logKapRat = Math.log(kapTot) - logKappa2[il][id];
            #//logKapRat = logKappaL[il][id] - logKappa2[il][id];
            #////With Rosseland optical depth scale as reference scale:
            logKapRat = logKappaL[il][id] - logKappaRef[1][id]
            logKapRat = logKapRat + logE10*logTotalFudge

            #//opacity being handed in is now total opacity: line plux continuum:
            #//trapezoid rule:
            integ = 0.5 * (math.exp(logKapRat) + math.exp(lastLogKapRat))
            tau2 = tau1 + (integ * delta)

            logTauL[il][id] = math.log(tau2)
            tau1 = tau2
            lastLogKapRat = logKapRat

        #} //id loop

    #} //il loop

    return logTauL

#} //end method tauLambda

#//

def tauLambdaCont(numCont, logKappaCont, logKappaRef, 
                  numDeps, tauRef, logTotalFudge):

    """/* This version is for computing the monochromatic optical depth distribution from a continuum monochromatic extinction 
 * distribution and a reference extinction scale */ """
 
    #// kappaRef is usual 2 x numDeps array with linear (row 0) and logarithmic (row 1) reference extinction coefficient
    #// values
    #// tauRef is the optical depth distribution corresponding to the extinction distribution kappaRef

    #//No monochromatic optical depth can be less than the Rosseland optical depth,
    #// so prevent zero tau_lambda values by setting each tau_lambda(lambda) at the 
    #//top of the atmosphere to the tau_Ross value at the top 
    #// - prevents trying to take a log of zero!
    logE = math.log10(math.e) #// for debug output
    logE10 = math.log(10.0) 
    minTauC = tauRef[0][0]
    minLogTauC = tauRef[1][0]

    #//int numPoints = linePoints[0].length;
    #// returns numPoints+1 x numDeps array: the numPoints+1st row holds the line centre continuum tau scale
    logTauC = [ [ 0.0 for i in range(numDeps) ] for j in range(numCont) ]
    #double tau1, tau2, delta, tauL,
    #            integ, logKapRat, lastLogKapRat;

    #//Interpolate continuum opacity onto onto line-blanketed opacity lambda array:
    #//
    for il in range(numCont):

        tau1 = minTauC #//initialize accumulator
        logTauC[il][0] = minLogTauC #// Set upper boundary TauL           

        #//System.out.println("LineTau: minTauL: " + minTauL);
        #//Trapezoid method: first integrand:
        #//total extinction co-efficient
        #// Convert kappa_Ros to cm^-1 for consistency with kappaL:
        #//logKappaC = kappa[1][0] + rhoSun[1][0]; // + logg;
        #//WRONG!  kappa is now wavelength dependent!  
        #//logKappaC = kappa[1][0];

        #//delta = tauRos[0][1] - tauRos[0][0];
        #//logKapRat = logKappaL[il][0] - kappa[1][0];
        lastLogKapRat = logKappaCont[il][0] - logKappaRef[1][0]
        lastLogKapRat = lastLogKapRat + logE10*logTotalFudge
        #//tau2 = tau1 + ((Math.exp(logKapRat) + 1.0) * delta);
        #//opacity being handed in is now total oapcity: line plux continuum:
        #//tau2 = tau1 + (Math.exp(logKapRat) * delta);
        #//logTauL[il][1] = Math.log(tau2);
        #//tau1 = tau2;
        for id in range(1, numDeps):

            #// To test: continue with Euler's method:
            #// Convert kappa_Ros to cm^-1 for consistency with kappaL:
            #//logKappaC = kappa[1][id] + rhoSun[1][id]; // - logg;
            #//logKappaC = kappa[1][id];
            delta = tauRef[0][id] - tauRef[0][id - 1]
            #//logKapRat = logKappaL[il][id] - kappa[1][id];
            #//logKapRat = logKappaL[il][id] - logKappaC;
            logKapRat = logKappaCont[il][id] - logKappaRef[1][id]
            logKapRat = logKapRat + logE10*logTotalFudge
            #// if (id == 36){
            #//System.out.println("il " + il + " masterLams " + masterLams[il] + " logKappaL " + logE*logKappaL[il][id] + " kappa2 " + logE*kappa2[il][id]
            #//   + " logKapRat " + logKapRat);
            #//}

            #//tau2 = tau1 + ((Math.exp(logKapRat) + 1.0) * delta);
            #//opacity being handed in is now total oppcity: line plux continuum:
            #//trapezoid rule:
            integ = 0.5 * (math.exp(logKapRat) + math.exp(lastLogKapRat))
            tau2 = tau1 + (integ * delta)

            logTauC[il][id] = math.log(tau2)
            tau1 = tau2
            lastLogKapRat = logKapRat

            #//if (id == 12) {
            #// System.out.println("il " + il + " id " + id + " logTauL[il][id] " + logE * logTauL[il][id]);
            #// System.out.println("tauLambda: il, id, masterLams, logKappaL, logKappa2, logKapRat, logTauL : "
            #//     + il + " " + id + " " + masterLams[il] + " " + logE*logKappaL[il][id] + " " + logE*kappa2[il][id] + " " + logE*logKapRat + " " + logE*logTauL[il][id] );
            #//}

        #} //id loop

    #} //il loop

    """/* No!
        //This is probably superfluous here, but let's do it this way for consistency with code that was
        // dependent on Method 1:
        //Now compute the monochromatic line centre continuum optical depth scale and store it in an numPoints+1st column of
        // logTauL array:
        for (int id = 0; id < numDeps; id++) {

            logTauL[numPoints - 1][id] = tauRos[1][id];

        }
    */"""
    return logTauC

#} //end method tauLambda