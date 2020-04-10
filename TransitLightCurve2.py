# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:06:03 2020

@author: iansh


"""

import math
import numpy
import Useful
#import sys

import matplotlib.pyplot as plt

"""
# Reads in planetary system parameters for a single planet around a single star
#and computes the impact parameter and time coordinate of snapshots
# corresponding to the Gauss-Legendre quadrature as the planet transits the star
#in the stellar atmosphere coordinate system

#Integrated transit solution with stellar atmosphere and radiative tranfer code
#  :: transit light curve entirely due to specific intensity variation across
#   projected disk of background star
#  - ie. No limb darkening coefficient (LDC) parameterization!

Assumptions:
    o Planet's transit path is a chord (not an arc)
     :: equal intevals of length along chord --> equal intervals of transit time
         - okay if r_orbit >> R_star
    o Eclipsed intensity (I) does not vary as a function of position across the 
       projected disk of the planet
         - okay if R_planet << R_star
    o Planet's orbit is circular and centered on centre of star
    o Planet's intensity is 0
    o Ingress and egress excluded 
    
    - All light variation will be from background stellar intensity
        variation across projected stellar disk
    - Okay if r_planet << R_star - ??
         
#Input:
  o radius = radius of star (R_Sun)
     - NOTE: already fixed by stellar parameters massStar and grav
  o cosTheta - 2D array [2 x numThetas] - 2nd row is grid of cosTheta values in 
     stellar atmosphere coord system from main program
  o vTrans - velocity of planet's transit motion projected to surface of star
    
#Output:
  o 1D vector of transit times corresponding to theta values transited along transit chord

"""

def TransLight2(radius, cosTheta, vTrans, iFirstTheta, numTransThetas, impct):
    
    #Safety first:
    
    tiny = numpy.double(1.0e-49)
    logTiny = math.log(tiny)    
    

    if (impct >= radius):
        #There is no eclipse (transit)
        return
    #thetaMinRad is also the minimum theta of the eclipse path chord, in RAD
    thetaMinRad =  math.asin(impct/radius)
    #cos(theta) *decreases* with increasing theta in Quadrant I:
    cosThetaMax = math.cos(thetaMinRad)
    
    
    #Compute array of distances traveled, r, along semi-chord from position of
    #minimum impact parameter
    #12D array of length number-of-eclipse-thetas
    transit = [0.0 for i in range(numTransThetas)]
    #test = [0.0 for i in range(numThetas)]
    
    
    thisImpct = numpy.double(0.0)

    
    for i in range(numTransThetas):
        #print("i ", i)
        thisTheta = math.acos(cosTheta[1][i+iFirstTheta])
        thisImpct = radius * math.sin(thisTheta)
        #test[i+iFirstTheta] = math.exp(logRatio)
        # impact parameter corresponding to this theta:
        thisB = radius * math.sin(thisTheta)
        # linear distance travelled along transit semi-path in solar radii
        transit[i] = math.sqrt(thisB**2 - impct**2)
        transit[i] = transit[i]*Useful.rSun() #RSun to cm
        #row 1 is Times at which successive annuli are eclipsed, in s:
        #Ephemeris zero point at transit mid-point  
        transit[i] = transit[i]/vTrans
        #print("i ", i, " i+iFirstTheta ", i+iFirstTheta, " transit[1] ", transit[1][i+iFirstTheta])

    return transit

        
    
    
    
    
    
     
     