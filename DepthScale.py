# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:10:24 2017

@author: ishort
"""

import math

def depthScale(numDeps, tauRos, kappa, rho):
    
    """ /**
 * Returns vector of numDep linear geometric DEPTHS below top of atmosphere - in
 * cm (cgs) for consistency with log(g) units
 *
 */"""

    logE = math.log10(math.e) #// for debug output

    #//double ln10 = Math.log(10.0); //handy wee quantity 
    #//log_10 Rosseland optical depth scale  
    depths = [0.0 for i in range(numDeps)]

    #// Upper bounday condition: 
    #// Zero point at top of atmosphere - this can be shifted later?
    #// log(z) cannot really correspond to zero 
    #//double logZ1 = -10.0;  // log(cm)
    #//depths[0] = Math.pow(10.0, logZ1);  //cm
    #//Start at this depth index - the topmost layers have such low rhos that they correspond to HUUUGE geometric depths!
    iStart = 1
    z1 = 1.0e-19   #//cm
    #//double z1 = -500.0 * 1.0e5; // FOr comparison to O&ASP 3rd Ed. (D.F. Gray), Table 9.2
    for i in range(iStart+1):
        depths[i] = z1
        

    #//double minZ = 1.0E5; // = 1km - Minimum increase in depth from one point to the next
    #// declare scratch variables
    #//double deltaX, deltaZ, logZ2;
    #double deltaX, deltaZ, z2, z3, help, logHelp, helpNext;
    #//        h, k1, k2, k3, k4, logH, logK1, logK2, logK3, logK4;

    #//Trapezoid method for depth at 2nd point in
    #// Need to avoid using rho at upper boundary, so rho value must be taken at y_n+2 on all RHSs
    #/*
    #     deltaX = tauRos[1][1] - tauRos[1][0];
    #     logHelp = tauRos[1][0] - kappa[1][0] - rho[1][2];
    #     System.out.format("%12.8f   %12.8f   %12.8f%n", logE*tauRos[1][0], logE*kappa[1][0], logE*rho[1][2]);
    #     //help = ( tauRos[0][0] / kappa[0][0] ) / rho[0][1];
    #     help = Math.exp(logHelp);
    #     */
    #//First integrand:
    #//deltaX = tauRos[1][iStart+1] - tauRos[1][iStart];
    logHelp = tauRos[1][iStart] - kappa[1][iStart] - rho[1][iStart]
    helpNext = math.exp(logHelp)

#//  deltaZ = (deltaX) * (0.5 * (help + helpNext));
#//  z2 = z1 + deltaZ;
#//  depths[1] = z2;
    help = helpNext

    #//z1 =z2;
    for i in range(iStart + 1, numDeps):

        #//Trapezoid method:
        deltaX = tauRos[1][i] - tauRos[1][i - 1]
        logHelp = tauRos[1][i] - kappa[1][i] - rho[1][i]
        helpNext = math.exp(logHelp)
        #//System.out.format("%12.8f   %12.8f   %12.8f%n", logE*tauRos[1][i], logE*kappa[1][i], logE*rho[1][i]);
        deltaZ = deltaX * (0.5 * (help + helpNext))
        #//System.out.println("i " + i + " tauRos[1] " + logE*tauRos[1][i] + " kappa[1] " + logE*kappa[1][i] + " rho[1] " + logE*rho[1][i] + " deltaX " + deltaX + " deltaZ " + deltaZ);
        z2 = z1 + deltaZ

        depths[i] = z2
        z1 = z2
        help = helpNext

        #//System.out.format("%12.8f   %12.8f%n", logE*tauRos[1][i], z2);

    return depths
