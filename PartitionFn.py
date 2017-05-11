# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:12:02 2017

@author: ishort
"""

import math

def getPartFn(species):

    """// Partition functions at two temperatures (5000 K and 10000 K)
//From Allen's Astrophysical Quantities, 4th Ed. 
// CAUTION: Return Base 10 log10 of partition fn"""

#//Ionization stages that don't exist (eg. "HIII") are given dummy values of 0.0;

#// CAUTION: log10 base 10!!
    log10PartFn = [0.0 for i in range(2)] 
    
    #//default initialization
    log10PartFn[0] = 0.0 # //for theta = 5040.0/T = 1.0
    log10PartFn[1] = 0.0 # //for theta = 5040.0/T = 0.5

    if ("HI" == species):
         log10PartFn[0] = 0.30
         log10PartFn[1] = 0.30

    if ("HII" == species):
         log10PartFn[0] = 0.0  #//dummy
         log10PartFn[1] = 0.0   #//dummy

    if ("HIII" == species):
         log10PartFn[0] = 0.0   #//dummy
         log10PartFn[1] = 0.0   #//dummy

    if ("HIV" == species):
         log10PartFn[0] = 0.0   #//dummy
         log10PartFn[1] = 0.0   #//dummy

    if ("HV" == species):
         log10PartFn[0] = 0.0   #//dummy
         log10PartFn[1] = 0.0   #//dummy
       
    if ("HVI" == species):
         log10PartFn[0] = 0.0   #//dummy
         log10PartFn[1] = 0.0   #//dummy
       
    if ("HeI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("HeII" == species):
         log10PartFn[0] = 0.30
         log10PartFn[1] = 0.30

    if ("HeIII" == species):
         log10PartFn[0] = 0.0  #//dummy 
         log10PartFn[1] = 0.0  #//dummy 
           
    if ("HeIV" == species):
         log10PartFn[0] = 0.0  #//dummy 
         log10PartFn[1] = 0.0  #//dummy 
           
    if ("HeV" == species):
         log10PartFn[0] = 0.0   #//dummy 
         log10PartFn[1] = 0.0   #//dummy 
           
    if ("HeVI" == species):
         log10PartFn[0] = 0.0  #//dummy 
         log10PartFn[1] = 0.0  #//dummy 
           
    if ("LiI" == species):
         log10PartFn[0] = 0.32
         log10PartFn[1] = 0.49

    if ("LiII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("LiIII" == species):
         log10PartFn[0] = math.log10(2.0)  
         log10PartFn[1] = math.log10(2.0)

    if ("LiIV" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("LiV" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("LiVI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("BeI" == species):
         log10PartFn[0] = 0.01
         log10PartFn[1] = 0.13

    if ("BeII" == species):
         log10PartFn[0] = 0.30
         log10PartFn[1] = 0.30

    if ("BeIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] = math.log10(1.0)

    if ("BeIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BeV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BeVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BI" == species):
         log10PartFn[0] = 0.78
         log10PartFn[1] =  0.78

    if ("BII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("BIII" == species):
         log10PartFn[0] = math.log10(2.0)
         log10PartFn[1] = math.log10(2.0)

    if ("BIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CI" == species):
         log10PartFn[0] = 0.97
         log10PartFn[1] = 1.0

    if ("CII" == species):
         log10PartFn[0] = 0.78
         log10PartFn[1] = 0.78

    if ("CIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] = math.log10(1.0)

    if ("CIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] = 0.0

    if ("CV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] = 0.0

    if ("CVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] = 0.0

    if ("NI" == species):
         log10PartFn[0] = 0.61
         log10PartFn[1] = 0.66

    if ("NII" == species):
         log10PartFn[0] = 0.95
         log10PartFn[1] = 0.97

    if ("NIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] = math.log10(6.0)

    if ("NIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("OI" == species):
         log10PartFn[0] = 0.94
         log10PartFn[1] = 0.97

    if ("OII" == species):
         log10PartFn[0] = 0.60
         log10PartFn[1] = 0.61

    if ("OIII" == species):
         log10PartFn[0] = math.log10(9.0)
         log10PartFn[1] = math.log10(9.0)

    if ("OIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("OV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("OVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FI" == species):
         log10PartFn[0] = 0.75
         log10PartFn[1] =  0.77

    if ("FII" == species):
         log10PartFn[0] = 0.92
         log10PartFn[1] = 0.94

    if ("FIII" == species):
         log10PartFn[0] = math.log10(4.0)
         log10PartFn[1] = math.log10(4.0)

    if ("FIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NeI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("NeII" == species):
         log10PartFn[0] = 0.73
         log10PartFn[1] = 0.75

    if ("NeIII" == species):
         log10PartFn[0] = math.log10(9.0)
         log10PartFn[1] = math.log10(9.0)

    if ("NeIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NeV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NeVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NaI" == species):
         log10PartFn[0] = 0.31
         log10PartFn[1] = 0.60

    if ("NaII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("NaIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] =  math.log10(6.0)

    if ("NaIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NaV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NaVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MgI" == species):
         log10PartFn[0] = 0.01
         log10PartFn[1] = 0.15

    if ("MgII" == species):
         log10PartFn[0] = 0.31
         log10PartFn[1] = 0.31

    if ("MgIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("MgIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MgV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MgVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("AlI" == species):
         log10PartFn[0] = 0.77
         log10PartFn[1] = 0.81

    if ("AlII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.01

    if ("AlIII" == species):
         log10PartFn[0] = math.log10(2.0)
         log10PartFn[1] =  math.log10(2.0)

    if ("AlIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("AlV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("AlVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SiI" == species):
         log10PartFn[0] = 0.98
         log10PartFn[1] = 1.04

    if ("SiII" == species):
         log10PartFn[0] = 0.76
         log10PartFn[1] = 0.77

    if ("SiIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("SiIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SiV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SiVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("PI" == species):
         log10PartFn[0] = 0.65
         log10PartFn[1] = 0.79

    if ("PII" == species):
         log10PartFn[0] = 0.91
         log10PartFn[1] = 0.94

    if ("PIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] =  math.log10(6.0)

    if ("PIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("PV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("PVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SI" == species):
         log10PartFn[0] = 0.91
         log10PartFn[1] = 0.94

    if ("SII" == species):
         log10PartFn[0] = 0.62
         log10PartFn[1] = 0.72

    if ("SIII" == species):
         log10PartFn[0] = math.log10(9.0)
         log10PartFn[1] =  math.log10(9.0)

    if ("SIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ClI" == species):
         log10PartFn[0] = 0.72
         log10PartFn[1] = 0.75

    if ("ClII" == species):
         log10PartFn[0] = 0.89
         log10PartFn[1] = 0.92

    if ("ClIII" == species):
         log10PartFn[0] = math.log10(4.0)
         log10PartFn[1] =  math.log10(4.0)

    if ("ClIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ClV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ClVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ArI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("ArII" == species):
         log10PartFn[0] = 0.69
         log10PartFn[1] = 0.71

    if ("ArIII" == species):
         log10PartFn[0] = math.log10(9.0)
         log10PartFn[1] =  math.log10(9.0)

    if ("ArIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ArV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ArVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KI" == species):
         log10PartFn[0] = 0.34
         log10PartFn[1] = 0.60

    if ("KII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("KIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] =  math.log10(6.0)

    if ("KIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CaI" == species):
         log10PartFn[0] = 0.07
         log10PartFn[1] = 0.55

    if ("CaII" == species):
         log10PartFn[0] = 0.34
         log10PartFn[1] = 0.54

    if ("CaIII" == species):
       log10PartFn[0] =  math.log10(1.0)
       log10PartFn[1] =  math.log10(1.0)

    if ("CaIV" == species):
       log10PartFn[0] = 0.00
       log10PartFn[1] = 0.00

    if ("CaV" == species):
       log10PartFn[0] = 0.00
       log10PartFn[1] = 0.00

    if ("CaVI" == species):
       log10PartFn[0] = 0.00
       log10PartFn[1] = 0.00

    if ("ScI" == species):
         log10PartFn[0] = 1.08
         log10PartFn[1] = 1.49

    if ("ScII" == species):
         log10PartFn[0] = 1.36
         log10PartFn[1] = 1.52

    if ("ScIII" == species):
         log10PartFn[0] = math.log10(10.0)
         log10PartFn[1] =  math.log10(10.0)

    if ("ScIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ScV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ScVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("TiI" == species):
         log10PartFn[0] = 1.48
         log10PartFn[1] = 1.88

    if ("TiII" == species):
         log10PartFn[0] = 1.75
         log10PartFn[1] = 1.92

    if ("TiIII" == species):
         log10PartFn[0] = math.log10(21.0)
         log10PartFn[1] =  math.log10(21.0)

    if ("TiIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("TiV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("TiVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("VI" == species):
         log10PartFn[0] = 1.62
         log10PartFn[1] = 2.03

    if ("VII" == species):
         log10PartFn[0] = 1.64
         log10PartFn[1] = 1.89

    if ("VIII" == species):
         log10PartFn[0] = math.log10(28.0)
         log10PartFn[1] =  math.log10(28.0)

    if ("VIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("VV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("VVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CrI" == species):
         log10PartFn[0] = 1.02
         log10PartFn[1] = 1.51

    if ("CrII" == species):
         log10PartFn[0] = 0.86
         log10PartFn[1] = 1.22

    if ("CrIII" == species):
         log10PartFn[0] = math.log10(25.0)
         log10PartFn[1] =  math.log10(25.0)

    if ("CrIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CrV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CrVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MnI" == species):
         log10PartFn[0] = 0.81
         log10PartFn[1] = 1.16

    if ("MnII" == species):
         log10PartFn[0] = 0.89
         log10PartFn[1] = 1.13

    if ("MnIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] =  math.log10(6.0)

    if ("MnIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MnV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("MnVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FeI" == species):
         log10PartFn[0] = 1.43
         log10PartFn[1] = 1.74

    if ("FeII" == species):
         log10PartFn[0] = 1.63
         log10PartFn[1] = 1.80

    if ("FeIII" == species):
         log10PartFn[0] = math.log10(25.0)
         log10PartFn[1] =  math.log10(25.0)

    if ("FeIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FeV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("FeVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CoI" == species):
         log10PartFn[0] = 1.52
         log10PartFn[1] = 1.76

    if ("CoII)" == species):
         log10PartFn[0] = 1.46
         log10PartFn[1] = 1.66

    if ("CoIII" == species):
         log10PartFn[0] = math.log10(28.0)
         log10PartFn[1] =  math.log10(28.0)

    if ("CoIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CoV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CoVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NiI" == species):
         log10PartFn[0] = 1.47
         log10PartFn[1] = 1.60

    if ("NiII" == species):
         log10PartFn[0] = 1.02
         log10PartFn[1] = 1.28

    if ("NiIII" == species):
         log10PartFn[0] = math.log10(21.0)
         log10PartFn[1] =  math.log10(21.0)

    if ("NiIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NiV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NiVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CuI" == species):
         log10PartFn[0] = 0.36
         log10PartFn[1] = 0.58

    if ("CuII" == species):
         log10PartFn[0] = 0.01
         log10PartFn[1] = 0.18

    if ("CuIII" == species):
         log10PartFn[0] = math.log10(10.0)
         log10PartFn[1] =  math.log10(10.0)

    if ("CuIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CuV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CuVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZnI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.03

    if ("ZnII" == species):
        log10PartFn[0] = 0.30
        log10PartFn[1] = 0.30

    if ("ZnIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("ZnIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZnV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZnVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("GaI" == species):
         log10PartFn[0] = 0.73
         log10PartFn[1] = 0.77

    if ("GaII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("GaIII" == species):
         log10PartFn[0] = math.log10(2.0)
         log10PartFn[1] =  math.log10(2.0)

    if ("GaIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("GaV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("GaVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KrI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("KrII" == species):
         log10PartFn[0] = 0.62
         log10PartFn[1] = 0.66

    if ("KrIII" == species):
         log10PartFn[0] = math.log10(9.0)
         log10PartFn[1] =  math.log10(9.0)

    if ("KrIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KrV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("KrVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("RbI" == species):
         log10PartFn[0] = 0.36
         log10PartFn[1] = 0.70

    if ("RbII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("RbIII" == species):
         log10PartFn[0] = math.log10(6.0)
         log10PartFn[1] =  math.log10(6.0)

    if ("RbIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("RbV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("RbVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SrI" == species):
         log10PartFn[0] = 0.10
         log10PartFn[1] = 0.70

    if ("SrII" == species):
         log10PartFn[0] = 0.34
         log10PartFn[1] = 0.53

    if ("SrIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("SrIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SrV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("SrVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("YI" == species):
         log10PartFn[0] = 1.08
         log10PartFn[1] = 1.50

    if ("YII" == species):
         log10PartFn[0] = 1.18
         log10PartFn[1] = 1.41

    if ("YIII" == species):
         log10PartFn[0] = math.log10(10.0)
         log10PartFn[1] =  math.log10(10.0)

    if ("YIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("YV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("YVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZrI" == species):
         log10PartFn[0] = 1.53
         log10PartFn[1] = 1.99

    if ("ZrII" == species):
         log10PartFn[0] = 1.66
         log10PartFn[1] = 1.91

    if ("ZrIII" == species):
         log10PartFn[0] = math.log10(21.0)
         log10PartFn[1] =  math.log10(21.0)

    if ("ZrIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZrV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("ZrVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NbI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00;

    if ("NbII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("NbIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("NbIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NbV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("NbVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CsI" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("CsII" == species):
         log10PartFn[0] = 0.00
         log10PartFn[1] = 0.00

    if ("CsIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("CsIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CsV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("CsVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BaI" == species):
         log10PartFn[0] = 0.36
         log10PartFn[1] = 0.92

    if ("BaII" == species):
         log10PartFn[0] = 0.62
         log10PartFn[1] = 0.85

    if ("BaIII" == species):
         log10PartFn[0] = math.log10(1.0)
         log10PartFn[1] =  math.log10(1.0)

    if ("BaIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BaV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("BaVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("LaI" == species):
         log10PartFn[0] = 1.41
         log10PartFn[1] = 1.85

    if ("LaII" == species):
         log10PartFn[0] = 1.47
         log10PartFn[1] = 1.71

    if ("LaIII" == species):
         log10PartFn[0] =  math.log10(10.0)
         log10PartFn[1] =  math.log10(10.0)

    if ("LaIV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("LaV" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0

    if ("LaVI" == species):
         log10PartFn[0] = 0.0
         log10PartFn[1] =  0.0


#//
    return log10PartFn

#}  //end of method getPartFn    


def getMolPartFn(species):

    """// Diatomic Partition fn values, QAB, from 
    //http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A+A/588/A96 
    //See: Barklem, P. S.; Collet, R., 2016, Astronomy & Astrophysics, Volume 588, id.A96 """

#//Just do linear piecewise interpolation in log of to hottest five values for now:

    logPartFn = [0.0 for i in range(5)]
    #//default initialization
    logPartFn[0] = 0.0  #//for T = 130 K
    logPartFn[1] = 0.0  #//for T = 500 K
    logPartFn[2] = 0.0  #//for T = 3000 K
    logPartFn[3] = 0.0  #//for T = 8000 K
    logPartFn[4] = 0.0  #//for T = 10000 K


    if ("H2" == species):
         logPartFn[0] = math.log(8.83429e-01)
         logPartFn[1] = math.log(3.12970e+00)
         logPartFn[2] = math.log(2.22684e+01)
         logPartFn[3] = math.log(1.24852e+02)
         logPartFn[4] = math.log(1.94871e+02)


    if ("C2" == species):
         logPartFn[0] = math.log(2.53157e+01)
         logPartFn[1] = math.log(2.08677e+02)
         logPartFn[2] = math.log(6.75852e+03)
         logPartFn[3] = math.log(6.15554e+04)
         logPartFn[4] = math.log(1.07544e+05)


    if ("N2" == species):
         logPartFn[0] = math.log(2.28805e+01)
         logPartFn[1] = math.log(8.76988e+01)
         logPartFn[2] = math.log(7.89979e+02)
         logPartFn[3] = math.log(4.32734e+03)
         logPartFn[4] = math.log(6.68047e+03)


    if ("O2" == species):
         logPartFn[0] = math.log(9.78808e+01)
         logPartFn[1] = math.log(3.70966e+02)
         logPartFn[2] = math.log(4.34427e+03)
         logPartFn[3] = math.log(3.30098e+04)
         logPartFn[4] = math.log(5.76869e+04)


    if ("H2+" == species):
         logPartFn[0] = math.log(3.40918e+00)
         logPartFn[1] = math.log(1.21361e+01)
         logPartFn[2] = math.log(1.16205e+02)
         logPartFn[3] = math.log(7.56297e+02)
         logPartFn[4] = math.log(1.18728e+03)


    if ("CH" == species):
         logPartFn[0] = math.log(3.13181e+01)
         logPartFn[1] = math.log(1.03985e+02)
         logPartFn[2] = math.log(9.04412e+02)
         logPartFn[3] = math.log(6.99662e+03)
         logPartFn[4] = math.log(1.22732e+04)


    if ("NH" == species):
         logPartFn[0] = math.log(1.76430e+01)
         logPartFn[1] = math.log(6.50991e+01)
         logPartFn[2] = math.log(5.20090e+02)
         logPartFn[3] = math.log(3.35774e+03)
         logPartFn[4] = math.log(5.85785e+03)


    if ("OH" == species):
         logPartFn[0] = math.log(2.54704e+01)
         logPartFn[1] = math.log(8.07652e+01)
         logPartFn[2] = math.log(5.77700e+02)
         logPartFn[3] = math.log(3.11647e+03)
         logPartFn[4] = math.log(5.02698e+03)


    if ("MgH" == species):
         logPartFn[0] = math.log(3.22349e+01)
         logPartFn[1] = math.log(1.24820e+02)
         logPartFn[2] = math.log(1.69231e+03)
         logPartFn[3] = math.log(1.72862e+04)
         logPartFn[4] = math.log(3.16394e+04)


    if ("CaH" == species):
         logPartFn[0] = math.log(4.34133e+01)
         logPartFn[1] = math.log(1.69692e+02)
         logPartFn[2] = math.log(2.33105e+03)
         logPartFn[3] = math.log(2.24220e+04)
         logPartFn[4] = math.log(4.33139e+04)


    if ("CN" == species):
         logPartFn[0] = math.log(9.62592e+01)
         logPartFn[1] = math.log(3.69706e+02)
         logPartFn[2] = math.log(3.65207e+03)
         logPartFn[3] = math.log(2.59277e+04)
         logPartFn[4] = math.log(4.43257e+04)


    if ("CO" == species):
         logPartFn[0] = math.log(4.73391e+01)
         logPartFn[1] = math.log(1.81659e+02)
         logPartFn[2] = math.log(1.71706e+03)
         logPartFn[3] = math.log(9.67381e+03)
         logPartFn[4] = math.log(1.50689e+04)


    if ("NO" == species):
         logPartFn[0] = math.log(1.38024e+02)
         logPartFn[1] = math.log(7.06108e+02)
         logPartFn[2] = math.log(8.21159e+03)
         logPartFn[3] = math.log(4.97309e+04)
         logPartFn[4] = math.log(7.94214e+04)


    if ("FeO" == species):
         logPartFn[0] = math.log(1.85254e+03)
         logPartFn[1] = math.log(7.52666e+03)
         logPartFn[2] = math.log(1.23649e+05)
         logPartFn[3] = math.log(9.55089e+05)
         logPartFn[4] = math.log(1.58411e+06)

 
    if ("SiO" == species):
         logPartFn[0] = math.log(1.25136e+02)
         logPartFn[1] = math.log(4.95316e+02)
         logPartFn[2] = math.log(6.63653e+03)
         logPartFn[3] = math.log(4.56577e+04)
         logPartFn[4] = math.log(8.57529e+04)


    if ("CaO" == species):
         logPartFn[0] = math.log(2.03667e+02)
         logPartFn[1] = math.log(8.94430e+02)
         logPartFn[2] = math.log(2.08874e+04)
         logPartFn[3] = math.log(5.21424e+05)
         logPartFn[4] = math.log(1.08355e+06)


    if ("TiO" == species):
         logPartFn[0] = math.log(5.04547e+02)
         logPartFn[1] = math.log(3.27426e+03)
         logPartFn[2] = math.log(6.43969e+04)
         logPartFn[3] = math.log(5.28755e+05)
         logPartFn[4] = math.log(9.61395e+05)


    if ("VO" == species):
         logPartFn[0] = math.log(6.62935e+02)
         logPartFn[1] = math.log(2.70111e+03)
         logPartFn[2] = math.log(4.15856e+04)
         logPartFn[3] = math.log(3.57467e+05)
         logPartFn[4] = math.log(6.53298e+05)


    return logPartFn

#   }  //end of method getMolPartFn    

def getPartFn2(species):

    """// Diatomic Partition fn values, QAB, from
//http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A+A/588/A96
//See: Barklem, P. S.; Collet, R., 2016, Astronomy & Astrophysics, Volume 588, id.A96"""

#//Just do linear piecewise interpolation in log of to hottest five values for now:
    logPartFn = [0.0 for i in range(5)]
    #//default initialization
    logPartFn[0] = 0.0  #//for T = 130 K
    logPartFn[1] = 0.0  #//for T = 500 K
    logPartFn[2] = 0.0  #//for T = 3000 K
    logPartFn[3] = 0.0  #//for T = 8000 K
    logPartFn[4] = 0.0  #//for T = 10000 K

    if ("HI" == species):
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00001e+00) 
        logPartFn[4] = math.log(2.00015e+00)
    
    
    if ("HII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)

    
    #//dummy
    if ("HIII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    #//dummy
    if ("HIV" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("HII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("DI" == species):
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00001e+00) 
        logPartFn[4] = math.log(2.00014e+00)
    
    
    if ("DII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    #//dummy
    if ("DIII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    #//dummy
    if ("DIV" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("HeI" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("HeII" == species):
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00000e+00) 
        logPartFn[4] = math.log(2.00000e+00)
    
    
    if ("HeIII" == species):
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    #//dummy
    if ("HeIV" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("LiI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00473e+00) 
        logPartFn[3] = math.log(2.70188e+00) 
        logPartFn[4] = math.log(3.86752e+00)
    
    
    if ("LiII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("LiIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00000e+00) 
        logPartFn[4] = math.log(2.00000e+00)
    
    
    #//dummy
    if ("LiIV" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("BeI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00024e+00) 
        logPartFn[3] = math.log(1.17655e+00) 
        logPartFn[4] = math.log(1.41117e+00)
    
    
    if ("BeII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.01924e+00) 
        logPartFn[4] = math.log(2.06070e+00)
    
    
    if ("BeIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("BI" == species):  
        logPartFn[0] = math.log(5.37746e+00) 
        logPartFn[1] = math.log(5.82788e+00) 
        logPartFn[2] = math.log(5.97080e+00) 
        logPartFn[3] = math.log(6.06978e+00) 
        logPartFn[4] = math.log(6.27955e+00)
    
    
    if ("BII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.01090e+00) 
        logPartFn[4] = math.log(1.04184e+00)
    
    
    if ("BIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00100e+00) 
        logPartFn[4] = math.log(2.00569e+00)
    
    
    if ("CI" == species):  
        logPartFn[0] = math.log(6.59516e+00) 
        logPartFn[1] = math.log(8.27478e+00) 
        logPartFn[2] = math.log(8.91124e+00) 
        logPartFn[3] = math.log(9.78474e+00) 
        logPartFn[4] = math.log(1.02090e+01)
    
    
    if ("CII" == species):  
        logPartFn[0] = math.log(3.98273e+00) 
        logPartFn[1] = math.log(5.33283e+00) 
        logPartFn[2] = math.log(5.88018e+00) 
        logPartFn[3] = math.log(5.95988e+00) 
        logPartFn[4] = math.log(5.98845e+00)
    
    
    if ("CIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00073e+00) 
        logPartFn[4] = math.log(1.00478e+00)
    
    
    if ("NI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00100e+00) 
        logPartFn[3] = math.log(4.34860e+00) 
        logPartFn[4] = math.log(4.72409e+00)
    
    
    if ("NII" == species):  
        logPartFn[0] = math.log(3.92596e+00) 
        logPartFn[1] = math.log(7.03961e+00) 
        logPartFn[2] = math.log(8.63000e+00) 
        logPartFn[3] = math.log(9.17980e+00) 
        logPartFn[4] = math.log(9.45305e+00)
    
    
    if ("NIII" == species):  
        logPartFn[0] = math.log(2.58062e+00) 
        logPartFn[1] = math.log(4.42179e+00) 
        logPartFn[2] = math.log(5.67908e+00) 
        logPartFn[3] = math.log(5.87690e+00) 
        logPartFn[4] = math.log(5.90406e+00)
    
    
    if ("OI" == species):  
        logPartFn[0] = math.log(5.60172e+00) 
        logPartFn[1] = math.log(7.42310e+00) 
        logPartFn[2] = math.log(8.68009e+00) 
        logPartFn[3] = math.log(9.16637e+00) 
        logPartFn[4] = math.log(9.41864e+00)
    
    
    if ("OII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00003e+00) 
        logPartFn[3] = math.log(4.08460e+00) 
        logPartFn[4] = math.log(4.22885e+00)
    
    
    if ("OIII" == species):  
        logPartFn[0] = math.log(2.02626e+00) 
        logPartFn[1] = math.log(5.23819e+00) 
        logPartFn[2] = math.log(8.15906e+00) 
        logPartFn[3] = math.log(8.80275e+00) 
        logPartFn[4] = math.log(9.00956e+00)
    
    
    if ("FI" == species):  
        logPartFn[0] = math.log(4.02285e+00) 
        logPartFn[1] = math.log(4.62529e+00) 
        logPartFn[2] = math.log(5.64768e+00) 
        logPartFn[3] = math.log(5.85982e+00) 
        logPartFn[4] = math.log(5.88706e+00)
    
    
    if ("FII" == species):  
        logPartFn[0] = math.log(5.07333e+00) 
        logPartFn[1] = math.log(6.36892e+00) 
        logPartFn[2] = math.log(8.33830e+00) 
        logPartFn[3] = math.log(8.85472e+00) 
        logPartFn[4] = math.log(9.03812e+00)
    
    
    if ("FIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.02228e+00) 
        logPartFn[4] = math.log(4.07763e+00)
    
    
    if ("NeI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("NeII" == species):  
        logPartFn[0] = math.log(4.00036e+00) 
        logPartFn[1] = math.log(4.21176e+00) 
        logPartFn[2] = math.log(5.37562e+00) 
        logPartFn[3] = math.log(5.73812e+00) 
        logPartFn[4] = math.log(5.78760e+00)
    
    
    if ("NeIII" == species):  
        logPartFn[0] = math.log(5.00248e+00) 
        logPartFn[1] = math.log(5.54261e+00) 
        logPartFn[2] = math.log(7.84726e+00) 
        logPartFn[3] = math.log(8.56792e+00) 
        logPartFn[4] = math.log(8.73276e+00)
    
    
    if ("NaI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00178e+00) 
        logPartFn[3] = math.log(3.40984e+00) 
        logPartFn[4] = math.log(7.08960e+00)
    
    
    if ("NaII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("NaIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.03921e+00) 
        logPartFn[2] = math.log(5.03856e+00) 
        logPartFn[3] = math.log(5.56425e+00) 
        logPartFn[4] = math.log(5.64305e+00)
    
    
    if ("MgI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00025e+00) 
        logPartFn[3] = math.log(1.21285e+00) 
        logPartFn[4] = math.log(1.64434e+00)
    
    
    if ("MgII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00976e+00) 
        logPartFn[4] = math.log(2.03571e+00)
    
    
    if ("MgIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("AlI" == species):  
        logPartFn[0] = math.log(3.15743e+00) 
        logPartFn[1] = math.log(4.89757e+00) 
        logPartFn[2] = math.log(5.79075e+00) 
        logPartFn[3] = math.log(6.19328e+00) 
        logPartFn[4] = math.log(7.05012e+00)
    
    
    if ("AlII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.01064e+00) 
        logPartFn[4] = math.log(1.04138e+00)
    
    
    if ("AlIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00037e+00) 
        logPartFn[4] = math.log(2.00260e+00)
    
    
    if ("SiI" == species):  
        logPartFn[0] = math.log(2.70106e+00) 
        logPartFn[1] = math.log(6.03405e+00) 
        logPartFn[2] = math.log(8.62816e+00) 
        logPartFn[3] = math.log(1.04988e+01) 
        logPartFn[4] = math.log(1.13575e+01)
    
    
    if ("SiII" == species):  
        logPartFn[0] = math.log(2.16657e+00) 
        logPartFn[1] = math.log(3.75040e+00) 
        logPartFn[2] = math.log(5.48529e+00) 
        logPartFn[3] = math.log(5.80440e+00) 
        logPartFn[4] = math.log(5.86668e+00)
    
    
    if ("SiIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00066e+00) 
        logPartFn[4] = math.log(1.00443e+00)
    
    
    if ("PI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.04361e+00) 
        logPartFn[3] = math.log(5.50312e+00) 
        logPartFn[4] = math.log(6.38380e+00)
    
    
    if ("PII" == species):  
        logPartFn[0] = math.log(1.51156e+00) 
        logPartFn[1] = math.log(4.16319e+00) 
        logPartFn[2] = math.log(7.83534e+00) 
        logPartFn[3] = math.log(9.54223e+00) 
        logPartFn[4] = math.log(1.00500e+01)
    
    
    if ("PIII" == species):  
        logPartFn[0] = math.log(2.00822e+00) 
        logPartFn[1] = math.log(2.80054e+00) 
        logPartFn[2] = math.log(5.05924e+00) 
        logPartFn[3] = math.log(5.61779e+00) 
        logPartFn[4] = math.log(5.69424e+00)
    
    
    if ("SI" == species):  
        logPartFn[0] = math.log(5.03922e+00) 
        logPartFn[1] = math.log(6.15186e+00) 
        logPartFn[2] = math.log(8.30016e+00) 
        logPartFn[3] = math.log(9.66532e+00) 
        logPartFn[4] = math.log(1.01385e+01)
    
    
    if ("SII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00804e+00) 
        logPartFn[3] = math.log(4.76202e+00) 
        logPartFn[4] = math.log(5.35265e+00)
    
    
    if ("SIII" == species):  
        logPartFn[0] = math.log(1.11055e+00) 
        logPartFn[1] = math.log(2.72523e+00) 
        logPartFn[2] = math.log(6.97489e+00) 
        logPartFn[3] = math.log(8.80785e+00) 
        logPartFn[4] = math.log(9.31110e+00)
    
    
    if ("ClI" == species):  
        logPartFn[0] = math.log(4.00011e+00) 
        logPartFn[1] = math.log(4.15794e+00) 
        logPartFn[2] = math.log(5.31000e+00) 
        logPartFn[3] = math.log(5.70664e+00) 
        logPartFn[4] = math.log(5.76344e+00)
    
    
    if ("ClII" == species):  
        logPartFn[0] = math.log(5.00137e+00) 
        logPartFn[1] = math.log(5.46184e+00) 
        logPartFn[2] = math.log(7.78751e+00) 
        logPartFn[3] = math.log(9.10464e+00) 
        logPartFn[4] = math.log(9.53390e+00)
    
    
    if ("ClIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00171e+00) 
        logPartFn[3] = math.log(4.41428e+00) 
        logPartFn[4] = math.log(4.82231e+00)
    
    
    if ("ArI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00007e+00)
    
    
    if ("ArII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.03252e+00) 
        logPartFn[2] = math.log(5.00667e+00) 
        logPartFn[3] = math.log(5.54606e+00) 
        logPartFn[4] = math.log(5.62775e+00)
    
    
    if ("ArIII" == species):  
        logPartFn[0] = math.log(5.00001e+00) 
        logPartFn[1] = math.log(5.13320e+00) 
        logPartFn[2] = math.log(7.23696e+00) 
        logPartFn[3] = math.log(8.61527e+00) 
        logPartFn[4] = math.log(9.02887e+00)
    
    
    if ("KI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.01222e+00) 
        logPartFn[3] = math.log(4.77353e+00) 
        logPartFn[4] = math.log(9.82105e+00)
    
    
    if ("KII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("KIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00394e+00) 
        logPartFn[2] = math.log(4.70805e+00) 
        logPartFn[3] = math.log(5.35493e+00) 
        logPartFn[4] = math.log(5.46467e+00)
    
    
    if ("CaI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00701e+00) 
        logPartFn[3] = math.log(2.60365e+00) 
        logPartFn[4] = math.log(5.69578e+00)
    
    
    if ("CaII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.01415e+00) 
        logPartFn[3] = math.log(2.91713e+00) 
        logPartFn[4] = math.log(3.56027e+00)
    
    
    if ("CaIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("ScI" == species):  
        logPartFn[0] = math.log(4.93134e+00) 
        logPartFn[1] = math.log(7.69658e+00) 
        logPartFn[2] = math.log(9.68986e+00) 
        logPartFn[3] = math.log(2.16410e+01) 
        logPartFn[4] = math.log(3.31527e+01)
    
    
    if ("ScII" == species):  
        logPartFn[0] = math.log(6.34225e+00) 
        logPartFn[1] = math.log(1.13155e+01) 
        logPartFn[2] = math.log(1.78090e+01) 
        logPartFn[3] = math.log(2.94840e+01) 
        logPartFn[4] = math.log(3.36439e+01)
    
    
    if ("ScIII" == species):  
        logPartFn[0] = math.log(4.67343e+00) 
        logPartFn[1] = math.log(7.39773e+00) 
        logPartFn[2] = math.log(9.45747e+00) 
        logPartFn[3] = math.log(9.81083e+00) 
        logPartFn[4] = math.log(9.88331e+00)
    
    
    if ("TiI" == species):  
        logPartFn[0] = math.log(6.18965e+00) 
        logPartFn[1] = math.log(1.22473e+01) 
        logPartFn[2] = math.log(2.08195e+01) 
        logPartFn[3] = math.log(5.53232e+01) 
        logPartFn[4] = math.log(8.32038e+01)
    
    
    if ("TiII" == species):  
        logPartFn[0] = math.log(6.90468e+00) 
        logPartFn[1] = math.log(1.72793e+01) 
        logPartFn[2] = math.log(4.40264e+01) 
        logPartFn[3] = math.log(7.23680e+01) 
        logPartFn[4] = math.log(8.37248e+01)
    
    
    if ("TiIII" == species):  
        logPartFn[0] = math.log(5.99049e+00) 
        logPartFn[1] = math.log(1.17969e+01) 
        logPartFn[2] = math.log(1.89121e+01) 
        logPartFn[3] = math.log(2.32253e+01) 
        logPartFn[4] = math.log(2.49249e+01)
    
    
    if ("VI" == species):  
        logPartFn[0] = math.log(5.55703e+00) 
        logPartFn[1] = math.log(1.32751e+01) 
        logPartFn[2] = math.log(3.47920e+01) 
        logPartFn[3] = math.log(7.90427e+01) 
        logPartFn[4] = math.log(1.11459e+02)
    
    
    if ("VII" == species):  
        logPartFn[0] = math.log(5.45407e+00) 
        logPartFn[1] = math.log(1.46216e+01) 
        logPartFn[2] = math.log(3.18263e+01) 
        logPartFn[3] = math.log(6.43796e+01) 
        logPartFn[4] = math.log(8.08903e+01)
    
    
    if ("VIII" == species):  
        logPartFn[0] = math.log(5.39755e+00) 
        logPartFn[1] = math.log(1.28067e+01) 
        logPartFn[2] = math.log(2.40588e+01) 
        logPartFn[3] = math.log(3.19510e+01) 
        logPartFn[4] = math.log(3.59622e+01)
    
    
    if ("CrI" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00000e+00) 
        logPartFn[2] = math.log(7.65435e+00) 
        logPartFn[3] = math.log(2.01376e+01) 
        logPartFn[4] = math.log(3.31787e+01)
    
    
    if ("CrII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.08747e+00) 
        logPartFn[3] = math.log(1.21840e+01) 
        logPartFn[4] = math.log(1.84825e+01)
    
    
    if ("CrIII" == species):  
        logPartFn[0] = math.log(3.31635e+00) 
        logPartFn[1] = math.log(1.06851e+01) 
        logPartFn[2] = math.log(2.12330e+01) 
        logPartFn[3] = math.log(2.71108e+01) 
        logPartFn[4] = math.log(3.11257e+01)
    
    
    if ("MnI" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.01140e+00) 
        logPartFn[3] = math.log(9.82265e+00) 
        logPartFn[4] = math.log(1.53539e+01)
    
    
    if ("MnII" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00000e+00) 
        logPartFn[2] = math.log(7.07640e+00) 
        logPartFn[3] = math.log(1.07144e+01) 
        logPartFn[4] = math.log(1.45638e+01)
    
    
    if ("MnIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.00011e+00) 
        logPartFn[3] = math.log(6.46711e+00) 
        logPartFn[4] = math.log(7.39061e+00)
    
    
    if ("FeI" == species):  
        logPartFn[0] = math.log(9.07242e+00) 
        logPartFn[1] = math.log(1.20678e+01) 
        logPartFn[2] = math.log(2.19554e+01) 
        logPartFn[3] = math.log(4.28266e+01) 
        logPartFn[4] = math.log(5.96627e+01)
    
    
    if ("FeII" == species):  
        logPartFn[0] = math.log(1.01172e+01) 
        logPartFn[1] = math.log(1.40327e+01) 
        logPartFn[2] = math.log(3.43147e+01) 
        logPartFn[3] = math.log(5.64784e+01) 
        logPartFn[4] = math.log(6.69023e+01)
    
    
    if ("FeIII" == species):  
        logPartFn[0] = math.log(9.05759e+00) 
        logPartFn[1] = math.log(1.18492e+01) 
        logPartFn[2] = math.log(2.07199e+01) 
        logPartFn[3] = math.log(2.52719e+01) 
        logPartFn[4] = math.log(2.81882e+01)
    
    
    if ("CoI" == species):  
        logPartFn[0] = math.log(1.00010e+01) 
        logPartFn[1] = math.log(1.08918e+01) 
        logPartFn[2] = math.log(2.44719e+01) 
        logPartFn[3] = math.log(4.80929e+01) 
        logPartFn[4] = math.log(6.08394e+01)
    
    
    if ("CoII" == species):  
        logPartFn[0] = math.log(9.00019e+00) 
        logPartFn[1] = math.log(9.50563e+00) 
        logPartFn[2] = math.log(2.09531e+01) 
        logPartFn[3] = math.log(4.21891e+01) 
        logPartFn[4] = math.log(5.04464e+01)
    
    
    if ("CoIII" == species):  
        logPartFn[0] = math.log(1.00007e+01) 
        logPartFn[1] = math.log(1.08219e+01) 
        logPartFn[2] = math.log(1.99830e+01) 
        logPartFn[3] = math.log(2.65869e+01) 
        logPartFn[4] = math.log(2.93889e+01)
    
    
    if ("NiI" == species):  
        logPartFn[0] = math.log(9.72623e+00) 
        logPartFn[1] = math.log(1.34631e+01) 
        logPartFn[2] = math.log(2.63546e+01) 
        logPartFn[3] = math.log(3.63831e+01) 
        logPartFn[4] = math.log(4.15802e+01)
    
    
    if ("NiII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.05237e+00) 
        logPartFn[2] = math.log(8.29948e+00) 
        logPartFn[3] = math.log(1.57985e+01) 
        logPartFn[4] = math.log(1.94018e+01)
    
    
    if ("NiIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.14687e+00) 
        logPartFn[2] = math.log(1.43380e+01) 
        logPartFn[3] = math.log(1.87862e+01) 
        logPartFn[4] = math.log(2.01688e+01)
    
    
    if ("CuI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.03485e+00) 
        logPartFn[3] = math.log(3.25011e+00) 
        logPartFn[4] = math.log(4.17708e+00)
    
    
    if ("CuII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00032e+00) 
        logPartFn[3] = math.log(1.30264e+00) 
        logPartFn[4] = math.log(1.69815e+00)
    
    
    if ("CuIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.01031e+00) 
        logPartFn[2] = math.log(7.48119e+00) 
        logPartFn[3] = math.log(8.75641e+00) 
        logPartFn[4] = math.log(8.97397e+00)
    
    
    if ("ZnI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.02806e+00) 
        logPartFn[4] = math.log(1.11187e+00)
    
    
    if ("ZnII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00099e+00) 
        logPartFn[4] = math.log(2.00625e+00)
    
    
    if ("ZnIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00001e+00) 
        logPartFn[4] = math.log(1.00021e+00)
    
    
    if ("GaI" == species):  
        logPartFn[0] = math.log(2.00043e+00) 
        logPartFn[1] = math.log(2.37127e+00) 
        logPartFn[2] = math.log(4.69154e+00) 
        logPartFn[3] = math.log(5.64961e+00) 
        logPartFn[4] = math.log(6.47300e+00)
    
    
    if ("GaII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00154e+00) 
        logPartFn[4] = math.log(1.00881e+00)
    
    
    if ("GaIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00004e+00) 
        logPartFn[4] = math.log(2.00043e+00)
    
    
    if ("GeI" == species):  
        logPartFn[0] = math.log(1.00630e+00) 
        logPartFn[1] = math.log(1.69040e+00) 
        logPartFn[2] = math.log(6.00402e+00) 
        logPartFn[3] = math.log(9.09691e+00) 
        logPartFn[4] = math.log(1.01931e+01)
    
    
    if ("GeII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.02475e+00) 
        logPartFn[2] = math.log(3.71392e+00) 
        logPartFn[3] = math.log(4.91199e+00) 
        logPartFn[4] = math.log(5.10944e+00)
    
    
    if ("GeIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00010e+00) 
        logPartFn[4] = math.log(1.00101e+00)
    
    
    if ("AsI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.05774e+00) 
        logPartFn[3] = math.log(5.65799e+00) 
        logPartFn[4] = math.log(6.57374e+00)
    
    
    if ("AsII" == species):  
        logPartFn[0] = math.log(1.00002e+00) 
        logPartFn[1] = math.log(1.14402e+00) 
        logPartFn[2] = math.log(4.31914e+00) 
        logPartFn[3] = math.log(7.47497e+00) 
        logPartFn[4] = math.log(8.25460e+00)
    
    
    if ("AsIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00085e+00) 
        logPartFn[2] = math.log(2.97673e+00) 
        logPartFn[3] = math.log(4.35751e+00) 
        logPartFn[4] = math.log(4.62049e+00)
    
    
    if ("SeI" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.01048e+00) 
        logPartFn[2] = math.log(6.50285e+00) 
        logPartFn[3] = math.log(8.64654e+00) 
        logPartFn[4] = math.log(9.28469e+00)
    
    
    if ("SeII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.01539e+00) 
        logPartFn[3] = math.log(4.96394e+00) 
        logPartFn[4] = math.log(5.62894e+00)
    
    
    if ("SeIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.02009e+00) 
        logPartFn[2] = math.log(3.06837e+00) 
        logPartFn[3] = math.log(6.14277e+00) 
        logPartFn[4] = math.log(6.95690e+00)
    
    
    if ("BrI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00005e+00) 
        logPartFn[2] = math.log(4.34162e+00) 
        logPartFn[3] = math.log(5.03126e+00) 
        logPartFn[4] = math.log(5.18274e+00)
    
    
    if ("BrII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00038e+00) 
        logPartFn[2] = math.log(5.84067e+00) 
        logPartFn[3] = math.log(7.78362e+00) 
        logPartFn[4] = math.log(8.38287e+00)
    
    
    if ("BrIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00537e+00) 
        logPartFn[3] = math.log(4.62671e+00) 
        logPartFn[4] = math.log(5.14171e+00)
    
    
    if ("KrI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00001e+00) 
        logPartFn[4] = math.log(1.00044e+00)
    
    
    if ("KrII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.15228e+00) 
        logPartFn[3] = math.log(4.76145e+00) 
        logPartFn[4] = math.log(4.92367e+00)
    
    
    if ("KrIII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00001e+00) 
        logPartFn[2] = math.log(5.42146e+00) 
        logPartFn[3] = math.log(7.07047e+00) 
        logPartFn[4] = math.log(7.64176e+00)
    
    
    if ("RbI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.01473e+00) 
        logPartFn[3] = math.log(5.41664e+00) 
        logPartFn[4] = math.log(1.13631e+01)
    
    
    if ("RbII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("RbIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.05824e+00) 
        logPartFn[3] = math.log(4.53101e+00) 
        logPartFn[4] = math.log(4.69229e+00)
    
    
    if ("SrI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.01064e+00) 
        logPartFn[3] = math.log(2.98824e+00) 
        logPartFn[4] = math.log(6.20304e+00)
    
    
    if ("SrII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00865e+00) 
        logPartFn[3] = math.log(2.78698e+00) 
        logPartFn[4] = math.log(3.40185e+00)
    
    
    if ("SrIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("YI" == species):  
        logPartFn[0] = math.log(4.01695e+00) 
        logPartFn[1] = math.log(5.30447e+00) 
        logPartFn[2] = math.log(8.85992e+00) 
        logPartFn[3] = math.log(2.22176e+01) 
        logPartFn[4] = math.log(3.32369e+01)
    
    
    if ("YII" == species):  
        logPartFn[0] = math.log(1.00032e+00) 
        logPartFn[1] = math.log(1.62308e+00) 
        logPartFn[2] = math.log(1.09488e+01) 
        logPartFn[3] = math.log(2.25715e+01) 
        logPartFn[4] = math.log(2.70276e+01)
    
    
    if ("YIII" == species):  
        logPartFn[0] = math.log(4.00199e+00) 
        logPartFn[1] = math.log(4.74694e+00) 
        logPartFn[2] = math.log(8.29546e+00) 
        logPartFn[3] = math.log(9.79259e+00) 
        logPartFn[4] = math.log(1.01030e+01)
    
    
    if ("ZrI" == species):  
        logPartFn[0] = math.log(5.01271e+00) 
        logPartFn[1] = math.log(6.60966e+00) 
        logPartFn[2] = math.log(1.99689e+01) 
        logPartFn[3] = math.log(6.46409e+01) 
        logPartFn[4] = math.log(9.29133e+01)
    
    
    if ("ZrII" == species):  
        logPartFn[0] = math.log(4.18616e+00) 
        logPartFn[1] = math.log(7.54284e+00) 
        logPartFn[2] = math.log(2.91432e+01) 
        logPartFn[3] = math.log(6.73523e+01) 
        logPartFn[4] = math.log(8.12269e+01)
    
    
    if ("ZrIII" == species):  
        logPartFn[0] = math.log(5.00371e+00) 
        logPartFn[1] = math.log(6.10992e+00) 
        logPartFn[2] = math.log(1.49741e+01) 
        logPartFn[3] = math.log(2.35798e+01) 
        logPartFn[4] = math.log(2.64105e+01)
    
    
    if ("NbI" == species):  
        logPartFn[0] = math.log(2.80828e+00) 
        logPartFn[1] = math.log(8.30968e+00) 
        logPartFn[2] = math.log(3.50009e+01) 
        logPartFn[3] = math.log(9.41753e+01) 
        logPartFn[4] = math.log(1.32663e+02)
    
    
    if ("NbII" == species):  
        logPartFn[0] = math.log(1.55657e+00) 
        logPartFn[1] = math.log(5.28597e+00) 
        logPartFn[2] = math.log(2.62767e+01) 
        logPartFn[3] = math.log(7.22928e+01) 
        logPartFn[4] = math.log(9.34755e+01)
    
    
    if ("NbIII" == species):  
        logPartFn[0] = math.log(4.01990e+00) 
        logPartFn[1] = math.log(5.66842e+00) 
        logPartFn[2] = math.log(1.76187e+01) 
        logPartFn[3] = math.log(3.32180e+01) 
        logPartFn[4] = math.log(3.96549e+01)
    
    
    if ("MoI" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00000e+00) 
        logPartFn[2] = math.log(7.13826e+00) 
        logPartFn[3] = math.log(1.94435e+01) 
        logPartFn[4] = math.log(3.41087e+01)
    
    
    if ("MoII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.10323e+00) 
        logPartFn[3] = math.log(1.57858e+01) 
        logPartFn[4] = math.log(2.53531e+01)
    
    
    if ("MoIII" == species):  
        logPartFn[0] = math.log(1.20909e+00) 
        logPartFn[1] = math.log(3.47425e+00) 
        logPartFn[2] = math.log(1.49713e+01) 
        logPartFn[3] = math.log(2.84296e+01) 
        logPartFn[4] = math.log(3.53071e+01)
    
    
    if ("TcI" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00698e+00) 
        logPartFn[2] = math.log(1.26513e+01) 
        logPartFn[3] = math.log(4.01671e+01) 
        logPartFn[4] = math.log(5.99532e+01)
    
    
    if ("TcII" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00047e+00) 
        logPartFn[2] = math.log(1.05476e+01) 
        logPartFn[3] = math.log(2.00471e+01) 
        logPartFn[4] = math.log(2.31663e+01)
    
    
    if ("TcIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.00000e+00) 
        logPartFn[3] = math.log(6.00000e+00) 
        logPartFn[4] = math.log(6.00000e+00)
    
    
    if ("RuI" == species):  
        logPartFn[0] = math.log(1.10000e+01) 
        logPartFn[1] = math.log(1.13122e+01) 
        logPartFn[2] = math.log(2.23319e+01) 
        logPartFn[3] = math.log(5.81063e+01) 
        logPartFn[4] = math.log(7.89315e+01)
    
    
    if ("RuII" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.01050e+01) 
        logPartFn[2] = math.log(1.71302e+01) 
        logPartFn[3] = math.log(3.64331e+01) 
        logPartFn[4] = math.log(4.65540e+01)
    
    
    if ("RuIII" == species):  
        logPartFn[0] = math.log(9.00002e+00) 
        logPartFn[1] = math.log(9.28086e+00) 
        logPartFn[2] = math.log(1.64154e+01) 
        logPartFn[3] = math.log(2.09762e+01) 
        logPartFn[4] = math.log(2.17901e+01)
    
    
    if ("RhI" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.01020e+01) 
        logPartFn[2] = math.log(1.86621e+01) 
        logPartFn[3] = math.log(3.88108e+01) 
        logPartFn[4] = math.log(4.81045e+01)
    
    
    if ("RhII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00716e+00) 
        logPartFn[2] = math.log(1.22675e+01) 
        logPartFn[3] = math.log(2.08582e+01) 
        logPartFn[4] = math.log(2.51822e+01)
    
    
    if ("RhIII" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.00168e+01) 
        logPartFn[2] = math.log(1.45746e+01) 
        logPartFn[3] = math.log(2.50952e+01) 
        logPartFn[4] = math.log(2.95669e+01)
    
    
    if ("PdI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.46384e+00) 
        logPartFn[3] = math.log(5.77132e+00) 
        logPartFn[4] = math.log(7.96499e+00)
    
    
    if ("PdII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00015e+00) 
        logPartFn[2] = math.log(6.73288e+00) 
        logPartFn[3] = math.log(8.40680e+00) 
        logPartFn[4] = math.log(9.23953e+00)
    
    
    if ("PdIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00065e+00) 
        logPartFn[2] = math.log(1.10655e+01) 
        logPartFn[3] = math.log(1.69387e+01) 
        logPartFn[4] = math.log(1.89830e+01)
    
    
    if ("AgI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00001e+00) 
        logPartFn[3] = math.log(2.07520e+00) 
        logPartFn[4] = math.log(2.29282e+00)
    
    
    if ("AgII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.01183e+00) 
        logPartFn[4] = math.log(1.05173e+00)
    
    
    if ("AgIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00001e+00) 
        logPartFn[2] = math.log(6.43868e+00) 
        logPartFn[3] = math.log(7.74647e+00) 
        logPartFn[4] = math.log(8.06409e+00)
    
    
    if ("CdI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.03706e+00) 
        logPartFn[4] = math.log(1.13787e+00)
    
    
    if ("CdII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00166e+00) 
        logPartFn[4] = math.log(2.00881e+00)
    
    
    if ("CdIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00001e+00) 
        logPartFn[4] = math.log(1.00013e+00)
    
    
    if ("InI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00688e+00) 
        logPartFn[2] = math.log(3.38443e+00) 
        logPartFn[3] = math.log(4.93682e+00) 
        logPartFn[4] = math.log(5.96634e+00)
    
    
    if ("InII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00309e+00) 
        logPartFn[4] = math.log(1.01538e+00)
    
    
    if ("InIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00013e+00) 
        logPartFn[4] = math.log(2.00111e+00)
    
    
    if ("SnI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.02333e+00) 
        logPartFn[2] = math.log(3.37985e+00) 
        logPartFn[3] = math.log(7.09384e+00) 
        logPartFn[4] = math.log(8.36474e+00)
    
    
    if ("SnII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00002e+00) 
        logPartFn[2] = math.log(2.52079e+00) 
        logPartFn[3] = math.log(3.86439e+00) 
        logPartFn[4] = math.log(4.18355e+00)
    
    
    if ("SnIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00033e+00) 
        logPartFn[4] = math.log(1.00255e+00)
    
    
    if ("SbI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.12205e+00) 
        logPartFn[3] = math.log(6.14860e+00) 
        logPartFn[4] = math.log(7.20611e+00)
    
    
    if ("SbII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00046e+00) 
        logPartFn[2] = math.log(2.03582e+00) 
        logPartFn[3] = math.log(5.05509e+00) 
        logPartFn[4] = math.log(5.97984e+00)
    
    
    if ("SbIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.17082e+00) 
        logPartFn[3] = math.log(3.22630e+00) 
        logPartFn[4] = math.log(3.55562e+00)
    
    
    if ("TeI" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.44375e+00) 
        logPartFn[3] = math.log(7.47891e+00) 
        logPartFn[4] = math.log(8.22338e+00)
    
    
    if ("TeII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.04540e+00) 
        logPartFn[3] = math.log(5.38198e+00) 
        logPartFn[4] = math.log(6.15477e+00)
    
    
    if ("TeIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.40826e+00) 
        logPartFn[3] = math.log(3.64876e+00) 
        logPartFn[4] = math.log(4.47090e+00)
    
    
    if ("II" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.05220e+00) 
        logPartFn[3] = math.log(4.51156e+00) 
        logPartFn[4] = math.log(4.69382e+00)
    
    
    if ("III" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.15261e+00) 
        logPartFn[3] = math.log(6.58097e+00) 
        logPartFn[4] = math.log(7.18642e+00)
    
    
    if ("IIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.01931e+00) 
        logPartFn[3] = math.log(4.94321e+00) 
        logPartFn[4] = math.log(5.56234e+00)
    
    
    if ("XeI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00015e+00) 
        logPartFn[4] = math.log(1.00319e+00)
    
    
    if ("XeII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.01278e+00) 
        logPartFn[3] = math.log(4.30069e+00) 
        logPartFn[4] = math.log(4.43930e+00)
    
    
    if ("XeIII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.04902e+00) 
        logPartFn[3] = math.log(5.97976e+00) 
        logPartFn[4] = math.log(6.47644e+00)
    
    
    if ("CsI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.03442e+00) 
        logPartFn[3] = math.log(7.88683e+00) 
        logPartFn[4] = math.log(1.69354e+01)
    
    
    if ("CsII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00001e+00)
    
    
    if ("CsIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00261e+00) 
        logPartFn[3] = math.log(4.16580e+00) 
        logPartFn[4] = math.log(4.27282e+00)
    
    
    if ("BaI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.21060e+00) 
        logPartFn[3] = math.log(8.29000e+00) 
        logPartFn[4] = math.log(1.66116e+01)
    
    
    if ("BaII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.78137e+00) 
        logPartFn[3] = math.log(5.96568e+00) 
        logPartFn[4] = math.log(6.97202e+00)
    
    
    if ("BaIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("LaI" == species):  
        logPartFn[0] = math.log(4.00005e+00) 
        logPartFn[1] = math.log(4.29315e+00) 
        logPartFn[2] = math.log(1.42312e+01) 
        logPartFn[3] = math.log(5.77343e+01) 
        logPartFn[4] = math.log(8.81122e+01)
    
    
    if ("LaII" == species):  
        logPartFn[0] = math.log(5.00009e+00) 
        logPartFn[1] = math.log(5.51405e+00) 
        logPartFn[2] = math.log(2.03638e+01) 
        logPartFn[3] = math.log(4.28241e+01) 
        logPartFn[4] = math.log(5.27740e+01)
    
    
    if ("LaIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.05954e+00) 
        logPartFn[2] = math.log(7.09841e+00) 
        logPartFn[3] = math.log(1.19933e+01) 
        logPartFn[4] = math.log(1.34792e+01)
    
    
    if ("CeI" == species):  
        logPartFn[0] = math.log(9.39731e+00) 
        logPartFn[1] = math.log(1.20470e+01) 
        logPartFn[2] = math.log(7.59152e+01) 
        logPartFn[3] = math.log(4.66858e+02) 
        logPartFn[4] = math.log(7.08652e+02)
    
    
    if ("CeII" == species):  
        logPartFn[0] = math.log(8.00018e+00) 
        logPartFn[1] = math.log(8.83511e+00) 
        logPartFn[2] = math.log(8.20718e+01) 
        logPartFn[3] = math.log(3.70729e+02) 
        logPartFn[4] = math.log(4.91152e+02)
    
    
    if ("CeIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.13795e+00) 
        logPartFn[2] = math.log(2.59288e+01) 
        logPartFn[3] = math.log(7.43305e+01) 
        logPartFn[4] = math.log(9.01542e+01)
    
    
    if ("PrI" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.02326e+01) 
        logPartFn[2] = math.log(3.50798e+01) 
        logPartFn[3] = math.log(3.18645e+02) 
        logPartFn[4] = math.log(5.02583e+02)
    
    
    if ("PrII" == species):  
        logPartFn[0] = math.log(9.08268e+00) 
        logPartFn[1] = math.log(1.22739e+01) 
        logPartFn[2] = math.log(5.41964e+01) 
        logPartFn[3] = math.log(2.74460e+02) 
        logPartFn[4] = math.log(3.80580e+02)
    
    
    if ("PrIII" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.02182e+01) 
        logPartFn[2] = math.log(2.19864e+01) 
        logPartFn[3] = math.log(6.64136e+01) 
        logPartFn[4] = math.log(9.66706e+01)
    
    
    if ("NdI" == species):  
        logPartFn[0] = math.log(9.00004e+00) 
        logPartFn[1] = math.log(9.44310e+00) 
        logPartFn[2] = math.log(2.95270e+01) 
        logPartFn[3] = math.log(3.13305e+02) 
        logPartFn[4] = math.log(5.42293e+02)
    
    
    if ("NdII" == species):  
        logPartFn[0] = math.log(8.03412e+00) 
        logPartFn[1] = math.log(1.05550e+01) 
        logPartFn[2] = math.log(4.95287e+01) 
        logPartFn[3] = math.log(3.20614e+02) 
        logPartFn[4] = math.log(5.04711e+02)
    
    
    if ("NdIII" == species):  
        logPartFn[0] = math.log(9.00004e+00) 
        logPartFn[1] = math.log(9.43038e+00) 
        logPartFn[2] = math.log(2.35346e+01) 
        logPartFn[3] = math.log(4.66105e+01) 
        logPartFn[4] = math.log(5.66490e+01)
    
    
    if ("PmI" == species):  
        logPartFn[0] = math.log(6.00110e+00) 
        logPartFn[1] = math.log(6.86120e+00) 
        logPartFn[2] = math.log(2.40772e+01) 
        logPartFn[3] = math.log(7.47623e+01) 
        logPartFn[4] = math.log(1.13054e+02)
    
    
    if ("PmII" == species):  
        logPartFn[0] = math.log(5.05009e+00) 
        logPartFn[1] = math.log(7.39584e+00) 
        logPartFn[2] = math.log(4.17360e+01) 
        logPartFn[3] = math.log(1.35782e+02) 
        logPartFn[4] = math.log(1.78314e+02)
    
    
    if ("PmIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.00000e+00) 
        logPartFn[3] = math.log(6.00000e+00) 
        logPartFn[4] = math.log(6.00000e+00)
    
    
    if ("SmI" == species):  
        logPartFn[0] = math.log(1.11838e+00) 
        logPartFn[1] = math.log(2.88715e+00) 
        logPartFn[2] = math.log(1.84133e+01) 
        logPartFn[3] = math.log(1.09023e+02) 
        logPartFn[4] = math.log(1.89582e+02)
    
    
    if ("SmII" == species):  
        logPartFn[0] = math.log(2.10827e+00) 
        logPartFn[1] = math.log(4.26988e+00) 
        logPartFn[2] = math.log(3.12536e+01) 
        logPartFn[3] = math.log(1.19821e+02) 
        logPartFn[4] = math.log(1.75950e+02)
    
    
    if ("SmIII" == species):  
        logPartFn[0] = math.log(1.11724e+00) 
        logPartFn[1] = math.log(2.88059e+00) 
        logPartFn[2] = math.log(1.77904e+01) 
        logPartFn[3] = math.log(3.49109e+01) 
        logPartFn[4] = math.log(4.10217e+01)
    
    
    if ("EuI" == species):  
        logPartFn[0] = math.log(8.00000e+00) 
        logPartFn[1] = math.log(8.00000e+00) 
        logPartFn[2] = math.log(8.15223e+00) 
        logPartFn[3] = math.log(2.69921e+01) 
        logPartFn[4] = math.log(5.13327e+01)
    
    
    if ("EuII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.05745e+00) 
        logPartFn[2] = math.log(1.24460e+01) 
        logPartFn[3] = math.log(2.38118e+01) 
        logPartFn[4] = math.log(3.15054e+01)
    
    
    if ("EuIII" == species):  
        logPartFn[0] = math.log(8.00000e+00) 
        logPartFn[1] = math.log(8.00000e+00) 
        logPartFn[2] = math.log(8.00004e+00) 
        logPartFn[3] = math.log(8.65078e+00) 
        logPartFn[4] = math.log(1.03670e+01)
    
    
    if ("GdI" == species):  
        logPartFn[0] = math.log(5.67234e+00) 
        logPartFn[1] = math.log(1.14248e+01) 
        logPartFn[2] = math.log(3.48245e+01) 
        logPartFn[3] = math.log(1.36394e+02) 
        logPartFn[4] = math.log(2.17943e+02)
    
    
    if ("GdII" == species):  
        logPartFn[0] = math.log(6.45033e+00) 
        logPartFn[1] = math.log(1.18671e+01) 
        logPartFn[2] = math.log(4.85326e+01) 
        logPartFn[3] = math.log(1.46650e+02) 
        logPartFn[4] = math.log(1.95931e+02)
    
    
    if ("GdIII" == species):  
        logPartFn[0] = math.log(5.32234e+00) 
        logPartFn[1] = math.log(9.64026e+00) 
        logPartFn[2] = math.log(3.56490e+01) 
        logPartFn[3] = math.log(6.82437e+01) 
        logPartFn[4] = math.log(7.69994e+01)
    
    
    if ("TbI" == species):  
        logPartFn[0] = math.log(1.67331e+01) 
        logPartFn[1] = math.log(2.93841e+01) 
        logPartFn[2] = math.log(8.97544e+01) 
        logPartFn[3] = math.log(3.47204e+02) 
        logPartFn[4] = math.log(5.12797e+02)
    
    
    if ("TbII" == species):  
        logPartFn[0] = math.log(1.70002e+01) 
        logPartFn[1] = math.log(1.78116e+01) 
        logPartFn[2] = math.log(5.25407e+01) 
        logPartFn[3] = math.log(1.68157e+02) 
        logPartFn[4] = math.log(2.17753e+02)
    
    
    if ("TbIII" == species):  
        logPartFn[0] = math.log(1.60000e+01) 
        logPartFn[1] = math.log(1.60044e+01) 
        logPartFn[2] = math.log(2.36107e+01) 
        logPartFn[3] = math.log(7.90783e+01) 
        logPartFn[4] = math.log(1.08698e+02)
    
    
    if ("DyI" == species):  
        logPartFn[0] = math.log(1.70000e+01) 
        logPartFn[1] = math.log(1.70001e+01) 
        logPartFn[2] = math.log(2.11524e+01) 
        logPartFn[3] = math.log(1.37365e+02) 
        logPartFn[4] = math.log(2.61442e+02)
    
    
    if ("DyII" == species):  
        logPartFn[0] = math.log(1.80017e+01) 
        logPartFn[1] = math.log(1.94761e+01) 
        logPartFn[2] = math.log(3.37600e+01) 
        logPartFn[3] = math.log(1.26585e+02) 
        logPartFn[4] = math.log(2.08424e+02)
    
    
    if ("DyIII" == species):  
        logPartFn[0] = math.log(1.70000e+01) 
        logPartFn[1] = math.log(1.70000e+01) 
        logPartFn[2] = math.log(1.70000e+01) 
        logPartFn[3] = math.log(1.70000e+01) 
        logPartFn[4] = math.log(1.70000e+01)
    
    
    if ("HoI" == species):  
        logPartFn[0] = math.log(1.60000e+01) 
        logPartFn[1] = math.log(1.60000e+01) 
        logPartFn[2] = math.log(1.87758e+01) 
        logPartFn[3] = math.log(9.97150e+01) 
        logPartFn[4] = math.log(1.71521e+02)
    
    
    if ("HoII" == species):  
        logPartFn[0] = math.log(1.70130e+01) 
        logPartFn[1] = math.log(1.93968e+01) 
        logPartFn[2] = math.log(3.03102e+01) 
        logPartFn[3] = math.log(5.61173e+01) 
        logPartFn[4] = math.log(7.13807e+01)
    
    
    if ("HoIII" == species):  
        logPartFn[0] = math.log(1.60000e+01) 
        logPartFn[1] = math.log(1.60000e+01) 
        logPartFn[2] = math.log(1.73144e+01) 
        logPartFn[3] = math.log(3.55564e+01) 
        logPartFn[4] = math.log(5.14625e+01)
    
    
    if ("ErI" == species):  
        logPartFn[0] = math.log(1.30000e+01) 
        logPartFn[1] = math.log(1.30000e+01) 
        logPartFn[2] = math.log(1.62213e+01) 
        logPartFn[3] = math.log(1.03737e+02) 
        logPartFn[4] = math.log(1.94418e+02)
    
    
    if ("ErII" == species):  
        logPartFn[0] = math.log(1.40917e+01) 
        logPartFn[1] = math.log(1.73794e+01) 
        logPartFn[2] = math.log(2.71056e+01) 
        logPartFn[3] = math.log(9.05747e+01) 
        logPartFn[4] = math.log(1.40942e+02)
    
    
    if ("ErIII" == species):  
        logPartFn[0] = math.log(1.30000e+01) 
        logPartFn[1] = math.log(1.30000e+01) 
        logPartFn[2] = math.log(1.52920e+01) 
        logPartFn[3] = math.log(3.23775e+01) 
        logPartFn[4] = math.log(4.33307e+01)
    
    
    if ("TmI" == species):  
        logPartFn[0] = math.log(8.00000e+00) 
        logPartFn[1] = math.log(8.00000e+00) 
        logPartFn[2] = math.log(8.16070e+00) 
        logPartFn[3] = math.log(2.89498e+01) 
        logPartFn[4] = math.log(5.79555e+01)
    
    
    if ("TmII" == species):  
        logPartFn[0] = math.log(9.50853e+00) 
        logPartFn[1] = math.log(1.25401e+01) 
        logPartFn[2] = math.log(1.54699e+01) 
        logPartFn[3] = math.log(3.09619e+01) 
        logPartFn[4] = math.log(4.97225e+01)
    
    
    if ("TmIII" == species):  
        logPartFn[0] = math.log(8.00000e+00) 
        logPartFn[1] = math.log(8.00000e+00) 
        logPartFn[2] = math.log(8.08981e+00) 
        logPartFn[3] = math.log(1.09856e+01) 
        logPartFn[4] = math.log(1.49391e+01)
    
    
    if ("YbI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00151e+00) 
        logPartFn[3] = math.log(2.45238e+00) 
        logPartFn[4] = math.log(5.30693e+00)
    
    
    if ("YbII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00045e+00) 
        logPartFn[3] = math.log(2.90499e+00) 
        logPartFn[4] = math.log(4.84517e+00)
    
    
    if ("YbIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.10983e+00) 
        logPartFn[4] = math.log(1.44387e+00)
    
    
    if ("LuI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.01936e+00) 
        logPartFn[2] = math.log(6.69800e+00) 
        logPartFn[3] = math.log(1.39052e+01) 
        logPartFn[4] = math.log(2.05472e+01)
    
    
    if ("LuII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.03231e+00) 
        logPartFn[3] = math.log(2.81256e+00) 
        logPartFn[4] = math.log(4.21040e+00)
    
    
    if ("LuIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.35394e+00) 
        logPartFn[3] = math.log(4.70352e+00) 
        logPartFn[4] = math.log(5.50348e+00)
    
    
    if ("HfI" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00797e+00) 
        logPartFn[2] = math.log(8.96794e+00) 
        logPartFn[3] = math.log(2.73353e+01) 
        logPartFn[4] = math.log(4.03170e+01)
    
    
    if ("HfII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00104e+00) 
        logPartFn[2] = math.log(7.28122e+00) 
        logPartFn[3] = math.log(2.20042e+01) 
        logPartFn[4] = math.log(2.94434e+01)
    
    
    if ("HfIII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.00000e+00) 
        logPartFn[3] = math.log(5.00000e+00) 
        logPartFn[4] = math.log(5.00000e+00)
    
    
    if ("TaI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.01856e+00) 
        logPartFn[2] = math.log(8.90727e+00) 
        logPartFn[3] = math.log(3.81227e+01) 
        logPartFn[4] = math.log(5.94676e+01)
    
    
    if ("TaII" == species):  
        logPartFn[0] = math.log(3.00006e+00) 
        logPartFn[1] = math.log(3.26126e+00) 
        logPartFn[2] = math.log(1.20456e+01) 
        logPartFn[3] = math.log(4.24778e+01) 
        logPartFn[4] = math.log(5.72237e+01)
    
    
    if ("TaIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00000e+00) 
        logPartFn[4] = math.log(4.00000e+00)
    
    
    if ("WI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.02634e+00) 
        logPartFn[2] = math.log(6.30546e+00) 
        logPartFn[3] = math.log(2.85590e+01) 
        logPartFn[4] = math.log(4.57837e+01)
    
    
    if ("WII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.05127e+00) 
        logPartFn[2] = math.log(6.98039e+00) 
        logPartFn[3] = math.log(2.94443e+01) 
        logPartFn[4] = math.log(4.35189e+01)
    
    
    if ("WIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00456e+00) 
        logPartFn[2] = math.log(3.26242e+00) 
        logPartFn[3] = math.log(1.74093e+01) 
        logPartFn[4] = math.log(2.62418e+01)
    
    
    if ("ReI" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.10431e+00) 
        logPartFn[3] = math.log(1.55905e+01) 
        logPartFn[4] = math.log(2.56949e+01)
    
    
    if ("ReII" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00000e+00) 
        logPartFn[2] = math.log(7.02641e+00) 
        logPartFn[3] = math.log(1.17977e+01) 
        logPartFn[4] = math.log(1.72060e+01)
    
    
    if ("ReIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.00000e+00) 
        logPartFn[3] = math.log(6.00000e+00) 
        logPartFn[4] = math.log(6.00000e+00)
    
    
    if ("OsI" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00193e+00) 
        logPartFn[2] = math.log(1.28046e+01) 
        logPartFn[3] = math.log(3.57251e+01) 
        logPartFn[4] = math.log(5.01909e+01)
    
    
    if ("OsII" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.00003e+01) 
        logPartFn[2] = math.log(1.29335e+01) 
        logPartFn[3] = math.log(2.68382e+01) 
        logPartFn[4] = math.log(3.34231e+01)
    
    
    if ("OsIII" == species):  
        logPartFn[0] = math.log(7.00000e+00) 
        logPartFn[1] = math.log(7.00000e+00) 
        logPartFn[2] = math.log(7.00000e+00) 
        logPartFn[3] = math.log(7.00000e+00) 
        logPartFn[4] = math.log(7.00000e+00)
    
    
    if ("IrI" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.00029e+01) 
        logPartFn[2] = math.log(1.43208e+01) 
        logPartFn[3] = math.log(3.28930e+01) 
        logPartFn[4] = math.log(4.25998e+01)
    
    
    if ("IrII" == species):  
        logPartFn[0] = math.log(1.10000e+01) 
        logPartFn[1] = math.log(1.10141e+01) 
        logPartFn[2] = math.log(1.64858e+01) 
        logPartFn[3] = math.log(3.43934e+01) 
        logPartFn[4] = math.log(4.27953e+01)
    
    
    if ("IrIII" == species):  
        logPartFn[0] = math.log(1.00000e+01) 
        logPartFn[1] = math.log(1.00000e+01) 
        logPartFn[2] = math.log(1.00000e+01) 
        logPartFn[3] = math.log(1.00000e+01) 
        logPartFn[4] = math.log(1.00000e+01)
    
    
    if ("PtI" == species):  
        logPartFn[0] = math.log(7.00192e+00) 
        logPartFn[1] = math.log(8.37770e+00) 
        logPartFn[2] = math.log(1.68661e+01) 
        logPartFn[3] = math.log(2.39027e+01) 
        logPartFn[4] = math.log(2.70210e+01)
    
    
    if ("PtII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00001e+00) 
        logPartFn[2] = math.log(7.18367e+00) 
        logPartFn[3] = math.log(1.45322e+01) 
        logPartFn[4] = math.log(1.81439e+01)
    
    
    if ("PtIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00000e+00) 
        logPartFn[2] = math.log(9.00000e+00) 
        logPartFn[3] = math.log(9.00000e+00) 
        logPartFn[4] = math.log(9.00000e+00)
    
    
    if ("AuI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.07431e+00) 
        logPartFn[3] = math.log(3.26015e+00) 
        logPartFn[4] = math.log(3.89945e+00)
    
    
    if ("AuII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00623e+00) 
        logPartFn[3] = math.log(1.73082e+00) 
        logPartFn[4] = math.log(2.36680e+00)
    
    
    if ("AuIII" == species):  
        logPartFn[0] = math.log(6.00000e+00) 
        logPartFn[1] = math.log(6.00000e+00) 
        logPartFn[2] = math.log(6.00000e+00) 
        logPartFn[3] = math.log(6.00000e+00) 
        logPartFn[4] = math.log(6.00000e+00)
    
    
    if ("HgI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00627e+00) 
        logPartFn[4] = math.log(1.03521e+00)
    
    
    if ("HgII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.01083e+00) 
        logPartFn[4] = math.log(2.04111e+00)
    
    
    if ("HgIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00459e+00) 
        logPartFn[4] = math.log(1.02282e+00)
    
    
    if ("TlI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.09532e+00) 
        logPartFn[3] = math.log(3.13616e+00) 
        logPartFn[4] = math.log(4.01172e+00)
    
    
    if ("TlII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00046e+00) 
        logPartFn[4] = math.log(1.00317e+00)
    
    
    if ("TlIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00000e+00) 
        logPartFn[3] = math.log(2.00006e+00) 
        logPartFn[4] = math.log(2.00068e+00)
    
        
    if ("PbI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.10102e+00) 
        logPartFn[3] = math.log(2.61747e+00) 
        logPartFn[4] = math.log(3.50725e+00)
    
    
    if ("PbII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00467e+00) 
        logPartFn[3] = math.log(2.31815e+00) 
        logPartFn[4] = math.log(2.52964e+00)
    
    
    if ("PbIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00005e+00) 
        logPartFn[4] = math.log(1.00051e+00)
    
    
    if ("BiI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.02047e+00) 
        logPartFn[3] = math.log(4.95911e+00) 
        logPartFn[4] = math.log(5.65786e+00)
    
    
    if ("BiII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00645e+00) 
        logPartFn[3] = math.log(1.51854e+00) 
        logPartFn[4] = math.log(1.91272e+00)
    
    
    if ("BiIII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.00019e+00) 
        logPartFn[3] = math.log(2.09519e+00) 
        logPartFn[4] = math.log(2.20117e+00)
    
    
    if ("PoI" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.02832e+00) 
        logPartFn[3] = math.log(5.51747e+00) 
        logPartFn[4] = math.log(5.89033e+00)
    
    
    if ("PoII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00000e+00) 
        logPartFn[4] = math.log(4.00000e+00)
    
    
    if ("PoIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("AtI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00297e+00) 
        logPartFn[4] = math.log(4.01505e+00)
    
    
    if ("AtII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.00000e+00) 
        logPartFn[3] = math.log(5.00000e+00) 
        logPartFn[4] = math.log(5.00000e+00)
    
    
    if ("AtIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00000e+00) 
        logPartFn[4] = math.log(4.00000e+00)
    
    
    if ("RnI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00086e+00) 
        logPartFn[4] = math.log(1.00996e+00)
    
    
    if ("RnII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00773e+00) 
        logPartFn[4] = math.log(4.02348e+00)
    
    
    if ("RnIII" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00000e+00) 
        logPartFn[2] = math.log(5.00000e+00) 
        logPartFn[3] = math.log(5.00000e+00) 
        logPartFn[4] = math.log(5.00000e+00)
    
    
    if ("FrI" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.01509e+00) 
        logPartFn[3] = math.log(4.72683e+00) 
        logPartFn[4] = math.log(8.72909e+00)
    
    
    if ("FrII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("FrIII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.00000e+00) 
        logPartFn[3] = math.log(4.00000e+00) 
        logPartFn[4] = math.log(4.00000e+00)
    
    
    if ("RaI" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.02509e+00) 
        logPartFn[3] = math.log(3.46852e+00) 
        logPartFn[4] = math.log(5.89341e+00)
    
    
    if ("RaII" == species):  
        logPartFn[0] = math.log(2.00000e+00) 
        logPartFn[1] = math.log(2.00000e+00) 
        logPartFn[2] = math.log(2.02050e+00) 
        logPartFn[3] = math.log(3.04735e+00) 
        logPartFn[4] = math.log(3.76227e+00)
    
    
    if ("RaIII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("AcI" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00977e+00) 
        logPartFn[2] = math.log(6.29803e+00) 
        logPartFn[3] = math.log(1.61130e+01) 
        logPartFn[4] = math.log(2.21832e+01)
    
    
    if ("AcII" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.99066e+00) 
        logPartFn[3] = math.log(9.40315e+00) 
        logPartFn[4] = math.log(1.34413e+01)
    
    
    if ("AcIII" == species):  
        logPartFn[0] = math.log(2.00057e+00) 
        logPartFn[1] = math.log(2.39921e+00) 
        logPartFn[2] = math.log(5.52353e+00) 
        logPartFn[3] = math.log(8.45689e+00) 
        logPartFn[4] = math.log(9.28067e+00)
    
    
    if ("ThI" == species):  
        logPartFn[0] = math.log(5.00000e+00) 
        logPartFn[1] = math.log(5.00263e+00) 
        logPartFn[2] = math.log(1.10507e+01) 
        logPartFn[3] = math.log(4.50659e+01) 
        logPartFn[4] = math.log(5.99031e+01)
    
    
    if ("ThII" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.09432e+00) 
        logPartFn[2] = math.log(1.45463e+01) 
        logPartFn[3] = math.log(6.18533e+01) 
        logPartFn[4] = math.log(8.01502e+01)
    
    
    if ("ThIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00000e+00) 
        logPartFn[2] = math.log(9.00000e+00) 
        logPartFn[3] = math.log(9.00000e+00) 
        logPartFn[4] = math.log(9.00000e+00)
    
    
    if ("PaI" == species):  
        logPartFn[0] = math.log(1.20011e+01) 
        logPartFn[1] = math.log(1.30217e+01) 
        logPartFn[2] = math.log(4.32464e+01) 
        logPartFn[3] = math.log(1.22610e+02) 
        logPartFn[4] = math.log(1.49295e+02)
    
    
    if ("PaII" == species):  
        logPartFn[0] = math.log(9.00122e+00) 
        logPartFn[1] = math.log(1.01871e+01) 
        logPartFn[2] = math.log(4.27330e+01) 
        logPartFn[3] = math.log(9.03874e+01) 
        logPartFn[4] = math.log(1.01197e+02)
    
    
    if ("PaIII" == species):  
        logPartFn[0] = math.log(1.20000e+01) 
        logPartFn[1] = math.log(1.20000e+01) 
        logPartFn[2] = math.log(1.20000e+01) 
        logPartFn[3] = math.log(1.20000e+01) 
        logPartFn[4] = math.log(1.20000e+01)
    
    
    if ("UI" == species):  
        logPartFn[0] = math.log(1.30115e+01) 
        logPartFn[1] = math.log(1.48466e+01) 
        logPartFn[2] = math.log(3.35353e+01) 
        logPartFn[3] = math.log(1.07772e+02) 
        logPartFn[4] = math.log(1.36160e+02)
    
    
    if ("UII" == species):  
        logPartFn[0] = math.log(1.04902e+01) 
        logPartFn[1] = math.log(1.60511e+01) 
        logPartFn[2] = math.log(5.15324e+01) 
        logPartFn[3] = math.log(1.55945e+02) 
        logPartFn[4] = math.log(1.91265e+02)
    
    
    if ("UIII" == species):  
        logPartFn[0] = math.log(9.00000e+00) 
        logPartFn[1] = math.log(9.00000e+00) 
        logPartFn[2] = math.log(9.00000e+00) 
        logPartFn[3] = math.log(9.00000e+00) 
        logPartFn[4] = math.log(9.00000e+00)
    
    
    if ("H-" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("C-" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.08591e+00) 
        logPartFn[3] = math.log(5.67986e+00) 
        logPartFn[4] = math.log(6.40004e+00)
    
    
    if ("O-" == species):  
        logPartFn[0] = math.log(4.28183e+00) 
        logPartFn[1] = math.log(5.20160e+00) 
        logPartFn[2] = math.log(5.83718e+00) 
        logPartFn[3] = math.log(5.93732e+00) 
        logPartFn[4] = math.log(5.94969e+00)
    
    
    if ("F-" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00) 
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)
    
    
    if ("Si-" == species):  
        logPartFn[0] = math.log(4.00000e+00) 
        logPartFn[1] = math.log(4.00000e+00) 
        logPartFn[2] = math.log(4.38825e+00) 
        logPartFn[3] = math.log(7.70408e+00) 
        logPartFn[4] = math.log(8.92238e+00)

    
    if ("S-" == species):  
        logPartFn[0] = math.log(4.00949e+00) 
        logPartFn[1] = math.log(4.49753e+00) 
        logPartFn[2] = math.log(5.58609e+00) 
        logPartFn[3] = math.log(5.83344e+00) 
        logPartFn[4] = math.log(5.86560e+00)
    
    
    if ("Cl-" == species):  
        logPartFn[0] = math.log(1.00000e+00) 
        logPartFn[1] = math.log(1.00000e+00)
        logPartFn[2] = math.log(1.00000e+00) 
        logPartFn[3] = math.log(1.00000e+00) 
        logPartFn[4] = math.log(1.00000e+00)

    return logPartFn

#   } //end of method getPartFn2

