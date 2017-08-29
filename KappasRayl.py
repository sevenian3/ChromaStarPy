# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:18:39 2017

@author: ishort
"""
import math
import Useful
import PartitionFn

#/* Rayleigh scattering opacity routines taken from Moog (moogjul2014/, MOOGJUL2014.tar)
#Chris Sneden (Universtiy of Texas at Austin)  and collaborators
#http://www.as.utexas.edu/~chris/moog.html
#//From Moog source file Opacscat.f
#*/


def masterRayl(numDeps, numLams, temp, lambdaScale, stagePops, molPops):

    """ /*c******************************************************************************
c  The subroutines needed to calculate the opacities from scattering by
c  H I, H2, He I, are in this file.  These are from ATLAS9.
c******************************************************************************
*/"""   
        
#//System.out.println("masterRayl called...");

#//From Moog source file Opacitymetals.f
#// From how values such as aC1[] are used in Moog file Opacit.f to compute the total opacity
#// and then the optical depth scale, I infer that they are extinction coefficients 
#// in cm^-1 
#//
#// There does not seem to be any correction for stimulated emission 

    logE = math.log10(math.e)

    masterRScat = [ [ 0.0 for i in range(numDeps) ] for j in range(numLams) ]

    logUH1 = [0.0 for i in range(5)]
    logUHe1 = [0.0 for i in range(5)]

    logStatWH1 = 0.0
    logStatWHe1 = 0.0

    theta = 1.0
    species = ""
    
    logGroundPopsH1 = [0.0 for i in range(numDeps)]
    logGroundPopsHe1 = [0.0 for i in range(numDeps)]
#//
#// H I: Z=1 --> iZ=0:
    sigH1 = [0.0 for i in range(numDeps)]
#// He I: Z=2 --> iZ=1:
    sigHe1 = [0.0 for i in range(numDeps)]
    species = "HI"
    logUH1 = PartitionFn.getPartFn2(species)
    species = "HeI"
    logUHe1 = PartitionFn.getPartFn2(species)

    #//System.out.println("iD     PopsH1     PopsHe1");
    for iD in range(numDeps):
#//neutral stage
#//Assumes ground state stat weight, g_1, is 1.0
        #theta = 5040.0 / temp[0][iD]
#// U[0]: theta = 1.0, U[1]: theta = 0.5
        """
        if (theta <= 0.5):
            logStatWH1 = logUH1[1]
            logStatWHe1 = logUHe1[1]
        elif ( (theta < 1.0) and (theta > 0.5) ):
            logStatWH1 = ( (theta-0.5) * logUH1[0] ) + ( (1.0-theta) * logUH1[1] )
            logStatWHe1 = ( (theta-0.5) * logUHe1[0] ) + ( (1.0-theta) * logUHe1[1] )
            #//divide by common factor of interpolation interval of 0.5 = (1.0 - 0.5):
            logStatWH1 = 2.0 * logStatWH1 
            logStatWHe1 = 2.0 * logStatWHe1 
        else: 
            logStatWH1 = logUH1[0]
            logStatWHe1 = logUHe1[0]
        """
        
#// NEW Interpolation with temperature for new partition function: lburns
        thisTemp = temp[0][iD];
        if (thisTemp <= 130):
            logStatWH1 = logUH1[0]
            logStatWHe1 = logUHe1[0]
        elif (thisTemp > 130 and thisTemp <= 500):
            logStatWH1 = logUH1[1] * (thisTemp - 130)/(500 - 130) \
                       + logUH1[0] * (500 - thisTemp)/(500 - 130)
            logStatWHe1 = logUHe1[1] * (thisTemp - 130)/(500 - 130) \
                       + logUHe1[0] * (500 - thisTemp)/(500 - 130)
        elif (thisTemp > 500 and thisTemp <= 3000):
            logStatWH1 = logUH1[2] * (thisTemp - 500)/(3000 - 500) \
                       + logUH1[1] * (3000 - thisTemp)/(3000 - 500)
            logStatWHe1 = logUHe1[2] * (thisTemp - 500)/(3000 - 500) \
                       + logUHe1[1] * (3000 - thisTemp)/(3000 - 500)
        elif (thisTemp > 3000 and thisTemp <= 8000):
            logStatWH1 = logUH1[3] * (thisTemp - 3000)/(8000 - 3000) \
                       + logUH1[2] * (8000 - thisTemp)/(8000 - 3000)
            logStatWHe1 = logUHe1[3] * (thisTemp - 3000)/(8000 - 3000) \
                       + logUHe1[2] * (8000 - thisTemp)/(8000 - 3000)
        elif (thisTemp > 8000 and thisTemp < 10000):
            logStatWH1 = logUH1[4] * (thisTemp - 8000)/(10000 - 8000) \
                       + logUH1[3] * (10000 - thisTemp)/(10000 - 8000)
            logStatWHe1 = logUHe1[4] * (thisTemp - 8000)/(10000 - 8000) \
                       + logUHe1[3] * (10000 - thisTemp)/(10000 - 8000)
        else:
            #// for temperatures of greater than or equal to 10000K lburns
            logStatWH1 = logUH1[4]
            logStatWHe1 = logUHe1[4]
        
        
        logGroundPopsH1[iD] = stagePops[0][0][iD] - logStatWH1 
        logGroundPopsHe1[iD] = stagePops[1][0][iD] - logStatWHe1

           #// if (iD%10 == 1){
           #//     System.out.format("%03d, %21.15f, %21.15f %n",
           #//          iD, logE*logGroundPopsH1[iD], logE*logGroundPopsHe1[iD]);
           #// }

       
        kapRScat = 0.0 
        #//System.out.println("iD    iL    lambda    sigH1    sigHe1 ");
        for iL in range(numLams):
#//
            for i in range(numDeps):
                sigH1[i] = 0.0
                sigHe1[i] = 0.0
            

            #//System.out.println("Calling opacH1 from masterMetal..."); 
            sigH1 = opacHscat(numDeps, temp, lambdaScale[iL], logGroundPopsH1)
            sigHe1 = opacHescat(numDeps, temp, lambdaScale[iL], logGroundPopsHe1)

            for iD in range(numDeps):
                kapRScat = sigH1[iD] + sigHe1[iD]
                masterRScat[iL][iD] = math.log(kapRScat)
                #//if ( (iD%10 == 0) && (iL%10 == 0) ) {
                #//  System.out.format("%03d, %03d, %21.15f, %21.15f, %21.15f %n",
                #//     iD, iL, lambdaScale[iL], Math.log10(sigH1[iD]), Math.log10(sigHe1[iD]));
                #//}

             #} //iD
 
        #} //iL

    return masterRScat;

    #} //end method masterRayl


def opacHscat(numDeps, temp, lambda2, logGroundPops):

    """//c******************************************************************************
//c  This routine computes H I Rayleigh scattering opacities.
//c******************************************************************************"""
    
    #//System.out.println("opacHscat called");

    sigH = [0.0 for i in range(numDeps)]

#//cross-section is zero below threshold, so initialize:
    for i in range(numDeps):
        sigH[i] = 0.0
      

    freq = Useful.c() / lambda2  

#//      include 'Atmos.com'
#//      include 'Kappa.com'
#//      include 'Linex.com'

    wavetemp = 2.997925e18 / min(freq, 2.463e15)
    ww = math.pow(wavetemp, 2)
    sig = ( 5.799e-13 + (1.422e-6/ww) + (2.784/(ww*ww)) ) / (ww*ww)
    for i in range(numDeps):
        sigH[i] = sig * 2.0 * math.exp(logGroundPops[i])
     

    return sigH

  #} //end method opacHscat


def opacHescat(numDeps, temp, lambda2, logGroundPops):

    """//c******************************************************************************
//c  This routine computes He I Rayleigh scattering opacities.
//c******************************************************************************"""
    
    #//System.out.println("opacHescat called");

    sigHe = [0.0 for i in range(numDeps)]

#//cross-section is zero below threshold, so initialize:
    for i in range(numDeps):
        sigHe[i] = 0.0
      

    freq = Useful.c() / lambda2  


#//      include 'Atmos.com'
#//      include 'Kappa.com'
#//      include 'Linex.com'

    wavetemp = 2.997925e18 / min(freq, 5.15e15)
    ww = math.pow(wavetemp, 2)
    sig = (5.484e-14/ww/ww) * math.pow( ( 1.0 + ((2.44e5 + (5.94e10/(ww-2.90e5)))/ww) ), 2 )
    for i in range(numDeps):
        sigHe[i] = sig * math.exp(logGroundPops[i]) 

    return sigHe

    #} //end method opacHescat

"""
/* Need molecular H_2 number density for this:
 *
      public static double[] opacH2scat(int numDeps, double[][] temp, double lambda, double[] molPops){

      double[] sigH2 = new double[numDeps];

//cross-section is zero below threshold, so initialize:
      for (int i = 0; i < numDeps; i++){
         sigH2[i] = 0.0;
      }

      double freq = Useful.c / lambda;  

//c******************************************************************************
//c  This routine computes H2 I Rayleigh scattering opacities.
//c******************************************************************************

//      include 'Atmos.com'
//      include 'Kappa.com'
//      include 'Linex.com'

      double wavetemp = 2.997925e18 / min(freq, 2.463e15);
      double ww = math.pow(wavetemp, 2);
      double sig = ( 8.14e-13 + (1.28d-6/ww) + (1.61/(ww*ww)) ) / (ww*ww);
      for (int i = 0; i < numDeps; i++){
       sigH2[i] = sig * math.exp(molPops);
      }

      return sigH2;

      } //end method opacH2scat
*/"""
