# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:12:02 2017

@author: ishort
"""

import math
import Planck
import Useful

def kappas2(numDeps, pe, zScale, temp, rho, numLams, lambdas, logAHe, \
            logNH1, logNH2, logNHe1, logNHe2, Ne, teff, logKapFudge):

    
    """/* Compute opacities properly from scratch with real physical cross-sections
 */ //  *** CAUTION:
//
//  This return's "kappa" as defined by Gray 3rd Ed. - cm^2 per *relelvant particle* where the "releveant particle"
//  depends on *which* kappa """
#//
#//  *** CAUTION:
#//
#//  This return's "kappa" as defined by Gray 3rd Ed. - cm^2 per *relelvant particle* where the "releveant particle"
#//  depends on *which* kappa

    log10E = math.log10(math.e) #//needed for g_ff
    logLog10E = math.log(log10E)
    logE10 = math.log(10.0)
    logNH = [0.0 for i in range(numDeps)] #//Total H particle number density cm^-3
    #double logPH1, logPH2, logPHe1, logPHe2;
    for i in range(numDeps):
        logNH[i] = math.exp(logNH1[i]) + math.exp(logNH2[i])
        logNH[i] = math.log(logNH[i])

        #//System.out.println("i " + i + " logNH1 " + log10E*logNH1[i] + " logNH2 " + log10E*logNH2[i] 
    #//+ " logNHe1 " + log10E*logNHe1[i] + " logNHe2 " + log10E*logNHe2[i] + " logPe " + log10E*pe[1][i]);
     #//   logPH1 = logNH1[i] + temp[1][i] + Useful.logK();
      #//  logPH2 = logNH2[i] + temp[1][i] + Useful.logK();
       #// logPHe1 = logNHe1[i] + temp[1][i] + Useful.logK();
       #// logPHe2 = logNHe2[i] + temp[1][i] + Useful.logK();
        #//System.out.println("i " + i + " logPH1 " + log10E*logPH1 + " logPH2 " + log10E*logPH2 
    #//+ " logPHe1 " + log10E*logPHe1 + " logPHe2 " + log10E*logPHe2 + " logPe " + log10E*pe[1][i]);
     

    #double[][] logKappa = new double[numLams][numDeps];
    logKappa = [ [0.0 for i in range(numDeps)] for j in range(numLams) ]
    #double kappa; //helper
    #double stimEm; //temperature- and wavelength-dependent stimulated emission correction  
    #double stimHelp, logStimEm;
 
    #double ii; //useful for converting integer loop counter, i, to float
#//
#//
#//Input data and variable declarations:
#//
#//
#// H I b-f & f-f
    chiIH = 13.598433  #//eV
    Rydberg = 1.0968e-2  #// "R" in nm^-1
    #//Generate threshold wavelengths and b-f Gaunt (g_bf) helper factors up to n=10:
    #double n; //principle quantum number of Bohr atom E-level
    numHlevs = 10
     #double logChiHlev;
    invThresh = [0.0 for i in range(numHlevs)] #//also serves as g_bf helper factor
    threshLambs = [0.0 for i in range(numHlevs)]
    chiHlev = [0.0 for i in range(numHlevs)]
    for i in range(numHlevs):
        n = 1.0 + float(i)
        invThresh[i] = Rydberg / n / n #//nm^-1; also serves as g_bf helper factor 
        threshLambs[i] = 1.0 / invThresh[i] #//nm
        logChiHlev = Useful.logH() + Useful.logC() + math.log(invThresh[i]) + 7.0*logE10 #// ergs
        chiHlev[i] = math.exp(logChiHlev - Useful.logEv()) #//eV
        chiHlev[i] = chiIH - chiHlev[i]
#// System.out.println("i " + i + " n " + n + " invThresh " + invThresh[i] + " threshLambs[i] " + threshLambs[i] + " chiHlev " + chiHlev[i]);

    logGauntPrefac = math.log(0.3456) - 0.333333*math.log(Rydberg)

    #// ****  Caution: this will require lamba in A!:
    a0 = 1.0449e-26  #//if lambda in A 
    logA0 = math.log(a0)
#// Boltzmann const "k" in eV/K - needed for "theta"
    logKeV = Useful.logK() - Useful.logEv() 

    #//g_bf Gaunt factor - depends on lower E-level, n:
    loggbf = [0.0 for i in range(numHlevs)]
    #//initialize quantities that depend on lowest E-level contributing to opacity at current wavelength:
    for iThresh in range(numHlevs):
        loggbf[iThresh] = 0.0
     
     #double logGauntHelp, gauntHelp; 
     #double gbf, gbfHelp, loggbfHelp;
     #double gff, gffHelp, loggffHelp, logffHelp, loggff;
     #double help, logHelp3;
     #double chiLambda, logChiLambda;
     #double bfTerm, logbfTerm, bfSum, logKapH1bf, logKapH1ff;
 
#//initial defaults:
    gbf = 1.0
    gff = 1.0
    loggff = 0.0
 
    logChiFac = math.log(1.2398e3) #// eV per lambda, for lambda in nm

#// Needed for kappa_ff: 
    #double ffBracket; 
    logffHelp = logLog10E - math.log(chiIH) - math.log(2.0)
    #//logHelp = logffHelp - math.log(2.0)

#//
#//Hminus:
#//
#// H^- b-f
#//This is for the sixth order polynomial fit to the cross-section's wavelength dependence
    numHmTerms = 7
    logAHm = [0.0 for i in range(numHmTerms)]
    signAHm = [0.0 for i in range(numHmTerms)]     
 
    aHmbf = 4.158e-10
    #//double logAHmbf = Math.log(aHmbf);
    #//Is the factor of 10^-18cm^2 from the polynomial fit to alpha_Hmbf missing in Eq. 8.12 on p. 156 of Gray 3rd Ed??
    logAHmbf = math.log(aHmbf) - 18.0*logE10
    #double alphaHmbf, logAlphaHmbf, logTermHmbf, logKapHmbf; 

    #//Computing each polynomial term logarithmically
    logAHm[0] = math.log(1.99654)
    signAHm[0] = 1.0
    logAHm[1] = math.log(1.18267e-5)
    signAHm[1] = -1.0
    logAHm[2] = math.log(2.64243e-6)
    signAHm[2] = 1.0
    logAHm[3] = math.log(4.40524e-10)
    signAHm[3] = -1.0
    logAHm[4] = math.log(3.23992e-14)
    signAHm[4] = 1.0
    logAHm[5] = math.log(1.39568e-18)
    signAHm[5] = -1.0
    logAHm[6] = math.log(2.78701e-23)
    signAHm[6] = 1.0
    alphaHmbf = math.exp(logAHm[0]) #//initialize accumulator

#// H^- f-f:

    logAHmff = -26.0*logE10
    numHmffTerms = 5
    #double fPoly, logKapHmff, logLambdaAFac; 
    fHmTerms = [ [ 0.0 for i in range(numHmffTerms) ] for j in range(3) ]
    fHm = [0.0 for i in range(3)]
    fHmTerms[0][0] = -2.2763
    fHmTerms[0][1] = -1.6850
    fHmTerms[0][2] = 0.76661
    fHmTerms[0][3] = -0.053346
    fHmTerms[0][4] = 0.0
    fHmTerms[1][0] = 15.2827
    fHmTerms[1][1] = -9.2846
    fHmTerms[1][2] = 1.99381
    fHmTerms[1][3] = -0.142631
    fHmTerms[1][4] = 0.0
    fHmTerms[2][0] = -197.789
    fHmTerms[2][1] = 190.266
    fHmTerms[2][2] = -67.9775
    fHmTerms[2][3] = 10.6913
    fHmTerms[2][4] = -0.625151

#//
#//H_2^+ molecular opacity - cool stars
#// scasles with proton density (H^+)
#//This is for the third order polynomial fit to the "sigma_l(lambda)" and "U_l(lambda)"
#//terms in the cross-section
    numH2pTerms = 4
    sigmaH2pTerm = [0.0 for i in range(numH2pTerms)]
    UH2pTerm = [0.0 for i in range(numH2pTerms)]
    #double logSigmaH2p, sigmaH2p, UH2p, logKapH2p;  
    aH2p = 2.51e-42
    logAH2p = math.log(aH2p)
    sigmaH2pTerm[0] = -1040.54
    sigmaH2pTerm[1] = 1345.71
    sigmaH2pTerm[2] = -547.628
    sigmaH2pTerm[3] = 71.9684
    #//UH2pTerm[0] = 54.0532
    #//UH2pTerm[1] = -32.713
    #//UH2pTerm[2] = 6.6699
    #//UH2pTerm[3] = -0.4574
    #//Reverse signs on U_1 polynomial expansion co-efficients - Dave Gray private communcation 
    #//based on Bates (1952)
    UH2pTerm[0] = -54.0532
    UH2pTerm[1] = 32.713
    UH2pTerm[2] = -6.6699
    UH2pTerm[3] = 0.4574
 

#// He I b-f & ff: 
    #double totalH1Kap, logTotalH1Kap, helpHe, logKapHe;

#//
#//He^- f-f
  
    AHe = math.exp(logAHe) 
    #double logKapHemff, nHe, logNHe, thisTerm, thisLogTerm, alphaHemff, log10AlphaHemff;

#// Gray does not have this pre-factor, but PHOENIX seems to and without it
#// the He opacity is about 10^26 too high!:
    logAHemff = -26.0*logE10

    numHemffTerms = 5
    logC0HemffTerm = [0.0 for i in range(numHemffTerms)]
    logC1HemffTerm = [0.0 for i in range(numHemffTerms)]
    logC2HemffTerm = [0.0 for i in range(numHemffTerms)]
    logC3HemffTerm = [0.0 for i in range(numHemffTerms)]
    signC0HemffTerm = [0.0 for i in range(numHemffTerms)]
    signC1HemffTerm = [0.0 for i in range(numHemffTerms)]
    signC2HemffTerm = [0.0 for i in range(numHemffTerms)]
    signC3HemffTerm = [0.0 for i in range(numHemffTerms)]

#//we'll be evaluating the polynominal in theta logarithmically by adding logarithmic terms - 
    logC0HemffTerm[0] = math.log(9.66736) 
    signC0HemffTerm[0] = 1.0
    logC0HemffTerm[1] = math.log(71.76242) 
    signC0HemffTerm[1] = -1.0
    logC0HemffTerm[2] = math.log(105.29576) 
    signC0HemffTerm[2] = 1.0
    logC0HemffTerm[3] = math.log(56.49259) 
    signC0HemffTerm[3] = -1.0
    logC0HemffTerm[4] = math.log(10.69206) 
    signC0HemffTerm[4] = 1.0
    logC1HemffTerm[0] = math.log(10.50614) 
    signC1HemffTerm[0] = -1.0
    logC1HemffTerm[1] = math.log(48.28802) 
    signC1HemffTerm[1] = 1.0
    logC1HemffTerm[2] = math.log(70.43363) 
    signC1HemffTerm[2] = -1.0
    logC1HemffTerm[3] = math.log(37.80099) 
    signC1HemffTerm[3] = 1.0
    logC1HemffTerm[4] = math.log(7.15445)
    signC1HemffTerm[4] = -1.0
    logC2HemffTerm[0] = math.log(2.74020)
    signC2HemffTerm[0] = 1.0
    logC2HemffTerm[1] = math.log(10.62144) 
    signC2HemffTerm[1] = -1.0
    logC2HemffTerm[2] = math.log(15.50518) 
    signC2HemffTerm[2] = 1.0
    logC2HemffTerm[3] = math.log(8.33845)
    signC2HemffTerm[3] = -1.0
    logC2HemffTerm[4] = math.log(1.57960)
    signC2HemffTerm[4] = 1.0
    logC3HemffTerm[0] = math.log(0.19923)
    signC3HemffTerm[0] = -1.0
    logC3HemffTerm[1] = math.log(0.77485)
    signC3HemffTerm[1] = 1.0
    logC3HemffTerm[2] = math.log(1.13200)
    signC3HemffTerm[2] = -1.0
    logC3HemffTerm[3] = math.log(0.60994)
    signC3HemffTerm[3] = 1.0
    logC3HemffTerm[4] = math.log(0.11564)
    signC3HemffTerm[4] = -1.0
#    //initialize accumulators:
    cHemff = [0.0 for i in range(4)]
    cHemff[0] = signC0HemffTerm[0] * math.exp(logC0HemffTerm[0]);   
    cHemff[1] = signC1HemffTerm[0] * math.exp(logC1HemffTerm[0]);   
    cHemff[2] = signC2HemffTerm[0] * math.exp(logC2HemffTerm[0]);   
    cHemff[3] = signC3HemffTerm[0] * math.exp(logC3HemffTerm[0]);   
#//
#//Should the polynomial expansion for the Cs by in 10g10Theta??  No! Doesn't help:
    #//double[] C0HemffTerm = new double[numHemffTerms];
    #//double[] C1HemffTerm = new double[numHemffTerms];
    #//double[] C2HemffTerm = new double[numHemffTerms];
    #//double[] C3HemffTerm = new double[numHemffTerms];
#//
    #//C0HemffTerm[0] = 9.66736; 
    #//C0HemffTerm[1] = -71.76242; 
    #//C0HemffTerm[2] = 105.29576; 
    #//C0HemffTerm[3] = -56.49259; 
    #//C0HemffTerm[4] = 10.69206; 
    #//C1HemffTerm[0] = -10.50614; 
    #//C1HemffTerm[1] = 48.28802; 
    #//C1HemffTerm[2] = -70.43363; 
    #//C1HemffTerm[3] = 37.80099; 
    #//C1HemffTerm[4] = -7.15445;
    #//C2HemffTerm[0] = 2.74020; 
    #//C2HemffTerm[1] = -10.62144; 
    #//C2HemffTerm[2] = 15.50518; 
    #//C2HemffTerm[3] = -8.33845; 
    #//C2HemffTerm[4] = 1.57960;
    #//C3HemffTerm[0] = -0.19923; 
    #//C3HemffTerm[1] = 0.77485; 
    #//C3HemffTerm[2] = -1.13200; 
    #//C3HemffTerm[3] = 0.60994; 
    #//C3HemffTerm[4] = -0.11564;
    #//initialize accumulators:
    #// double[] cHemff = new double[4];
    #// cHemff[0] = C0HemffTerm[0];   
    #// cHemff[1] = C1HemffTerm[0];   
    #// cHemff[2] = C2HemffTerm[0];   
    #// cHemff[3] = C3HemffTerm[0];   

#//
#// electron (e^-1) scattering (Thomson scattering)

    #double kapE, logKapE;
    alphaE = 0.6648e-24 #//cm^2/e^-1
    logAlphaE = math.log(0.6648e-24)
  

#//Universal:
#//
#     double theta, logTheta, log10Theta, log10ThetaFac;
#     double logLambda, lambdaA, logLambdaA, log10LambdaA, lambdanm, logLambdanm;
#//Okay - here we go:
#//Make the wavelength loop the outer loop - lots of depth-independnet lambda-dependent quantities:
#//
#//
#   //System.out.println("Kappas called...");
#//
#//  **** START WAVELENGTH LOOP iLam
#//
#//
#//
    for iLam in range(numLams):
 #//
 #//Re-initialize all accumulators to be on safe side:
        kappa = 0.0
        logKapH1bf = -99.0 
        logKapH1ff = -99.0
        logKapHmbf = -99.0 
        logKapHmff = -99.0
        logKapH2p = -99.0
        logKapHe = -99.0
        logKapHemff = -99.0
        logKapE = -99.0
#//
#//*** CAUTION: lambda MUST be in nm here for consistency with Rydbeg 
        logLambda = math.log(lambdas[iLam])  #//log cm
        lambdanm = 1.0e7 * lambdas[iLam]
        logLambdanm = math.log(lambdanm)
        lambdaA = 1.0e8 * lambdas[iLam] #//Angstroms
        logLambdaA = math.log(lambdaA)
        log10LambdaA = log10E * logLambdaA

        logChiLambda = logChiFac - logLambdanm
        chiLambda = math.exp(logChiLambda)   #//eV

#// Needed for both g_bf AND g_ff: 
        logGauntHelp = logGauntPrefac - 0.333333*logLambdanm #//lambda in nm here
        gauntHelp = math.exp(logGauntHelp)

  #//            if (iLam == 142){
   #// System.out.println("lambdaA " + lambdaA);
   #//         }

#//HI b-f depth independent factors:
#//Start at largest threshold wavelength and break out of loop when next threshold lambda is less than current lambda:
        #for (iThresh = numHlevs-1; iThresh >= 0; iThresh--){
        for iThresh in range(0, numHlevs-1, -1):
            if (threshLambs[iThresh] < lambdanm):
                break
           
            if (lambdanm <= threshLambs[iThresh]):
           #//this E-level contributes
                loggbfHelp = logLambdanm + math.log(invThresh[iThresh]) # //lambda in nm here; invThresh here as R/n^2
                gbfHelp = math.exp(loggbfHelp)
                gbf = 1.0 - (gauntHelp * (gbfHelp - 0.5))
#//              if (iLam == 1){}
#//    System.out.println("iThresh " + iThresh + " threshLambs " + threshLambs[iThresh] +  " gbf " + gbf);
#//              }
                loggbf[iThresh] = math.log(gbf)
           
        #//end iThresh loop 

#//HI f-f depth independent factors:
#        //logChi = logLog10E + logLambdanm - logChiFac; //lambda in nm here
#        //chi = Math.exp(logChi);
        loggffHelp = logLog10E - logChiLambda

#//
#//
#//
#//  ******  Start depth loop iTau ******
#//
#//
#//
#//
        for iTau in range(numDeps):
#//
# //Re-initialize all accumulators to be on safe side:
            kappa = 0.0
            logKapH1bf = -99.0 
            logKapH1ff = -99.0
            logKapHmbf = -99.0 
            logKapHmff = -99.0
            logKapH2p = -99.0
            logKapHe = -99.0
            logKapHemff = -99.0
            logKapE = -99.0
#//
#//
#//if (iTau == 36 && iLam == 142){
#//    System.out.println("lambdanm[142] " + lambdanm + " temp[0][iTau=36] " + temp[0][iTau=36]);
#// }
#//This is "theta" ~ 5040/T:
            logTheta = logLog10E - logKeV - temp[1][iTau]
            log10Theta = log10E * logTheta
            theta = math.exp(logTheta)
            #//System.out.println("theta " + theta + " logTheta " + logTheta);

#// temperature- and wavelength-dependent stimulated emission coefficient:
            stimHelp = -1.0 * theta * chiLambda * logE10
            stimEm = 1.0 - math.exp(stimHelp)
            logStimEm = math.log(stimEm)
# //          if (iTau == 36 && iLam == 142){
# //   System.out.println("stimEm " + stimEm);
# //}


            ffBracket = math.exp(loggffHelp - logTheta) + 0.5 
            gff = 1.0 + (gauntHelp*ffBracket)


#//if (iTau == 36 && iLam == 1){
#//    System.out.println("gff " + gff);
#// }
            loggff = math.log(gff)

#//H I b-f:
#//Start at largest threshold wavelength and break out of loop when next threshold lambda is less than current lambda:
            bfSum = 0.0 #//initialize accumulator
            logHelp3 = logA0 + 3.0*logLambdaA #//lambda in A here
            #for (int iThresh = numHlevs-1; iThresh >= 0; iThresh--){
            for iThresh in range(0, numHlevs-1, -1):
                if (threshLambs[iThresh] < lambdanm):
                    break
              
            n = 1.0 + float(iThresh)
            if (lambdanm <= threshLambs[iThresh]):
                #//this E-level contributes
                logbfTerm = loggbf[iThresh] - 3.0*math.log(n) 
                logbfTerm = logbfTerm - (theta*chiHlev[iThresh])*logE10 
                bfSum = bfSum + math.exp(logbfTerm)
#//if (iTau == 36 && iLam == 142){
#  //System.out.println("lambdanm " + lambdanm + " iThresh " + iThresh + " threshLambs[iThresh] " + threshLambs[iThresh]);
#  //System.out.println("loggbf " + loggbf[iThresh] + " theta " + theta + " chiHlev " + chiHlev[iThresh]);
#  //System.out.println("bfSum " + bfSum + " logbfTerm " + logbfTerm);
#//  }
              
            #//end iThresh loop 

#// cm^2 per *neutral* H atom
            logKapH1bf = logHelp3 + math.log(bfSum) 

#//Stimulated emission correction
            logKapH1bf = logKapH1bf + logStimEm
#//System.out.println("lambda " + lambdas[iLam] + "iTau " + iTau + " sigma " + Math.exp(logKapH1bf)); 

#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
            logKapH1bf = logKapH1bf + logNH1[iTau]
#//System.out.println(" aH1 " + Math.exp(logKapH1bf)); 
#////Nasty fix to make Balmer lines show up in A0 stars!
#//     if (teff > 8000){
#//          logKapH1bf = logKapH1bf - logE10*1.5;
#//     
            kappa = math.exp(logKapH1bf) 
#//System.out.println("HIbf " + log10E*logKapH1bf);
#//if (iTau == 36 && iLam == 142){
#//           System.out.println("lambdaA " + lambdaA + " logKapH1bf " + log10E*(logKapH1bf)); //-rho[1][iTau]));
#//}
#//H I f-f:
#// cm^2 per *neutral* H atom
            logKapH1ff = logHelp3 + loggff + logffHelp - logTheta - (theta*chiIH)*logE10

#//Stimulated emission correction
            logKapH1ff = logKapH1ff + logStimEm
#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
            logKapH1ff = logKapH1ff + logNH1[iTau]
#////Nasty fix to make Balmer lines show up in A0 stars!
#//     if (teff > 8000){
#//          logKapH1ff = logKapH1ff - logE10*1.5;
#//     
            kappa = kappa + math.exp(logKapH1ff); 
#//System.out.println("HIff " + log10E*logKapH1ff);

#//if (iTau == 36 && iLam == 142){
#//           System.out.println("logKapH1ff " + log10E*(logKapH1ff)); //-rho[1][iTau]));
#//}

#//
#//Hminus:
#//
#// H^- b-f:
#//if (iTau == 36 && iLam == 142){
# // System.out.println("temp " + temp[0][iTau] + " lambdanm " + lambdanm);
# // }
            logKapHmbf =  -99.0 #//initialize default
            #//if ( (temp[0][iTau] > 2500.0) && (temp[0][iTau] < 10000.0) ){
            #//if ( (temp[0][iTau] > 2500.0) && (temp[0][iTau] < 8000.0) ){
            #//Try lowering lower Teff limit to avoid oapcity collapse in outer layers of late-type stars
            if ( (temp[0][iTau] > 1000.0) and (temp[0][iTau] < 10000.0) ):
                if ((lambdanm > 225.0) and (lambdanm < 1500.0) ):  # //nm 
#//if (iTau == 36 && iLam == 142){
# //              System.out.println("In KapHmbf condition...");
#//}
                    ii = 0.0
                    alphaHmbf = signAHm[0]*math.exp(logAHm[0]) #//initialize accumulator
                    #for (int i = 1; i < numHmTerms; i++){
                    for i in range(1, numHmTerms):
                        ii = float(i)
#//if (iTau == 36 && iLam == 142){
#//                   System.out.println("ii " + ii);
#//}
                        logTermHmbf = logAHm[i] + ii*logLambdaA 
                        alphaHmbf = alphaHmbf + signAHm[i]*math.exp(logTermHmbf)  
#//if (iTau == 36 && iLam == 142){
#//                  System.out.println("logTermHmbf " + log10E*logTermHmbf + " i " + i + " logAHm " + log10E*logAHm[i]); 
#//}
                
                    logAlphaHmbf = math.log(alphaHmbf)
#// cm^2 per neutral H atom
                    logKapHmbf = logAHmbf + logAlphaHmbf + pe[1][iTau] + 2.5*logTheta + (0.754*theta)*logE10 
#//Stimulated emission correction
                    logKapHmbf = logKapHmbf + logStimEm
#//if (iTau == 36 && iLam == 142){
#//  System.out.println("alphaHmbf " + alphaHmbf);
#//  System.out.println("logKapHmbf " + log10E*logKapHmbf + " logAHmbf " + log10E*logAHmbf + " logAlphaHmbf " + log10E*logAlphaHmbf);
#//  }

#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
                    logKapHmbf = logKapHmbf + logNH1[iTau]
                    kappa = kappa + math.exp(logKapHmbf)
#//System.out.println("Hmbf " + log10E*logKapHmbf);
#//if (iTau == 36 && iLam == 142){
#//           System.out.println("logKapHmbf " + log10E*(logKapHmbf)); //-rho[1][iTau]));
#//}
                #//wavelength condition
            #// temperature condition

#// H^- f-f:
            logKapHmff = -99.0 #//initialize default
          #//if ( (temp[0][iTau] > 2500.0) && (temp[0][iTau] < 10000.0) ){
          #//Try lowering lower Teff limit to avoid oapcity collapse in outer layers of late-type stars
          #//if ( (temp[0][iTau] > 2500.0) && (temp[0][iTau] < 8000.0) ){
            if ( (temp[0][iTau] > 1000.0) and (temp[0][iTau] < 10000.0) ):
                if ((lambdanm > 260.0) and (lambdanm < 11390.0) ): #//nm 
                    #//construct "f_n" polynomials in log(lambda)
                    for j in range(3):
                        fHm[j] = fHmTerms[j][0]  #//initialize accumulators                        
                    ii = 0.0  
                    for i in range(1, numHmffTerms):
                        ii = float(i)
                        logLambdaAFac = math.pow(log10LambdaA, ii)
                        for j in range(3):
                            fHm[j] = fHm[j] + (fHmTerms[j][i]*logLambdaAFac)    
                        #} #// i
                    #} #// j
#// 
                    fPoly = fHm[0] + fHm[1]*log10Theta + fHm[2]*log10Theta*log10Theta
#// In cm^2 per neutral H atom:
#// Stimulated emission alreadya ccounted for
                    logKapHmff = logAHmff + pe[1][iTau] + fPoly*logE10

#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
                    logKapHmff = logKapHmff + logNH1[iTau]
                    kappa = kappa + math.exp(logKapHmff)
#//System.out.println("Hmff " + log10E*logKapHmff);
#//if (iTau == 36 && iLam == 142){
#//           System.out.println("logKapHmff " + log10E*(logKapHmff)); //-rho[1][iTau]));
#//}
                #//wavelength condition
            #// temperature condition


#// H^+_2:
#//
            logKapH2p = -99.0 #//initialize default 
            if ( temp[0][iTau] < 4000.0 ):
                if ((lambdanm > 380.0) and (lambdanm < 2500.0) ): # //nm 
                    sigmaH2p = sigmaH2pTerm[0] #//initialize accumulator
                    UH2p = UH2pTerm[0] #//initialize accumulator
                    ii = 0.0#
                    for i in range(1, numH2pTerms):
                        ii = float(i) 
                        logLambdaAFac = math.pow(log10LambdaA, ii)
                        #// kapH2p way too large with lambda in A - try cm:  No! - leads to negative logs
                        #//logLambdaAFac = Math.pow(logLambda, ii);
                        sigmaH2p = sigmaH2p +  sigmaH2pTerm[i] * logLambdaAFac 
                        UH2p = UH2p +  UH2pTerm[i] * logLambdaAFac                    
                    logSigmaH2p = math.log(sigmaH2p)
                    logKapH2p = logAH2p + logSigmaH2p - (UH2p*theta)*logE10 + logNH2[iTau] 
#//Stimulated emission correction
                    logKapH2p = logKapH2p + logStimEm

#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
                    logKapH2p = logKapH2p + logNH1[iTau]
                    kappa = kappa + math.exp(logKapH2p) 
#//System.out.println("H2p " + log10E*logKapH2p);
#//if (iTau == 16 && iLam == 142){
#           //System.out.println("logKapH2p " + log10E*(logKapH2p-rho[1][iTau]) + " logAH2p " + log10E*logAH2p
#// + " logSigmaH2p " + log10E*logSigmaH2p + " (UH2p*theta)*logE10 " + log10E*((UH2p*theta)*logE10) + " logNH2[iTau] " + log10E*logNH2[iTau]);
#//}
                #//wavelength condition
            #// temperature condition


#//He I 
#//
#//  HeI b-f + f-f
#//Scale sum of He b-f and f-f with sum of HI b-f and f-f 

#//wavelength condition comes from requirement that lower E level be greater than n=2 (edge at 22.78 nm)
            logKapHe = -99.0 #//default intialization
            if ( temp[0][iTau] > 10000.0 ):
                if (lambdanm > 22.8): #//nm  
                    totalH1Kap = math.exp(logKapH1bf) + math.exp(logKapH1ff)
                    logTotalH1Kap = math.log(totalH1Kap) 
                    helpHe = Useful.k() * temp[0][iTau]
#// cm^2 per neutral H atom (after all, it's scaled wrt kappHI
#// Stimulated emission already accounted for
#//
#//  *** CAUTION: Is this *really* the right thing to do???
#//    - we're re-scaling the final H I kappa in cm^2/g corrected for stim em, NOT the raw cross section
                    logKapHe = math.log(4.0) - (10.92 / helpHe) + logTotalH1Kap

#//Add it in to total - opacity per neutral HI atom, so multiply by logNH1 
#// This is now linear opacity in cm^-1
                    logKapHe = logKapHe + logNH1[iTau]
                    kappa = kappa + math.exp(logKapHe) 
#//System.out.println("He " + log10E*logKapHe);
#//if (iTau == 36 && iLam == 142){
#//           System.out.println("logKapHe " + log10E*(logKapHe)); //-rho[1][iTau]));
#//}
                #//wavelength condition
            #// temperature condition


#//
#//He^- f-f:
            logKapHemff = -99.0 #//default initialization
            if ( (theta > 0.5) and (theta < 2.0) ):
                if ((lambdanm > 500.0) and (lambdanm < 15000.0) ): 

#// initialize accumulators:
                    cHemff[0] = signC0HemffTerm[0]*math.exp(logC0HemffTerm[0]);   
                    #//System.out.println("C0HemffTerm " + signC0HemffTerm[0]*Math.exp(logC0HemffTerm[0]));
                    cHemff[1] = signC1HemffTerm[0]*math.exp(logC1HemffTerm[0]);   
                    #//System.out.println("C1HemffTerm " + signC1HemffTerm[0]*Math.exp(logC1HemffTerm[0]));
                    cHemff[2] = signC2HemffTerm[0]*math.exp(logC2HemffTerm[0]);   
                    #//System.out.println("C2HemffTerm " + signC2HemffTerm[0]*Math.exp(logC2HemffTerm[0]));
                    cHemff[3] = signC3HemffTerm[0]*math.exp(logC3HemffTerm[0]);   
                    #//System.out.println("C3HemffTerm " + signC3HemffTerm[0]*Math.exp(logC3HemffTerm[0]));
#//build the theta polynomial coefficients
                    ii = 0.0
                    for i in range(1, numHemffTerms):
                        ii = float(i)
                        thisLogTerm = ii*logTheta + logC0HemffTerm[i] 
                        cHemff[0] = cHemff[0] + signC0HemffTerm[i]*math.exp(thisLogTerm) 
                        #//System.out.println("i " + i + " ii " + ii + " C0HemffTerm " + signC0HemffTerm[i]*Math.exp(logC0HemffTerm[i]));
                        thisLogTerm = ii*logTheta + logC1HemffTerm[i] 
                        cHemff[1] = cHemff[1] + signC1HemffTerm[i]*math.exp(thisLogTerm) 
                        #//System.out.println("i " + i + " ii " + ii + " C1HemffTerm " + signC1HemffTerm[i]*Math.exp(logC1HemffTerm[i]));
                        thisLogTerm = ii*logTheta + logC2HemffTerm[i]
                        cHemff[2] = cHemff[2] + signC2HemffTerm[i]*math.exp(thisLogTerm) 
                        #//System.out.println("i " + i + " ii " + ii + " C2HemffTerm " + signC2HemffTerm[i]*Math.exp(logC2HemffTerm[i]));
                        thisLogTerm = ii*logTheta + logC3HemffTerm[i] 
                        cHemff[3] = cHemff[3] + signC3HemffTerm[i]*math.exp(thisLogTerm) 
                        #//System.out.println("i " + i + " ii " + ii + " C3HemffTerm " + signC3HemffTerm[i]*Math.exp(logC3HemffTerm[i]));
     
    #//// Should polynomial expansion for Cs be in log10Theta??: - No! Doesn't help
    #// initialize accumulators:
    #// cHemff[0] = C0HemffTerm[0];   
    #// cHemff[1] = C1HemffTerm[0];   
    #// cHemff[2] = C2HemffTerm[0];   
    #// cHemff[3] = C3HemffTerm[0];   
    #// ii = 0.0;
    #// for (int i = 1; i < numHemffTerms; i++){
    #//    ii = (double) i;
    #//    log10ThetaFac = Math.pow(log10Theta, ii);
    #//    thisTerm = log10ThetaFac * C0HemffTerm[i]; 
    #//    cHemff[0] = cHemff[0] + thisTerm; 
    #//    thisTerm = log10ThetaFac * C1HemffTerm[i]; 
    #//    cHemff[1] = cHemff[1] + thisTerm; 
    #//    thisTerm = log10ThetaFac * C2HemffTerm[i]; 
    #//    cHemff[2] = cHemff[2] + thisTerm; 
    #//    thisTerm = log10ThetaFac * C3HemffTerm[i]; 
    #//    cHemff[3] = cHemff[3] + thisTerm; 
    #// }
     
#//Build polynomial in logLambda for alpha(He^1_ff):
                    log10AlphaHemff = cHemff[0] #//initialize accumulation
                    #//System.out.println("cHemff[0] " + cHemff[0]);
                    ii = 0.0
                    for i in range(1, 3+1):
                        #//System.out.println("i " + i + " cHemff[i] " + cHemff[i]);
                        ii = float(i)
                        thisTerm = cHemff[i] * math.pow(log10LambdaA, ii)
                        log10AlphaHemff = log10AlphaHemff + thisTerm 
        
                    #//System.out.println("log10AlphaHemff " + log10AlphaHemff);
                    alphaHemff = math.pow(10.0, log10AlphaHemff) #//gives infinite alphas!
                    #// alphaHemff = log10AlphaHemff; // ?????!!!!!
                    #//System.out.println("alphaHemff " + alphaHemff);

#// Note: this is the extinction coefficient per *Hydrogen* particle (NOT He- particle!)
#       //nHe = Math.exp(logNHe1[iTau]) + Math.exp(logNHe2[iTau]);
#       //logNHe = Math.log(nHe);
#       //logKapHemff = Math.log(alphaHemff) + Math.log(AHe) + pe[1][iTau] + logNHe1[iTau] - logNHe;
                    logKapHemff = logAHemff + math.log(alphaHemff) + pe[1][iTau] + logNHe1[iTau] - logNH[iTau]

#//Stimulated emission already accounted for
#//Add it in to total - opacity per H particle, so multiply by logNH 
#// This is now linear opacity in cm^-1
                    logKapHemff = logKapHemff + logNH[iTau]
                    kappa = kappa + math.exp(logKapHemff) 
#//System.out.println("Hemff " + log10E*logKapHemff);
#//if (iTau == 36 && iLam == 155){
#//if (iLam == 155){
#//           System.out.println("logKapHemff " + log10E*(logKapHemff)); //-rho[1][iTau]));
#//}
 
                #//wavelength condition
            #// temperature condition

#//
#// electron (e^-1) scattering (Thomson scattering)

#//coefficient per *"hydrogen atom"* (NOT per e^-!!) (neutral or total H??):
            logKapE = logAlphaE + Ne[1][iTau] - logNH[iTau]

#//Stimulated emission not relevent 
#//Add it in to total - opacity per H particle, so multiply by logNH 
#// This is now linear opacity in cm^-1
#//I know, we're adding logNH right back in after subtracting it off, but this is for dlarity and consistency for now... :
            logKapE = logKapE + logNH[iTau]   
            kappa = kappa + math.exp(logKapE) 
#//System.out.println("E " + log10E*logKapE);
#//if (iTau == 36 && iLam == 142){
#//           System.out.println("logKapE " + log10E*(logKapE)); //-rho[1][iTau]));
#//}

#//Metal b-f
#//Fig. 8.6 Gray 3rd Ed.
#//

#//
#// This is now linear opacity in cm^-1
#// Divide by mass density
#// This is now mass extinction in cm^2/g
#//
            logKappa[iLam][iTau] = math.log(kappa) - rho[1][iTau]
#// Fudge is in cm^2/g:  Converto to natural log:
            logEKapFudge = logE10 * logKapFudge
            logKappa[iLam][iTau] = logKappa[iLam][iTau] + logEKapFudge
#//if (iTau == 36 && iLam == 142){
#//System.out.println(" " + log10E*(logKappa[iLam][iTau]+rho[1][iTau]));
#//}


        #// close iTau depth loop
#//
    #//close iLam wavelength loop 

    return logKappa

    #} //end method kappas2

def kapRos(numDeps, numLams, lambdas, logKappa, temp):

    kappaRos = [ [0.0 for i in range(numDeps)] for j in range(2) ]

    #double numerator, denominator, deltaLam, logdBdTau, logNumerator, logDenominator;
    #double logTerm, logDeltaLam, logInvKap, logInvKapRos;

    for iTau in range(numDeps):

        numerator = 0.0 #//initialize accumulator
        denominator = 0.0

        for iLam in range(1, numLams):
          
            deltaLam = lambdas[iLam] - lambdas[iLam-1]  #//lambda in cm
            logDeltaLam = math.log(deltaLam)

            logInvKap = -1.0 * logKappa[iLam][iTau]
            logdBdTau = Planck.dBdT(temp[0][iTau], lambdas[iLam])
            logTerm = logdBdTau + logDeltaLam
            denominator = denominator + math.exp(logTerm) 
            logTerm = logTerm + logInvKap;
            numerator = numerator + math.exp(logTerm)
        
        logNumerator = math.log(numerator)
        logDenominator = math.log(denominator)
        logInvKapRos = logNumerator - logDenominator 
        kappaRos[1][iTau] = -1.0 * logInvKapRos #//logarithmic
        kappaRos[0][iTau] = math.exp(kappaRos[1][iTau])

    return kappaRos

    #} //end method kapRos