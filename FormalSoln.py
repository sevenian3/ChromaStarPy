# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:29:05 2017

@author: Ian
"""

import math
import Planck

def formalSoln(numDeps, cosTheta, lambda2, tau, temp, lineMode):
    
    """/**
 * Formal solution of the LTE radiative transfer for the monochromatic *surface*
 * intensity, I_lambda(Tau=0, theta) at wavelength lambda"""
 
# *
# * Calls Planck.planck(lambda, temp) to get the LTE source function Input lambda
# * in nm for Planck
# */

    logE = math.log10(math.e) #// for debug output

    cutoff = 0.001  #// tolerance for stopping deeper contriibutions to I(Tau=0)

    #//  cosTheta is a 2xnumThetas array:
    #// row 0 is used for Gaussian quadrature weights
    #// row 1 is used for cos(theta) values
    #// Gaussian quadrature:
    #// Number of angles, numThetas, will have to be determined after the fact
    numThetas = len(cosTheta[0])
    #//System.out.println("FORMALSOLN: numThetas= " + numThetas);
    #//double[][] intens = new double[numLams][numThetas];
    intens = [0.0 for i in range(numThetas)]

    #// scratch variables:
    #double logSource, lnInteg, integrand, invCosTheta, delta, newInt, increment;
    lineSourceVec = [0.0 for i in range(numDeps)]

    #//Get line source function vector, of needed:
    if (lineMode): 
        lineSourceVec = LineProf.lineSource(numDeps, tau, temp, lambda2)
        

    #//for (int il = 0; il < numLams; il++ ) {  
    for it in range(numThetas):

        invCosTheta = 1.0 / cosTheta[1][it]

        newInt = 0

        #// Extended Simpson's Rule - Numerical Recipes in F77, 2nd Ed., p. 128
        #// First point in formula: - Extended Simpson's Rule
        #//  lnSource = Planck.planck(temp[0][0], lambda);
        #//  lnInteg = lnSource - (tau[0][0] * invCosTheta);
        #//  integrand = Math.exp(lnInteg) * invCosTheta;
        #//  delta = (tau[0][1] - tau[0][0]);
        #//  increment = (1.0 / 3.0) * integrand * delta;
        #//  newInt = newInt + increment;
        #//           for (int id = 1; id < numDeps-1; id++) {  //Extended Simpson's Rule
        for id in range(1, numDeps):   #//Extended rectangle rule

            if (lineMode == True):
                #//Line mode mode - ETLA + coherent scattering: S_lambda = (1-eps)*J_lambda + eps*B_lambda
                logSource = lineSourceVec[id]
                #//if (id == 5 && it == 0) {
                #//    System.out.println("logSource scat " + logE * logSource);
                #//}
                #////logSource = Planck.planck(temp[0][id], lambda);
                #//if (id == 5 && it == 0) {
                #//    System.out.println("logSource therm " + logE * logSource);
                #//}
            else:
                #//Continuum mode - S_lambda = B_lambda
                logSource = Planck.planck(temp[0][id], lambda2)
            
                #//        }
            lnInteg = logSource - (tau[0][id] * invCosTheta)
            integrand = math.exp(lnInteg) * invCosTheta
            delta = (tau[0][id] - tau[0][id - 1])

            #// Extended Simpson's rule: 
            #// if ((id % 2) == 1) {
            #//     increment = (4.0 / 3.0) * integrand * delta;
            #//     newInt = newInt + increment;
            #// }
#//
            #//              if ((id % 2) == 0) {
            #//                increment = (2.0 / 3.0) * integrand * delta;
            #//              newInt = newInt + increment;
            #//        }
            #// Extended rectangle rule:
            increment = integrand * delta
            newInt = newInt + increment

            #// the following break-out condition is not so simple if using a closed formula: 
            #// //Only keep adding contributions from deper layers if the contribution
            #// // is significant
            if (tau[0][id] > 2.0 / 3.0):
                if (newInt > 0):
                    if (increment / newInt < cutoff):
                        break




        #} //id - depth loop

        #//   //Last point - Extended Simpson's Rule:
        #//   lnSource = Planck.planck(temp[0][numDeps - 1], lambda);
        #//   lnInteg = lnSource - (tau[0][numDeps - 1] * invCosTheta);
        #//   integrand = Math.exp(lnInteg) * invCosTheta;
        #//   delta = (tau[0][numDeps - 1] - tau[0][numDeps - 2]);
        #//   increment = (1.0 / 3.0) * integrand * delta;
        #//   newInt = newInt + increment;
        intens[it] = newInt

    #}   //it - theta loop

    ##//} // il - lambda loop
    return intens
 #}