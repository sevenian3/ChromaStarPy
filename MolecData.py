# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:53:32 2017

@author: ishort
"""

#//Various diatomic molecular transition data needed for the 
#//Just-overlapping-line-approximation (JOLA)
#// to molecular band opacity

#//Input SYSTEM is a string with both the molecular species AND the band "system"


import math


def getSqTransMoment(system):

    """//Input SYSTEM is a string with both the molecular species AND the band "system"
// Electronic transition moment, Re, needed for "Line strength", S = |R_e|^2*q_v'v" or just |R_e|^2
// //Allen's Astrophysical quantities, 4.12.2 - 4.13.1  
// // ROtational & vibrational constants for TiO states:, p. 87, Table 4.17"""
    
    #// Square electronic transition moment, |Re|^2, 
    #// needed for "Line strength", S = |R_e|^2*q_v'v" or just |R_e|^2
    #// // //Allen's Astrophysical quantities, 4.12.2 - 4.13.1
    #// As of Feb 2017 - try the band-head value R_00^2 from last column of table:
    RSqu = 0.0 #//default initialization

    if ("TiO_C3Delta_X3Delta" == system):
        RSqu = 0.84
       
    if ("TiO_c1Phi_a1Delta" == system):
        RSqu = 4.63
       
    if ("TiO_A3Phi_X3Delta" == system):
         RSqu = 5.24

#//
    return RSqu

#}  //end of method getSqTransMoment 


def getRotConst(system):


    """// vibrational constant, B (cm^-1): // ??? what is this??? 
    // //Allen's Astrophysical quantities, p. 87, Table 4.17
    //"""
    #// Feb 2017 - Problem:
    #// Eq. 1 of Zeidler & Koester 1982 1982A&A...113..173Z
    #// suggests that "B" is a vibrational E-level constant
    #// BUT: Allens Astrop. Quant., 4th Ed.,  p. 45 has
    #// "B_e & alpha_e" as *rotational* constants and
    #// 'omega_e" and "omega_e*x_e" as vibrational constants
    #// and "T_0" as electronic energy, all in cm^-1
    #// I dunno - assume we want Allen's "B_e" values from Table 4.17  
    #// values for now - I don'r really know what's going on in Zeidler & Koester 82

    B = [0.0 for i in range(2)]
    B[1] = 0.0 #//Blow = B" - upper vibrational level 
    B[0] = 0.0 #//Bup = B' - lower vibrational level

   
    #// I dunno - assume we want Allen's "B_e" values from Table 4.17  
    #// values for now - I don'r really know what's going on in Zeidler & Koester 82
    #// units: cm^-1
    #//
    #// Generally: Higher vibrational states have *smaller* B values
    if ("TiO_C3Delta_X3Delta" == system):
        B[1] = 0.489888 #// upper
        B[0] = 0.535431 #//lower
      
    if ("TiO_c1Phi_a1Delta" == system):
        B[1] = 0.500000 #// upper - NO DATA in Allen - make up a value for now (that's right!)
        B[0] = 0.537602 #//lower 
      
    if ("TiO_A3Phi_X3Delta" == system):
        B[1] = 0.507390 #// upper
        B[0] = 0.535431 #//lower
       

    """/*
// Okay - try the omega_e values in Allen's Table 4.17
// units: cm^-1 - no!
      if ("TiO_C3Delta_X3Delta".equals(system)){
         B[1] = 838.2567; // upper
         B[0] = 1009.1697; //lower
      }
      if ("TiO_c1Phi_a1Delta".equals(system)){
         B[1] = 1018.273; // lower??
         B[0] = 1150.0; //lower NO DATA in Allen - make up a value for now (that's right!)
      }
      if ("TiO_A3Phi_X3Delta".equals(system)){
         B[1] = 867.7799; // upper 
         B[0] = 1009.1697;; //lower
       }
*/"""
#//
    return B

#}  //end of method getRotConst


def getWaveRange(system):


    #// vibrational constant, B: // ??? what is this??? 
    #// //Allen's Astrophysical quantities, p. 87, Table 4.17

    lambda2 = [0.0 for i in range(2)]
    lambda2[1] = 0.0 #// upper end of approx wavelength range of band (nm)  
    lambda2[0] = 0.0 #// lower end of approx wavelength range of band (nm)
   

    if ("TiO_C3Delta_X3Delta" == system):
        lambda2[0] = 405.0
        lambda2[1] = 630.0
      
    if ("TiO_c1Phi_a1Delta" == system):
        lambda2[0] = 490.0
        lambda2[1] = 580.0
      
    if ("TiO_A3Phi_X3Delta" == system):
        lambda2[0] = 570.0
        lambda2[1] = 865.0
       

#//
    return lambda2

#}  //end of method getWaveRange

def getQuantumS(system):

    #//This is "script S" from Alles 4th Ed. p. 88 - Eq. for line strength, S
    #//Computed from a Wigner 6-j symbols - ??
    #//Here we tune the values by hand to make the band strengths look right
    #// - I just don't have the molecular data, or knowledge to use it, that I need
    #// Can anyone out there help, or am I really on my own??

    jolaQuantumS = 1.0 #//default for a multiplicative factor

    if ("TiO_C3Delta_X3Delta" == system):
        jolaQuantumS = 1.0e-14

    if ("TiO_c1Phi_a1Delta" == system):
        jolaQuantumS = 1.0e-14
      
    if ("TiO_A3Phi_X3Delta" == system):
        jolaQuantumS = 1.0e-14
      

    return jolaQuantumS

#} //end method getQuantumS


def getOrigin(system):

    #// Wavenumber of band origin, omega_0 (cm^-1)
    #// //Allen's Astrophysical quantities, p. 91, Table 4.18

    nu00 = 0.0 #//

    if ("TiO_C3Delta_X3Delta" == system):
        nu00 = 19341.7
      
    if ("TiO_c1Phi_a1Delta" == system):
        nu00 = 17840.6
      
    if ("TiO_A3Phi_X3Delta" == system):
        nu00 = 14095.9
       

#//Return frequency:
#  //no!  double omega00 = Useful.c * nu00;
    return nu00

#}  //end of method getOrigin
