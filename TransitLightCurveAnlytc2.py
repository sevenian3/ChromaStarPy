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

#
# Compute the analytic light curve in the small-planet approximation of Mandel
# and Agol 2002, Eq. Section 5 ("Analytic Lightcurves for Planetary Transit Searches")
#
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
  o Input parameter "p" defined in Mandel 7 Agol (2002) Section 2
  o intensLam is the 1D monochromatic I_lambda (theta) distribution "sliced" from the
    2D I(lambda, cosTheta) "intens" array in CSPy
    
#Output:
  o 1D vector of transit times corresponding to theta values transited along transit chord

"""

def transLightAnlytc2(intensLam, radius, p, cosTheta, vTrans, iFirstTheta, numTransThetas, impct):
    
    #Safety first:
    
    tiny = numpy.double(1.0e-49)
    logTiny = math.log(tiny)    
    
    #M&A 2002 seems to have a curve with more flux removed than we have:
    #fudge = 2.0/math.pi
    fudge = 2.0

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
    #Mandel & Agol (2002)'s "F" - "relative flux"
    F = [0.0 for i in range(numTransThetas)]

    #for i in range(numTransThetas):
    #    print("i ", i, " intensLam[i] ", intensLam[i])

    
    #test = [0.0 for i in range(numThetas)]
    
    #Parameters for Mandel & Agol (2002) Eq. Sect 5 for relatie flux, their "F":
    #coefficients for Claret (2000)'s four-parameter limb darkening law:
    #A&A 363, 1081
    # From J/A+A/363/1081  
    #http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=J/A+A/363/1081
    #Non-linear limb-darkening law for LTE models (Claret 2000) 2000A&A...363.1081C
    #In order of *increasing* order: c_0 to c_4 (Claret's a_1 to a_4)
    #For 5750/4.5/0.0/1.0 ATLAS9, V band: 
    c = [0.0, 0.5169, -0.0211, 0.6944, -0.3892]
    c[0] = 1.0 - c[1] - c[2] - c[3] - c[4]  
    omegaMA = 0.0
    for n in range(5):
        omegaMA+= c[n] / (n+4)
    #print("omegaMA ", omegaMA)
    
    #thisB = numpy.double(0.0)
    mu = 0.0 #Initialize
    I = 0.0

#Note Mandel & Agol Sect 5 Eq:
#    Istar(z) = 1/(4pz)*Int^z+p_z-p {I(z)2r dr}
#    in case of small planet (p<z): 
#    --> I(z) = constant over range (z-p to z+p) 
#     Istar(z) = I(z) * 4pz/4pz = I(z)
        
    for i in range(0, numTransThetas):
        #print("i ", i)
        #thisTheta = math.acos(cosTheta[1][i+iFirstTheta])
        #test[i+iFirstTheta] = math.exp(logRatio)
        # impact parameter corresponding to this theta, in solar radii:
        #thisB = radius * math.sin(thisTheta)
        # Build Mandel & Agol's "F" from Eq.Sect 5:
        #Test with actual CSPy I(theta) values:
        #F[i] =  1.0 - fudge * ( p**2 * intensLam[i]/(4.0*omegaMA) )
        #With I(theta) from Claret (2000) four paramter limb-darkening law
        # consistent with Mandel & Agol (2002)
        mu = cosTheta[1][i+iFirstTheta]
        I = 1.0 - c[1]*(1-math.sqrt(mu)) - c[2]*(1-mu)\
            - c[3]*(1-math.pow(mu, 1.5)) - c[4]*(1-mu**2) 
        F[i] =  1.0 - fudge * ( p**2 * I/(4.0*omegaMA) )
        #print("i ", i, " F[i] ", F[i])

    return F

