# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:26:42 2017

@author: Ian
"""
import math
import Useful
import ToolBox

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

def delta(linePoints, lam0In, numDeps, tauRos, massIn, xiTIn, teff):

    """//delta function line profile for initiali check of line strength"""

    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)

    logE = math.log10(math.e) #// for debug output

    #//System.out.println("LineProf: doppler, logDopp: " + doppler + " " + logE*logDopp);

    #//Put input parameters into linear cgs units:

    #//System.out.println("LINEGRID: Tau1: " + tau1);
    #//logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp;
    #//a = Math.exp(logA);
    #//System.out.println("LINEGRID: logA: " + logE * logA);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    numPoints = 1
    #//System.out.println("LineProf: numPoints: " + numPoints);

    #// Return a 2D numPoints X numDeps array of normalized line profile points (phi)

    lineProf = [ [ 0.0 for i in range(numDeps) ] for j in range(1) ]
    c = Useful.c()
    logC = Useful.logC()
    logK = Useful.logK()
    amu = Useful.amu()
    ln10 = math.log(10.0)
    ln2 = math.log(2.0)
    lnSqRtPi = 0.5 * math.log(math.pi)
    logTeff = math.log(teff)
    xiT = xiTIn * 1.0E5 #//km/s to cm/s
    logMass = math.log(massIn * amu)  #//amu to g
    #// Compute depth-independent Doppler width, Delta_lambda_D:
    #double doppler, logDopp;
    #double logHelp, help; //scratch
    logHelp = ln2 + logK + logTeff - logMass #// M-B dist, square of v_mode
    help = math.exp(logHelp) + xiT * xiT #// quadratic sum of thermal v and turbulent v
    logHelp = 0.5 * math.log(help)
    logDopp = logHelp + logLam0 - logC
    doppler = math.exp(logDopp)  #// cm


    #// Line profile points in Doppler widths - needed for Voigt function, H(a,v):
    #double ii;

    #// lineProf[0][0] = 0.0; v[0] = 0.0; //Line centre - cannot do logaritmically!
    #double  delta, core, logDelta;
    #//int il0 = 36;
    #//System.out.println("il0 " + il0 + " temp[il] " + temp[0][il0] + " press[il] " + logE*press[1][il0]);
    for id in range(numDeps):

        #//if (il <= numCore) {

        #// - Gaussian ONLY - at line centre Lorentzian will diverge!
        delta = 1.0
        #//System.out.println("LINEGRID- CORE: core: " + core);

        #//System.out.println("LINEGRID: il, v[il]: " + il + " " + v[il] + " lineProf[0][il]: " + lineProf[0][il]);
        #//System.out.println("LINEGRID: il, Voigt, H(): " + il + " " + voigt);
        #//Convert from H(a,v) in dimensionless Voigt units to physical phi((Delta lambda) profile:
        logDelta = math.log(delta) + 2.0 * logLam0 - lnSqRtPi - logDopp - logC

        lineProf[0][id] = math.exp(logDelta)
        #//if (id == 36) {
        #//    System.out.println("il " + il + " linePoints " + 1.0e7 * linePoints[0][il] + " id " + id + " lineProf[il][id] " + lineProf[il][id]);
        #//}

        #//System.out.println("LineProf: il, id, lineProf[il][id]: " + il + " " + id + " " + lineProf[il][id]);

        #// if (id == 20) {
        #//     for (int il = 0; il < numPoints; il++) {
        #//        System.out.format("Voigt: %20.16f   %20.16f%n", linePoints[1][il], logE * Math.log(lineProf[il][id]));
        #//    }
        #// }
    #} //id loop

    return lineProf

#} //end method delta()


def gauss(linePoints, lam0In, numDeps, teff, tauRos, temp, tempSun):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;

    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)

    ln10 = math.log(10.0)
    ln2 = math.log(2.0)
    ln4pi = math.log(4.0 * math.pi)
    lnSqRtPi = 0.5 * math.log(math.pi)
    sqPi = math.sqrt(math.pi)
    #//double ln100 = 2.0*Math.log(10.0);

    logE = math.log10(math.e) #// for debug output

    doppler = linePoints[0][1] / linePoints[1][1]
    logDopp = math.log(doppler)
    tiny = 1.0e-19  #//??


    #//System.out.println("LineProf: doppler, logDopp: " + doppler + " " + logE*logDopp);

    #//Put input parameters into linear cgs units:

    #//System.out.println("LINEGRID: Tau1: " + tau1);
    #//logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp;
    #//a = Math.exp(logA);
    #//System.out.println("LINEGRID: logA: " + logE * logA);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    numPoints = len(linePoints[0])
    #//System.out.println("LineProf: numPoints: " + numPoints);

    #// Return a 2D numPoints X numDeps array of normalized line profile points (phi)
    lineProf = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [ 0.0 for i in range(numPoints) ]
    #double logV, ii;

    #// lineProf[0][0] = 0.0; v[0] = 0.0; //Line centre - cannot do logaritmically!
    #double  gauss, core, logGauss;
    gauss = tiny  #//default initialization
    #//int il0 = 36;
    #//System.out.println("il0 " + il0 + " temp[il] " + temp[0][il0] + " press[il] " + logE*press[1][il0]);
    for id in range(numDeps):

        for il in range(numPoints):

            v[il] = linePoints[1][il]
            #//System.out.println("LineProf: il, v[il]: " + il + " " + v[il]);

            #//if (il <= numCore) {
            if (v[il] <= 3.5 and v[il] >= -3.5):

                #// - Gaussian ONLY - at line centre Lorentzian will diverge!
                core = math.exp(-1.0 * (v[il] * v[il]))
                gauss = core
                #//System.out.println("LINEGRID- CORE: core: " + core);

            #} 

            #//System.out.println("LINEGRID: il, v[il]: " + il + " " + v[il] + " lineProf[0][il]: " + lineProf[0][il]);
            #//System.out.println("LINEGRID: il, Voigt, H(): " + il + " " + voigt);
            #//Convert from H(a,v) in dimensionless Voigt units to physical phi((Delta lambda) profile:
            logGauss = math.log(gauss) + 2.0 * logLam0 - lnSqRtPi - logDopp - logC

            lineProf[il][id] = math.exp(logGauss)
            #//if (id == 36) {
            #//    System.out.println("il " + il + " linePoints " + 1.0e7 * linePoints[0][il] + " id " + id + " lineProf[il][id] " + lineProf[il][id]);
            #//}

            #//System.out.println("LineProf: il, id, lineProf[il][id]: " + il + " " + id + " " + lineProf[il][id]);
        #} // il lambda loop

        #// if (id == 20) {
        #//     for (int il = 0; il < numPoints; il++) {
        #//        System.out.format("Voigt: %20.16f   %20.16f%n", linePoints[1][il], logE * Math.log(lineProf[il][id]));
        #//    }
        #// }
    #} //id loop


    """  /* Debug
         // Check that line profile is area-normalized (it is NOT, area = 1.4845992503443734E-19!, but IS constant with depth - !?:
         double delta;
         for (int id = 0; id < numDeps; id++) {
         double sum = 0.0;
         for (int il = 1; il < numPoints2; il++) {
         delta = lineProf2[0][il][id] - lineProf2[0][il - 1][id];
         sum = sum + (lineProf2[1][il][id] * delta);
         }
         System.out.println("LineGrid: id, Profile area = " + id + " " + sum );
         }
         */ """
    return lineProf

#} //end method gauss()


def voigt(linePoints, lam0In, logAij, logGammaCol,
          numDeps, teff, tauRos, temp, pGas,
          tempSun, pGasSun, hjertComp, dbgHandle):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;

    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)

    ln10 = math.log(10.0)
    ln2 = math.log(2.0);
    ln4pi = math.log(4.0 * math.pi)
    #lnSqRtPi = 0.5 * math.log(math.pi)
    sqRtPi = math.sqrt(math.pi)
    sqPi = math.sqrt(math.pi)
    #//double ln100 = 2.0*Math.log(10.0);

    logE = math.log10(math.e) #// for debug output

    doppler = linePoints[0][1] / linePoints[1][1]
    logDopp = math.log(doppler)
    #//System.out.println("LineProf: doppler, logDopp: " + doppler + " " + logE*logDopp);

    #//Put input parameters into linear cgs units:
    #//double gammaCol = Math.pow(10.0, logGammaCol);
    #// Lorentzian broadening:
    #// Assumes Van der Waals dominates radiative damping
    #// log_10 Gamma_6 for van der Waals damping around Tau_Cont = 1 in Sun 
    #//  - p. 57 of Radiative Transfer in Stellar Atmospheres (Rutten)
    logGammaSun = 9.0 * ln10 #// Convert to base e 
    #//double logFudge = Math.log(2.5);  // Van der Waals enhancement factor

    tau1 = ToolBox.tauPoint(numDeps, tauRos, 1.0)
    #outline = ("tau1 "+ str(tau1) + "\n")
    #dbgHandle.write(outline)

    #//System.out.println("LINEGRID: Tau1: " + tau1);
    #//logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp;
    #//a = Math.exp(logA);
    #//System.out.println("LINEGRID: logA: " + logE * logA);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    numPoints = len(linePoints[0])
    #//System.out.println("LineProf: numPoints: " + numPoints);

    #// Return a 2D numPoints X numDeps array of normalized line profile points (phi)
    lineProf = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [0.0 for i in range(numPoints)]
    #double logV, ii;

    #//  lineProf[0][0] = 0.0; v[0] = 0.0; //Line centre - cannot do logaritmically!
    #double gamma, logGamma, a, logA, voigt, core, wing, logWing, logVoigt;
    Aij = math.pow(10.0, logAij)
    il0 = 36
    #// For Hjerting function approximation:
    #double vSquare, vFourth, vAbs, a2, a3, a4, Hjert0, Hjert1, Hjert2, Hjert3, Hjert4, hjertFn;
    #//System.out.println("il0 " + il0 + " temp[il] " + temp[0][il0] + " press[il] " + logE*press[1][il0]);
    for id in range(numDeps):

        #//Formula from p. 56 of Radiative Transfer in Stellar Atmospheres (Rutten),
        #// logarithmically with respect to solar value:
        logGamma = pGas[1][id] - pGasSun[1][tau1] + 0.7 * (tempSun[1][tau1] - temp[1][id]) + logGammaSun
        #if (id%5 == 1): 
        #    outline = ("id "+ str(id)+ " logGamma "+ str(logGamma) + "\n")
        #    dbgHandle.write(outline)
        #//logGamma = logGamma + logFudge + logGammaCol;
        logGamma = logGamma + logGammaCol
        #//Add radiation (natural) broadning:
        gamma = math.exp(logGamma) + Aij
        logGamma = math.log(gamma)
        #//
        #//if (id == 12){
        #//System.out.println("LineGrid: logGamma: " + id + " " + logE * logGamma + " press[1][id] " + press[1][id] + " pressSun[1][tau1] " 
        #// + pressSun[1][tau1] + " temp[1][id] " + temp[1][id] + " tempSun[1][tau1] " + tempSun[1][tau1]); 
        #//     }

        #//Voigt "a" parameter with line centre wavelength:
        logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp
        a = math.exp(logA)
        a2 = math.exp(2.0*logA)
        a3 = math.exp(3.0*logA)
        a4 = math.exp(4.0*logA)

        #//    if (id == 12) {
        #//System.out.println("LineGrid: lam0: " + lam0 + " logGam " + logE * logGamma + " logA " + logE * logA);
        #//     }
        #//if (id == 30) {
        #//    //System.out.println("il   v[il]   iy   y   logNumerator   logDenominator   logInteg ");
        #//    System.out.println("voigt:   v   logVoigt: ");
        #//}
        for il in range(numPoints):

            v[il] = linePoints[1][il]
            vAbs = abs(v[il])
            vSquare = vAbs * vAbs
            vFourth = vSquare * vSquare
            #//System.out.println("LineProf: il, v[il]: " + il + " " + v[il]);

            #//Approximate Hjerting fn from tabulated expansion coefficients:
            #// Interpolate in Hjerting table to exact "v" value for each expanstion coefficient:
            #// Row 0 of Hjerting component table used for tabulated abscissae, Voigt "v" parameter
            if (vAbs <= 12.0):
                #//we are within abscissa domain of table
                Hjert0 = ToolBox.interpol(hjertComp[0], hjertComp[1], vAbs)
                Hjert1 = ToolBox.interpol(hjertComp[0], hjertComp[2], vAbs)
                Hjert2 = ToolBox.interpol(hjertComp[0], hjertComp[3], vAbs)
                Hjert3 = ToolBox.interpol(hjertComp[0], hjertComp[4], vAbs)
                Hjert4 = ToolBox.interpol(hjertComp[0], hjertComp[5], vAbs)
            else:
                #// We use the analytic expansion
                Hjert0 = 0.0
                Hjert1 = (0.56419 / vSquare) + (0.846 / vFourth)
                Hjert2 = 0.0
                Hjert3 = -0.56 / vFourth
                Hjert4 = 0.0
           
#//Approximate Hjerting fn with power expansion in Voigt "a" parameter
#// "Observation & Analysis of Stellar Photospeheres" (D. Gray), 3rd Ed., p. 258:
            hjertFn = Hjert0 + a*Hjert1 + a2*Hjert2 + a3*Hjert3 + a4*Hjert4
            #if ((id%5 == 1) and (il%2 == 0)):
            #    outline = ("il "+ str(il)+ " hjertFn "+ str(hjertFn) + "\n")
            #    dbgHandle.write(outline)
            """/* Gaussian + Lorentzian approximation:
                //if (il <= numCore) {
                if (v[il] <= 2.0 && v[il] >= -2.0) {

                    // - Gaussian ONLY - at line centre Lorentzian will diverge!
                    core = Math.exp(-1.0 * (v[il] * v[il]));
                    voigt = core;
                    //System.out.println("LINEGRID- CORE: core: " + core);

                } else {

                    logV = Math.log(Math.abs(v[il]));

                    //Gaussian core:
                    core = Math.exp(-1.0 * (v[il] * v[il]));
               // if (id == 12) {
                //    System.out.println("LINEGRID- WING: core: " + core);
                 //   }
                    //Lorentzian wing:
                    logWing = logA - lnSqRtPi - (2.0 * logV);
                    wing = Math.exp(logWing);

                    voigt = core + wing;
               // if (id == 12) {
                //    System.out.println("LINEGRID- WING: wing: " + wing + " logV " + logV);
                 //     }
                } // end else
            */"""
            #//System.out.println("LINEGRID: il, v[il]: " + il + " " + v[il] + " lineProf[0][il]: " + lineProf[0][il]);
            #//System.out.println("LINEGRID: il, Voigt, H(): " + il + " " + voigt);
            #//Convert from H(a,v) in dimensionless Voigt units to physical phi((Delta lambda) profile:
            #//logVoigt = Math.log(voigt) + 2.0 * logLam0 - lnSqRtPi - logDopp - logC;
            #//System.out.println("voigt: Before log... id " + id + " il " + il + " hjertFn " + hjertFn);
            #logVoigt = math.log(hjertFn) + 2.0 * logLam0 - lnSqRtPi - logDopp - logC
            voigt = hjertFn * math.pow(lam0, 2) / sqRtPi / doppler / c
            #logVoigt = math.log(voigt)
            #lineProf[il][id] = math.exp(logVoigt)
            lineProf[il][id] = voigt
            if (lineProf[il][id] <= 0.0):
                lineProf[il][id] = 1.0e-49
            #// if (id == 12) {
            #//    System.out.println("il " + il + " linePoints " + 1.0e7 * linePoints[0][il] + " id " + id + " lineProf[il][id] " + lineProf[il][id]);
            #// }

            #//System.out.println("LineProf: il, id, lineProf[il][id]: " + il + " " + id + " " + lineProf[il][id]);
        #} // il lambda loop

        #// if (id == 20) {
        #//     for (int il = 0; il < numPoints; il++) {
        #//        System.out.format("Voigt: %20.16f   %20.16f%n", linePoints[1][il], logE * Math.log(lineProf[il][id]));
        #//    }
        #// }
    #} //id loop


    return lineProf

#} //end method voigt()


def stark(linePoints, lam0In, logAij, logGammaCol,
          numDeps, teff, tauRos, temp, pGas, Ne,
          tempSun, pGasSun, hjertComp, lineName):

    c = Useful.c()
    logC = Useful.logC()
    #//double k = Useful.k;
    logK = Useful.logK()
    #//double e = Useful.e;
    #//double mE = Useful.mE;

    lam0 = lam0In #// * 1.0E-7; //nm to cm
    logLam0 = math.log(lam0)
    logLam0A = math.log(lam0) + 8.0*math.log(10.0) #//cm to A

    ln10 = math.log(10.0)
    ln2 = math.log(2.0)
    ln4pi = math.log(4.0 * math.pi)
    lnSqRtPi = 0.5 * math.log(math.pi)
    sqRtPi = math.sqrt(math.pi)
    sqPi = math.sqrt(math.pi)
    #//double ln100 = 2.0*Math.log(10.0);

    logE = math.log10(math.e) #// for debug output

    doppler = linePoints[0][1] / linePoints[1][1]
    logDopp = math.log(doppler)
    #//System.out.println("LineProf: doppler, logDopp: " + doppler + " " + logE*logDopp);

    #//Put input parameters into linear cgs units:
    #//double gammaCol = Math.pow(10.0, logGammaCol);
    #// Lorentzian broadening:
    #// Assumes Van der Waals dominates radiative damping
    #// log_10 Gamma_6 for van der Waals damping around Tau_Cont = 1 in Sun 
    #//  - p. 57 of Radiative Transfer in Stellar Atmospheres (Rutten)
    logGammaSun = 9.0 * ln10 #// Convert to base e 
    #//double logFudge = Math.log(2.5);  // Van der Waals enhancement factor

    tau1 = ToolBox.tauPoint(numDeps, tauRos, 1.0)

    #//System.out.println("LINEGRID: Tau1: " + tau1);
    #//logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp;
    #//a = Math.exp(logA);
    #//System.out.println("LINEGRID: logA: " + logE * logA);
    #//Set up a half-profile Delta_lambda grid in Doppler width units 
    #//from line centre to wing
    numPoints = len(linePoints[0])
    #//System.out.println("LineProf: numPoints: " + numPoints);

    #// Return a 2D numPoints X numDeps array of normalized line profile points (phi)
    lineProf = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    #// Line profiel points in Doppler widths - needed for Voigt function, H(a,v):
    v = [0.0 for i in range(numPoints)]
    #double logV, ii;

    #//   lineProf[0][0] = 0.0; v[0] = 0.0; //Line centre - cannot do logaritmically!
    #double gamma, logGamma, a, logA, voigt, core, wing, logWing, logVoigt;
    Aij = math.pow(10.0, logAij)
    il0 = 36
    #// For Hjerting function approximation:
    #double vSquare, vFourth, vAbs, a2, a3, a4, Hjert0, Hjert1, Hjert2, Hjert3, Hjert4, hjertFn;

    #//Parameters for linear Stark broadening:
    #//Assymptotic ("far wing") "K" parameters
    #//Stehle & Hutcheon, 1999, A&A Supp Ser, 140, 93 and CDS data table
    #//Assume K has something to do with "S" and proceed as in Observation and Analysis of
    #// Stellar Photosphere, 3rd Ed. (D. Gray), Eq. 11.50,
    #//
    logTuneStark = math.log(3.16e7) #//convert DeltaI K parameters to deltaS STark profile parameters
    logKStark = [0.0 for i in range(11)]
    logKStark[0] = math.log(2.56e-03) + logTuneStark  #//Halpha
    logKStark[1] = math.log(7.06e-03) + logTuneStark   #//Hbeta
    logKStark[2] = math.log(1.19e-02) + logTuneStark  #//Hgamma
    logKStark[3] = math.log(1.94e-02) + logTuneStark  #//Hdelta
    logKStark[4] = math.log(2.95e-02) + logTuneStark  #//Hepsilon
    logKStark[5] = math.log(4.62e-02) + logTuneStark  #//H8 JB
    logKStark[6] = math.log(6.38e-02) + logTuneStark  #//H9 JB
    logKStark[7] = math.log(8.52e-02) + logTuneStark  #//H10 JB
    logKStark[8] = math.log(1.12e-01) + logTuneStark  #//H11 JB
    logKStark[9] = math.log(1.43e-01) + logTuneStark  #//H12 JB
    logKStark[10] = math.log(1.80e-01) + logTuneStark  #//H13 JB
   #//logKStark[11] = Math.log(2.11) + logTuneStark; //H30 JB
    
    thisLogK = [0.0 for i in range(4)] #//default initialization
    #//double thisLogK = logKStark[10]; //default initialization
    
    #//which Balmer line are we?  crude but effective:
    if (lam0In > 650.0e-7):
        thisLogK = logKStark[0]  #//Halpha
        #//System.out.println("Halpha")
    #}
    if ( (lam0In > 480.0e-7) and (lam0In < 650.0e-7) ):
        #//System.out.println("Hbeta");
        thisLogK = logKStark[1]  #//Hbeta
    #}
    if ( (lam0In > 420.0e-7) and (lam0In < 470.0e-7) ):
       #//System.out.println("Hgamma");
       thisLogK = logKStark[2]  #//Hgamma
    #}
    if ( (lam0In > 400.0e-7) and (lam0In < 450.0e-7) ):
       #//System.out.println("Hdelta");
       thisLogK = logKStark[3]  #//Hdelta
   
    if ( (lam0In < 400.0e-7) ):
       #//System.out.println("Hepsilon");
       thisLogK = logKStark[4]  #//Hepsilon
    #}
#//   if ((lam0In < 390.0e-7)){
#//
#////This won't work here - "species" is always just "HI":
#//      int numberInName = (int) lineName.substring("HI".length());
#//      //console.log(numberInName);
#//      thisLogK = logKStark[numberInName-3];
#//   }


#//
    #double F0, logF0, lamOverF0, logLamOverF0; //electrostatic field strength (e.s.u.)
    #double deltaAlpha, logDeltaAlpha, logStark, logStarkTerm; //reduced wavelength de-tuning parameter (Angstroms/e.s.u.)
    logF0Fac = math.log(1.249e-9)
#// log wavelength de-tunings in A:
    #double logThisPoint, thisPoint;

    #//System.out.println("il0 " + il0 + " temp[il] " + temp[0][il0] + " press[il] " + logE*press[1][il0]);
    for id in range(numDeps):

        #//linear Stark broadening stuff:
        logF0 = logF0Fac + (0.666667)*Ne[1][id]
        logLamOverF0 = logLam0A - logF0
        lamOverF0 = math.exp(logLamOverF0)

        #//System.out.println("id " + id + " logF0 " + logE*logF0 + " logLamOverF0 " + logE*logLamOverF0 + " lamOverF0 " + lamOverF0);
        #//Formula from p. 56 of Radiative Transfer in Stellar Atmospheres (Rutten),
        #// logarithmically with respect to solar value:
        logGamma = pGas[1][id] - pGasSun[1][tau1] + 0.7 * (tempSun[1][tau1] - temp[1][id]) + logGammaSun
        #//logGamma = logGamma + logFudge + logGammaCol
        logGamma = logGamma + logGammaCol
        #//Add radiation (natural) broadning:
        gamma = math.exp(logGamma) + Aij
        logGamma = math.log(gamma)
        #//
        #//if (id == 12){
        #//System.out.println("LineGrid: logGamma: " + id + " " + logE * logGamma + " press[1][id] " + press[1][id] + " pressSun[1][tau1] " 
        #// + pressSun[1][tau1] + " temp[1][id] " + temp[1][id] + " tempSun[1][tau1] " + tempSun[1][tau1]); 
        #//     }

        #//Voigt "a" parameter with line centre wavelength:
        logA = 2.0 * logLam0 + logGamma - ln4pi - logC - logDopp
        a = math.exp(logA)
        a2 = math.exp(2.0*logA)
        a3 = math.exp(3.0*logA)
        a4 = math.exp(4.0*logA)

        #//    if (id == 12) {
        #//System.out.println("LineGrid: lam0: " + lam0 + " logGam " + logE * logGamma + " logA " + logE * logA);
        #//     }
        #//if (id == 30) {
        #//    //System.out.println("il   v[il]   iy   y   logNumerator   logDenominator   logInteg ");
        #//    System.out.println("voigt:   v   logVoigt: ");
        #//}
        for il in range(numPoints):

            v[il] = linePoints[1][il]
            vAbs = abs(v[il])
            vSquare = vAbs * vAbs
            vFourth = vSquare * vSquare
            #//System.out.println("LineProf: il, v[il]: " + il + " " + v[il]);

            #//Approximate Hjerting fn from tabulated expansion coefficients:
            #// Interpolate in Hjerting table to exact "v" value for each expanstion coefficient:
            #// Row 0 of Hjerting component table used for tabulated abscissae, Voigt "v" parameter
            if (vAbs <= 12.0):
                #//we are within abscissa domain of table
                Hjert0 = ToolBox.interpol(hjertComp[0], hjertComp[1], vAbs)
                Hjert1 = ToolBox.interpol(hjertComp[0], hjertComp[2], vAbs)
                Hjert2 = ToolBox.interpol(hjertComp[0], hjertComp[3], vAbs)
                Hjert3 = ToolBox.interpol(hjertComp[0], hjertComp[4], vAbs)
                Hjert4 = ToolBox.interpol(hjertComp[0], hjertComp[5], vAbs)
            else:
                #// We use the analytic expansion
                Hjert0 = 0.0
                Hjert1 = (0.56419 / vSquare) + (0.846 / vFourth)
                Hjert2 = 0.0
                Hjert3 = -0.56 / vFourth
                Hjert4 = 0.0
            #}
            #//Approximate Hjerting fn with power expansion in Voigt "a" parameter
            #// "Observation & Analysis of Stellar Photospeheres" (D. Gray), 3rd Ed., p. 258:
            hjertFn = Hjert0 + a*Hjert1 + a2*Hjert2 + a3*Hjert3 + a4*Hjert4;
            logStark = -49.0 #//re-initialize

            if (vAbs > 2.0):

                #//System.out.println("Adding in Stark wing");

                thisPoint = 1.0e8 * abs(linePoints[0][il]) #//cm to A
                logThisPoint = math.log(thisPoint)
                logDeltaAlpha = logThisPoint - logF0
                deltaAlpha = math.exp(logDeltaAlpha)
                logStarkTerm = ( math.log(lamOverF0 + deltaAlpha) - logLamOverF0 )
                logStark = thisLogK + 0.5*logStarkTerm - 2.5*logDeltaAlpha

                #//System.out.println("il " + il + " logDeltaAlpha " + logE*logDeltaAlpha + " logStarkTerm " + logE*logStarkTerm  + " logStark " + logE*logStark);
                #//console.log("il " + il + " logDeltaAlpha " + logE*logDeltaAlpha + " logStarkTerm " + logE*logStarkTerm  + " logStark " + logE*logStark);

                #//System.out.println("id " + id + " il " + il + " v[il] " + v[il] 
                #//  + " hjertFn " + hjertFn + " Math.exp(logStark) " + Math.exp(logStark));
                #//not here! hjertFn = hjertFn + Math.exp(logStark);
            

            #//System.out.println("LINEGRID: il, v[il]: " + il + " " + v[il] + " lineProf[0][il]: " + lineProf[0][il]);
            #//System.out.println("LINEGRID: il, Voigt, H(): " + il + " " + voigt);
            #//Convert from H(a,v) in dimensionless Voigt units to physical phi((Delta lambda) profile:
            #//logVoigt = Math.log(voigt) + 2.0 * logLam0 - lnSqRtPi - logDopp - logC;
            #//System.out.println("stark: Before log... id " + id + " il " + il + " hjertFn " + hjertFn);
            #logVoigt = math.log(hjertFn) - lnSqRtPi - logDopp
            voigt = hjertFn / sqRtPi / doppler
            #//logVoigt = math.log(voigt)
            logStark = logStark - logF0
            if (vAbs > 2.0):
                #//if (id == 24) {
                #//   System.out.println("il " + il + " v[il] " + v[il] + " logVoigt " + logE*logVoigt + " logStark " + logE*logStark);
                #//}
                #//voigt = math.exp(logVoigt) + math.exp(logStark)
                voigt = voigt + math.exp(logStark)
                #//logVoigt = math.log(voigt)
            
            #logVoigt = logVoigt + 2.0 * logLam0 - logC
            voigt = voigt * math.pow(lam0, 2) / c
            #//lineProf[il][id] = math.exp(logVoigt)
            lineProf[il][id] = voigt
            if (lineProf[il][id] <= 0.0):
                lineProf[il][id] = 1.0e-49
            #//if (id == 24) {
            #//    System.out.println("lam0In " + lam0In);
            #//    System.out.println("il " + il + " linePoints " + 1.0e7 * linePoints[0][il] + " id " + id + " lineProf[il][id] " + lineProf[il][id]);
            #//}

            #//System.out.println("LineProf: il, id, lineProf[il][id]: " + il + " " + id + " " + lineProf[il][id]);
        #} // il lambda loop

        #// if (id == 20) {
        #//     for (int il = 0; il < numPoints; il++) {
        #//        System.out.format("Voigt: %20.16f   %20.16f%n", linePoints[1][il], logE * Math.log(lineProf[il][id]));
        #//    }
        #// }
    #} //id loop


    return lineProf

#} //end method stark()



def lineSource(numDeps, tau, temp, lambda2):

    """#// Make line source function:
    #// Equivalenth two-level atom (ETLA) approx
    #//CAUTION: input lambda in nm"""
    
    lineSource = [0.0 for i in range(numDeps)]

    #//thermal photon creation/destruction probability
    epsilon = 0.01 #//should decrease with depth??

    #//This is an artifact of jayBinner's original purpose:
    grayLevel = 1.0

    #//int iLam0 = numLams / 2; //+/- 1 deltaLambda
    #//double lam0 = linePoints[0][iLam0];  //line centre lambda in cm - not needed:
    #//double lamStart = lambda - 0.1; // nm
    #//double lamStop = lambda + 0.1; // nm
    #//double lamRange = (lamStop - lamStart); // * 1.0e-7; // line width in cm
    #//System.out.println("lamStart " + lamStart + " lamStop " + lamStop + " lamRange " + lamRange);
    jayLambda = [0.0 for i in range(numDeps)]
    BLambda = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
    #double linSrc;

    #// Dress up Blambda to look like what jayBinner expects:
    for i in range(numDeps):
        #//Planck.planck return log(B_lambda):
        BLambda[0][i] = math.exp(Planck.planck(temp[0][i], lambda2))
        BLambda[1][i] = 1.0  #//supposed to be dB/dT, but not needed. 
        

    #//CAUTION: planckBin Row 0 is linear lambda-integrated B_lambda; Row 1 is same for dB_lambda/dT
    #//planckBin = MulGrayTCorr.planckBinner(numDeps, temp, lamStart, lamStop);
    jayLambda = MulGrayTCorr.jayBinner(numDeps, tau, temp, BLambda, grayLevel)
    #//To begin with, coherent scattering - we're not computing line profile-weighted average Js and Bs
    for i in range(numDeps):

        #//planckBin[0][i] = planckBin[0][i] / lamRange;  //line average
        #//jayBin[i] = jayBin[i];  
        linSrc = (1.0 - epsilon) * jayLambda[i] + epsilon * BLambda[0][i]
        lineSource[i] = math.log(linSrc)
        

    return lineSource