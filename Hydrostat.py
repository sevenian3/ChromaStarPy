# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:07:56 2017

@author: ishort
"""

import math
import Useful

def hydroFormalSoln(numDeps, grav, tauRos, kappa, temp, guessPGas):
    
    """This approach is based on integrating the formal solution of the hydrostaitc equilibrium equation
// on the otical depth (Tau) scale.  Advantage is that it makes better use of the itial guess at
// pgas 
//
//  Takes in *Gas* pressure, converts tot *total pressure*, then returns *Gas* pressure
//
"""

    press = [ [0.0 for i in range(numDeps)] for j in range(2)]
    logC = Useful.logC()
    logSigma = Useful.logSigma()

    radFac = math.log(4.0) + logSigma - math.log(3.0) - logC

    logEg = math.log(grav) #//Natural log g!! 
    #// no needed if integrating in natural log?? //double logLogE = Math.log(Math.log10(Math.E));
    log1p5 = math.log(1.5)
    logE = math.log10(math.e)

#//Compute radiation pressure for this temperature structure and add it to Pgas 
#//
    #double pT, pRad;
    logPRad = [0.0 for i in range(numDeps)]
    logPTot = [0.0 for i in range(numDeps)]
    #//  System.out.println("hydroFormalSoln: ");
    for i in range(numDeps):
        logPRad[i] = radFac + 4.0 * temp[1][i]
        pRad = math.exp(logPRad[i])
        #//System.out.println("i " + i + " pRad " + pRad);
        pT = guessPGas[0][i] + pRad
        #//       System.out.println("i " + i + " guessPGas[1] " + logE*guessPGas[1][i]);
        logPTot[i] = math.log(pT)

    #double help, logHelp, logPress;
    #double term, logSum, integ, logInteg, lastInteg;
    #double deltaLogT; 
  
    sum = [0.0 for i in range(numDeps)]

#//Upper boundary - inherit from intiial guess:
#//Carefull here - P at upper boundary can be an underestimate, but it must not be greater than value at next depth in!
#//  press[1][0] = logPTot[0];
#//  press[1][0] = guessPGas[1][0];
#//   press[1][0] = Math.log(1.0e-4); //try same upper boundary as Phoenix
#//
#//   press[0][0] = Math.exp(press[1][0]);
    press[0][0] = 0.1 * guessPGas[0][0]
    press[1][0] = math.log(press[0][0])
#//Corresponding value of basic integrated quantity at top of atmosphere:
    logSum = 1.5 * press[1][0] + math.log(0.666667) - logEg
    sum[0] = math.exp(logSum) 
  
#// Integrate inward on logTau scale

#// CAUTION; This is not an integral for Delta P, but for P once integral at each tau is exponentiated by 2/3!
#// Accumulate basic integral to be exponentiated, then construct pressure values later:

#//Jump start integration with an Euler step:
    deltaLogT = tauRos[1][1] - tauRos[1][0]
#// log of integrand
    logInteg = tauRos[1][1] + 0.5*logPTot[1] - kappa[1][1]
    lastInteg = math.exp(logInteg)  
    sum[1] = sum[0] + lastInteg * deltaLogT 

#// Continue with extended trapezoid rule:
   
    for i in range(2, numDeps):

        deltaLogT = tauRos[1][i] - tauRos[1][i-1]
        logInteg = tauRos[1][i] + 0.5*logPTot[i] - kappa[1][i]
        integ = math.exp(logInteg)
        term = 0.5 * (integ + lastInteg) * deltaLogT
        sum[i] = sum[i-1] + term #//accumulate basic integrated quantity
        lastInteg = integ  

    #//System.out.println("hydroFormalSoln: ");
    for i in range(1, numDeps):
#//Evaluate total pressures from basic integrated quantity at edach depth 
#// our integration variable is the natural log, so I don't think we need the 1/log(e) factor
        logPress = 0.666667 * (log1p5 + logEg + math.log(sum[i]))
#//Subtract radiation pressure:
        logHelp = logPRad[i] - logPress
        help = math.exp(logHelp)
# For hot and low g stars: limit Prad to 50% Ptot so we doen't get netaive Pgas and rho values:
        if (help > 0.5):
            help = 0.5
       
        press[1][i] = logPress + math.log(1.0 - help)
        #//System.out.println("i " + i + " guessPGas[1] " + logE*guessPGas[1][i] + " press[1] " + logE*press[1][i]);
        press[0][i] = math.exp(press[1][i])
    

    return press   #//*Gas* pressure

#//end method hydroFormalSoln()
 

#// Compute radiation pressure
def radPress(numDeps, temp):

        
    pRad = [ [0.0 for i in range(numDeps)] for j in range(2)]        

    logC = Useful.logC()
    logSigma = Useful.logSigma()
    radFac = math.log(4.0) + logSigma - math.log(3.0) - logC
    for i in range(numDeps):
        pRad[1][i] = radFac + 4.0 * temp[1][i]
        pRad[0][i] = math.exp( pRad[1][i])
      

    return pRad;

    #//end method radPress


   
