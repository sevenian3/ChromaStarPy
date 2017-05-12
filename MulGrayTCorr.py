# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:25:33 2017

@author: ishort
"""

import math
import Useful
import ToolBox

def mgTCorr(numDeps, teff, tauRos, temp, rho, kappa):

    #// updated temperature structure
    newTemp = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
    #//Teff boundary between early and late-type stars:
    isCool = 6500.0

    #//Set up multi-gray opacity:
    #// lambda break-points and gray levels:
    #// No. multi-gray bins = num lambda breakpoints +1
    #//double[] grayLams = {30.0, 1.0e6};  //nm //test
    #//double[] grayLevel = {1.0};  //test
    #// ***  Late type stars, Teff < 9500 K (???):
    #//
    minLambda = 30.0  #//nm
    maxLambda = 1.0e6  #//nm
    maxNumBins = 11
    grayLams = [0.0 for i in range(maxNumBins + 1)]
    grayLevel = [0.0 for i in range(maxNumBins)]
    epsilon = [0.0 for i in range(maxNumBins)]
    #//initialize everything first:
    for iB in range(maxNumBins):
        grayLams[iB] = maxLambda
        grayLevel[iB] = 1.0
        epsilon[iB] = 0.99
        
    grayLams[maxNumBins] = maxLambda #//Set final wavelength

    grayLevelsEpsilons = grayLevEps(maxNumBins, minLambda, maxLambda, teff, isCool)
    
    #//Find actual number of multi-gray bins:
    numBins = 0 #//initialization
    for i in range(maxNumBins):
        if (grayLevelsEpsilons[0][i] < maxLambda):
            numBins+=1
            
        
    #//Add one more for final lambda:
    #//numBins++;
    #//System.out.println("numBins: " + numBins);

    """/*
    if (teff < isCool) {
        #// physically based wavelength break-points and gray levels for Sun from Rutten Fig. 8.6
        #// H I Balmer and Lyman jumps for lambda <=3640 A, H^- b-f opacity hump in visible & hole at 1.6 microns, increasing f-f beyond that
        double[] lamSet = {minLambda, 91.1, 158.5, 364.0, 794.3, 1600.0, 3.0e3, 1.0e4, 3.3e4, 1.0e5, 3.3e5, maxLambda}; //nm
        double[] levelSet = {1000.0, 100.0, 5.0, 1.0, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 1000.0};
        #//photon *thermal* destruction and creation probability (as opposed to scattering)
        #//WARNING:  THese cannot be set exactly = 1.0 or a Math.log() will blow up!!
        double[] epsilonSet = {0.50, 0.50, 0.50, 0.50, 0.50, 0.9, 0.99, 0.99, 0.99, 0.99, 0.99};
        int numBins = levelSet.length;

        for (int iB = 0; iB < numBins; iB++) {
            grayLams[iB] = lamSet[iB] * 1.0e-7;
            grayLevel[iB] = levelSet[iB];
            epsilon[iB] = epsilonSet[iB];
        }
        grayLams[numBins] = lamSet[numBins] * 1.0e-7; //Get final wavelength
    } else {
        #// *** Early type stars, Teff > 9500 K (???)
        #// It's all about H I b-f (??) What about Thomson scattering (gray)?
        #// Lyman, Balmer, Paschen, Brackett jumps
        #//What about He I features?
        double[] lamSet = {minLambda, 91.1, 364.0, 820.4, 1458.0, maxLambda};  //nm
        double[] levelSet = {100.0, 10.0, 2.0, 1.0, 1.0};  //???
        double[] epsilonSet = {0.5, 0.6, 0.7, 0.8, 0.5};
        int numBins = levelSet.length;
        for (int iB = 0; iB < numBins; iB++) {
            grayLams[iB] = lamSet[iB] * 1.0e-7;;
            grayLevel[iB] = levelSet[iB];
            epsilon[iB] = epsilonSet[iB];
        }
        grayLams[numBins] = lamSet[numBins] * 1.0e-7; //Get final wavelength
    }

    #//Find out how many bins we really have:
    #int numBins = 0;  //initialize
    #for (int iB = 0; iB < maxNumBins; iB++) {
    if (grayLams[iB] < maxLambda) {
        numBins++;
    #}
    }
    */"""
    for iB in range(numBins):
        grayLams[iB] = grayLevelsEpsilons[0][iB]
        grayLevel[iB] = grayLevelsEpsilons[1][iB]
        epsilon[iB] = grayLevelsEpsilons[2][iB];
        
    grayLams[numBins] = grayLevelsEpsilons[0][numBins] #//Get final wavelength

    #//Set overall gray-level - how emissive and absorptive the gas is overall
    #// a necessary "fudge" because our kappa values are arbitrary rather than "in situ"
    graySet = 1.0

    #//double tcDamp = 0.5; // damp the temperature corrections, Delta T, by this *multiplicative* factor
    tcDamp = 1.0   #// no damping - Lambda iteration is slow rather than oscillatory

    logE = math.log10(math.E) #// for debug output

    #//double[][] planckBol = MulGrayTCorr.planckBin(numDeps, temp, lamStart, lamStop);
    planckBol = [0.0 for i in range(numDeps)] #//just for reference - not really needed - ??   
    jayBol = [0.0 for i in range(numDeps)] #//just for reference - not really needed - ??
    dBdTBol = [0.0 for i in range(numDeps)] #//just for reference - not really needed - ??
    cool = [0.0 for i in range(numDeps)]  #// cooling term in Stromgren equation
    heat = [0.0 for i in range(numDeps)]  #// heating term in Stromgren equation
    corrDenom = [0.0 for i in range(numDeps)] #//denominator in 1st order temp correction
    #//double[] accumB = new double[numDeps]; //accumulator
    

    #//CAUTION: planckBin[2][]: Row 0 is bin-integrated B_lambda; row 1 is bin integrated dB/dT_lambda
    planckBin = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
    jayBin = [0.0 for i in range(numDeps)]
    dBdTBin = [0.0 for i in range(numDeps)]
    #//double logCool, logHeat, logCorrDenom, logCoolTherm, logCoolScat;

    #// initialize accumulators & set overell gray kappa level:
    for iTau in range(numDeps):

        planckBol[iTau] = 0.0  #//just for reference - not really needed - ??
        jayBol[iTau] = 0.0  #//just for reference - not really needed - ??
        dBdTBol[iTau] = 0.0  #//just for reference - not really needed - ??
        cool[iTau] = 0.0
        heat[iTau] = 0.0
        corrDenom[iTau] = 0.0

        kappa[1][iTau] = kappa[1][iTau] + math.log(graySet)
        kappa[0][iTau] = math.exp(kappa[1][iTau])

        

    for iB in range(numBins):
        #//System.out.println("iB: " + iB + " grayLams[iB] " + grayLams[iB]);
        planckBin = planckBinner(numDeps, temp, grayLams[iB], grayLams[iB + 1])

        #// We are lambda-operating on a wavelength integrated B_lambda for each multi-gray bin
        jayBin = jayBinner(numDeps, tauRos, temp, planckBin, grayLevel[iB])
        #//System.out.println("tauRos[1][iTau]   planckBin[0]   planckBin[1]   jayBin");
        for iTau in range(numDeps):
            #//System.out.format("%12.8f   %12.8f   %12.8f   %12.8f%n",
            #//        logE * tauRos[1][iTau], logE * Math.log(planckBin[0][iTau]), logE * Math.log(planckBin[1][iTau]), logE * Math.log(jayBin[iTau]));
            #//CAUTION: planckBin[2][]: Row 0 is bin-integrated B_lambda; row 1 is bin integrated dB/dT_lambda
            #//Net LTE volume cooling rate deltaE = Integ_lam=0^infnty(4*pi*kappa*rho*B_lam)dlam - Integ_lam=0^infnty(4*pi*kappa*rho*J_lam)dlam
            #// where Jlam = LambdaO[B_lam] - Rutten Eq. 7.32, 7.33 
            #// CAUTION: the 4pi and rho factors cancel out when diving B-J term by dB/dT term 
            planckBol[iTau] = planckBol[iTau] + planckBin[0][iTau]  #//just for reference - not really needed - ??
            #//logCool = Math.log(grayLevel[iB]) + kappa[1][iTau] + Math.log(planckBin[0][iTau])  #//no scatering
            #//cool[iTau] = cool[iTau] + Math.exp(logCool);   //no scattering
            logCoolTherm = math.log(grayLevel[iB]) + math.log(epsilon[iB]) + kappa[1][iTau] + math.log(planckBin[0][iTau])
            logCoolScat = math.log(grayLevel[iB]) + math.log((1.0 - epsilon[iB])) + kappa[1][iTau] + math.log(jayBin[iTau])
            cool[iTau] = cool[iTau] + math.exp(logCoolTherm) + math.exp(logCoolScat)
            jayBol[iTau] = jayBol[iTau] + jayBin[iTau]  #//just for reference - not really needed - ??
            logHeat = math.log(grayLevel[iB]) + kappa[1][iTau] + math.log(jayBin[iTau])
            heat[iTau] = heat[iTau] + math.exp(logHeat)
            dBdTBol[iTau] = dBdTBol[iTau] + planckBin[1][iTau]  #//just for reference - not really needed - ??
            logCorrDenom = math.log(grayLevel[iB]) + kappa[1][iTau] + math.log(planckBin[1][iTau])
            corrDenom[iTau] = corrDenom[iTau] + math.exp(logCorrDenom)
            #// if (iTau == 10){
            #//    System.out.format("iB: %02d   %12.8f   %12.8f   %12.8f   %12.8f%n", iB, logE*Math.log(planckBin[0][iTau]), logE*Math.log(cool[iTau]), logE*Math.log(heat[iTau]), logE*Math.log(corrDenom[iTau]));
            #//}
        #} // iTau loop
    #} //iB loop

    #// System.out.println("i   tauRos[1][iTau]   planckBol[0]   planckBol[1]   jayBol      cool      heat      corrDenom");
    #// for (int iTau = 0; iTau < numDeps; iTau++) {
    #//System.out.format("%02d   %12.8f   %12.8f   %12.8f   %12.8f   %12.8f   %12.8f   %12.8f%n", iTau,
    #//        logE * tauRos[1][iTau], logE * Math.log(planckBol[iTau]), logE * Math.log(dBdTBol[iTau]), logE * Math.log(jayBol[iTau]),
    #//        logE * Math.log(cool[iTau]), logE * Math.log(heat[iTau]), logE * Math.log(corrDenom[iTau]));
    #// }
    #double logRatio, ratio, deltaTemp, logDeltaTemp;
    sign = 1.0 #//initialize for positive JminusB

    #//System.out.println("tauRos[1][iTau]   deltaTemp[iTau]");
    for iTau in range(numDeps):
        #// Compute a 1st order T correction:  Compute J-B so that DeltaT < 0 if J < B:
        #// avoid direct subtraction of two large almost equal numbers, J & B:

        """/* 
        //Gray method:
   
        double JminusB
        logRatio = Math.log(planckBol[iTau]) - Math.log(jayBol[iTau]);
        ratio = Math.exp(logRatio);
        JminusB = jayBol[iTau] * (1.0 - ratio);
        if (JminusB < 0.0) {
            sign = -1.0;
        }

        #// DeltaB/DeltaT ~ dB/dT & dB/dT = (4/pi)sigma*T^3
        logDeltaTemp = Math.log(Math.abs(JminusB)) + Math.log(Math.PI) - Math.log(4.0) - Useful.logSigma() - 3.0 * temp[1][iTau];
        deltaTemp[iTau] = sign * Math.exp(logDeltaTemp) * tcDamp;
        #//System.out.format("%12.8f   %12.8f%n", tauRos[1][iTau], deltaTemp[iTau]);

        sign = 1.0; //reset sign
        */"""
        #//Multi-Gray method:
        #double deltaE;
        #//double logHeatNorm, heatNorm, logCoolNorm, deltaENorm;

        #////Normalize numbers by dividing heat and cool terms each by common denominator derivative term first:
        #//logHeatNorm = Math.log(heat[iTau]) - Math.log(corrDenom[iTau]);
        #//heatNorm = Math.exp(logHeatNorm);
        #//logCoolNorm = Math.log(cool[iTau]) - Math.log(corrDenom[iTau]);
        logRatio = math.log(cool[iTau]) - math.log(heat[iTau])
        #//logRatio = logCoolNorm - logHeatNorm

        ratio = math.exp(logRatio)
        deltaE = heat[iTau] * (1.0 - ratio)
        #//deltaENorm = heatNorm * (1.0 - ratio)
        if (deltaE < 0.0):
            sign = -1.0
            
        #//CHEAT: Try a Tau-dependent deltaE damping here - things are flaky at tdepth where t(Tau) steepens
        deltaE = deltaE * math.exp(1.0 * (tauRos[0][0] - tauRos[0][iTau]))

        #// DeltaE/DeltaT ~ dB/dT_Bol
        logDeltaTemp = math.log(math.abs(deltaE)) - math.log(corrDenom[iTau])
        deltaTemp = sign * math.exp(logDeltaTemp) * tcDamp
        #//deltaTemp = sign * deltaENorm * tcDamp;

        newTemp[0][iTau] = temp[0][iTau] + deltaTemp;
        newTemp[1][iTau] = math.log(newTemp[0][iTau]);

    #} //iTau loop

    return newTemp

#}  //end method

    
def jayBinner(numDeps, tauRos, temp, planckBin, grayLevel):

    """// method jayBolom computes bolometric angle-averaged mean intensity, J
    // This is a Lambda operation, ie. the Schwartzschild equation"""

    #// For bolometric J on a Gray Tau scale in LTE: 
    #// J(Tau) = 1/2 * Sigma_Tau=0^Infty { E_1(|t-Tau|)*Planck_Bol(Tau) }
    logE = math.log10(math.e) #// for debug output

    #double E1 #//E_1(x)

    #//Set up local optical depth scale:
        
    tauBin = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
    #double deltaTauRos
    tauBin[0][0] = tauRos[0][0] * grayLevel #// Is this a good idea??
    tauBin[1][0] = math.log(tauBin[0][0])
    for iTau in range(1, numDeps):
        deltaTauRos = tauRos[0][iTau] - tauRos[0][iTau - 1]
        #//grayLevel *is*, by definition, the ratio kappa_Bin/kappaRos that we need here!
        tauBin[0][iTau] = tauBin[0][iTau - 1] + grayLevel * deltaTauRos;
        tauBin[1][iTau] = math.log(tauBin[0][iTau]);
        

    #double logInteg, integ, integ1, integ2, logInteg1, logInteg2, meanInteg, logMeanInteg, term, logTerm;
    #double deltaTau, logDeltaTau; //accumulator
    accum = 0.0 #//accumulator

    jayBin = [0.0 for i in range(numDeps)]
    
    #// if E_1(t-Tau) evaluated at Tau=bottom of atmosphere, then just set Jay=B at that Tau - we're deep enough to be thermalized
    #// and we don't want to let lambda operation implicitly include depths below bottom of model where B=0 implicitly 
    tiny = 1.0e-14  #//tuned to around maxTauDIff at Tau_Ros ~ 3
    #double maxTauDiff;

    #//stipulate the {|t-Tau|} grid at which E_1(x)B will be evaluated - necessary to sample the 
    #// sharply peaked integrand properly
    #// ** CAUTION: minLog10TmTau and maxLog10TmTau are tau offsets from the centre of J integration, 
    #//  NOT the optical depth scale of the atmosphere!
    #//stipulate the {|t-Tau|} grid at which E_1(x)B will be evaluated - necessary to sample the 
    #// sharply peaked integrand properly
    fineFac = 3.0 #// integrate E1 on a grid fineFac x finer in logTau space
    E1Range = 36.0 #// number of master tauBin intervals within which to integrate J 
    numInteg = E1Range * fineFac
    deltaLogTauE1 = (tauBin[1][numDeps - 1] - tauBin[1][0]) / numDeps
    deltaLogTauE1 = deltaLogTauE1 / fineFac

    #double thisTau1, logThisTau1, thisTau2, logThisTau2, logE1, deltaTauE1, logThisPlanck, iFloat;

    #//Prepare 1D vectors for Interpol.interpol:
    logTauBin = [0.0 for i in range(numDeps)]
    logPlanck = [0.0 for i in range(numDeps)]
    #//System.out.println("logTauBin  logB");
    for k in range(numDeps):
        logTauBin[k] = tauBin[1][k]
        logPlanck[k] = math.log(planckBin[0][k])
        #//System.out.format("%12.8f   %12.8f%n", logE*logTauBin[k], logE*logPlanck[k]);
        

    #//Outer loop over Taus where Jay(Tau) being computed:
    #// Start from top and work down to around tau=1 - below that assume we're thermalized with J=B
    #//System.out.println("For logTauRos = " + logE*tauRos[1][40] + ": thisTau  E1xB  E1  B");
    #//System.out.println("tauRos[1][iTau]   Math.log(planckBin[iTau])   jayBin[1][iTau]");
    for iTau in range(numDeps):
        #//System.out.println("jayBinner: iTau: " + iTau + " tauRos[0] " + tauRos[0][iTau] + " tauRos[1] " + logE * tauRos[1][iTau]);
        jayBin[iTau] = planckBin[0][iTau] #//default initialization J_bin = B_bin

        if (tauRos[0][iTau] < 66.67):
            #//System.out.println("tauRos[0] < limit condition passed");
            #// initial test - don't let E_1(x) factor in integrand run off bottom of atmosphere
            #// - we have no emissivity down there and J will drop below B again, like at surface!
            maxTauDiff = math.abs(tauBin[0][numDeps - 1] - tauBin[0][iTau])
            #//System.out.println("tauBin[0][numDeps - 1]: " + tauBin[0][numDeps - 1] + " tauBin[0][iTau] " + tauBin[0][iTau] + " maxTauDiff " + maxTauDiff);
            #//System.out.println("maxTauDiff= " + maxTauDiff + " expOne(maxTauDiff)= " + expOne(maxTauDiff));
            if (expOne(maxTauDiff) < tiny):

                #//System.out.println("maxTauDiff < tiny condition passed, expOne(maxTauDiff): " + expOne(maxTauDiff));
                #// We're above thermalization depth: J may not = B:
                #//Inner loop over depths contributing to each Jay(iTau):
                #// work outward from t=Tau (ie. i=iTau) piece-wise  
                accum = 0.0;
                #// conribution from depths above Tau:
                #//initial integrand:
                #// start at i=1 instead of i=0 - cuts out troublesome central cusp of E_1(x) - but now we underestimate J!
                logThisTau1 = tauBin[1][iTau] - deltaLogTauE1
                thisTau1 = math.exp(logThisTau1)
                deltaTauE1 = tauBin[0][iTau] - thisTau1
                E1 = expOne(deltaTauE1)
                logE1 = math.log(E1)
                logThisPlanck = ToolBox.interpol(logTauBin, logPlanck, logThisTau1)
                logInteg1 = logE1 + logThisPlanck
                integ1 = Math.exp(logInteg1);

                for i in range(2, numInteg-1):

                    iFloat = float(i)
                    #// Evaluate E_1(x) and log(E_1(x)) one and for all here

                    #//System.out.format("%02d %12.8f %12.8f%n", j, tmTau[j], E1);
                    #// LTE bolometric source function is Bolometric Planck function
                    #// Extended trapezoidal rule for non-uniform abscissae - this is an exponential integrand!             
                    #// We cannot evaluate E_1(x) at x=0 - singular:
                    logThisTau2 = tauBin[1][iTau] - iFloat * deltaLogTauE1
                    thisTau2 = math.exp(logThisTau2)

                    #//if (i == numInteg - 2) {
                    #//    System.out.println("i " + i + " logThisTau1 " + logE * logThisTau1 + " logThisTau2 " + logE * logThisTau2);
                    #//}
                    #// Make sure we're still in the atmosphere!
                    if (logThisTau2 > tauBin[1][0]):
                        #//if (i == numInteg - 2) {
                        #//    System.out.println("thisTau2 > tauBin[0][0] condition passed");
                        #//}
                        #//if (iTau == 37) {
                        #//    System.out.println("i " + i + " logThisTau1 " + logE * logThisTau1 + " logThisTau2 " + logE * logThisTau2);
                        #//}

                        deltaTauE1 = tauBin[0][iTau] - thisTau2
                        E1 = expOne(deltaTauE1)
                        logE1 = math.log(E1)
                        #// interpolate log(B(log(Tau)) to the integration abscissa
                        logThisPlanck = ToolBox.interpol(logTauBin, logPlanck, logThisTau2)
                        logInteg2 = logE1 + logThisPlanck
                        integ2 = math.exp(logInteg2)

                        logDeltaTau = math.log(thisTau1 - thisTau2) #// logDeltaTau *NOT* the same as deltaLogTau!!

                        meanInteg = 0.5 * (integ1 + integ2) #//Trapezoid rule
                        logMeanInteg = math.log(meanInteg)
                        #//if (iTau == 40) {
                        #//    System.out.format("%15.8f    %15.8f    %15.8f   %15.8f%n", logE*Math.log(thisTau1), logE*logMeanInteg, logE*logE1, logE*logThisPlanck);
                        #//}

                        logTerm = logMeanInteg + logDeltaTau
                        term = math.exp(logTerm)
                        accum = accum + term

                        integ1 = integ2
                        thisTau1 = thisTau2
                        #//if (iTau == 41){
                        #//    System.out.println("term " + term + " accum " + accum);
                        #//}
                    #} // thisTau > 0
                #} // i ("t") loop, above iTau 

                jayBin[iTau] = 0.5 * accum  #//store what we have.
                #//test jayBin[iTau] = 0.5 * planckBin[0][iTau]; // fake upper half with isotropic result
                #//test jayBin[iTau] = jayBin[iTau] + 0.5 * planckBin[0][iTau]; // test upper atmosphere part of J integration by fixing lower part with isotropic result

                #// conribution from depths below Tau:
                #// include iTau itself so we don't miss the area under the central peak of E_1(x) - the expOne function
                #// will protect itself from the x=0 singularity using variable 'tiny'
                accum = 0.0
                #//initial integrand:
                #// start at i=1 instead of i=0 - cuts out troublesome central cusp of E_1(x) - but now we underestimate J!
                logThisTau1 = tauBin[1][iTau] + deltaLogTauE1
                thisTau1 = math.exp(logThisTau1)
                deltaTauE1 = thisTau1 - tauBin[0][iTau]
                E1 = expOne(deltaTauE1)
                logE1 = math.log(E1)
                logThisPlanck = ToolBox.interpol(logTauBin, logPlanck, logThisTau1)
                logInteg1 = logE1 + logThisPlanck
                integ1 = math.exp(logInteg1)

                for i in range(2, numInteg - 1):

                    iFloat = float(i)

                    logThisTau2 = tauBin[1][iTau] + iFloat * deltaLogTauE1
                    thisTau2 = math.exp(logThisTau2)
                    #// We cannot evaluate E_1(x) at x=0 - singular:
                    #// Extended trapezoidal rule for non-uniform abscissae - the is an exponential integrand! 

                    #// make sure we're still in the atmosphere!
                    if (logThisTau2 < tauBin[1][numDeps - 1]):

                        deltaTauE1 = thisTau2 - tauBin[0][iTau]
                        E1 = expOne(deltaTauE1)
                        logE1 = math.log(E1)

                        logThisPlanck = ToolBox.interpol(logTauBin, logPlanck, logThisTau2)
                        logInteg2 = logE1 + logThisPlanck
                        integ2 = math.exp(logInteg2)

                        logDeltaTau = math.log(thisTau2 - thisTau1) #// logDeltaTau *NOT* the same as deltaLogTau!!

                        meanInteg = 0.5 * (integ1 + integ2) #//Trapezoid rule
                        logMeanInteg = math.log(meanInteg)
                        #//if (iTau == 40) {
                        #//    System.out.format("%15.8f    %15.8f    %15.8f    %15.8f%n", logE*Math.log(thisTau1), logE*logMeanInteg, logE*logE1, logE*logThisPlanck);
                        #//}

                        #// LTE bolometric source function is Bolometric Plnack function
                        logTerm = logMeanInteg + logDeltaTau
                        term = math.exp(logTerm)
                        accum = accum + term

                        integ1 = integ2
                        thisTau1 = thisTau2

                    #}// if thisTau < tauBin[0][numDeps-1]
                #} #// i ("t") loop, below iTau

                jayBin[iTau] = jayBin[iTau] + 0.5 * accum

            #} //if branch for E_1(x) safely dwindling away before reaching bottom of atmosphere
        #} #// if branch for above thermalization depth of Tau=10? 

        #//System.out.format("%12.8f   %12.8f  %12.8f%n",
        #//       logE * tauRos[1][iTau], Math.log10(planckBin[iTau]), Math.log10(jayBin[iTau]));
    #} //iTau loop

    return jayBin

#}   //end method

    
def planckBinner(numDeps, temp, lamStart, lamStop):
    """// Compute linear wave-bin-specific lambda-integrated Planck fn AND it's T derivative at all depths:
    // Row 0: B_bin(tau);   Row 1: dB/dT_bin(tau);"""

    planckBin = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]

    logE = math.log10(math.E) #// for debug output

    #//MultiGray-ready:
    #// Parameters of overall lambda grid (nm):
    #// Planck.planck() will convert nm to cm - not any more!
    #//double log10LamStart = 1.5 * 1.0e-7;  //must be < first Gray lambda break point
    #//double log10LamStop = 5.0 * 1.0e-7;   //must be > last Gray lambda break point 
    log10LamStart = math.log10(lamStart)
    log10LamStop = math.log10(lamStop)
    deltaLog10Lam = 0.1

    #int numLamAll;
    numLamAll = int((log10LamStop - log10LamStart) / deltaLog10Lam)
    #//System.out.println("lamStart " + lamStart + " log10LamStart " + log10LamStart + " lamStop " + lamStop + " log10LamStop " + log10LamStop + " numLamAll " + numLamAll);
    lambda2 = [0.0 for i in range(numLamAll)]

    #//Generate lambda grid separately to avoid duplicate lambda generation
    #double iFloat, thisLogLam;
    #//System.out.println("lambdas");
    for i in range(numLamAll):

        iFloat = float(i)
        thisLogLam = log10LamStart + iFloat * deltaLog10Lam
        lambda2[i] = math.pow(10.0, thisLogLam)
        #//System.out.format("%02d   %12.8f%n", i, lambda[i]);

        

        #double thisLam1, thisLam2, deltaLam, planck1, planck2, logPlanck1, logPlanck2;
        #double term, integ, accum;
        #double dBdT1, dBdT2, logdBdT1, logdBdT2, accum2;

        #//trapezoid rule integration
        #//System.out.println("Trapezoid: ");
    for iTau in range(numDeps):
        #//reset accumulators for new depth
        accum = 0.0
        accum2 = 0.0

        #//initial integrands:
        logPlanck1 = Planck.planck(temp[0][iTau], lambda2[0])
        planck1 = math.exp(logPlanck1)
        logdBdT1 = Planck.dBdT(temp[0][iTau], lambda2[0])
        dBdT1 = math.exp(logdBdT1)
        for i in range(1, numLamAll - 1):

            deltaLam = lambda2[i + 1] - lambda2[i]
            #//deltaLam = deltaLam * 1.0e-7;  //nm to cm
            
            #//Planck.planck returns log(B_lambda)
            logPlanck2 = Planck.planck(temp[0][iTau], lambda2[i])

            planck2 = math.exp(logPlanck2)

            #//if (i == 20) {
            #//    System.out.println("lambda " + thisLam1 + " temp[0][iTau] " + temp[0][iTau] + " logPlanck1 " + logE*logPlanck1);
            #//}
            #//trapezoid rule integration
            integ = 0.5 * (planck1 + planck2) * deltaLam
            accum = accum + integ

            planck1 = planck2

            #//Now do the same for dB/dT:
            #//Planck.dBdT returns log(dB/dT_lambda)
            logdBdT2 = Planck.dBdT(temp[0][iTau], lambda2[i])

            dBdT2 = math.exp(logdBdT2)

            #//trapezoid rule integration
            integ = 0.5 * (dBdT1 + dBdT2) * deltaLam
            accum2 = accum2 + integ

            dBdT1 = dBdT2

        #} // lambda i loop
        planckBin[0][iTau] = accum
        planckBin[1][iTau] = accum2
        #//System.out.format("%02d   %12.8f%n", iTau, planckBin[iTau]);

    #} //iTau loop

    #//// Gray only:
    #////if (lamStart == 1000.0) {  //Could be for any gray wavelength
    #//double[][] planckBol = new double[2][numDeps];
    #//double[][] dBdTBol = new double[2][numDeps];
    #//System.out.println("Stefan-Boltzmann:  tauRos[1]  B_Bol   dBdT_Bol");
    #//for (int i = 0; i < numDeps; i++) {
    #//    planckBol[1][i] = Useful.logSigma() + 4.0 * temp[1][i] - Math.log(Math.PI);
    #//    planckBol[0][i] = Math.exp(planckBol[1][i]);
    #//    dBdTBol[1][i] = Math.log(4.0) + Useful.logSigma() + 3.0 * temp[1][i] - Math.log(Math.PI);
    #//    dBdTBol[0][i] = Math.exp(dBdTBol[1][i]);
    #//    System.out.format("%02d   %12.8f   %12.8f%n", i, logE * planckBol[1][i], logE * dBdTBol[1][i]);
    #//}
    #//}
    return planckBin
#}   // end method

def grayLevEps(maxNumBins, minLambda, maxLambda, teff, isCool):

    #//double minLambda = 30.0;  //nm
    #//double maxLambda = 1.0e6;  //nm
    #//int maxNumBins = 11;
        
    grayLevelsEpsilons = [ [ 0.0 for i in range(3) ] for j in range(maxNumBins + 1) ]
    #// The returned structure:
    #//Row 0 is wavelength breakpoints
    #//Row 1 is relative opacity gray levels
    #//Row 2 is absolute thermal photon creation fractions, epsilon

    #//initialize everything first:
    for iB in range(maxNumBins):
        grayLevelsEpsilons[0][iB] = maxLambda
        grayLevelsEpsilons[1][iB] = 1.0
        grayLevelsEpsilons[2][iB] = 0.99
        
    grayLevelsEpsilons[0][maxNumBins] = maxLambda #//Set final wavelength

    if (teff < isCool):
        #// physically based wavelength break-points and gray levels for Sun from Rutten Fig. 8.6
        #// H I Balmer, Lyman, and Paschen jumps for lambda <=3640 A, H^- b-f opacity hump in visible & hole at 1.6 microns, increasing f-f beyond that
        lamSet = [minLambda, 91.1, 158.5, 364.0, 820.4, 1600.0, 3.0e3, 1.0e4, 3.3e4, 1.0e5, 3.3e5, maxLambda] #//nm
        #//double[] levelSet =       {1000.0,100.0, 5.0,   0.5,   0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 1000.0};
        levelSet = [1000.0, 100.0, 5.0, 1.0, 0.5, 0.1, 3.0, 10.0, 30.0, 100.0, 1000.0]
        #//photon *thermal* destruction and creation probability (as opposed to scattering)
        #//WARNING:  THese cannot be set exactly = 1.0 or a Math.log() will blow up!!
        #//double[] epsilonSet =      {0.50, 0.50,  0.50,  0.50,  0.50, 0.9, 0.99, 0.99, 0.99, 0.99, 0.99};
        epsilonSet = [0.50, 0.50, 0.90, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]
        numBins = len(levelSet)

        for iB in range(numBins):
            grayLevelsEpsilons[0][iB] = lamSet[iB] * nm2cm
            grayLevelsEpsilons[1][iB] = levelSet[iB]
            grayLevelsEpsilons[2][iB] = epsilonSet[iB];
            
        grayLevelsEpsilons[0][numBins] = lamSet[numBins] * 1.0e-7; //Get final wavelength
    else: 
        #// *** Early type stars, Teff > 9500 K (???)
        #// It's all about H I b-f (??) What about Thomson scattering (gray)?
        #// Lyman, Balmer, Paschen, Brackett jumps
        #//What about He I features?
        lamSet = [minLambda, 91.1, 364.0, 820.4, 1458.0, maxLambda]  #//nm
        levelSet = [100.0, 10.0, 2.0, 1.0, 1.0]  #//???
        epsilonSet = [0.5, 0.6, 0.7, 0.8, 0.5]
        numBins = len(levelSet)
        for iB in range(numBins):
            grayLevelsEpsilons[0][iB] = lamSet[iB] * nm2cm  #//cm
            grayLevelsEpsilons[1][iB] = levelSet[iB]
            grayLevelsEpsilons[2][iB] = epsilonSet[iB];
        #}
        grayLevelsEpsilons[0][numBins] = lamSet[numBins] * 1.0e-7; //Get final wavelength
    #}

    return grayLevelsEpsilons

#}   //end method

    
def expOne(x): 
    
    """// Approximate first exponential integral function E_1(x) = -Ei(-x)"""

    #// From http://en.wikipedia.org/wiki/Exponential_integral 
    #// Series expansion for first exponential integral function, E_1(x) = -Ei(-x)
    #// Ee_one(x) = -gamma - ln(abs(x)) - Sigma_k=1^infnty{(-x)^k)/(k*k!)}
    #// where: gamma =  Eulerâ€“Mascheroni constant = 0.577215665...
    #double E1;

    x = math.abs(x) #// x must be positive
    #// E1(x) undefined at x=0 - singular:
    #//double tiny = 1.25;  //tuned to give J ~ 0.5B @ tau=0
    tiny = 1.0e-6
    if (x < tiny): 
        x = tiny
        

    #// Caution: even at 11th order acuracy (k=11), approximation starts to diverge for x . 3.0:
    if (x > 3.0):

        E1 = math.exp(-1.0 * x) / x #// large x approx

    else:
        gamma = 0.577215665 #//Eulerâ€“Mascheroni constant
        kTerm = 0.0
        order = 11 #//order of approximation
        #double kFloat;
        accum = 0.0  #//accumulator
        kFac = 1.0 #// initialize k! (k factorial)

        for k in range(1, order+1):
            kFloat = float(k)
            kFac = kFac * kFloat
            accum = accum + Math.pow((-1.0 * x), kFloat) / (k * kFac);
            #//System.out.println("k: " + k + " kFac: " + kFac);
            #//System.out.println("k: " + k + " Math.pow(x, kFloat): " + Math.pow(x, kFloat));
            
        kTerm = accum

        E1 = -1.0 * gamma - Math.log(Math.abs(x)) - kTerm
    #}

    #//System.out.println("x: " + x + " exp1(x): " + E1);
    return E1

#}
