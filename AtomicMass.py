# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:33:22 2017

//Atomic  AND molecular masses in atomic mass units (amu. "mu")

@author: ishort
"""

def getMass(elName):
    
    """//Atomic masses in atomic mass units (amu. "mu")
//From CIAAW
//Atomic weights of the elements 2015 ciaaw.org/atomic-weights.htm, Aug. 2015
//Heaviest element treated is La (57)"""

    elMass = 1.0  #//default initialization

    if ("H" == elName):
       elMass = 1.007
        
    if ("He" == elName):
       elMass  = 4.002
   
    if ("Li" == elName):
       elMass = 6.938
 
    if ("Be" == elName):
       elMass  = 9.012
 
    if ("B" == elName):
       elMass = 10.806
   
    if ("C" == elName):
       elMass = 12.0096
   
    if ("N" == elName):
       elMass = 14.006
 
    if ("O" == elName):
       elMass = 15.999
 
    if ("F" == elName):
       elMass = 18.998
 
    if ("Ne" == elName):
       elMass  = 20.1797
 
    if ("Na" == elName):
       elMass  = 22.989
 
    if ("Mg" == elName):
       elMass  = 24.304
 
    if ("Al" == elName):
       elMass  = 26.981
 
    if ("Si" == elName):
       elMass  = 28.084
 
    if ("P" == elName):
       elMass = 30.973
 
    if ("S" == elName):
       elMass = 32.059
 
    if ("Cl" == elName):
       elMass  = 35.446
 
    if ("Ar" == elName):
       elMass  = 39.948
 
    if ("K" == elName):
       elMass = 39.0983
 
    if ("Ca" == elName):
       elMass  = 40.078
 
    if ("Sc" == elName):
       elMass  = 44.955
 
    if ("Ti" == elName):
       elMass  = 47.867
 
    if ("Va" == elName):
       elMass  = 50.9415
 
    if ("Cr" == elName):
       elMass  = 51.9961
 
    if ("Mn" == elName):
       elMass  = 54.938
 
    if ("Fe" == elName):
       elMass  = 55.845
 
    if ("Co" == elName):
       elMass  = 58.933
 
    if ("Ni" == elName):
       elMass  = 58.6934
 
    if ("Cu" == elName):
       elMass  = 63.546
 
    if ("Zn" == elName):
       elMass  = 65.38
 
    if ("Ga" == elName):
       elMass  = 69.723
 
    if ("Ge" == elName):
       elMass  = 72.630
 
    if ("As" == elName):
       elMass  = 74.921
 
    if ("Se" == elName):
       elMass  = 78.971
 
    if ("Br" == elName):
       elMass  = 79.901
 
    if ("Kr" == elName):
       elMass  = 83.798
 
    if ("Rb" == elName):
       elMass  = 85.4678
 
    if ("Sr" == elName):
       elMass  = 87.62
 
    if ("Y" == elName):
       elMass = 88.905
 
    if ("Zr" == elName):
       elMass  = 91.224
 
    if ("Nb" == elName):
       elMass  = 92.906
 
    if ("Mo" == elName):
       elMass  = 95.95
 
    if ("Ru" == elName):
       elMass  = 101.07
 
    if ("Rh" == elName):
       elMass  = 102.905
 
    if ("Pd" == elName):
       elMass  = 106.42
 
    if ("Ag" == elName):
       elMass  = 107.8682
 
    if ("Cd" == elName):
       elMass  = 112.414
 
    if ("In" == elName):
       elMass  = 114.818
 
    if ("Sn" == elName):
       elMass  = 118.710
 
    if ("Sb" == elName):
       elMass  = 121.760
 
    if ("Te" == elName):
       elMass  = 127.60
 
    if ("I" == elName):
       elMass = 126.904
 
    if ("Xe" == elName):
       elMass  = 131.293
 
    if ("Cs" == elName):
       elMass  = 132.905
 
    if ("Ba" == elName):
       elMass  = 137.327
 
    if ("La" == elName):
       elMass  = 138.905
 
    return elMass; 


#// end of getMass method

#//Molecular masses in atomic mass units (amu. "mu")
def getMolMass(molName):

    molMass = 2.0  #//default initialization (H_2)

    if ("TiO" == molName):
       molMass = getMass("O") + getMass("Ti")
   
    return molMass 

