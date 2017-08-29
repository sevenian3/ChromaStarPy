# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:31:10 2017

@author: Ian
"""

import math
import Useful

"""/**
 * Line profile, phi_lambda(lambda): Assume Voigt function profile - need H(a,v)
 * Assumes CRD, LTE, ??? Input parameters: lam0 - line center wavelength in nm
 * mass - mass of absorbing particle (amu) logGammaCol - log_10(gamma) - base 10
 * logarithmic collisional (pressure) damping co-efficient (s^-1) epsilon -
 * convective microturbulence- non-thermal broadening parameter (km/s) Also
 * needs atmospheric structure information: numDeps WON'T WORK - need observer's
 * frame fixed lambda at all depths: temp structure for depth-dependent thermal
 * line broadening Teff as typical temp instead of above pressure structure,
 * pGas, if scaling gamma
 */"""

def lineGridDelta(lam0In, massIn, xiTIn, numDeps, teff):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;
    amu = Useful.amu()

    ln10 = math.log(10.0)
    ln2 = math.log(2.0)

    logE = math.log10(math.e) #// for debug output

    #//Put input parameters into linear cgs units:
    #//double gammaCol = Math.pow(10.0, logGammaCol);
    logTeff = math.log(teff)

    xiT = xiTIn * 1.0E5 #//km/s to cm/s
    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)
    logMass = math.log(massIn * amu)  #//amu to g 

    #// Compute depth-independent Doppler width, Delta_lambda_D:
    #double doppler, logDopp;
    #double logHelp, help; //scratch

    logHelp = ln2 + logK + logTeff - logMass #// M-B dist, square of v_mode
    help = math.exp(logHelp) + xiT * xiT #// quadratic sum of thermal v and turbulent v
    logHelp = 0.5 * math.log(help)
    logDopp = logHelp + logLam0 - logC

    doppler = math.exp(logDopp)  #// cm

    #//System.out.println("LineGrid: doppler, logDopp: " + doppler + " " + logE*logDopp);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    #//int numCore = 5;
    #//int numWing = 5;
    #//int numWing = 0;  //debug
    numPoints = 1

    #// a 2D 2 X numPoints array of Delta Lambdas 
    #// Row 0 : Delta lambdas in cm - will need to be in nm for Planck and Rad Trans?
    #// Row 1 : Delta lambdas in Doppler widths
    linePoints = [ [ 0.0 for i in range(numPoints) ] for j in range(2) ]

    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [ 0.0 for i in range(numPoints) ]


    #double logV, ii, jj;

    il = 0
    ii = float(il)


    #// In core, space v points linearly:
    #// Voigt "v" parameter
    #// v > 0 --> This is the *red* wing:
    v[il] = ii
    linePoints[0][il] = doppler * v[il]
    linePoints[1][il] = v[il]

    #//System.out.println("LineGrid: il, lam, v: " + il + " " + 
    #//        linePoints[0][il] + " " + linePoints[1][il]);

    return linePoints

#} //end method lineGridDelta
#//
#//
#//
def lineGridGauss(lam0In, massIn, xiTIn, numDeps, teff, numCore):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;
    amu = Useful.amu()

    dln10 = math.log(10.0)
    ln2 = math.log(2.0)

    logE = math.log10(math.e) #// for debug output

    #//Put input parameters into linear cgs units:
    #//double gammaCol = Math.pow(10.0, logGammaCol);
    logTeff = math.log(teff)

    xiT = xiTIn * 1.0E5 #//km/s to cm/s
    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)
    logMass = math.log(massIn * amu)  #//amu to g 

    #// Compute depth-independent Doppler width, Delta_lambda_D:
    #double doppler, logDopp;
    #double logHelp, help; //scratch

    logHelp = ln2 + logK + logTeff - logMass #// M-B dist, square of v_mode
    help = math.exp(logHelp) + xiT * xiT #// quadratic sum of thermal v and turbulent v
    logHelp = 0.5 * math.log(help)
    logDopp = logHelp + logLam0 - logC

    doppler = math.exp(logDopp)  #// cm

    #//System.out.println("LineGrid: doppler, logDopp: " + doppler + " " + logE*logDopp);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    #//int numCore = 5;
    #//int numWing = 5;
    #//int numWing = 0;  //debug
    numPoints = numCore

    #// a 2D 2 X numPoints array of Delta Lambdas 
    #// Row 0 : Delta lambdas in cm - will need to be in nm for Planck and Rad Trans?
    #// Row 1 : Delta lambdas in Doppler widths
    linePoints = [ [ 0.0 for i in range(numPoints) ] for j in range(2) ]

    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [0.0 for i in range(numPoints)]

    maxCoreV = 3.5 #//core half-width ~ in Doppler widths
    #//double maxWingDeltaLogV = 1.5 * ln10; //maximum base e logarithmic shift from line centre in Doppler widths
    minWingDeltaLogV = math.log(maxCoreV + 1.5)
    maxWingDeltaLogV = 9.0 + minWingDeltaLogV

    #double logV, ii, jj;

    for il in range(numPoints):

        ii = float(il)


        #// In core, space v points linearly:
        #// Voigt "v" parameter
        #// v > 0 --> This is the *red* wing:
        v[il] = ii * maxCoreV / (numCore - 1)
        linePoints[0][il] = doppler * v[il]
        linePoints[1][il] = v[il]


        #//System.out.println("LineGrid: il, lam, v: " + il + " " + 
        #//        linePoints[0][il] + " " + linePoints[1][il]);
    #} // il lambda loop

    #// Add the negative DeltaLambda half of the line:
    numPoints2 = (2 * numPoints) - 1
    #//System.out.println("LineGrid: numpoints2: " + numPoints2);

    #// Return a 2D 2 X (2xnumPoints-1) array of Delta Lambdas 
    #// Row 0 : Delta lambdas in cm - will need to be in nm for Planck and Rad Trans?
    #// Row 1 : Delta lambdas in Doppler widths
    linePoints2 = [ [ 0.0 for i in range(numPoints2) ] for j in range(2) ]

    #//wavelengths are depth-independent - just put them in the 0th depth slot:
    for il2 in range(numPoints2):

        if (il2 < numPoints - 1):

            il = (numPoints - 1) - il2
            linePoints2[0][il2] = -1.0 * linePoints[0][il]
            linePoints2[1][il2] = -1.0 * linePoints[1][il]

        else:

            #//Positive DelataLambda half:   
            il = il2 - (numPoints - 1)
            linePoints2[0][il2] = linePoints[0][il]
            linePoints2[1][il2] = linePoints[1][il]


    #//System.out.println("LineGrid: il2, lam, v: " + il2 + " " + 
    #//        linePoints2[0][il2] + " " + linePoints2[1][il2]);
    #} //il2 loop

    return linePoints2

#} //end method lineGridGauss

#//
#//
#//
   
def lineGridVoigt(lam0In, massIn, xiTIn, numDeps, teff, numCore, numWing, species):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;
    amu = Useful.amu()

    ln10 = math.log(10.0)
    ln2 = math.log(2.0)

    logE = math.log10(math.e) #// for debug output

    #//Put input parameters into linear cgs units:
    #//double gammaCol = Math.pow(10.0, logGammaCol);
    logTeff = math.log(teff)

    xiT = xiTIn * 1.0E5 #//km/s to cm/s
    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)
    logMass = math.log(massIn * amu)  #//amu to g 

    #// Compute depth-independent Doppler width, Delta_lambda_D:
    #double doppler, logDopp;
    #double logHelp, help; //scratch

    logHelp = ln2 + logK + logTeff - logMass #// M-B dist, square of v_mode
    help = math.exp(logHelp) + xiT * xiT #// quadratic sum of thermal v and turbulent v
    logHelp = 0.5 * math.log(help)
    logDopp = logHelp + logLam0 - logC

    doppler = math.exp(logDopp)  #// cm

    #//System.out.println("LineGrid: doppler, logDopp: " + doppler + " " + logE*logDopp);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    #//int numCore = 5;
    #//int numWing = 5;
    #//int numWing = 0;  //debug
    numPoints = numCore + numWing

    #// a 2D 2 X numPoints array of Delta Lambdas 
    #// Row 0 : Delta lambdas in cm - will need to be in nm for Planck and Rad Trans?
    #// Row 1 : Delta lambdas in Doppler widths
    linePoints = [ [ 0.0 for i in range(numPoints) ] for j in range(2) ]

    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [0.0 for i in range(numPoints) ]

    maxCoreV = 3.5 #//core half-width ~ in Doppler widths
    #//double maxWingDeltaLogV = 1.5 * ln10; //maximum base e logarithmic shift from line centre in Doppler widths
    minWingDeltaLogV = math.log(maxCoreV + 1.5)
    maxWingDeltaLogV = 9.0 + minWingDeltaLogV
    
    if(species=="HI" and teff>=7000): 
        maxCoreV = 3.5 
        minWingDeltaLogV = math.log(maxCoreV + 1.5)
        maxWingDeltaLogV = 12.0 + minWingDeltaLogV

#//console.log("2)"+maxWingDeltaLogV);
      

    

    #double logV, ii, jj;

    for il in range(numPoints):

        ii = float(il)

        if (il < numCore):

            #// In core, space v points linearly:
            #// Voigt "v" parameter
            #// v > 0 --> This is the *red* wing:
            v[il] = ii * maxCoreV / (numCore - 1)
            linePoints[0][il] = doppler * v[il]
            linePoints[1][il] = v[il]

        else:

            #//Space v points logarithmically in wing
            jj = ii - numCore
            logV = (jj * (maxWingDeltaLogV - minWingDeltaLogV) / (numPoints - 1)) + minWingDeltaLogV
            v[il] = math.exp(logV)
            linePoints[0][il] = doppler * v[il]
            linePoints[1][il] = v[il]

        #} // end else

        #//System.out.println("LineGrid: il, lam, v: " + il + " " + 
        #//        linePoints[0][il] + " " + linePoints[1][il]);
    #} // il lambda loop

    #// Add the negative DeltaLambda half of the line:
    numPoints2 = (2 * numPoints) - 1
    #//System.out.println("LineGrid: numpoints2: " + numPoints2);

    #// Return a 2D 2 X (2xnumPoints-1) array of Delta Lambdas 
    #// Row 0 : Delta lambdas in cm - will need to be in nm for Planck and Rad Trans?
    #// Row 1 : Delta lambdas in Doppler widths
    linePoints2 = [ [ 0.0 for i in range(numPoints2) ] for j in range(2) ]

    #//wavelengths are depth-independent - just put them in the 0th depth slot:
    for il2 in range(numPoints2):

        if (il2 < numPoints - 1):

            il = (numPoints - 1) - il2
            linePoints2[0][il2] = -1.0 * linePoints[0][il]
            linePoints2[1][il2] = -1.0 * linePoints[1][il]

        else:

            #//Positive DelataLambda half:   
            il = il2 - (numPoints - 1)
            linePoints2[0][il2] = linePoints[0][il]
            linePoints2[1][il2] = linePoints[1][il]

            

        #//System.out.println("LineGrid: il2, lam, v: " + il2 + " " + 
        #//        linePoints2[0][il2] + " " + linePoints2[1][il2]);
    #} //il2 loop

    return linePoints2
