# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:10:06 2017

@author: ishort
"""

import math
import Useful
import AtomicMass

def massDensity(numDeps, temp, press, mmw, zScale):

    """Solves the equation of state (EOS) for the mass density (rho) given total
 * pressure from HSE solution, for a mixture of ideal gas particles and photons
 *
 * Need to assume a mean molecular weight structure, mu(Tau)
  """
    
    logE = math.log10(math.e) #// for debug output

    #//press is a 4 x numDeps array:
    #// rows 0 & 1 are linear and log *gas* pressure, respectively
    #// rows 2 & 3 are linear and log *radiation* pressure
    #// double c = 9.9989E+10; // light speed in vaccuum in cm/s
    #// double sigma = 5.670373E-5;   //Stefan-Boltzmann constant ergs/s/cm^2/K^4   
    #//Row 0 of mmwNe is Mean molecular weight in amu
    k = Useful.k()
    logK = Useful.logK()
    amu = Useful.amu()
    logAmu = Useful.logAmu()
    #double logMuAmu

#//System.out.println("STATE: logK " + logK + " logMuAmu " + logMuAmu);
    rho = [[0.0 for i in range(numDeps)] for j in range(2)]

    #// Declare scatch variables:
    #// double logPrad, pRad, pGas, logPgas;
    for i in range(numDeps):

        logMuAmu = math.log(mmw[i]) + logAmu

        #// Compute LTE bolometric radiation contribution to total HSE pressure
        #//logPrad = radFac + 4.0*temp[1][i] ;
        #//pRad = Math.exp(logPrad);
        #//pGas = press[0][i] - pRad;
        #//logPgas = Math.log(pGas);
        rho[1][i] = press[1][i] - temp[1][i] + (logMuAmu - logK)
        rho[0][i] = math.exp(rho[1][i])
        #//System.out.println("i " + i + " press[1] " + logE * press[1][i] + " mmw[i] " + mmw[i] + " rho " + logE * rho[1][i]);
        #//System.out.println("temp " + temp[0][i] + " rho " + rho[0][i]);
        

    return rho

def mmwFn(numDeps, temp, zScale):

    #// mean molecular weight in amu 
        
    mmw = [0.0 for i in range(numDeps)]
    #double logMu, logMuN, logMuI, logTempN, logTempI;

    #// Carrol & Ostlie 2nd Ed., p. 293: mu_N = 1.3, mu_I = 0.62
    logMuN = math.log(1.3)
    logMuI = math.log(0.62)
    logTempN = math.log(4000.0) #// Teff in K for fully neutral gas?
    logTempI = math.log(10000.0) #// Teff in K for *Hydrogen* fully ionized?

    #//System.out.println("temp   logNe   mu");
    for id in range(numDeps):

        #//Give mu the same temperature dependence as 1/Ne between the fully neutral and fully ionized limits?? - Not yet! 
        if (temp[1][id] < logTempN):
            mmw[id] = math.exp(logMuN)
        elif ((temp[1][id] > logTempN) and (temp[1][id] < logTempI)): 
            logMu = logMuN + ((temp[1][id] - logTempN) / (logTempI - logTempN)) * (logMuI - logMuN)
            #//Mean molecular weight in amu
            mmw[id] = math.exp(logMu)
        else:
            mmw[id] = math.exp(logMuI)
            
        
    return mmw

def getNz(numDeps, temp, pGas, pe, ATot, nelemAbnd, logAz):

   #double[][] logNz = new double[nelemAbnd][numDeps];
   logNz = [ [0.0 for i in range(numDeps)] for j in range(nelemAbnd) ]
   
   logATot = math.log(ATot)

   #double help, logHelp, logNumerator;
   
   for i in range(numDeps):

 #// Initial safety check to avoid negative logNz as Pg and Pe each converge:
 #// maximum physical Pe is about 0.5*PGas (complete ionization of pure H): 
       if (pe[0][i] > 0.5 * pGas[0][i]):
           pe[0][i] = 0.5 * pGas[0][i]
           pe[1][i] = math.log(pe[0][i])
      
 #// H (Z=1) is a special case: N_H(tau) = (Pg(tau)-Pe(tau))/{kTk(tau)A_Tot}
       logHelp = pe[1][i] - pGas[1][i]
       help = 1.0 - math.exp(logHelp)
       logHelp = math.log(help)
       logNumerator = pGas[1][i] + logHelp 
       logNz[0][i] = logNumerator - Useful.logK() - temp[1][i] - logATot

#// Remaining elements:
       for j in range(nelemAbnd):
          #// N_z = A_z * N_H:
           logNz[j][i] = logAz[j] + logNz[0][i]
       
   return logNz 

def massDensity2(numDeps, nelemAbnd, logNz, cname):
   
    rho = [[0.0 for i in range(numDeps)] for j in range(2)]

    #double logAddend, addend;
    lAmu = Useful.logAmu()

#//Prepare log atomic masses once for each element:
    logAMass = [0.0 for i in range(nelemAbnd)]
    for j in range(nelemAbnd):
        logAMass[j] = math.log(AtomicMass.getMass(cname[j]))
        #//System.out.println("j " + j + " logAMass " + logAMass[j]);
     
    for i in range(numDeps):

        rho[0][i] = 0.0
        for j in range(nelemAbnd):
            logAddend = logNz[j][i] + lAmu + logAMass[j]
            rho[0][i] = rho[0][i] + math.exp(logAddend) 
            rho[1][i] = math.log(rho[0][i])
            
    return rho  
