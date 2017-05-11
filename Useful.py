# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:00:20 2017

linear and logarithmic physical constant and conversion factors cgs units

@author: ishort
"""

import math

def c():
    return 2.9979249E+10        #// light speed in vaccuum in cm/s

def sigma():
    return 5.670373E-5   #//Stefan-Boltzmann constant ergs/s/cm^2/K^4
  
def k():
    return 1.3806488E-16          #// Boltzmann constant in ergs/K

def h():
    return 6.62606957E-27         #//Planck's constant in ergs sec

def ee(): 
    return 4.80320425E-10   #//fundamental charge unit in statcoulombs (cgs)

def mE(): 
    return 9.10938291E-28  #//electron mass (g)

def GConst():
    return 6.674e-8         #//Newton's gravitational constant (cgs)

#    //Conversion factors
def amu(): 
    return 1.66053892E-24  #// atomic mass unit in g

def eV(): 
    return 1.602176565E-12  #// eV in ergs

def rSun(): 
    return 6.955e10   #// solar radii to cm

def mSun(): 
    return 1.9891e33  #// solar masses to g

def lSun(): 
    return 3.846e33   #// solar bolometric luminosities to ergs/s

#//Natural logs more useful than base 10 logs - Eg. Formal soln module: 
#// Fundamental constants
def logC(): 
    return math.log(c())
    
def logSigma(): 
    return math.log(sigma())
    
def logK():
    return math.log(k())
    
def logH(): 
    return math.log(h())
    
def logEe():
    return math.log(ee())
     #//Named so won't clash with log_10(e)

def logMe(): 
    return math.log(mE())
        
def logGConst(): 
    return math.log(GConst())
    
#//Conversion factors
def logAmu(): 
    return math.log(amu())
    
def logEv():
    return math.log(eV())
        
def logRSun(): 
    return math.log(rSun())
    
def logMSun(): 
    return math.log(mSun())
    
def logLSun(): 
    return math.log(lSun())


