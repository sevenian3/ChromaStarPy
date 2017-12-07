# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:42:58 2017

@author: Ian
"""

import math
import random
import numpy
import Useful
import ToolBox

def flux(intens, cosTheta):

    """// returns surface flux as a 2XnumLams vector
    //  - Row 0 linear flux (cgs units)
    //  - Row 1 log_e flux"""
    
    #//double[][] fluxSurfSpec = new double[2][numLams];
    fluxSurfSpec = [0.0 for i in range(2)]
    #//double fluxSurfBol, logFluxSurfBol, lambda2, lambda1;  // Bolometric quantities for reality check

    #//  cosTheta is a 2xnumThetas array:
 
    #// Gaussian quadrature
 
    numThetas = len(cosTheta[0])

    #//fluxSurfBol = 0;
    #//for (int il = 0; il < numLams; il++) {
    flx = 0.0

    for it in range(numThetas):

        #//flx = flx + intens[il][it] * cosTheta[1][it] * cosTheta[0][it];
        flx = flx + intens[it] * cosTheta[1][it] * cosTheta[0][it]

    #}  // it - theta loop

    #//fluxSurfSpec[0][il] = 2.0 * Math.PI * flx;
    #//fluxSurfSpec[1][il] = Math.log(fluxSurfSpec[0][il]);
    fluxSurfSpec[0] = 2.0 * math.pi * flx
    fluxSurfSpec[1] = math.log(fluxSurfSpec[0])

    """/* Can no longer do this test here:
         if (il > 1) {
         lambda2 = lambdas[il]; // * 1.0E-7;  // convert nm to cm
         lambda1 = lambdas[il - 1]; // * 1.0E-7;  // convert nm to cm
         fluxSurfBol = fluxSurfBol
         + fluxSurfSpec[0][il] * (lambda2 - lambda1);
         }
         */"""
    #//} //il - lambda loop

    """/* Can no longer do this test here:
         logFluxSurfBol = Math.log(fluxSurfBol);
         double logTeff = (logFluxSurfBol - Useful.logSigma()) / 4.0;
         double teff = Math.exp(logTeff);

         String pattern = "0000.00";
         //String pattern = "#####.##";
         DecimalFormat myFormatter = new DecimalFormat(pattern);

         System.out.println("FLUX: Recovered Teff = " + myFormatter.format(teff));
         */"""
    return fluxSurfSpec

#}

#//
def flux3(intens, lambdas, cosTheta, phi,
          radius, omegaSini, macroV):
   
    #//console.log("Entering flux3");
    
    #//System.out.println("radius " + radius + " omegaSini " + omegaSini + " macroV " + macroV);
    
    numLams = len(lambdas)
    numThetas = len(cosTheta[0])
    fluxSurfSpec = [ [ 0.0 for i in range(numLams) ] for j in range(2) ]
    #// returns surface flux as a 2XnumLams vector
    #//  - Row 0 linear flux (cgs units)
    #//  - Row 1 log_e flux
    #//  cosTheta is a 2xnumThetas array:
    #// row 0 is used for Gaussian quadrature weights
    #// row 1 is used for cos(theta) values
    #// Gaussian quadrature:
    #// Number of angles, numThetas, will have to be determined after the fact

    """/* Re-sampling makes thing worse - ?? 
//For internal use, interpolate flux spectrum onto uniform fine sampling grid:
   double specRes = 3.0e5; //spectral resolution R = lambda/deltaLambda
   double midLam = lambdas[numLams/2]  * 1.0e7; //nm 
   double delFine = midLam / specRes;  //nm
   double lam1 = lambdas[0] * 1.0e7; //nm
   double lam2 = lambdas[numLams-1] * 1.0e7; //nm;
   double numFineD = (lam2 - lam1) / delFine; 
   int numFine = (int) numFineD - 1;
   double newLambda[] = new double[numFine];
   double newIntens[][] = new double[numFine][numThetas];
   double thisNewIntens[] = new double[numFine];
   double thisIntens[] = new double[numLams];

   //System.out.println("midLam " + midLam + " delFine " + delFine + " lam1 " + lam1 + " lam2 " + lam2 + " numFine " + numFine);
//Create fine wavelength array
   double ilD;
   for (int il = 0; il < numFine; il++){
      ilD = (double) il;
      newLambda[il] = lam1 + ilD*delFine;  //nm
      newLambda[il] = newLambda[il] * 1.0e-7; //cm
   }
   //System.out.println("newLambda[0] " + newLambda[0] + " [numFine-1] " + newLambda[numFine-1]);

   for (int it = 0; it < numThetas; it++){
       for (int il = 0; il < numLams; il++){
          thisIntens[il] = intens[il][it]; 
       } //il loop
       thisNewIntens = ToolBox.interpolV(thisIntens, lambdas, newLambda);
       for (int il = 0; il < numFine; il++){
          newIntens[il][it] = thisNewIntens[il];
       } //il
   } //it loop
    */"""
#//For geometry calculations: phi = 0 is direction of positive x-axis of right-handed
#// 2D Cartesian coord system in plane of sky with origin at sub-stellar point (phi
#// increases CCW)

    #double thisThetFctr;
    #//var numThetas = 11;
    numPhi = len(phi)
    delPhi = 2.0 * math.pi / numPhi
    #//console.log("delPhi " + delPhi);

    #//macroturbulent broadening helpers:
    #double uRnd1, uRnd2, ww, arg, gRnd1, gRnd2;
    #//intializations:
    uRnd1 = 0.0
    uRnd2 = 0.0
    gRnd1 = 0.0
    gRnd2 = 0.0
    arg = 0.0

    #//For macroturbulent broadening, we need to transform uniformly
    #//generated random numbers on [0, 1] to a Gaussian distribution
    #// with a mean of 0.0 and a sigma of 1.0
    #//Use the polar form of the Box-Muller transformation
    #// http://www.design.caltech.edu/erik/Misc/Gaussian.html
    #// Everett (Skip) Carter, Taygeta Scientific Inc.
    #//// Original code in c:
    #//    ww = Math.sqrt
    #//         do {
    #//                 x1 = 2.0 * ranf() - 1.0;
    #//                 x2 = 2.0 * ranf() - 1.0;
    #//                 w = x1 * x1 + x2 * x2;
    #//         } while ( w >= 1.0 );
    #//
    #//         w = sqrt( (-2.0 * log( w ) ) / w );
    #//         y1 = x1 * w;
    #//         y2 = x2 * w;


    #//helpers for rotational broadening
    #double x, opposite, theta; //, delLam;
    thisIntens = [0.0 for i in range(numLams)]
    intensLam = [0.0 for i in range(numLams)]
    #//double[] intensLam = new double[numFine];

    #//This might not be the smartest approach, but, for now, compute the
    #//Doppler shifted wavelength scale across the whole tiled projected disk:

    #// 
    #double sinTheta;
    #//double shiftedLam = 0.0;
    shiftedLamV = [0.0 for i in range(numLams)]
    #//double[] shiftedLamV = new double[numFine];
    vRad = [ [ 0.0 for i in range(numPhi) ] for j in range(numThetas) ]
    #//For each (theta, phi) tile, compute the contributions to radial velocity
    #// from rotational broadening and macoturbulent broadening:
    #//test omegaSini = 0.0; //test
    for it in range(numThetas):
        #//theta = Math.acos(cosTheta[1][it]);
        #//opposite = radius * Math.sin(theta);
        #// Faster??
        sinTheta = math.sqrt( 1.0 - (cosTheta[1][it]*cosTheta[1][it]) )
        opposite = radius * sinTheta
        for ip in range(numPhi):

            #// x-position of each (theta, phi) point:
            #////theta = Math.acos(cosTheta[1][it]);
            #////opposite = radius * Math.sin(theta);
            #//sinTheta = Math.sqrt( 1.0 - (cosTheta[1][it]*cosTheta[1][it]) );
            #//opposite = radius * sinTheta;
            x = opposite * math.cos(phi[ip])
            vRad[it][ip] = x * omegaSini #// should be in cm/s
            #//System.out.println("it " + it + " cosTheta[1][it] " + cosTheta[1][it] + " ip " + ip + " phi[ip] " + (phi[ip]/2.0/Math.PI) + " x/R " + (x/radius) + " vRad " + (vRad[it][ip]/1.0e5));

            #//For macroturbulent broadening, we need to transform uniformly
            #//generated random numbers on [0, 1] to a Gaussian distribution
            #// with a mean of 0.0 and a sigma of 1.0
            #//Use the polar form of the Box-Muller transformation
            #// http://www.design.caltech.edu/erik/Misc/Gaussian.html
            #// Everett (Skip) Carter, Taygeta Scientific Inc.

            #//initialization that guarantees at least one cycle of the while loop
            ww = 2.0;

            #//cycle through pairs of uniform random numbers until we get a
            #//ww value that is less than unity
            while (ww >= 1.0):
                #// range [0, 1]
                uRnd1 = random.random()
                uRnd2 = random.random()
                #// range [-1, 1]
                uRnd1 = (2.0 * uRnd1) - 1.0
                uRnd2 = (2.0 * uRnd2) - 1.0
                ww = (uRnd1 * uRnd1) + (uRnd2 * uRnd2)
  
            #// We have a valid ww value - transform the uniform random numbers
            #// to Gaussian random numbers with sigma = macroturbulent velocity broadening
            arg = (-2.0 * math.log(ww)) / ww
            gRnd1 = macroV * arg * uRnd1
            #//gRnd2 = macroV * arg * uRnd2; //not needed?

            #//console.log("gRnd1 " + gRnd1)
    
            vRad[it][ip] = vRad[it][ip] + gRnd1 #// should be in cm/s

        #} //ip loop - phi
    #} //it loop - theta

    flx = [0.0 for i in range(numLams)]
    #//double[] newFlx = new double[numFine];
    #//Inititalize flux acumulator:
    for il in range(numLams):
    #//for (int il = 0; il < numFine; il++){
        flx[il] = 0.0
      #//newFlx[il] = 0.0;
    
    for it in range(numThetas):

        #//flx = flx + ( intens[it] * cosTheta[1][it] * cosTheta[0][it] ); //axi-symmetric version
        #//non-axi-symmetric version:
        thisThetFctr = cosTheta[1][it] * cosTheta[0][it]
        #//console.log("it " + it + " cosTheta[1] " + cosTheta[1][it] + " cosTheta[0] " + cosTheta[0][it]);
        #//console.log("thisThetFctr " + thisThetFctr);
        for il in range(numLams):
            #//for (int il = 0; il < numFine; il++){
            intensLam[il] = intens[il][it]
            #//intensLam[il] = newIntens[il][it];
        
        for ip in range(numPhi):
            for il in range(numLams):
                #//for (int il = 0; il < numFine; il++){
                #//delLam = lambdas[il] * vRad[it][ip] / Useful.c;
                #//shiftedLamV[il] = lambdas[il] + delLam;
                shiftedLamV[il] = lambdas[il] * ( (vRad[it][ip]/Useful.c()) + 1.0 )
                #//delLam = newLambda[il] * vRad[it][ip] / Useful.c;
                #//shiftedLamV[il] = newLambda[il] + delLam;
                #//shiftedLamV[il] = shiftedLam;
                #//if (il == 1){
                #//System.out.println("it " + it + " cosTheta[1][it] " + cosTheta[1][it] + " ip " + ip + " phi[ip] " + (phi[ip]/2.0/Math.PI) + " vRad[it][ip] " + (vRad[it][ip]/1.0e5));
                #//  System.out.println("it " + it + " ip " + ip + " il " + il + " delLam " + delLam + " shiftedLamV " + shiftedLamV[il] + " intensLam[il] " + intensLam[il]);
                #//}
            #}
            #//for (int il = 0; il < numLams; il++){
            #//   intensLam[il] = intens[il][it];
            #//}
            #thisIntens = ToolBox.interpolV(intensLam, shiftedLamV, lambdas);
            thisIntens = numpy.interp(lambdas, shiftedLamV, intensLam)
            #//thisIntens = ToolBox.interpolV(intensLam, shiftedLamV, newLambda);
            #//flx = flx + ( intens[it] * thisThetFctr * delPhi );
            for il in range(numLams):
                #//for (int il = 0; il < numFine; il++){
                flx[il] = flx[il] + ( thisIntens[il] * thisThetFctr * delPhi )
                #//newFlx[il] = newFlx[il] + ( thisIntens[il] * thisThetFctr * delPhi )
                #//console.log("il " + il + " thisIntens " + thisIntens[il] + " flx " + flx[il]);
           
        #} //ip - phi loop
    #}  // it - theta loop

    #//flx = ToolBox.interpolV(newFlx, newLambda, lambdas);

    #//fluxSurfSpec[0] = 2.0 * Math.PI * flx; //axi-symmetric version
    for il in range(numLams):
        fluxSurfSpec[0][il] = flx[il] #// non-axi-symmetric version
        fluxSurfSpec[1][il] = math.log(fluxSurfSpec[0][il])
    

    return fluxSurfSpec

   