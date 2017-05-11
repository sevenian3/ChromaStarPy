# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import Useful

def planck(temp, lambda2):
    
    """ /**
 * Inputs: lambda: a single scalar wavelength in cm temp: a single scalar
 * temperature in K Returns log of Plank function in logBBlam - B_lambda
 * distribution in pure cgs units: ergs/s/cm^2/ster/cm
 */"""

    #//int numLams = (int) (( lamSetup[1] - lamSetup[0] ) / lamSetup[2]) + 1; 
    #double logBBlam; //, BBlam;

    #//double c = Useful.c; //linear
    logC = Useful.logC() # //log
    #//double k = Useful.k;  //linear
    logK = Useful.logK()  #//log
    #//double h = Useful.h;  //linear
    logH = Useful.logH()  #//log

    logPreFac = math.log(2.0) + logH + 2.0 * logC  #//log
    logExpFac = logH + logC - logK      #//log
    #//double preFac = 2.0 * h * ( c * c );  //linear
    #//double expFac = ( h / k ) * c;      //linear

    #//System.out.println("logC " + logC + " logK " + logK + " logH " + logH);
    #//System.out.println("logPreFac " + logPreFac + " logExpFac " + logExpFac);
    #//Declare scratch variables:
    #double logLam, logPreLamFac, logExpLamFac, expon, logExpon, eTerm, denom, logDenom;  //log
    #//double preLamFac, expLamFac, expon, denom; //linear

    #//for (int il = 0; il < numLams; il++){
    #//lambda = lambda[il] * 1.0E-7;  // convert nm to cm
    #//lambda = lambda * 1.0E-7;  // convert nm to cm
    logLam = math.log(lambda2) #// Do the call to log for lambda once //log
    #//System.out.println("lambda " + lambda + " logLam " + logLam);

    logPreLamFac = logPreFac - 5.0 * logLam  #//log
    logExpLamFac = logExpFac - logLam    #//log
    #//System.out.println("logPreLamFac " + logPreLamFac + " logExpLamFac " + logExpLamFac);
    #// Be VERY careful about how we divide by lambda^5:
    #//preLamFac = preFac / ( lambda * lambda ); //linear
    #//preLamFac = preLamFac / ( lambda * lambda );  //linear
    #//preLamFac = preLamFac / lambda;   //linear
    #//expLamFac = expFac / lambda;

    #//for (int id = 0; id < numDeps; id++){
    #//logExpon = logExpLamFac - temp[1][id];
        
    #//This is very subtle and dangerous!
    logExpon = logExpLamFac - math.log(temp)  #// log of hc/kTlambda
    #//System.out.println("temp " + temp + " logTemp " + Math.log(temp));
    expon = math.exp(logExpon)  #// hc/kTlambda
    #//System.out.println("logExpon " + logExpon + " expon " + expon + " denom " + denom);
    #// expon = expLamFac / temp;  //linear
    eTerm = math.exp(expon) #// e^hc/ktlambda
    denom = eTerm - 1.0 #// e^hc/ktlambda - 1
    logDenom = math.log(denom) #// log(e^hc/ktlambda - 1)

    #//BBlam[1][id][il] = logPreLamFac - logDenom;
    #//BBlam[0][id][il] = Math.exp(BBlam[1][id][il]);
    logBBlam = logPreLamFac - logDenom  #//log
    #// Not needed? BBlam = math.exp(logBBlam)  #//log
    #//BBlam = preLamFac / denom;  //linear

    #// } //id loop - depths
    #// } //il loop - lambdas
    return logBBlam;
    #} //end method planck()

    
def dBdT(temp, lambda2):
    
    """// Computes the first partial derivative of B(T) wrt T, dB/dT:"""

    #double logdBdTlam; 

    #//double c = Useful.c; //linear
    logC = Useful.logC()  #//log
    #//double k = Useful.k  #//linear
    logK = Useful.logK()  #//log
    #//double h = Useful.h  #//linear
    logH = Useful.logH()  #//log

    logPreFac = math.log(2.0) + logH + 2.0 * logC  #//log
    logExpFac = logH + logC - logK      #//log

    #//Declare scratch variables:
    #double logLam, logTemp, logPreLamFac, logExpLamFac, expon, logExpon, eTerm, denom, logDenom;  //log

    #//lambda = lambda * 1.0E-7;  // convert nm to cm
    logLam = math.log(lambda2) #// Do the call to log for lambda once //log
    logTemp = math.log(temp)

    logPreLamFac = logPreFac + logExpFac - 6.0 * logLam - 2.0 * logTemp  #//log
        
    logExpLamFac = logExpFac - logLam    #//log
        
    #//This is very subtle and dangerous!
    logExpon = logExpLamFac - logTemp  #// log of hc/kTlambda
    expon = math.exp(logExpon)  #// hc/kTlambda
       
    eTerm = math.exp(expon) #// e^hc/ktlambda
    denom = eTerm - 1.0 #// e^hc/ktlambda - 1
    logDenom = math.log(denom) #// log(e^hc/ktlambda - 1)
        
    logdBdTlam = logPreLamFac + expon - 2.0 * logDenom  #//log
        
    return logdBdTlam;
    #} //end method dBdT