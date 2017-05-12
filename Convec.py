# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:40:19 2017

@author: ishort
"""

import math
import Useful

def convec(numDeps, tauRos, depths, temp, press, rho, kappa, kappaSun,
            zScale, teff, logg, mmw):

    logE = math.log10(math.E) #// for debug output
    ln10 = math.log(10.0) #//needed to convert logg from base 10 to base e

    convTemp = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]

    #//Schwarzschild criterion for convective instability:
    gamma = 5.0 / 3.0  #//adiabatic gamma for ideal monatomic gas - the photon gas is negligible in stars w convection
    gammaFac = gamma / (gamma - 1.0)  #// yeah, yeah - I know it's 2.5, but let's show where it comes from for the record...
    invGamFac = 1.0 / gammaFac
    #//CHEAT: Set gammaThing to value that makes convection just disappear at bottom of mid-F star (7000 K)
    #//double gammaThing = 1.60;
    #//double invGamThing = 1.0 / gammaThing;
    #double invGamThing;
    #//System.out.println("gammaThing " + gammaThing);

    #double deltaP, deltaT; //, dlnPdlnT;
    #double dlnTdlnP, dlnMudlnP, deltaMu;

    #double Hp, logHp;

    #//double HpSun = 1.2535465715411615E7;  //cm, as computed by GrayStar at depth index=36
    HpSun = 2.0e7  #//cm, approximately as computed by GrayStar at depth index=36
    logHpSun = math.log(HpSun)

    #//Compute the presure scale height as a reality check:
    HpRefDep=36  #//index of reference depth for computing pressure scale height
    logHp = press[1][HpRefDep] - rho[1][HpRefDep] - ln10 * logg
    Hp = math.exp(logHp)
        
    #//Try scaling gamma to "fix" the convective boundary
    #//invGamThing = invGamFac * HpSun/Hp;

    #//System.out.println("Hp/HpSun " + Hp/HpSun);
        
    #//double[] mmw = State.mmwFn(numDeps, temp, zScale);

    #//Search outward for top of convection zone
    isStable = False
    iBound = numDeps - 1 #//initialize index of depth where convection begins to bottom of atmosphere
    for i in range(numDeps - 2, 0, -1):

        #//System.out.println("Hp " + Hp);
        #//1st order finite difference - erratic?
        #//double deltaP = press[1][i] - press[1][i-1];
        #//double deltaT = temp[1][i] - temp[1][i-1];
        #//Try "2nd order" finite difference - non-uniform spacing in deltaT
        deltaP = press[1][i + 1] - press[1][i - 1]
        deltaT = temp[1][i + 1] - temp[1][i - 1]
        deltaMu = (mmw[i + 1] - mmw[i]) * Useful.amu
        #//dlnPdlnT = deltaP / deltaT;
        dlnTdlnP = deltaT / deltaP
        dlnMudlnP = deltaMu / deltaP
        #//System.out.format("%12.8f   %12.8f%n", logE * tauRos[1][i], dlnPlndT);
        #// This can be finicky - let's say we have not found the radiative zone unless two consecutive layers meet the criterion
        #//if (dlnPdlnT > gammaThing) {
        if (dlnTdlnP < invGamFac + dlnMudlnP):

            #//Convectively stable
            if (isStable == False):
                #//The previous convectively unstable layer was an isolated anomoly - we're have NOT found the zone!  Reset:
                isStable = true
                iBound = i
                #//System.out.println("First stable layer was found, tauRos " + logE * tauRos[1][i] + " NOW: isStable " + isStable);
                
            #}
        #}
    #}
    #//System.out.println("Convec: iBound " + iBound);

    #//Radiative zone - leave temperatures alone:
    for i in range(iBound):
        convTemp[0][i] = temp[0][i]
        convTemp[1][i] = temp[1][i]
        

    baseTemp = temp[0][iBound]
    baseLogTemp = temp[1][iBound]
    baseTau = tauRos[0][iBound]
    baseLogTau = tauRos[1][iBound]
    #//double baseDepth = depths[iBound]

    logSigma = Useful.logSigma()
    logK = Useful.logK()
    logAmu = Useful.logAmu()

    mixLSun = 1.0  #// convective mixing length in pressure scale heights (H_P)

    betaSun = 0.5  #// factor for square of  convective bubble velocity (range: 0.0 - 1.0)

    #double Cp, logCp;  //Specific heat capacity at constant pressure
    mixL = mixLSun  #//initialization
    beta = betaSun  #//initialization
    teffSun = 5778.0
    loggSun = 4.44

        
    #//Shameless fix:
    #//It seems mixL and beta need to be temp and press dependent:
    if (teff < teffSun):
        mixL = mixLSun * math.pow(teff / teffSun, 4.0)  #//lower teff -> smaller mixL -> steeper SAdGrad
        beta = betaSun * math.pow(teff / teffSun, 4.0)  #//lower teff -> smaller beta -> steeper SAdGrad
         
    mixL = mixL * math.pow(loggSun / logg, 2.0) #// lower logg -> larger mixL -> smaller sAdGrad
    beta = beta * math.pow(loggSun / logg, 2.0) #// lower logg -> larger beta -> smaller sAdGrad
         
    """/*
        //Shameless fix:
        beta = betaSun;  // no fix?
        mixL = mixLSun * Math.pow(Hp / HpSun, 4.0);  //lower teff -> smaller Hp -> smaller mixL -> steeper SAdGrad
        //mixL = mixL * Math.pow(logg / loggSun, 4.0); // lower logg -> smaller mixL -> larger sAdGrad
    */"""
    logMixL = math.log(mixL)
    logBeta = math.log(beta)

    logFluxSurfBol = logSigma + 4.0 * math.log(teff)

    #// This will get hairy when we take it super-adiabatic so let's take it *really* easy and make every factor and term clear:
    logInvGamFac = math.log(invGamFac)

    #//Get the mean molecular weight in amu from State - Row 0 is "mu" in amu:
    #double mu, logMu, logFctr1, logFctr2, logFctr3;
    #double nextTemp, lastTemp, nextTemp2;

    #//Adiabatic dT/dx gradients in various coordinates
    #//tau, logTau space
    #double logAdGradTauMag, logAdGradLogTauMag, adGradLogTau;
    #//SuperAdiabatic dT/dx gradients in various coordinates
    #double deltaTau, logDeltaTau, deltaLogTau, logDeltaLogTau;
    #double sAdGradLogTau, logSadGradR, logSadGradTau, logSadGradLogTau;
    #double lastLogTau;

    #//r space:
    #double logAdGradRMag, adGradR;

    #//SuperAdiabatic dT/dx gradients in various coordinates
    #double deltaR, logDeltaR;
    #/*
    #     double sAdGradR;
    #     double lastDepth;
    #     */

    lastTemp = baseTemp
    lastLogTau = baseLogTau
    #//lastDepth = baseDepth;

    #//System.out.println(
    #//        "tauRos[1][i]   (tauRos[1][i]-lastLogTau)   adGradLogTau   rho[1][i]   kappa[1][i]   lastTemp   nextTemp");
    for i in range(iBound, numDeps):

        mu = mmw[i]
        logMu = math.log(mu)
        logFctr1 = logMu + logAmu - logK
        #//System.out.println("logFactr1 " + logE*logFctr1 + " logInvGamFac " + logE*logInvGamFac + " logg " + logg);
        logCp = math.log(5.0 / 2.0) - logFctr1  #//ideal monatomic gas - underestimate that neglects partial ionization

        #// ** Caution: These are log_e of the *magnitude* of the temperature gradients!
        #//The adiabatic dT/dTau in r space
        logAdGradRMag = logInvGamFac + logFctr1 + ln10 * logg #//logg is in base 10

        #//This is baaad stuff - remember our tuaRos scale has *nothing* to do with our kappa values!
        #//The adiabatic dT/dTau in tau space - divide dT/dr by rho and kappa and make it +ve becasue we're in tau-space:
        #//Bad fake to fix artificially small dT/dr at low Teff - use kappaSun instead of kappa
        logAdGradTauMag = logAdGradRMag - rho[1][i] - kappa[1][i]
        #//The adiabatic dT/dLnTau in log_e(tau) space
        logAdGradLogTauMag = tauRos[1][i] + logAdGradTauMag

        #//Build the T(tau) in the convection zone:
        #// Work in logTau space - numerically safer??
        adGradLogTau = math.exp(logAdGradLogTauMag) #//No minus sign - logTau increases inward...
        nextTemp = lastTemp + adGradLogTau * (tauRos[1][i] - lastLogTau)

        #//System.out.format("%12.8f   %12.8f   %12.8f   %12.8f   %12.8f   %7.1f   %7.1f%n", logE * tauRos[1][i], logE * (tauRos[1][i] - lastLogTau), adGradLogTau, logE * rho[1][i], logE * kappa[1][i], lastTemp, nextTemp);
        """/*
             // Do in geometric depth space
             adGradR = Math.exp(logAdGradRMag); // no minus sign - our depths *increase* inwards (they're NOT heights!)
             nextTemp = lastTemp + adGradR * (depths[i] - lastDepth);  
            
             //System.out.format("%12.8f   %12.8f   %12.8f   %7.1f   %7.1f%n", logE*tauRos[1][i], (depths[i] - lastDepth), adGradR, lastTemp, nextTemp);
             */"""
        #//Okay - now the difference between the superadiabatic and adiabatic dT/dr:
        logFctr2 = rho[1][i] + logCp + 2.0 * logMixL

        #// ** NOTE ** Should temp in the following line be the *convective* temp of the last depth???
        #// logg is in base 10 - convert to base e
        logFctr3 = 3.0 * (ln10 * logg - math.log(lastTemp)) / 2.0

        #//Difference between SuperAdibatic dT/dr and Adiabtic dT/dr in r-space - Carroll & Ostlie 2nd Ed. p. 328
        #//System.out.println("logFluxSurfBol " + logE * logFluxSurfBol + " logFctr2 " + logE * logFctr2 + " logFctr1 " + logE * logFctr1 + " logFctr3 " + logE * logFctr3 + " logBeta " + logE * logBeta);
        logDeltaR = logFluxSurfBol - logFctr2 + 2.0 * logFctr1 + logFctr3 - 0.5 * logBeta
        logDeltaR = 2.0 * logDeltaR / 3.0 #//DeltaR is above formula to the 2/3 power

        #//This is baaad stuff - remember our tuaRos scale has *nothing* to do with our kappa values!
        #//Bad fake to fix artificially small dT/dr at low Teff - use kappaSun instead of kappa
        logDeltaTau = logDeltaR - rho[1][i] - kappa[1][i]
        logDeltaLogTau = tauRos[1][i] + logDeltaTau
        sAdGradLogTau = adGradLogTau + math.exp(logDeltaLogTau)
        #//System.out.format("%12.8f   %12.8f   %12.8f   %12.8f%n", logE*tauRos[1][i], logE*logDeltaR, logE*logDeltaTau, logE*logDeltaLogTau);
        nextTemp2 = lastTemp + sAdGradLogTau * (tauRos[1][i] - lastLogTau)

        """/*
        // Do in geometric depth space
        sAdGradR = adGradR + Math.exp(logDeltaR);
        nextTemp2 = lastTemp + sAdGradR * (depths[i] - lastDepth);
        */"""
        #// set everything to nextTemp2 for superadibatic dT/dr, and to nexTemp for adiabatic dT/dr 
        convTemp[0][i] = nextTemp2
        convTemp[1][i] = math.log(nextTemp2)
        lastTemp = nextTemp2
        lastLogTau = tauRos[1][i]
        #//lastDepth = depths[i]
    #}

    return convTemp
