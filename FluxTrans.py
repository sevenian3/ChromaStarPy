# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:42:58 2017

@author: Ian
"""

import math
import numpy
import random
import numpy
import Useful
import ToolBox

#Returns a vector of reduced fluxes for each angle theta being tannsited by planet


#//
def fluxTrans(intens, flx, lambdas, cosTheta, phi,
          radius, omegaSini, macroV,
             iFirstTheta, numTransThetas, rPlanet):
    #print("iFirstTheta ", iFirstTheta, " numTransThetas ", numTransThetas,\
    #      " rPlanet ", rPlanet)
   
    #//console.log("Entering flux3");
    
    #//System.out.println("radius " + radius + " omegaSini " + omegaSini + " macroV " + macroV);

    logTiny = -49.0
    tiny = math.exp(logTiny)
    
    numLams = len(lambdas)
    numThetas = len(cosTheta[0])
    fluxTransSpec = [ [ [ numpy.double(0.0) for i in range(numTransThetas) ] for k in range(numLams) ] for j in range(2) ]
    #Earth-radii to solar radii:
    rPlanet = numpy.double(rPlanet)
    rPlanet = rPlanet * Useful.rEarth() / Useful.rSun()
    
    #dPlanet = 2.0 * rPlanet
    #print("dPlanet ", dPlanet)

    #subtract off flux eclipsed by transiting planet:
    #thisImpct = rPlanet  #Default
    ##Can it really be this simple??:
    logOmega = numpy.double(2.0) * ( math.log(rPlanet) - math.log(radius) )
    omega = math.pi * math.exp(logOmega)
    #print("omega ", omega)
    helper = 0.0
    logHelper = 0.0

    for it in range(iFirstTheta, numThetas):

        for il in range(numLams):
 
            #Subtracting the very small from the very large - let's be sophisticated about it:
            logHelper = math.log(intens[il][it]) + logOmega - flx[1][il]
            helper = numpy.double(1.0) - math.exp(logHelper)
            #if (fluxTransSpec[0][il][it-iFirstTheta] > tiny):
            fluxTransSpec[1][il][it-iFirstTheta] = flx[1][il] + math.log(helper) 
            #if (il == 150):
            #    print("logHelper ", logHelper, " helper ", helper, " logFluxTransSpec ", logFluxTransSpec)
            fluxTransSpec[0][il][it-iFirstTheta] = math.exp(fluxTransSpec[1][il][it-iFirstTheta])
            #if (il == 150):            
            #    print("fluxTransSpec 2 ", fluxTransSpec[0][il][it-iFirstTheta])
                
        #plt.plot(cosTheta[1][iFirstTheta: iFirstTheta+numTransThetas],\
        #         )

    return fluxTransSpec

   