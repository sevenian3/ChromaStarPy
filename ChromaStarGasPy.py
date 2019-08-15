# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the main source file for ChromaStarPy.  We start here.

"""

"""
/*
 * The openStar project: stellar atmospheres and spectra
 *
 * ChromaStarPy
 *
 * Version 2019-07-08
 * Use date based versioning with ISO 8601 date (YYYY-MM-DD)
 *
 * December 2017
 * 
 * C. Ian Short
 * Saint Mary's University
 * Department of Astronomy and Physics
 * Institute for Computational Astrophysics (ICA)
 * Halifax, NS, Canada
 *  * ian.short@smu.ca
 * www.ap.smu.ca/~ishort/
 *
 *
 * Philip D. Bennett
 * Saint Mary's University
 * Department of Astronomy and Physics
 * Institute for Computational Astrophysics (ICA)
 * Halifax, NS, Canada
 *
 *
 *  * Co-developers:
 *  *
 *  * Lindsey Burns (SMU) - 2017 - "lburns"
 *  * Jason Bayer (SMU) - 2017 - "JB"
 *
 * 
 * Open source pedagogical computational stellar astrophysics
 *
 * 1D, static, plane-parallel, LTE stellar atmospheric model
 * Voigt spectral line profile
 *
 * July 2019 - Equation sof state (EOS) and chemical/ionization equilibrium now computed
 * with Phil Bennett's "GAS" package.  Includes 51 molecules, including 16 polyatomic
 * molecules
 * 
 * 
 *
 * Suitable for pedagogical purposes only
 * 
 *
 * python V. 3
 *
 * System requirements for Java version: Java run-time environment (JRE)
 * System requirements for JavaScript version: JavaScript intrepretation enabld in WWW browser (usually by default)
 *
 * Code provided "as is" - there is no formal support 
 *
 */

"""

"""/*
 * The MIT License (MIT)
 * Copyright (c) 2016 C. Ian Short 
 *
 * Permission is hereby granted, free of charge, to any person 
 obtaining a copy of this software and associated documentation 
 files (the "Software"), to deal in the Software without 
 restriction, including without limitation the rights to use, 
 copy, modify, merge, publish, distribute, sublicense, and/or 
 sell copies of the Software, and to permit persons to whom the 
 Software is furnished to do so, subject to the following 
 conditions:
 *
 * The above copyright notice and this permission notice shall 
 be included in all copies or substantial portions of the 
 Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY 
 KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
 WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
 AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
 OTHER DEALINGS IN THE SOFTWARE.
*
 */"""
 
#from decimal import Decimal as D

import Input
import Restart
import Useful
import LamGrid
import TauScale
import ScaleSolar
import State
import Hydrostat
import ScaleT4250g20
import ScaleT5000
import ScaleT10000
import LevelPopsGasServer
import Kappas
import KappasMetal
import KappasRaylGas
import DepthScale
import IonizationEnergy
import PartitionFn
import AtomicMass
import ToolBox
import Thetas
import MolecData
import Jola
import SpecSyn
import SpecSyn2
import HjertingComponents
import LineGrid
import LineProf
import LineKappa
import LineTau2
import FormalSoln
import Flux
import LDC
import PostProcess

# GAS ESO/checmial equilibrium package, ported from Phil Bennett/Athena
#Requires special python ports of some blas and lapack routines - part of CSPy distribution
#import CSBlockData
#import GasData
#import GasData2
import CSGsRead2
import CSGasEst
import CSGas

#from Documents.ChromaStarPy.GAS import BlockData
#from Documents.ChromaStarPy.GAS.GsRead2 import gsread
#from Documents.ChromaStarPy.GAS.GasEst import gasest
#from Documents.ChromaStarPy.GAS.Gas import gas

#plotting:
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
import math
import numpy

from functools import reduce
import subprocess
import os
import sys

#############################################
#
#
#
#    Initial set-up:
#     - import all python modules
#     - set input parameters for *everything* (atmospheric modeling
#        spectrum synthesis, user-defined 2-level atom & line, 
#        post-processing, ...)
#     - prepare reference solar model and template models
#        for re-scaling to initial guess
#     
#
#
##############################################


#Detect python version
pythonV = sys.version_info
if pythonV[0] != 3:
    print("")
    print("")
    print(" ********************************************* ")
    print("")
    print("WARNING!!  WARNING!!   WARNING!!")
    print("")
    print("")
    print("ChromaStarPy developed for python V. 3!!" )
    print("")
    print("May not work in other version")
    print("")
    print("")
    print("*********************************************** ")
    print("")
    print("")



thisOS = "unknown" #default
myOS= ""
#returns 'posix' form unix-like OSes and 'nt' for Windows??
thisOS = os.name
print("")
print("Running on OS: ", thisOS)
print("")

absPath0 = "./"  #default

if thisOS == "nt": 
    #windows
    absPath0 = subprocess.check_output("cd", shell=True)    
    backSpace = 2
elif thisOS == "posix":
    absPath0 = subprocess.check_output("pwd", shell=True)
    backSpace = 1
    
absPath0 = bytes.decode(absPath0)

#remove OS_dependent trailing characters 'r\n'
nCharsPath = len(absPath0)
nCharsPath -= backSpace
absPath0 = absPath0[0: nCharsPath]

slashIndex = absPath0.find('\\') #The first backslash is the escape character!
while slashIndex != -1:
    #python strings are immutable:
    absPathCopy = absPath0[0: slashIndex]
    absPathCopy += '/'
    absPathCopy += absPath0[slashIndex+1: len(absPath0)]
    absPath0 = absPathCopy
    #print(absPathCopy, absPath0)
    slashIndex = absPath0.find('\\')
    
absPath = absPath0 + '/'

makePlot = Input.makePlot
print("")
print("Will make plot: ", makePlot)
print("")
#stop
#color platte for plt plotting
#palette = ['black', 'brown','red','orange','yellow','green','blue','indigo','violet']
#grayscale
#stop
#Grayscale:
numPal = 12
palette = ['0.0' for i in range(numPal)]
delPal = 0.04
#for i in range(numPal):
#    ii = float(i)
#    helpPal = 0.481 - ii*delPal
#    palette[i] = str(helpPal) 
      
palette = [ str( 0.481 - float(i)*delPal ) for i in range(numPal) ]
numClrs = len(palette)


#General file for printing ad hoc quantities
dbgHandle = open("debug.out", 'w')
outPath = absPath + "/Outputs/"

fileStem = Input.fileStem+"Gas"
#Not usedoutFileString = outPath+fileStem+"Gas.*"
print(" ")
print("Writing to files ", fileStem)
print(" ")


""" test
#// Representative spectral line and associated atomic parameters
#//NaID
userLam0 = 589.592   #nm 
userA12 = 6.24    #// A_12 logarithmic abundance = log_10(N/H_H) = 12
userLogF = math.log10(math.e)*math.log(0.320)  #// log(f) oscillaotr strength // saturated line
testAij = math.log(6.14e+07)
userStage = 0 #//ionization stage of user species (0 (I) - 3 (IV)
userChiI1 = 5.5 #// ground state chi_I, eV
userChiI2 = 8.0 #// 1st ionized state chi_I, eV
userChiI3 = 20.0 #// 2nd ionized state chi_I, eV
userChiI4 = 40.0  #// 3rd ionized state chi_I, eV
userChiL = 0.0 #// lower atomic E-level, eV
userGw1 = 2  #// ground state state. weight or partition fn (stage I) - unitless
userGw2 = 1  #// ground state state. weight or partition fn (stage II) - unitless
userGw3 = 1  #// ground state state. weight or partition fn (stage III) - unitless
userGw4 = 1  #// ground state state. weight or partition fn (stage IV) - unitless
userGwL = 2 #// lower E-level state. weight - unitless
userMass = 22.0  #//amu
userLogGammaCol = 1.0  #log_10 Lorentzian broadening enhancement factor
"""

#True for Voigt computed with true convolution instead of power-law expansion approx - probably not working well right now
ifVoigt = False
#Scattering term in line source fn - not yet enabled   
ifScatt = False 

#// Argument 0: Effective temperature, Teff, in K:
#teff = float(teffStr) 
teff = Input.teff       
#print(type(teff))

#// Argument 1: Logarithmic surface gravity, g, in cm/s/s:
#logg = float(loggStr)
logg = Input.logg

#//Argument 2: Linear sclae factor for solar Rosseland oapcity distribution
#log10ZScale = float(logZStr)
log10ZScale = Input.log10ZScale



#//Argument 3: Stellar mass, M, in solar masses
#massStar = float(massStarStr)
massStar = Input.massStar

#// Sanity check:
F0Vtemp = 7300.0;  #// Teff of F0 V star (K) 
                          
if (teff < 3000.0): 
    teff = 3000.0
#    teffStr = "3000"

if (teff > 50000.0):
    teff = 50000.0
#    teffStr = "50000"
    
#//logg limit is strongly Teff-dependent:
minLogg = 3.0; #//safe initialization
minLoggStr = "3.0";
if (teff <= 4000.0):
    minLogg = 0.0
#    minLoggStr = "0.0"
elif ((teff > 4000.0) and (teff <= 5000.0)): 
    minLogg = 0.5
#    minLoggStr = "0.5"
elif ((teff > 5000.0) and (teff <= 6000.0)): 
    minLogg = 1.5
#    minLoggStr = "1.5"
elif ((teff > 6000.0) and (teff <= 7000.0)): 
    minLogg = 2.0
#    minLoggStr = "2.0"
elif ((teff > 7000.0) and (teff < 9000.0)): 
    minLogg = 2.5
#    minLoggStr = "2.5"
elif (teff >= 9000.0): 
    minLogg = 3.0
#    minLoggStr = "3.0"

if (logg < minLogg): 
    logg = minLogg
#    loggStr = minLoggStr

if (logg > 7.0): 
    logg = 7.0
#    loggStr = "7.0"
        
if (log10ZScale < -3.0): 
    log10ZScale = -3.0
#    logZStr = "-3.0"
        
if (log10ZScale > 1.0): 
    log10ZScale = 1.0
#    logZStr = "1.0"

if (massStar < 0.1): 
    massStar = 0.1
#    massStarStr = "0.1"
        
if (massStar > 20.0): 
    massStar = 20.0
#    massStarStr = "20.0"

grav = math.pow(10.0, logg)
zScale = math.pow(10.0, log10ZScale)

#// Argument 5: microturbulence, xi_T, in km/s:
#xiT = float(xiTStr)
xiT = Input.xiT

if (xiT < 0.0): 
    xiT = 0.0
#    xitStr = "0.0"
        
if (xiT > 8.0): 
    xiT = 8.0
#    xitStr = "8.0"
    
#// Add new variables to hold values for new metallicity controls lburns
#logHeFe = float(logHeFeStr)  #// lburns
#logCO = float(logCOStr) #// lburns
#logAlphaFe = float(logAlphaFeStr) #// lburns
logHeFe = Input.logHeFe
logCO = Input.logCO
logAlphaFe = Input.logAlphaFe

#// For new metallicity commands lburns
#// For logHeFe: (lburns)
if (logHeFe < -1.0):
    logHeFe = -1.0;
#    logHeFeStr = "-1.0";
    
if (logHeFe > 1.0):
    logHeFe = 1.0
#    logHeFeStr = "1.0"
    
#// For logCO: (lburns)
if (logCO < -2.0):
    logCO = -2.0
#    logCOStr = "-2.0"

if (logCO > 2.0):
    logCO = 2.0
#    logCOStr = "2.0"

#// For logAlphaFe: (lburns)
if (logAlphaFe < -0.5):
    logAlphaFe = -0.5
#    logAlphaFeStr = "-0.5"

if (logAlphaFe > 0.5):
    logAlphaFe = 0.5
#    logAlphaFeStr = "0.5"

        

#// Argument 6: minimum ratio of monochromatic line center to background continuous
#// extinction for inclusion of linein spectrum 
#lineThreshStr = args[5];
#lineThreshStr = "-3.0"; #//test
#lineThresh = float(lineThreshStr)
lineThresh = Input.lineThresh    

if (lineThresh < -4.0): 
    lineThresh = -4.0
#    lineThreshStr = "-4.0"
        
if (lineThresh > 6.0): 
    lineThresh = 6.0
#    lineThreshStr = "6.0"
        

#// Argument 7: minimum ratio of monochromatic line center to background continuous
#voigtThresh = float(voigtThreshStr);
voigtThresh = Input.voigtThresh    

if (voigtThresh < lineThresh): 
    voigtThresh = lineThresh
#    voigtThreshStr = lineThreshStr
        
if (voigtThresh > 6.0): 
    voigtThresh = 6.0
#    voigtThreshStr = "6.0"
        
#//User defined spetrum synthesis region:
lamUV = 260.0;
lamIR = 2600.0;

#// Argument 8: starting wavelength for spectrum synthesis 

#lambdaStart = float(lambdaStartStr)
lambdaStart = Input.lambdaStart

if (lambdaStart < lamUV): 
    lambdaStart = lamUV
#    lambdaStartStr = str(lamUV)
        
if (lambdaStart > lamIR - 1.0): 
    lambdaStart = lamIR - 1.0
#    lambdaStartStr = str(lamIR - 1.0)
        
#// Argument 9: stopping wavelength for spectrum synthesis 
#lambdaStop = float(lambdaStopStr)
lambdaStop = Input.lambdaStop    

if (lambdaStop < lamUV + 1.0): 
    lambdaStop = lamUV + 1.0
#    lambdaStartStr = str(lamUV + 1.0)
        
if (lambdaStop > lamIR):
    lambdaStop = lamIR
#    lambdaStartStr = str(lamIR)

#//Prevent negative or zero lambda range:
if (lambdaStop <= lambdaStart):
    lambdaStop = lambdaStart + 0.5 #//0.5 nm = 5 A
#    lambdaStopStr = str(lambdaStop)

"""
#//limit size of synthesis region (nm):
maxSynthRange = 5.0 #//set default to minimum value //nm
#//if we're not in the blue we can get away wth more:
if (lambdaStart > 350.0):
    maxSynthRange = 10.0
if (lambdaStart > 550.0):
    maxSynthRange = 20.0
if (lambdaStart > 700.0):
    maxSynthRange = 50.0
if (lambdaStart > 1000.0):
    maxSynthRange = 100.0
if (lambdaStart > 1600.0):
    maxSynthRange = 200.0

#//console.log("maxSynthRange " + maxSynthRange + " lambdaStop " + lambdaStop);
if (lambdaStop > (lambdaStart+maxSynthRange)):
    #//console.log("lambdaStop > (lambdaStart+maxSynthRange) condition");
    lambdaStop = lambdaStart + maxSynthRange #//10 nm = 100 A
    lambdaStopStr = str(lambdaStop)
#//console.log("lambdaStop " + lambdaStop);
"""
if (lambdaStop > lamIR):
    #//console.log("lambdaStop > lamIR condition");
    lambdaStop = lamIR
#    lambdaStopStr = str(lamIR)

#//console.log("lambdaStop " + lambdaStop);

nm2cm = 1.0e-7
cm2nm = 1.0e7     
lambdaStart = nm2cm * lambdaStart #//nm to cm 
lambdaStop = nm2cm * lambdaStop  #//nm to cm
lamUV = nm2cm * lamUV
lamIR = nm2cm * lamIR
      
#//argument 10: line sampling selection (fine or coarse)
#sampling = "fine"

sampling = Input.sampling
vacAir = Input.vacAir

#// Argument 11: Lorentzian line broadening enhancement 
#logGammaCol = float(logGammaColStr)
logGammaCol = Input.logGammaCol

if (logGammaCol < 0.0):
    logGammaCol = 0.0
#    logGammaColStr = "0.0"
        
if (logGammaCol > 1.0):
    logGammaCol = 1.0
#    logGammaColStr = "1.0"
        
#// Argument 12: log_10 gray mass extinction fudge 
#logKapFudge = float(logKapFudgeStr)
logKapFudge = Input.logKapFudge

if (logKapFudge < -2.0):
    logKapFudge = -2.0
#    logKapFudgeStr = "-2.0"
        
if (logKapFudge > 2.0):
    logKapFudge = 2.0
#    logKapFudgeStr = "2.0"
        

#// Argument 13: macroturbulent velocity broadening parameter (sigma) (km/s) 
#macroV = float(macroVStr)
macroV = Input.macroV    
#// Argument 14: surface equatorial linear rotational velocity (km/s) 
#rotV  = float(rotVStr)
rotV = Input.rotV
#// Argument 15: inclination of rotation axis wrt line-of-sight (degrees) 
#rotI  = float(rotIStr)
rotI = Input.rotI
#print("Before test rotI ", rotI, " rotIStr ", rotIStr)
#// Argument 16: number of outer HSE-EOS-Opac iterations
#nOuterIter = int(nOuterIterStr)
nOuterIter = Input.nOuterIter
#// Argument 17: number of inner Pe-IonFrac iterations
#nInnerIter = int(nInnerIterStr)
nInnerIter = Input.nInnerIter
#//Argument 18: If TiO JOLA bands should be included:
#ifTiO = int(ifTiOStr)
ifMols = Input.ifMols

if (macroV < 0.0):
    macroV = 0.0
#    macroVStr = "0.0"
        
if (macroV > 8.0):
    macroV = 8.0
#    macroVStr = "8.0"
        

if (rotV < 0.0):
    rotV = 0.0
#    rotVStr = "0.0"
        
if (rotV > 300.0):
    rotV = 300.0
#    rotVStr = "300.0"
        

if (rotI < 0.0): 
    rotI = 0.0
#    rotIStr = "0.0"
        
if (rotI > 90.0):
    rotI = 90.0
#    rotIStr = "90.0"
        
if (nOuterIter < 1): 
    nOuterIter = 1
#    nOuterIterStr = "1"
        
if (nOuterIter > 30):
    nOuterIter = 30
#    nOuterIterStr = "12"
        
if (nInnerIter < 1):
    nInnerIter = 1
#    nInnerIterStr = "1"
        
if (nInnerIter > 30):
    nInnerIter = 30
#    nInnerIterStr = "12"
    
#print("After test rotI ", rotI, " rotIStr ", rotIStr)    
    
#//For rotation:
inclntn = math.pi * rotI / 180.0  #//degrees to radians
vsini = rotV * math.sin(inclntn)

#// Argument 19: wavelength of narrow Gaussian filter in nm
#diskLambda = float(diskLambdaStr)  #//nm
diskLambda = Input.diskLambda
#// Argument 20: bandwidth, sigma, of narrow Gaussian filter in nm
#diskSigma = float(diskSigmaStr)  #//nm
diskSigma = Input.diskSigma
#// Argument 21: radial velocity of star in km/s
#RV = float(RVStr)  #//nm   
RV = Input.RV
#// Argument 22: Spectrum synthesis wavelength scale options:

if (diskLambda < lamUV):
    diskLambda = lamUV
#    diskLambdaStr = str(lamUV)    
if (diskLambda > lamIR):
    diskLambda = lamIR
#    diskLambdaStr = str(lamIR)
    
if (diskSigma < 0.005):
    diskSigma = 0.005
#    diskSigmaStr = "0.005";
if (diskSigma > 10.0):
    diskSigma = 10.0
#    diskSigmaStr = "10"
    
if (RV < -200.0):
    RV = -200.0
#    RVStr = "-200"
if (RV > 200.0):
    RV = 200.0
#    RVStr = "200"
    
#vacAir = "vacuum" #//test

#// Representative spectral line and associated atomic parameters
#//
"""
userLam0 = float(userLam0Str)
userA12 = float(userA12Str)
userLogF = float(userLogFStr)
userStage = float(userStageStr)
userChiI1 = float(userChiI1Str)
userChiI2 = float(userChiI2Str)
userChiI3 = float(userChiI3Str)
userChiI4 = float(userChiI4Str)
userChiL = float(userChiLStr)
userGw1 = float(userGw1Str)
userGw2 = float(userGw2Str)
userGw3 = float(userGw3Str)
userGw4 = float(userGw4Str)
userGwL = float(userGwLStr)
userMass = float(userMassStr)
userLogGammaCol = float(userGammaColStr)
"""
userLam0 = Input.userLam0
userA12 = Input.userA12
userLogF = Input.userLogF
userStage = Input.userStage
userChiI1 = Input.userChiI1
userChiI2 = Input.userChiI2
userChiI3 = Input.userChiI3
userChiI4 = Input.userChiI4
userChiL = Input.userChiL
userGw1 = Input.userGw1
userGw2 = Input.userGw2
userGw3 = Input.userGw3
userGw4 = Input.userGw4
userGwL = Input.userGwL
userMass = Input.userMass
userLogGammaCol = Input.userLogGammaCol

if (userLam0 < 260.0):
    userLam0 = 260.0
#    userLamStr = "260"
if (userLam0 > 2600.0):
    userLam0 = 2600.0
#    userLamStr = "2600"

if (userA12 < 2.0):
    userA12 = 2.0
#    userNStr = "2.0"
#//Upper limit set high to accomodate Helium!:
if (userA12 > 11.0):
    userA12 = 11.0
#    userNStr = "11.0"

if (userLogF < -6.0):
    userLogF = -6.0
#    userFStr = "-6.0"
if (userLogF > 1.0):
    userLogF = 1.0
#    userFStr = "1.0"

if ( (userStage != 0) and (userStage != 1) and (userStage != 2) and (userStage != 3) ):
    userStage = 0
    userStageStr = "I"

if (userChiI1 < 3.0):
    userChiI1 = 3.0
#    userIonStr = "3.0"
if (userChiI1 > 25.0):
    userChiI1 = 25.0
#    userIonStr = "25.0"

if (userChiI2 < 5.0):
    userChiI2 = 5.0
#    userIonStr = "5.0"
if (userChiI2 > 55.0):
    userChiI2 = 55.0
#    userIonStr = "55.0"

if (userChiI3 < 5.0):
    userChiI3 = 5.0
#    userIonStr = "5.0"
if (userChiI3 > 55.0):
    userChiI3 = 55.0
#    userIonStr = "55.0"

if (userChiI4 < 5.0):
    userChiI4 = 5.0
#    userIonStr = "5.0"
if (userChiI4 > 55.0):
    userChiI4 = 55.0
#    userIonStr = "55.0"

#// Note: Upper limit of chiL depends on value of chiI1 above!
if (userChiL < 0.0):
    userChiL = 0.0 #// Ground state case!
#    userExcStr = "0.0"
if ( (userStage == 0) and (userChiL >= userChiI1) ):
    #//ionized = false;
    userChiL = 0.9 * userChiI1
#    userExcStr = userIonStr

if ( (userStage == 1) and (userChiL >= userChiI2) ):
    #//ionized = false;
    userChiL = 0.9 * userChiI2
#    userExcStr = userIonStr

if ( (userStage == 2) and (userChiL >= userChiI3) ):
    #//ionized = false;
    userChiL = 0.9 * userChiI3
#    userExcStr = userIonStr

if ( (userStage == 3) and (userChiL >= userChiI4) ):
    #//ionized = false;
    userChiL = 0.9 * userChiI4
#    userExcStr = userIonStr

if (userGw1 < 1.0):
    userGw1 = 1.0
#    userWghtStr = "1"
if (userGw1 > 100.0):
    userGw1 = 100.0
#    userWghtStr = "100"

if (userGw2 < 1.0):
    userGw2 = 1.0
#    userWghtStr = "1";
if (userGw2 > 100.0):
    userGw2 = 100.0
#    userWghtStr = "100";

if (userGw3 < 1.0):
    userGw3 = 1.0
#    userWghtStr = "1"
if (userGw3 > 100.0):
    userGw3 = 100.0
#    userWghtStr = "100"

if (userGw4 < 1.0):
    userGw4 = 1.0
#    userWghtStr = "1"
if (userGw4 > 100.0):
    userGw4 = 100.0
#    userWghtStr = "100"

if (userGwL < 1.0):
    userGwL = 1.0
#    userLWghtStr = "1"
if (userGwL > 100.0):
    userGwL = 100.0
#    userLWghtStr = "100"

if (userMass < 1.0):
    userMass = 1.0
#    userMassStr = "1.0"
if (userMass > 200.0):
    userMass = 200.0
#    userMassStr = "200"
    
if (userLogGammaCol < 0.0):
    userLogGammaCol = 0.0
#    useLogGammaColStr = "0.0"
if (userLogGammaCol > 1.0):
    userLogGammaCol = 1.0
#    useLogGammaColStr = "1.0"

userLam0 = userLam0 * nm2cm #// line centre lambda from nm to cm
#stop
#Create output file

"""
#File for structure output:
strucStem = "Teff" + teffStr + "Logg" + loggStr + "Z" + logZStr + "M" + massStarStr+"xiT"+xiTStr + \
"HeFe" + logHeFeStr + "CO" + logCOStr + "AlfFe" + logAlphaFeStr + "v" + runVers
strucFile = "struc." + strucStem + ".out"
specFile = "spec." + strucStem + "L"+lambdaStartStr+"-"+lambdaStopStr+"xiT"+xiTStr+"LThr"+lineThreshStr+ \
"GamCol"+logGammaColStr+"Mac"+macroVStr+"Rot"+rotVStr+"-"+rotIStr+"RV"+RVStr + ".out"
sedFile = "sed." + strucStem + "L"+lambdaStartStr+"-"+lambdaStopStr+"xiT"+xiTStr+"lThr"+lineThreshStr+ \
"Mac" + macroVStr + "Rot"+rotVStr+"-"+rotIStr+"RV"+ RVStr + ".out" 
ldcFile = "ldc." + strucStem + "L" + diskLambdaStr + "S" + diskSigmaStr + ".out"
lineFile = "line." + strucStem + "L0" + userLam0Str + ".out"
"""
#Echo input parameters *actually used* to console:
inputParamString = "Teff " + str(teff) + " logg " + str(logg) + " [Fe/H] " + str(log10ZScale) + " massStar " + \
      str(massStar) + " xiT " + str(xiT) + " HeFe " + str(logHeFe) + " CO " + str(logCO) + " AlfFe " + str(logAlphaFe) + \
       " lineThresh " + str(lineThresh) + " voigtThresh " + \
      str(voigtThresh) + " lambda0 " + str(lambdaStart) + " lambda1 " + str(lambdaStop) + " logGamCol " + \
      str(logGammaCol) + " logKapFudge " + str(logKapFudge) + " macroV " + str(macroV) + " rotV " + str(rotV) + \
      " rotI " + str(rotI) + " RV " + str(RV) + " nInner " + str(nInnerIter) + " nOuter " + str(nOuterIter) + \
      " ifMols " + str(ifMols) + " sampling " + sampling
print(inputParamString)

#stop
#// Wavelengths in Air : 
#    if ($("#air").is(":checked")) {
#        vacAir = $("#air").val(); // radio 
#    }
#// Wavelengths in vacuum: (default)
#    if ($("#vacuum").is(":checked")) {
#       vacAir = $("#vacuum").val(); // radio 
#    }
    
#//
#// ************************ 
#//
#//  OPACITY  PROBLEM #1 - logFudgeTune:  late type star coninuous oapcity needs to have by multiplied 
#//  by 10.0^0.5 = 3.0 for T_kin(tau~1) to fall around Teff and SED to look like B_lmabda(Trad=Teff).
#//   - related to Opacity problem #2 in LineKappa.lineKap() - ??
#//
logFudgeTune = 0.0
#//sigh - don't ask me - makes the Balmer lines show up around A0:
if (teff <= F0Vtemp):
    logFudgeTune = 0.5
    #logFudgeTune = 0.0
      
if (teff > F0Vtemp):
    logFudgeTune = 0.0

logTotalFudge = logKapFudge + logFudgeTune

logE = math.log10(math.e) #// for debug output
logE10 = math.log(10.0) #//natural log of 10

#//Gray structure and Voigt line code code begins here:
#// Initial set-up:
#// optical depth grid
numDeps = 48
log10MinDepth = -6.0
log10MaxDepth = 2.0
#//int numThetas = 10;  #// Guess

#//wavelength grid (cm):
lamSetup = [ 0.0 for i in range(3) ]
#for i in range(3):
#    lamSetup.append(0.0)

lamSetup[0] = 260.0 * nm2cm  #// test Start wavelength, cm
#lamSetup[0] = 100.0 * 1.0e-7;  // test Start wavelength, cm
lamSetup[1] = 2600.0 * nm2cm #// test End wavelength, cm
lamSetup[2] = 250;  #// test number of lambda
#//int numLams = (int) (( lamSetup[1] - lamSetup[0] ) / lamSetup[2]) + 1;  
numLams = int(lamSetup[2])

#//CONTINUUM lambda scale (nm)
lambdaScale = LamGrid.lamgrid(numLams, lamSetup) #//cm
        
#// Solar parameters:
teffSun = 5778.0
loggSun = 4.44
gravSun = math.pow(10.0, loggSun)
log10ZScaleSun = 0.0
zScaleSun = math.exp(log10ZScaleSun)

#//Solar units:
massSun = 1.0
radiusSun = 1.0
#//double massStar = 1.0; //solar masses // test
logRadius = 0.5 * (math.log(massStar) + math.log(gravSun) - math.log(grav))
radius = math.exp(logRadius); #//solar radii
#//double radius = Math.sqrt(massStar * gravSun / grav); // solar radii
logLum = 2.0 * math.log(radius) + 4.0 * math.log(teff / teffSun)
bolLum = math.exp(logLum) #// L_Bol in solar luminosities 
#//cgs units:
rSun = 6.955e10 #// solar radii to cm

cgsRadius = radius * rSun
omegaSini = (1.0e5 * vsini) / cgsRadius #// projected rotation rate in 1/sec
macroVkm = macroV * 1.0e5  #//km/s to cm/s

#//Composition by mass fraction - needed for opacity approximations
#//   and interior structure
massX = 0.70 #//Hydrogen
massY = 0.28 #//Helium
massZSun = 0.02 #// "metals"
massZ = massZSun * zScale #//approximation

#//double logNH = 17.0

#//
#////Detailed checmical composition:
#//Abundance table adapted from PHOENIX V. 15 input bash file
#// Grevesse Asplund et al 2010
#//Solar abundances:
#// c='abundances, Anders & Grevesse',

nelemAbnd = 41
numStages = 7
  
nome = [0 for i in range(nelemAbnd)] 
eheu = [0.0 for i in range(nelemAbnd)] #log_10 "A_12" values
logAz = [0.0 for i in range(nelemAbnd)] #N_z/H_H for element z
cname = ["" for i in range(nelemAbnd)]
logNH = [0.0 for i in range(numDeps)]
#double[][] logNz = new double[nelemAbnd][numDeps]; //N_z for element z
#logNz *normally* holds total population of that element over all ionization stages
logNz = [ [ 0.0 for i in range(numDeps) ] for j in range(nelemAbnd) ] #N_z for element z
#double[][][] masterStagePops = new double[nelemAbnd][numStages][numDeps];
masterStagePops = [ [ [ 0.0 for i in range(numDeps) ] for j in range(numStages) ] for k in range(nelemAbnd) ]

#//nome is the Kurucz code - in case it's ever useful
nome[0]=   100 
nome[1]=   200 
nome[2]=   300 
nome[3]=   400 
nome[4]=   500 
nome[5]=   600 
nome[6]=   700 
nome[7]=   800 
nome[8]=   900 
nome[9]=  1000 
nome[10]=  1100 
nome[11]=  1200 
nome[12]=  1300 
nome[13]=  1400 
nome[14]=  1500 
nome[15]=  1600 
nome[16]=  1700 
nome[17]=  1800 
nome[18]=  1900 
nome[19]=  2000 
nome[20]=  2100 
nome[21]=  2200 
nome[22]=  2300 
nome[23]=  2400 
nome[24]=  2500 
nome[25]=  2600 
nome[26]=  2700 
nome[27]=  2800 
nome[28]=  2900
nome[29]=  3000 
nome[30]=  3100 
nome[31]=  3600 
nome[32]=  3700 
nome[33]=  3800 
nome[34]=  3900 
nome[35]=  4000
nome[36]=  4100 
nome[37]=  5600 
nome[38]=  5700
nome[39]=  5500  
nome[40]=  3200  
#//log_10 "A_12" values:
eheu[0]= 12.00  
eheu[1]= 10.93 
eheu[2]=  1.05
eheu[3]=  1.38  
eheu[4]=  2.70 
eheu[5]=  8.43
eheu[6]=  7.83  
eheu[7]=  8.69 
eheu[8]=  4.56
eheu[9]=  7.93  
eheu[10]=  6.24
eheu[11]=  7.60  
eheu[12]=  6.45 
eheu[13]=  7.51
eheu[14]=  5.41  
eheu[15]=  7.12 
eheu[16]=  5.50
eheu[17]=  6.40  
eheu[18]=  5.03 
eheu[19]=  6.34
eheu[20]=  3.15  
eheu[21]=  4.95 
eheu[22]=  3.93
eheu[23]=  5.64  
eheu[24]=  5.43 
eheu[25]=  7.50
eheu[26]=  4.99 
eheu[27]=  6.22
eheu[28]=  4.19  
eheu[29]=  4.56 
eheu[30]=  3.04
eheu[31]=  3.25  
eheu[32]=  2.52 
eheu[33]=  2.87
eheu[34]=  2.21  
eheu[35]=  2.58 
eheu[36]=  1.46
eheu[37]=  2.18  
eheu[38]=  1.10 
eheu[39]=  1.12
eheu[40]=  3.65 #// Ge - out of sequence 

cname[0]="H";
cname[1]="He";
cname[2]="Li";
cname[3]="Be";
cname[4]="B";
cname[5]="C";
cname[6]="N";
cname[7]="O";
cname[8]="F";
cname[9]="Ne";
cname[10]="Na";
cname[11]="Mg";
cname[12]="Al";
cname[13]="Si";
cname[14]="P";
cname[15]="S";
cname[16]="Cl";
cname[17]="Ar";
cname[18]="K";
cname[19]="Ca";
cname[20]="Sc";
cname[21]="Ti";
cname[22]="V";
cname[23]="Cr";
cname[24]="Mn";
cname[25]="Fe";
cname[26]="Co";
cname[27]="Ni";
cname[28]="Cu";
cname[29]="Zn";
cname[30]="Ga";
cname[31]="Kr";
cname[32]="Rb";
cname[33]="Sr";
cname[34]="Y";
cname[35]="Zr";
cname[36]="Nb";
cname[37]="Ba";
cname[38]="La";
cname[39]="Cs";
cname[40]="Ge";



CSGsRead2.gsread(cname, eheu)


gsNspec = CSGsRead2.nspec
gsName = CSGsRead2.name
#GAS composition shoudl be corrected to CSPy values at this point:
gsComp = CSGsRead2.comp
# Number of atomic elements in GAS package:
gsNumEls = len(gsComp)

#Array of pointers FROM CSPy elements TO GAS elements
#CAUTION: elements are not contiguous in GAS' species array (are
# NOT the first gsNumEls entries!)

#Default value of -1 means CSPy element NOT in GAS package
csp2gas = [-1 for i in range(nelemAbnd)]
csp2gasIon1 = [-1 for i in range(nelemAbnd)]
csp2gasIon2 = [-1 for i in range(nelemAbnd)]

#gas2csp = [-1 for i in range(gsNspec)]

for i in range(nelemAbnd):
    for j in range(gsNspec):
        #print("i ", i, " j ", j, " cname ", cname[i], " gsName ", gsName[j]);
        #Captures neutral stages only in gsName[] 
        if (cname[i].strip() == gsName[j].strip()):
            csp2gas[i] = j
        if (cname[i].strip()+"+" == gsName[j].strip()):
            csp2gasIon1[i] = j
        if (cname[i].strip()+"++" == gsName[j].strip()):
            csp2gasIon2[i] = j          
            
#for i in range(gsNspec):
#    for j in range(nelemAbnd):
#        if (gsName[i].strip() == cname[j].strip()):
#            gas2csp[i] = j
            
#print("csp2gas ", csp2gas)
    
gsLogk = CSGsRead2.logk

gsFirstMol = -1  # index of 1st molecular species in Gas' species list
for i in range(gsNspec):
    gsFirstMol+=1
    if (gsLogk[0][i] != 0.0):
        break

# Number of molecular species in GAS package:
gsNumMols = gsNspec - gsFirstMol

# Number of ionic species in GAS package:
gsNumIons = gsNspec - gsNumEls - gsNumMols
#print("gsNspec ", gsNspec, " gsFirstMol ", gsFirstMol, " gsNumMols ", 
      #gsNumMols, " gsNumIon ", gsNumIons)

 
#//Set up for molecules with JOLA bands:
jolaTeff = 5000.0
numJola = 7 #//for now
#//int numJola = 1; //for now

jolaSpecies = ["" for i in range(numJola)]  #molecule name
jolaSystem = ["" for i in range(numJola)]   #band system
jolaDeltaLambda = [0 for i in range(numJola)]
jolaWhichF = ["" for i in range(numJola)]

if (teff <= jolaTeff):

    jolaSpecies[0] = "TiO" #// molecule name
    jolaSystem[0] = "TiO_C3Delta_X3Delta" #//band system
    jolaWhichF[0] = "Jorgensen"
    #jolaDeltaLambda[0] = 0 
    jolaSpecies[1] = "TiO" #// molecule name
    jolaSystem[1] = "TiO_c1Phi_a1Delta" #//band system 
    jolaWhichF[1] = "Jorgensen"
    #jolaDeltaLambda[1] = 1 
    jolaSpecies[2] = "TiO" #// molecule name
    jolaSystem[2] = "TiO_A3Phi_X3Delta" #//band system 
    jolaWhichF[2] = "Jorgensen"
    #jolaDeltaLambda[2] = 1 
    jolaSpecies[3] = "TiO" #// molecule name
    jolaSystem[3] = "TiO_B3Pi_X3Delta" #//band system 
    jolaWhichF[3] = "Jorgensen"
    jolaSpecies[4] = "TiO" #// molecule name
    jolaSystem[4] = "TiO_E3Pi_X3Delta" #//band system  
    jolaWhichF[4] = "Jorgensen"
    jolaSpecies[5] = "TiO" #// molecule name
    jolaSystem[5] = "TiO_b1Pi_a1Delta" #//band system 
    jolaWhichF[5] = "Jorgensen"
    jolaSpecies[6] = "TiO" #// molecule name
    jolaSystem[6] = "TiO_b1Pi_d1Sigma" #//band system
    jolaWhichF[6] = "Jorgensen"

    #"G-band" at 4300 A - MK classification diagnostic:
    #Needs Allen's approach to getting f
    #jolaSpecies[7] = "CH" #// molecule name
    #jolaSystem[7] = "CH_A2Delta_X2Pi" #//band system  
    #jolaWhichF[7] = "Allen"
        
ATot = 0.0
thisAz = 0.0 
eheuScale = 0.0

#// Set value of eheuScale for new metallicity options. 06/17 lburns
if (logHeFe != 0.0):
    eheu[1] = eheu[1] + logHeFe

if (logAlphaFe != 0.0):
    eheu[7] = eheu[7] + logAlphaFe
    eheu[9] = eheu[9] + logAlphaFe;
    eheu[11] = eheu[11] + logAlphaFe
    eheu[13] = eheu[13] + logAlphaFe
    eheu[15] = eheu[15] + logAlphaFe
    eheu[17] = eheu[17] + logAlphaFe
    eheu[19] = eheu[19] + logAlphaFe
    eheu[21] = eheu[21] + logAlphaFe
        
if (logCO > 0.0):
    eheu[5] = eheu[5] + logCO
    #//console.log("logCO " + logCO);
        
if (logCO < 0.0):
    eheu[7] = eheu[7] + math.abs(logCO)
    #//console.log("logCO " + logCO);
        
#//console.log("logCO " + logCO);



#for i in range(nelemAbnd):
#     eheuScale = eheu[i]  #//default initialization //still base 10
#     if (i > 1): #//if not H or He
#         eheuScale = eheu[i] + log10ZScale #//still base 10  
#     
#     #//logAz[i] = logE10 * (eheu[i] - 12.0); //natural log
#     logAz[i] = logE10 * (eheuScale - 12.0) #//natural log
#     thisAz = math.exp(logAz[i])
#     ATot = ATot + thisAz;
     #//System.out.println("i " + i + " logAz " + logE*logAz[i]);
     
#H and He do NOT get re-scaled with metallicity parameter:
logAz[0:2] = [ logE10 * (x - 12.0) for x in eheu[0:2] ]
#Everything else does:
logAz[2:] = [ logE10 * (x + log10ZScale - 12.0) for x in eheu[2:] ]

#print("logAz ", [logE*x for x in logAz] )

expAz = [ math.exp(x) for x in logAz ]
ATot = sum(expAz)
logATot = math.log(ATot) #//natural log

#print("logATot ", logATot)



"""//Apr 2016: Replace the following initial guesses with the following PSEUDOCODE:
   //
   // PHOENIX models at Teff0=5000 K, log(g0)=4.5, M0=0.0 (linear "zscl" = 10.0^M)
   //                   Teff0=10000 K, log(g0)=4.0, M0=0.0 (linear "zscl" = 10.0^M)
   //                   --> Tk0(tau), Pe0(tau), Pg0(tau)
   //
   //From Gray 3rd Ed. Ch.9, esp p. 189, 196
   // 1) Tk(tau)=Teff/Teff0*tk0(tau)
   // 2) Pg(tau)=(g/g0)^exp * Pg0(tau); exp = 0.64(bottom) - 0.54(top) for "cool" models
   //                                   exp = 0.85(bottom) - 0.53(top) for "hotter" models
   //    Pg(tau)= zscl^-0.333*Pg0(tau) if metals neutral - cooler models  
   //    Pg(tau)= zscl^-0.5*Pg0(tau) if metals ionized - hotter models
   //    Pg(tau) = {(1+4A_He)/(1+4A_He0)}^2/3 * Pg0(tau)  

   // 3) Pe(tau)=(g/g0)^exp * Pe0(tau); exp = 0.33(bottom) - 0.48(top) for "cool" models
   //                                   exp = 0.82(bottom) - 0.53(top) for "hotter" models
   //    Pe(tau)=exp(omega*Teff)/exp(omega*Teff0)* Pe0(tau), Teff < 10000 K
   //             - omega = 0.0015@log(tau)=1.0 & 0.0012@log(tau)=-1 to -3   
   //    Pe(tau)= zscl^+0.333*Pe0(tau) if metals neutral - cooler models  
   //    Pe(tau)= zscl^+0.5*Pe0(tau) if metals ionized - hotter models  
   //    Pe(tau) = {(1+4A_He)/(1+4A_He0)}^1/3 * Pe0(tau)"""
   


#//
#// END Initial guess for Sun section:
#//
#//Rescaled  kinetic temperature structure: 
#//double F0Vtemp = 7300.0;  // Teff of F0 V star (K)  
   
tauRos = [ [0.0 for i in range(numDeps)] for j in range(2) ]                         
temp = [ [0.0 for i in range(numDeps)] for j in range(2) ]
guessPGas = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
guessPe = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
guessNe = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
kappaRos = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
kappa500 = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
pGas = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
newPe = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
pRad = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
rho = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
newNe = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
mmw = [ 0.0 for i in range(numDeps) ]

depths = [ 0.0 for i in range(numDeps) ]

if Input.specSynMode == True:
    
    #ensure self-consistency between parameters and model being read in:
    teff = Restart.teffRS
    logg = Restart.loggRS
    log10ZSale = Restart.log10ZScaleRS
    logKapFudge = Restart.logKapFudgeRS
    logHeFe = Restart.logHeFeRS
    logCO = Restart.logCORS
    logAlphaFe = Restart.logAlphaFeRS

    tauRos[0] = [ x for x in Restart.tauRosRS[0] ]
    tauRos[1] = [ x for x in Restart.tauRosRS[1] ]    
    temp[0] = [ x for x in Restart.tempRS[0] ]
    temp[1] = [ x for x in Restart.tempRS[1] ]
    pGas[0] = [ x for x in Restart.pGasRS[0] ]
    pGas[1] = [ x for x in Restart.pGasRS[1] ]
    newPe[0] = [ x for x in Restart.peRS[0] ]
    newPe[1] = [ x for x in Restart.peRS[1] ]
    # set up everything as in normal structure mode:
    guessPGas[0] = [ x for x in Restart.pGasRS[0] ]
    guessPGas[1] = [ x for x in Restart.pGasRS[1] ]
    guessPe[0] = [ x for x in Restart.peRS[0] ]
    guessPe[1] = [ x for x in Restart.peRS[1] ]    
    newNe[1] = [newPe[1][iD] - temp[1][iD] - Useful.logK() for iD in range(numDeps)]
    newNe[0] = [math.exp(newNe[1][iD]) for iD in range(numDeps)]   
    pRad[0] = [ x for x in Restart.pRadRS[0] ]
    pRad[1] = [ x for x in Restart.pRadRS[1] ]
    rho[0] = [ x for x in Restart.rhoRS[0] ]
    rho[1] = [ x for x in Restart.rhoRS[1] ]
    kappa500[0] = [ x for x in Restart.kappa500RS[0] ]
    kappa500[1] = [ x for x in Restart.kappa500RS[1] ]
    kappaRos[0] = [ x for x in Restart.kappaRosRS[0] ]
    kappaRos[1] = [ x for x in Restart.kappaRosRS[1] ]
    mmw = [ x for x in Restart.mmwRS ]
    
    #We are reading in a converged model - minimal processing:
    nOuterIter = 1
    nInnerIter = 1
    
else:
    
        
    tauRos = TauScale.tauScale(numDeps, log10MinDepth, log10MaxDepth)
    if (teff <= F0Vtemp):
        if (logg > 3.5):
            #//We're a cool dwarf! - rescale from Teff=5000 reference model!
            #print("cool star branch")
            temp = ScaleT5000.phxRefTemp(teff, numDeps, tauRos)
        else:
            #We're a cool giant - rescale from teff=4250, log(g) = 2.0 model
            temp = ScaleT4250g20.phxRefTemp(teff, numDeps, tauRos)
    elif (teff > F0Vtemp): 
        #//We're a HOT star! - rescale from Teff=10000 reference model! 
        temp = ScaleT10000.phxRefTemp(teff, numDeps, tauRos)
    
    #//Scaled from Phoenix solar model:
        

    #//double[][] guessKappa = new double[2][numDeps];
    if (teff <= F0Vtemp):
        if (logg > 3.5):
            #//We're a cool dwarf - rescale from  Teff=5000 reference model!
            #// logAz[1] = log_e(N_He/N_H)
            guessPGas = ScaleT5000.phxRefPGas(grav, zScale, logAz[1], numDeps, tauRos)
            guessPe = ScaleT5000.phxRefPe(teff, grav, numDeps, tauRos, zScale, logAz[1])
            guessNe = ScaleT5000.phxRefNe(numDeps, temp, guessPe) 
            #//Ne = ScaleSolar.phxSunNe(grav, numDeps, tauRos, temp, kappaScale);
            #//guessKappa = ScaleSolar.phxSunKappa(numDeps, tauRos, kappaScale);
        else:
            #We're a cool giant - rescale from teff=4250, log(g) = 2.0 model
            guessPGas = ScaleT4250g20.phxRefPGas(grav, zScale, logAz[1], numDeps, tauRos)
            guessPe = ScaleT4250g20.phxRefPe(teff, grav, numDeps, tauRos, zScale, logAz[1])
            guessNe = ScaleT4250g20.phxRefNe(numDeps, temp, guessPe)                 
    elif (teff > F0Vtemp):
        #//We're a HOT star!! - rescale from Teff=10000 reference model 
        #// logAz[1] = log_e(N_He/N_H)
        guessPGas = ScaleT10000.phxRefPGas(grav, zScale, logAz[1], numDeps, tauRos)
        guessPe = ScaleT10000.phxRefPe(teff, grav, numDeps, tauRos, zScale, logAz[1])
        guessNe = ScaleT10000.phxRefNe(numDeps, temp, guessPe)
        #//logKapFudge = -1.5;  //sigh - don't ask me - makes the Balmer lines show up around A0 
    
#//Now do the same for the Sun, for reference:
tempSun = ScaleSolar.phxSunTemp(teffSun, numDeps, tauRos)
#//Now do the same for the Sun, for reference:
pGasSunGuess = ScaleSolar.phxSunPGas(gravSun, numDeps, tauRos)
NeSun = ScaleSolar.phxSunNe(gravSun, numDeps, tauRos, tempSun, zScaleSun)
kappaSun = ScaleSolar.phxSunKappa(numDeps, tauRos, zScaleSun)
mmwSun = State.mmwFn(numDeps, tempSun, zScaleSun)
rhoSun = State.massDensity(numDeps, tempSun, pGasSunGuess, mmwSun, zScaleSun)
pGasSun = Hydrostat.hydroFormalSoln(numDeps, gravSun, tauRos, kappaSun, tempSun, pGasSunGuess)

#Total population of element over all ionization stages:
logNz = State.getNz(numDeps, temp, guessPGas, guessPe, ATot, nelemAbnd, logAz)
#for i in range(numDeps): 
#    logNH[i] = logNz[0][i]
##//set the initial guess H^+ number density to the e^-1 number density
#    masterStagePops[0][1][i] = guessPe[1][i] #//iElem = 0: H; iStage = 1: II
    #//System.out.println("i " + i + " logNH[i] " + logE*logNH[i]);
logNH = [ x for x in logNz[0] ]
masterStagePops[0][1] = [ x for x in guessPe[1] ]
    
#//Load the total no. density of each element into the nuetral stage slots of the masterStagePops array as a first guess at "species B" neutral
#//populations for the molecular Saha eq. - Reasonable first guess at low temp where molecuales form

#for iElem in range(nelemAbnd):
#    for iD in range(numDeps):
#        masterStagePops[iElem][0][iD] = logNz[iElem][iD]

#Initial default - set neutral stage population to total number density of that element:     
masterStagePops[:][0][:] = [ [ logNz[i][j] for j in range(numDeps) ] for i in range(nelemAbnd) ]



warning = "";
if (teff < F0Vtemp):
    #//warning = "<span style='color:red'><em>T</em><sub>eff</sub> < 6000 K <br />Cool star mode";
    warning = "Cool star mode"
    print(warning)
else:
    #//warning = "<span style='color:blue'><em>T</em><sub>eff</sub> > 6000 K <br />Hot star mode</span>";
    warning = "Hot star mode"
    print(warning)
    
#//Add subclass to each spectral class (lburns)
spectralClass = " "
subClass = " " #//Create a variable for the subclass of the star. lburns
luminClass = "V" #//defaults to V
#//Determine the spectralClass and subClass of main sequence stars, subdwarfs and white dwarfs
#//var luminClass = "V" or luminClass = "VI" or luminClass = "WD"
#// Based on the data in Appendix G of An Introduction to Modern Astrophysics, 2nd Ed. by
#// Carroll & Ostlie
if ((logg >= 4.0) and (logg <= 6.0)):
    if (teff < 3000.0):
        spectralClass = "L";
    elif ((teff >= 3000.0) and (teff < 3900.0)):
        spectralClass = "M";
        if ((teff >= 3000.0) and (teff <= 3030.0)):
            subClass = "6";
        elif ((teff > 3030.0) and (teff <= 3170.0)):
            subClass = "5";
        elif ((teff > 3170.0) and (teff <= 3290.0)):
            subClass = "4";
        elif ((teff > 3290.0) and (teff <= 3400.0)):
            subClass = "3";
        elif ((teff > 3400.0) and (teff <= 3520.0)):
            subClass = "2";
        elif ((teff > 3520.0) and (teff <= 3660.0)):
            subClass = "1";
        elif ((teff > 3660.0) and (teff < 3900.0)):
            subClass = "0";
        
    elif ((teff >= 3900.0) and (teff < 5200.0)):
        spectralClass = "K";
        if ((teff >= 3900.0) and (teff <= 4150.0)):
            subClass = "7";
        elif ((teff > 4150.0) and (teff <= 4410.0)):
            subClass = "5";
        elif ((teff > 4410.0) and (teff <= 4540.0)):
            subClass = "4";
        elif ((teff > 4540.0) and (teff <= 4690.0)):
            subClass = "3";
        elif ((teff > 4690.0) and (teff <= 4990.0)):
            subClass = "1";
        elif ((teff > 4990.0) and (teff < 5200.0)):
            subClass = "0";
        
    elif ((teff >= 5200.0) and (teff < 5950.0)):
        spectralClass = "G";
        if ((teff >= 5200.0) and (teff <= 5310.0)):
            subClass = "8";
        elif ((teff > 5310.0) and (teff <= 5790.0)):
            subClass = "2";
        elif ((teff > 5790.0) and (teff < 5950.0)):
            subClass = "0";
        
    elif ((teff >= 5950.0) and (teff < 7300.0)):
        spectralClass = "F";
        if ((teff >= 5950.0) and (teff <= 6250.0)):
            subClass = "8";
        elif ((teff > 6250.0) and (teff <= 6650.0)):
            subClass = "5";
        elif ((teff > 6650.0) and (teff <= 7050.0)):
            subClass = "2";
        elif ((teff > 7050.0) and (teff < 7300.0)):
            subClass = "0";
        
    elif ((teff >= 7300.0) and (teff < 9800.0)):
        spectralClass = "A";
        if ((teff >= 7300.0) and (teff <= 7600.0)):
            subClass = "8";
        elif ((teff > 7600.0) and (teff <= 8190.0)):
            subClass = "5";
        elif ((teff > 8190.0) and (teff <= 9020.0)):
            subClass = "2";
        elif ((teff > 9020.0) and (teff <= 9400.0)):
            subClass = "1";
        elif ((teff > 9400.0) and (teff < 9800.0)):
            subClass = "0";
        
    elif ((teff >= 9800.0) and (teff < 30000.0)):
        spectralClass = "B";
        if ((teff >= 9300.0) and (teff <= 10500.0)):
            subClass = "9";
        elif ((teff > 10500.0) and (teff <= 11400.0)):
            subClass = "8";
        elif ((teff > 11400.0) and (teff <= 12500.0)):
            subClass = "7";
        elif ((teff > 12500.0) and (teff <= 13700.0)):
            subClass = "6";
        elif ((teff > 13700.0) and (teff <= 15200.0)):
            subClass = "5";
        elif ((teff > 15200.0) and (teff <= 18800.0)):
            subClass = "3";
        elif ((teff > 18800.0) and (teff <= 20900.0)):
            subClass = "2";
        elif ((teff > 20900.0) and (teff <= 25400.0)):
            subClass = "1";
        elif ((teff > 25400.0) and (teff < 30000.0)):
            subClass = "0";
        
    elif (teff >= 30000.0):
        spectralClass = "O";
        if ((teff >= 30000.0) and (teff <= 35800.0)):
            subClass = "8";
        elif ((teff > 35800.0) and (teff <= 37500.0)):
            subClass = "7";
        elif ((teff > 37500.0) and (teff <= 39500.0)):
            subClass = "6";
        elif ((teff > 39500.0) and (teff <= 42000.0)):
            subClass = "5";
        
    

#//Determine the spectralClass and subClass of giants and subgiants. lburns
#//var luminClass = "III" or luminClass = "IV"
#//Determine the spectralClass and subClass of giants and subgiants. lburns
#//var luminClass = "III" or luminClass = "IV"
if ((logg >= 1.5) and (logg < 4.0)):
    if (teff < 3000.0):
        spectralClass = "L";
    elif ((teff >= 3000.0) and (teff < 3700.0)):
        spectralClass = "M";
        if ((teff >= 3000.0) and (teff <= 3330.0)):
            subClass = "6";
        elif ((teff > 3330.0) and (teff <= 3380.0)):
            subclass = "5";
        elif ((teff > 3380.0) and (teff <= 3440.0)):
            subClass = "4";
        elif ((teff > 3440.0) and (teff <= 3480.0)):
            subClass = "3";
        elif ((teff > 3480.0) and (teff <= 3540.0)):
            subClass = "2";
        elif ((teff > 3540.0) and (teff <= 3600.0)):
            subClass = "1";
        elif ((teff > 3600.0) and (teff < 3700.0)):
            subClass = "0";
        
    elif ((teff >= 3700.0) and (teff < 4700.0)):
        spectralClass = "K"
        if ((teff >= 3700.0) and (teff <= 3870.0)):
            subClass = "7";
        elif ((teff > 3870.0) and (teff <= 4050.0)):
            subClass = "5";
        elif ((teff > 4050.0) and (teff <= 4150.0)):
            subClass = "4";
        elif ((teff > 4150.0) and (teff <= 4260.0)):
            subClass = "3";
        elif ((teff > 4260.0) and (teff <= 4510.0)):
            subClass = "1";
        elif ((teff > 4510.0) and (teff < 4700.0)):
            subClass = "0";
        
    elif ((teff >= 4700.0) and (teff < 5500.0)):
        spectralClass = "G";
        if ((teff >= 4700.0) and (teff <= 4800.0)):
            subClass = "8";
        elif ((teff > 4800.0) and (teff <= 5300.0)):
            subClass = "2";
        elif ((teff > 5300.0) and (teff < 5500.0)):
            subClass = "0";
        
    elif ((teff >= 5500.0) and (teff < 7500.0)):
        spectralClass = "F";
        if ((teff >= 5500.0) and (teff <= 6410.0)):
            subClass = "5";
        elif ((teff > 6410.0) and (teff <= 7000.0)):
            subClass = "2";
        elif ((teff > 7000.0) and (teff < 7500.0)):
            subClass = "0";
        
    elif ((teff >= 7500.0) and (teff < 10300.0)):
        spectralClass = "A";
        if ((teff >= 7500.0) and (teff <= 7830.0)):
            subClass = "8";
        elif ((teff > 7830.0) and (teff <= 8550.0)):
            subClass = "5";
        elif ((teff > 8550.0) and (teff <= 9460.0)):
            subClass = "2";
        elif ((teff > 9460.0) and (teff <= 9820.0)):
            subClass = "1";
        elif ((teff > 9820.0) and (teff < 10300.0)):
            subClass = "0";
        
    elif ((teff >= 10300.0) and (teff < 29300.0)):
        spectralClass = "B";
        if ((teff >= 10300.0) and (teff <= 10900.0)):
            subClass = "9";
        elif ((teff > 10900.0) and (teff <= 11700.0)):
            subClass = "8";
        elif ((teff > 11700.0) and (teff <= 12700.0)):
            subClass = "7";
        elif ((teff > 12700.0) and (teff <= 13800.0)):
            subClass = "6";
        elif ((teff > 13800.0) and (teff <= 15100.0)):
            subClass = "5";
        elif ((teff > 15100.0) and (teff <= 18300.0)):
            subClass = "3";
        elif ((teff > 18300.0) and (teff <= 20200.0)):
            subClass = "2";
        elif ((teff > 20200.0) and (teff <= 24500.0)):
            subClass = "1";
        elif ((teff > 24500.0) and (teff < 29300.0)):
            subClass = "0";
        
    elif ((teff >= 29300.0) and (teff < 40000.0)):
        spectralClass = "O";
        if ((teff >= 29300.0) and (teff <= 35000.0)):
            subClass = "8";
        elif ((teff > 35000.0) and (teff <= 36500.0)):
            subClass = "7";
        elif ((teff > 36500.0) and (teff <= 37800.0)):
            subClass = "6";
        elif ((teff > 37800.0) and (teff < 40000.0)):
            subClass = "5";
        
    


#//Determine the spectralClass and subClass of supergiants and bright giants. lburns
#//var luminClass = "I" or luminClass = "II"
if ((logg >= 0.0) and (logg < 1.5)):
    if (teff < 2700.0):
        spectralClass = "L";
    elif ((teff >= 2700.0) and (teff < 3650.0)):
        spectralClass = "M";
        if ((teff >= 2700.0) and (teff <= 2710.0)):
            subClass = "6";
        elif ((teff > 2710.0) and (teff <= 2880.0)):
            subClass = "5";
        elif ((teff > 2880.0) and (teff <= 3060.0)):
            subClass = "4";
        elif ((teff > 3060.0) and (teff <= 3210.0)):
            subClass = "3";
        elif ((teff > 3210.0) and (teff <= 3370.0)):
            subClass = "2";
        elif ((teff > 3370.0) and (teff <= 3490.0)):
            subClass = "1";
        elif ((teff > 3490.0) and (teff < 3650.0)):
            subClass = "0";
        
    elif ((teff >= 3650.0) and (teff < 4600.0)):
        spectralClass = "K";
        if ((teff >= 3650.0) and (teff <= 3830.0)):
            subClass = "7";
        elif ((teff > 3830.0) and (teff <= 3990.0)):
            subClass = "5";
        elif ((teff > 3990.0) and (teff <= 4090.0)):
            subClass = "4";
        elif ((teff > 4090.0) and (teff <= 4190.0)):
            subClass = "3";
        elif ((teff > 4190.0) and (teff <= 4430.0)):
            subClass = "1";
        elif ((teff > 4430.0) and (teff < 4600.0)):
            subClass = "0";
        
    elif ((teff >= 4600.0) and (teff < 5500.0)):
        spectralClass = "G";
        if ((teff >= 4600.0) and (teff <= 4700.0)):
            subClass = "8";
        elif ((teff > 4700.0) and (teff <= 5190.0)):
            subClass = "2";
        elif ((teff > 5190.0) and (teff < 5500.0)):
            subClass = "0";
        
    elif ((teff >= 5500.0) and (teff < 7500.0)):
        spectralClass = "F";
        if ((teff >= 5500.0) and (teff <= 5750.0)):
            subClass = "8";
        elif ((teff > 5750.0) and (teff <= 6370.0)):
            subClass = "5";
        elif ((teff > 6370.0) and (teff <= 7030.0)):
            subClass = "2";
        elif ((teff > 7030.0) and (teff < 7500.0)):
            subClass = "0";
        
    elif ((teff >= 7500.0) and (teff < 10000.0)):
        spectralClass = "A";
        if ((teff >= 7500.0) and (teff <= 7910.0)):
            subClass = "8";
        elif ((teff > 7910.0) and (teff <= 8610.0)):
            subClass = "5";
        elif ((teff > 8610.0) and (teff <= 9380.0)):
            subClass = "2";
        elif ((teff > 9380.0) and (teff < 10000.0)):
            subClass = "0";
        
    elif ((teff >= 10000.0) and (teff < 27000.0)):
        spectralClass = "B";
        if ((teff >= 10000.0) and (teff <= 10500.0)):
            subClass = "9";
        elif ((teff > 10500.0) and (teff <= 11100.0)):
            subClass = "8";
        elif ((teff > 11100.0) and (teff <= 11800.0)):
            subClass = "7";
        elif ((teff > 11800.0) and (teff <= 12600.0)):
            subClass = "6";
        elif ((teff > 12600.0) and (teff <= 13600.0)):
            subClass = "5";
        elif ((teff > 13600.0) and (teff <= 16000.0)):
            subClass = "3";
        elif ((teff > 16000.0) and (teff <= 17600.0)):
            subClass = "2";
        elif ((teff > 17600.0) and (teff <= 21400.0)):
            subClass = "1";
        elif ((teff > 21400.0) and (teff < 27000.0)):
            subClass = "0";
        
    elif ((teff >= 27000.0) and (teff < 42000.0)):
        spectralClass = "O";
        if ((teff >= 27000.0) and (teff <= 34000.0)):
            subClass = "8";
        elif ((teff > 34000.0) and (teff <= 36200.0)):
            subClass = "7";
        elif ((teff > 36200.0) and (teff <= 38500.0)):
            subClass = "6";
        elif ((teff > 38500.0) and (teff < 42000.0)):
            subClass = "5";
        
    


#//Determine luminClass based on logg
if ((logg >= 0.5) and (logg < 1.0)):
    luminClass = "I";
elif ((logg >= 1.0) and (logg < 1.5)):
    luminClass = "II";
elif ((logg >= 1.5) and (logg < 3.0)):
    luminClass = "III";
elif ((logg >= 3.0) and (logg < 4.0)):
    luminClass = "IV";
elif ((logg >= 4.0) and (logg < 5.0)):
    luminClass = "V";
elif ((logg >= 5.0) and (logg < 6.0)):
    luminClass = "VI";
elif ((logg >= 5.0)):
    luminClass = "WD";
    

spectralType = spectralClass + subClass + " " + luminClass
print("Spectral type: ", spectralType)      
#Initial guess atmospheric structure output: 
#Convert everything to log_10 OR re-scaled units for plotting, printing, etc:
    
log10e = math.log10(math.e)


#
#
#// END initial guess for Sun section
#
#
###################################################################
#
#
#
#   Converge atmospheric structure 
#
#    - Includes *initial* ionization equilibrium *without* molecules (for now)
#
#
#
###################################################################


#log10mmw = [0.0 for i in range(numDeps)]
#//
#// *********************
#//Jul 2016: Replace the following procedure for model building with the following PSEUDOCODE:
#//
#// 1st guess Tk(tau), Pe(tau), Pg(tau) from rescaling reference hot or cool model above
#// 1) Converge Pg-Pe relation for Az abundance distribution and  T_Kin(Tau)
#//   assuming all free e^-s from single ionizations - *inner* convergence
#// 2) Get Ne, rho, mu from Phil Bennet's GAS apckage
#// 3) kappa(tau) from Gray Ch. 8 sources - H, He, and e^- oapcity sources only
#// 4) P_Tot(tau) from HSE on tau scale with kappa from 4)
#//    - PRad(tau) from Tk(tau)
#//    - New Pg(tau) from P_Tot(tau)-PRad(tau)
#// 5) Iterate Pg - kappa relation to convergence - *outer* convergence
#// 6)Get rho(tau) = Sigma_z(m_z*N_z(tau)) and mu(tau) = rho(tau) / N(tau)
#//   and depth scale
#//
#//  ** Atmospheric structure converged **
#//
#// THEN for spectrum synthesis:
#//
#// 1) number densities of absorpbers from partial pressures (pps) from Phil
#  Bennett's GAS package)
#// 2) Temp correction??   


#/    **** STOP ****  No - do we *really* need N_HI, ... for kappa if we use rho in HSE? - Yes - needed even if kappa
#//    is in cm^-1 instead of cm^2/g - sigh

species = " "  #; //default initialization
#  double rho[][] = new double[2][numDeps];
#  double[][] tauOneStagePops = new double[nelemAbnd][numStages];

tauOneStagePops = [ [ 0.0 for i in range(numStages) ] for j in range(nelemAbnd) ]
unity = 1.0
zScaleList = 1.0 #//initialization   

numAtmPrtTmps = 5
numMolPrtTmps = 5
#  double[][] log10UwAArr = new double[numStages][2];
log10UwAArr = [ [ 0.0 for k in range(numAtmPrtTmps) ] for j in range(numStages) ] 
#for i in range(numStages):
#    for k in range(len(log10UwAArr[0])):
#        log10UwAArr[i][k] = 0.0 #//lburns default initialization - logarithmic
  
 
#//Ground state ionization E - Stage I (eV) 
#  double[] chiIArr = new double[numStages]
chiIArr = [ 999999.0 for i in range(numStages) ]
#// //Ground state ionization E - Stage II (eV)
#//
""" now GAS
#//For diatomic molecules:
speciesAB = " "
speciesA = " "
speciesB = " "
# double massA, massB, logMuAB;
"""
# double[][] masterMolPops = new double[nMols][numDeps];
#masterMolPops = [ [ -49.0 for i in range(numDeps) ] for j in range(nMols) ]
#Now with GAS:


#//initialize masterMolPops for mass density (rho) calculation:
masterMolPops = [ [ -49.0 for i in range(numDeps) ] for j in range(gsNumMols) ]
for i in range(gsNumMols):
    for j in range(numDeps):
        masterMolPops[i][j] = -49.0  #//these are logarithmic
    
  
Ng = [ 0.0 for i in range(numDeps) ]

  #double logMmw;
logKappa = [ [ 0.0 for i in range(numDeps) ] for j in range(numLams) ]
logKappaHHe = [ [ 0.0 for i in range(numDeps) ] for j in range(numLams) ]
logKappaMetalBF = [ [ 0.0 for i in range(numDeps) ] for j in range(numLams) ]
logKappaRayl = [ [ 0.0 for i in range(numDeps) ] for j in range(numLams) ]

newTemp = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]


#//
#//
#//We converge the Pgas - Pe relation first under the assumption that all free e^-s are from single ionizations
#// a la David Gray Ch. 9.  
#// This approach separates converging ionization fractions and Ne for spectrum synthesis purposes from
#// converging the Pgas-Pe-N_H-N_He relation for computing the mean opacity for HSE
#//
thisTemp = [ 0.0 for i in range(2) ]
log10UwUArr = [ 0.0 for i in range(numAtmPrtTmps) ]
log10UwLArr = [ 0.0 for i in range(numAtmPrtTmps) ]
#double chiI, peNumerator, peDenominator, logPhi, logPhiOverPe, logOnePlusPhiOverPe, logPeNumerTerm, logPeDenomTerm;

log300 = math.log(300.0)
log2 = math.log(2.0)

#GAS package parameters:
isolv = 1
tol = 1.0e-4
maxit = 100

#GAS package interface variables:
gsP0 = [0.0e0 for i in range(40)]
topP0 = [0.0e0 for i in range(40)]
gsPp = [0.0e0 for i in range(150)]
#For reporting purposes only:
log10MasterGsPp = [ [-99.0e0 for iD in range(numDeps)] for iSpec in range(gsNspec) ]
#ppix = [0.0e0 for i in range(30)]
#a = [0.0e0 for i in range(625)]

#//Begin Pgas-kapp iteration

#Test: 
GAStemp = 6000.0
#GAStemp = 100000.0

for pIter in range(nOuterIter):
#//

    #Try making return value a tuple:

    
        
    if (teff <= GAStemp):
    #if (teff <= 100000.0):   #test        
        
        for iD in range(numDeps):

            #print("isolv ", isolv, " temp ", temp[0][iD], " guessPGas ", guessPGas[0][iD])
            gasestReturn = CSGasEst.gasest(isolv, temp[0][iD], guessPGas[0][iD])
            gsPe0 = gasestReturn[0]
            gsP0 = gasestReturn[1]
            neq = gasestReturn[2]
        
            if (iD == 1):
                topP0 = [ (0.5 * gsP0[iSpec]) for iSpec in range(40) ]    
                
            #Upper boundary causes problems:
            if (pIter > 0 and iD == 0):
                gsPe0 = 0.5 * newPe[0][1]
                gsP0 = [ topP0[iSpec] for iSpec in range(40) ] 
                
            
            #print("Calling GAS 1 iD ", iD, " temp ", temp[0][iD])
            #print("iD ", iD, " gsPe0 ", gsPe0, " gsP0[0] ", gsP0[0], " neq ", neq)

            
            gasReturn = CSGas.gas(isolv, temp[0][iD], guessPGas[0][iD], gsPe0, gsP0, neq, tol, maxit)
            #a = gasReturn[0]
            #nit = gasReturn[1]
            gsPe = gasReturn[2]
            #pd = gasReturn[3]
            gsPp = gasReturn[4]
            #Can't pythonize this - gsPp padded at end with 0.0s
            #log10MasterGsPp[:][iD] = [math.log10(x) for x in gsPp]
            #for iSpec in range(gsNspec):
            #    log10MasterGsPp[iSpec][iD] = math.log10(gsPp[iSpec])
            #print("1: ", gsPp[0]/guessPGas[0][iD])
            #ppix = gasReturn[5]
            gsMu = gasReturn[6]
            gsRho = gasReturn[7]
        
            #print("iD ", iD, " gsPe ", gsPe, " gsPp[0] ", gsPp[0], " gsMu ", gsMu, " gsRho ", gsRho)
        
            newPe[0][iD] = gsPe
            newPe[1][iD] = math.log(gsPe)
            newNe[0][iD] = gsPe / Useful.k() / temp[0][iD]
            newNe[1][iD] = math.log(newNe[0][iD])
            guessPe[0][iD] = newPe[0][iD]
            guessPe[1][iD] = newPe[1][iD]
            guessNe[0][iD] = newNe[0][iD]
            guessNe[1][iD] = newNe[1][iD]        
        
            rho[0][iD] = gsRho
            rho[1][iD] = math.log(gsRho)
            mmw[iD] = gsMu * Useful.amu()
            
                    #Take neutral stage populations for atomic species from GAS: 
            for iElem in range(nelemAbnd):
            
                if (csp2gas[iElem] != -1):
                    #element is in GAS package:  
                    #Neutral stage onnly:
                    thisN = gsPp[csp2gas[iElem]] / Useful.k() / temp[0][iD]    
                    masterStagePops[iElem][0][iD] = math.log(thisN)
            
            #print("iD ", iD, cname[19], gsName[csp2gas[19]], " logNCaI ", logE*masterStagePops[19][0][iD])
            
            for i in range(gsNumMols):
                thisN = gsPp[i+gsFirstMol] / Useful.k() / temp[0][iD]
                masterMolPops[i][iD] = math.log(thisN)
        
            #Needed  now GAS??  
            for iA in range(nelemAbnd):
                if (csp2gas[iA] != -1):
                    #element is in GAS package:  
                    #Captures neutral stage only
                    logNz[iA][iD] = math.log10(gsPp[csp2gas[iA]]) - Useful.logK() - temp[1][iD]
                    
        for iElem in range(26):
            species = cname[iElem] + "I"
            chiIArr[0] = IonizationEnergy.getIonE(species)
            #//THe following is a 2-element vector of temperature-dependent partitio fns, U, 
            #// that are base e log_e U
            log10UwAArr[0] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "II"
            chiIArr[1] = IonizationEnergy.getIonE(species)
            log10UwAArr[1] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "III"
            chiIArr[2] = IonizationEnergy.getIonE(species)
            log10UwAArr[2] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "IV"
            chiIArr[3] = IonizationEnergy.getIonE(species)
            log10UwAArr[3] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "V"
            chiIArr[4] = IonizationEnergy.getIonE(species)
            log10UwAArr[4] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "VI"
            chiIArr[5] = IonizationEnergy.getIonE(species)
            log10UwAArr[5] = PartitionFn.getPartFn2(species) #//base e log_e U
            #//double logN = (eheu[iElem] - 12.0) + logNH;


        
            #Neeed?  Now GAS:
            logNums = LevelPopsGasServer.stagePops3(masterStagePops[iElem][0], guessNe, chiIArr, log10UwAArr,   \
                                #thisNumMols, logNumBArr, dissEArr, log10UwBArr, logQwABArr, logMuABArr, \
                                numDeps, temp)

        #for iStage in range(numStages):
        #    for iTau in range(numDeps):
        #
        #        masterStagePops[iElem][iStage][iTau] = logNums[iStage][iTau]
        #masterStagePops[iElem][:][:] = [ [logNums[iStage][iTau] for iTau in range(numDeps)] for iStage in range(numStages) ]
        
            masterStagePops[iElem][:] = [x for x in logNums[:]]                    
        
        
            
    if (teff > GAStemp):  #teff > FoVtemp:
            
            #//  Converge Pg-Pe relation starting from intital guesses at Pg and Pe
            #//  - assumes all free electrons are from single ionizations
            #//  - David Gray 3rd Ed. Eq. 9.8:
        #print("guessPe[1] ", [logE*x for x in guessPe[1]] )
        for neIter in range(nInnerIter):
            
            for iD in range(numDeps):
                #//System.out.println("iD    logE*newPe[1][iD]     logE*guessPe[1]     logE*guessPGas[1]");
        
                #//re-initialize accumulators:
                thisTemp[0] = temp[0][iD]
                thisTemp[1] = temp[1][iD]
                peNumerator = 0.0 
                peDenominator = 0.0
                for iElem in range(nelemAbnd):
                    species = cname[iElem] + "I"
                    chiI = IonizationEnergy.getIonE(species)
                    #//THe following is a 2-element vector of temperature-dependent partitio fns, U, 
                #// that are base e log_e U
                    log10UwLArr = PartitionFn.getPartFn2(species) #//base e log_e U
                    species = cname[iElem] + "II"
                    log10UwUArr = PartitionFn.getPartFn2(species) #//base e log_e U
                    logPhi = LevelPopsGasServer.sahaRHS(chiI, log10UwUArr, log10UwLArr, thisTemp)
                    #if (iD%10 == 0):
                    #    print("iD ", iD, " iElem ", iElem, " logPhi ", logE*logPhi)
                    logPhiOverPe = logPhi - guessPe[1][iD]
                    logOnePlusPhiOverPe = math.log(1.0 + math.exp(logPhiOverPe)) 
                    logPeNumerTerm = logAz[iElem] + logPhiOverPe - logOnePlusPhiOverPe
                    peNumerator = peNumerator + math.exp(logPeNumerTerm)
                    logPeDenomTerm = logAz[iElem] + math.log(1.0 + math.exp(logPeNumerTerm))
                    peDenominator = peDenominator + math.exp(logPeDenomTerm)
                    #if (iD%10 == 0):
                    #    print("iD ", iD, " iElem ", iElem, " peNum ", peNumerator, " peDen ", peDenominator)                    
                #print("peNum ", math.log10(peNumerator), " peDen ", math.log10(peDenominator))
                #//iElem chemical element loop
                newPe[1][iD] = guessPGas[1][iD] + math.log(peNumerator) - math.log(peDenominator) 
                newPe[0][iD] = math.exp(newPe[1][iD])
                guessPe[1][iD] = newPe[1][iD]
                guessPe[0][iD] = math.exp(guessPe[1][iD])
            
        newNe[1] = [newPe[1][iD] - temp[1][iD] - Useful.logK() for iD in range(numDeps)]
        newNe[0] = [math.exp(newNe[1][iD]) for iD in range(numDeps)]   
        #guessNe[1][:] = [newNe[1][iD] for iD in range(numDeps)]
        #guessNe[0][:] = [newNe[0][iD] for iD in range(numDeps)]
        guessNe[1][:] = [ x for x in newNe[1][:] ]
        guessNe[0][:] = [ x for x in newNe[0][:] ]

        #print("newPe ", [logE*x for x in newPe[1]])
        #print("guessNe ", [logE*x for x in guessNe[1]])       
        #print("iD ", iD, " logT ", logE*temp[1][iD], " logNe ", logE*newNe[1][iD], " logRho ", logE*rho[1][iD], " mmw ", logE*math.log(mmw[iD]*Useful.amu()) )
        
    #if (teff > 100000.0):     #test
        
        logNz = State.getNz(numDeps, temp, guessPGas, guessPe, ATot, nelemAbnd, logAz)
    #for i in range(numDeps): 
    #    logNH[i] = logNz[0][i]
    #logNH[:] = [ logNz[0][i] for i in range(numDeps) ]
        logNH = [ x for x in logNz[0] ]
        
        zScaleList = 1.0 #//initialization   
        
        for iElem in range(26):
            species = cname[iElem] + "I"
            chiIArr[0] = IonizationEnergy.getIonE(species)
                #//THe following is a 2-element vector of temperature-dependent partitio fns, U, 
            #// that are base e log_e U
            log10UwAArr[0] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "II"
            chiIArr[1] = IonizationEnergy.getIonE(species)
            log10UwAArr[1] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "III"
            chiIArr[2] = IonizationEnergy.getIonE(species)
            log10UwAArr[2] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "IV"
            chiIArr[3] = IonizationEnergy.getIonE(species)
            log10UwAArr[3] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "V"
            chiIArr[4] = IonizationEnergy.getIonE(species)
            log10UwAArr[4] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "VI"
            chiIArr[5] = IonizationEnergy.getIonE(species)
            log10UwAArr[5] = PartitionFn.getPartFn2(species) #//base e log_e U
            
            logNums = LevelPopsGasServer.stagePops(logNz[iElem], guessNe, chiIArr, log10UwAArr,\
                     numDeps, temp)

            #for iStage in range(numStages):
            #    for iTau in range(numDeps):
            #
            #        masterStagePops[iElem][iStage][iTau] = logNums[iStage][iTau]
            #masterStagePops[iElem][:][:] = [ [logNums[iStage][iTau] for iTau in range(numDeps)] for iStage in range(numStages) ]
            masterStagePops[iElem][:] = [x for x in logNums[:]]
            
        #print("logNz[0] ", [logE*x for x in logNz[0]])
        #print("masterStagePops[0][0] ", [logE*x for x in masterStagePops[0][0]])            
    
            
        #//double logN = (eheu[iElem] - 12.0) + logNH;
        
            #//Get mass density from chemical composition: 
        rho = State.massDensity2(numDeps, nelemAbnd, logNz, cname)

        #//Total number density of gas particles: nuclear species + free electrons:
        #//AND
        # //Compute mean molecular weight, mmw ("mu"):
        #for i in range(numDeps):
        #    Ng[i] = newNe[0][i] #//initialize accumulation with Ne 
        #Ng[:] = [ newNe[0][i] for i in range(numDeps) ]
        Ng[:] = [ x for x in newNe[0] ]
    
        #Seems like this can't be "de-looped" without resorting to cryptic black boxes in python, like zip()
        for i in range(numDeps):
            for j in range(nelemAbnd):
                Ng[i] =  Ng[i] + math.exp(logNz[j][i]) #//initialize accumulation 
      
        #logMmw = rho[1][i] - math.log(Ng[i]) # // in g
        #mmw[i] = math.exp(logMmw) 
    
        mmw = [ rho[1][i] - math.log(Ng[i]) for i in range(numDeps) ]
        mmw = [ math.exp(x) for x in mmw ]

    
#//
#//Refine the number densities of the chemical elements at all depths  
    #logNz = State.getNz(numDeps, temp, guessPGas, guessPe, ATot, nelemAbnd, logAz)
    #for i in range(numDeps): 
    #    logNH[i] = logNz[0][i]
    #logNH[:] = [ logNz[0][i] for i in range(numDeps) ]
    
    
    #Needed now GAS??
    #logNH = [ x for x in logNz[0] ]
        #//System.out.println("i " + i + " logNH[i] " + logE*logNH[i]); 

#//
#//  Compute ionization fractions of H & He for kappa calculation 
#//
#//  Default inializations:

    #//these 2-element temperature-dependent partition fns are logarithmic  


#//
#////H & He only for now... we only compute H, He, and e^- opacity sources: 
#   //for (int iElem = 0; iElem < 2; iElem++){
#//H to Fe only for now... we only compute opacity sources for elements up to Fe: 
    

        
    #for iD in range(numDeps):
        #print("CSGPy: iD ", iD, cname[0], " logNCaI ", logE*masterStagePops[0][0][iD])
        #print("Ne ", newPe[0][iD], " logNe ", newPe[1][iD])      
            
                #//save ion stage populations at tau = 1:
            #//iTau loop
        #//iStage loop
    #//iElem loop

    #//Get mass density from chemical composition: 
#Needed?  Now Gas package
    #rho = State.massDensity2(numDeps, nelemAbnd, logNz, cname)

#Needed?  Now Gas package
#//Total number density of gas particles: nuclear species + free electrons:
#//AND
# //Compute mean molecular weight, mmw ("mu"):
    #for i in range(numDeps):
    #    Ng[i] = newNe[0][i] #//initialize accumulation with Ne 
    #Ng[:] = [ newNe[0][i] for i in range(numDeps) ]
    #Ng[:] = [ x for x in newNe[0] ]
    
    #Seems like this can't be "de-looped" without resorting to cryptic black boxes in python, like zip()
    #for i in range(numDeps):
    #    for j in range(nelemAbnd):
    #        Ng[i] =  Ng[i] + math.exp(logNz[j][i]) #//initialize accumulation 
      
        #logMmw = rho[1][i] - math.log(Ng[i]) # // in g
        #mmw[i] = math.exp(logMmw) 
    
    #mmw = [ rho[1][i] - math.log(Ng[i]) for i in range(numDeps) ]
    #mmw = [ math.exp(x) for x in mmw ]

    

#//H & He only for now... we only compute H, He, and e^- opacity sources: 
    logKappaHHe = Kappas.kappas2(numDeps, newPe, zScale, temp, rho,  \
                     numLams, lambdaScale, logAz[1],  \
                     masterStagePops[0][0], masterStagePops[0][1],  \
                     masterStagePops[1][0], masterStagePops[1][1], newNe,  \
                     teff, logTotalFudge)


#//Add in metal b-f opacity from adapted Moog routines:
    logKappaMetalBF = KappasMetal.masterMetal(numDeps, numLams, temp, lambdaScale, masterStagePops)
#//Add in Rayleigh scattering opacity from adapted Moog routines:
    logKappaRayl = KappasRaylGas.masterRayl(numDeps, numLams, temp, lambdaScale, masterStagePops, gsName, gsFirstMol, masterMolPops)
    
    #print("logKappaHHe ", [logKappaHHe[:][36]])
    #print("logKappaMetalBF ", [logKappaMetalBF[:][36]])
    #print("logKappaRayl ", [logKappaRayl[:][36]])
    
    #for i in range(numLams):
    #    print("logKappaHHe " , logE*logKappaHHe[i][36]);
    #for i in range(numLams):
    #    print("logKappaMetalBF " , logE*logKappaMetalBF[i][36]);
    #for i in range(numLams):
    #   print("logKappaRayl " , logE*logKappaRayl[i][36]);


#//Convert metal b-f & Rayleigh scattering opacities to cm^2/g and sum up total opacities
    #double logKapMetalBF, logKapRayl, kapContTot;
    #for iL in range(numLams):
    #    for iD in range(numDeps):
    #        logKapMetalBF = logKappaMetalBF[iL][iD] - rho[1][iD] 
    #        logKapRayl = logKappaRayl[iL][iD] - rho[1][iD] 
    #        kapContTot = math.exp(logKappaHHe[iL][iD]) + math.exp(logKapMetalBF) + math.exp(logKapRayl) 
    #        logKappa[iL][iD] = math.log(kapContTot)
    
    logKappa = [ [ math.exp(logKappaHHe[iL][iD]) + \
            math.exp(logKappaMetalBF[iL][iD] - rho[1][iD]) +\
            math.exp(logKappaRayl[iL][iD] - rho[1][iD]) for iD in range(numDeps)] for iL in range(numLams) ]
    logKappa = [ [math.log(logKappa[iL][iD]) for iD in range(numDeps)] for iL in range(numLams) ]
          
    kappaRos = Kappas.kapRos(numDeps, numLams, lambdaScale, logKappa, temp); 

#//Extract the "kappa_500" monochroamtic continuum oapcity scale
#// - this means we'll try interpreting the prescribed tau grid (still called "tauRos")as the "tau500" scale
    it500 = ToolBox.lamPoint(numLams, lambdaScale, 500.0e-7)
    #for i in range(numDeps):
    #    kappa500[1][i] = logKappa[it500][i]
    #    kappa500[0][i] = math.exp(kappa500[1][i])
    kappa500[1] = [ x for x in logKappa[it500] ]
    kappa500[0] = [ math.exp(x) for x in logKappa[it500] ] 
        
    pGas = Hydrostat.hydroFormalSoln(numDeps, grav, tauRos, kappaRos, temp, guessPGas)
    pRad = Hydrostat.radPress(numDeps, temp)

#//Update Pgas guess for iteration:
    #for i in range(numDeps):
#// Now we can update guessPGas:
    #    guessPGas[0][i] = pGas[0][i]
    #    guessPGas[1][i] = pGas[1][i]
    #    log10pgas[i] = log10e * pGas[1][i]
    #    log10pe[i] = log10e * (newNe[1][i] + Useful.logK() + temp[1][i])
    #    pe[i] = newNe[1][i] + Useful.logK() + temp[1][i]
    #    log10prad[i] = log10e * pRad[1][i]
    #    log10ne[i] = log10e * newNe[1][i]
        
    guessPGas[0] = [ x for x in pGas[0] ]
    guessPGas[1] = [ x for x in pGas[1] ]
    log10pgas = [ log10e * x for x in pGas[1] ]
    log10pe = [ log10e * (newNe[1][i] + Useful.logK() + temp[1][i]) for i in range(numDeps) ]
    pe = [ newNe[1][i] + Useful.logK() + temp[1][i] for i in range(numDeps) ]
    log10prad = [ log10e * x for x in pRad[1] ]
    log10ne = [ log10e * x for x in newNe[1] ]


    #Uncomment this block to inspect iteration-by-iteration convergence
    #Graphically inspect convergence:  Issue 'matplotlib qt5' in console before running code

    thisClr = palette[pIter%numClrs]
    #plt.plot(log10tauRos, log10pgas, color=thisClr)
    #plt.plot(log10tauRos, log10pgas, color=thisClr)
    #plt.plot(log10tauRos, log10pe, color=thisClr, linestyle='--')     
    #plt.plot(tauRos[1][:], newNe[1][:], thisClr)
#print("logKappa ", logKappa[:][36])

#//end Pgas-kappa iteration, nOuter
#Save as encapsulated postscript (eps) for LaTex
#plt.savefig('PConverge.eps', format='eps', dpi=1000)    
    
#//diagnostic
#//   int tauKapPnt01 = ToolBox.tauPoint(numDeps, tauRos, 0.01);
#//   System.out.println("logTauRos " + logE*tauRos[1][tauKapPnt01] + " temp " + temp[0][tauKapPnt01] + " pGas " + logE*pGas[1][tauKapPnt01]);
#//   System.out.println("tau " + " temp " + " logPgas " + " logPe " + " logRho "); 
#//   for (int iD = 1; iD < numDeps; iD+=5){
#//       System.out.println(" " + tauRos[0][iD] + " " + temp[0][iD] + " " +  logE*pGas[1][iD] + " " + logE*newPe[1][iD] + " " + logE*rho[1][iD]); 
#//   }
#//   for (int iL = 0; iL < numLams; iL++){
#//       //System.out.println(" " + lambdaScale[iL] + " " + logE*logKappa[iL][tauKapPnt01]); 
#//       System.out.println(" " + lambdaScale[iL]); 
#//       for (int iD = 1; iD < numDeps; iD+=5){
#//           System.out.println(" " + logE*(logKappa[iL][iD]+rho[1][iD]));  //cm^-1
#//       }
#//   } 
#   //int tauKapPnt1 = ToolBox.tauPoint(numDeps, tauRos, 1.0);
#   //System.out.println("logTauRos " + logE*tauRos[1][tauKapPnt1] + " temp " + temp[0][tauKapPnt1] + " pGas " + logE*pGas[1][tauKapPnt1]);
#   //for (int iL = 0; iL < numLams; iL++){
#   //    //System.out.println(" " + lambdaScale[iL] + " " + logE*logKappa[iL][tauKapPnt1]); 
#   //} 

 #       // Then construct geometric depth scale from tau, kappa and rho
 
#for iD in range(numDeps):
#    print("2 : ", (10.0**log10MasterGsPp[0][iD])/pGas[0][iD])
    
depths = DepthScale.depthScale(numDeps, tauRos, kappaRos, rho)

ifTcorr = False
ifConvec = False    
#//int numTCorr = 10;  //test
numTCorr = 0
for i in range(numTCorr):
    #//newTemp = TCorr.tCorr(numDeps, tauRos, temp);
    newTemp = MulGrayTCorr.mgTCorr(numDeps, teff, tauRos, temp, rho, kappaRos)
    #//newTemp = MulGrayTCorr.mgTCorr(numDeps, teff, tauRos, temp, rho, kappa500);
    #for iTau in range(numDeps):
    #    temp[1][iTau] = newTemp[1][iTau]
    #    temp[0][iTau] = newTemp[0][iTau]
    temp[1] = [ x for x in newTemp[1] ]
    temp[0] = [ x for x in newTemp[0] ]

"""/*
     //Convection:
     // Teff below which stars are convective.  
     //  - has to be finessed because Convec.convec() does not work well :-(
     double convTeff = 6500.0;
     double[][] convTemp = new double[2][numDeps];
     if (teff < convTeff) {
     convTemp = Convec.convec(numDeps, tauRos, depths, temp, press, rho, kappaRos, kappaSun, zScale, teff, logg);
     for (int iTau = 0; iTau < numDeps; iTau++) {
     temp[1][iTau] = convTemp[1][iTau];
     temp[0][iTau] = convTemp[0][iTau];
      }
     }
     */"""

#if ((ifTcorr == True) or (ifConvec == True)):
    #//Recall hydrostat with updates temps            
    #//Recall state withupdated Press                    
    #//recall kappas withupdates rhos
    #//Recall depths with re-updated kappas




###################################################
#
#
#
# Re-converge Ionization/chemical equilibrium WITH molecules
#
#
#
####################################################

#//
#// Now that the atmospheric structure is settled: 
#// Separately converge the Ne-ionization-fractions-molecular equilibrium for
#// all elements and populate the ionization stages of all the species for spectrum synthesis:
#//
#//stuff to save ion stage pops at tau=1:
    

iTauOne = ToolBox.tauPoint(numDeps, tauRos, unity)

#//
#//  Default inializations:
zScaleList = 1.0 #/initialization
#//these 2-element temperature-dependent partition fns are logarithmic
    
#//Default initialization:
#for i in range(numAssocMols):
#    for j in range(numDeps):
#        logNumBArr[i][j] = -49.0
#              
#    for k in range(numAtmPrtTmps):
#        log10UwBArr[i][k] = 0.0 #// default initialization lburns
#          
#    
#    dissEArr[i] = 29.0  #//eV
#    for kk in range(numMolPrtTmps):
#        logQwABArr[i][kk] = math.log(300.0)
#           
#    logMuABArr[i] = math.log(2.0) + Useful.logAmu()  #//g
#    mname_ptr[i] = 0
#    specB_ptr[i] = 0
 

#Iterations needed?   Now ga?
#for neIter2 in range(nInnerIter):
    
#Final run through Phil's GAS EOS/Chemic equil. for consistency with last HSE call above:

    
if (teff <= GAStemp):
        
    for iD in range(numDeps):    
        
        #print("isolv ", isolv, " temp ", temp[0][iD], " guessPGas ", guessPGas[0][iD])
        gasestReturn = CSGasEst.gasest(isolv, temp[0][iD], guessPGas[0][iD])
        gsPe0 = gasestReturn[0]
        gsP0 = gasestReturn[1]
        neq = gasestReturn[2]
        
        #print("iD ", iD, " gsPe0 ", gsPe0, " gsP0 ", gsP0, " neq ", neq)

        gasReturn = CSGas.gas(isolv, temp[0][iD], guessPGas[0][iD], gsPe0, gsP0, neq, tol, maxit)
        #a = gasReturn[0]
        #nit = gasReturn[1]
        gsPe = gasReturn[2]
        #pd = gasReturn[3]
        gsPp = gasReturn[4]
        #Can't pythonize this - gsPp padded at end with 0.0s
        #log10MasterGsPp[:][iD] = [math.log10(x) for x in gsPp]
        for iSpec in range(gsNspec):
            log10MasterGsPp[iSpec][iD] = math.log10(gsPp[iSpec])
            #print("1: ", gsPp[0]/guessPGas[0][iD])
            #ppix = gasReturn[5]
        gsMu = gasReturn[6]
        gsRho = gasReturn[7]
        
        
        newPe[0][iD] = gsPe
        newPe[1][iD] = math.log(gsPe)
        newNe[0][iD] = gsPe / Useful.k() / temp[0][iD]
        newNe[1][iD] = math.log(newNe[0][iD])
        guessPe[0][iD] = newPe[0][iD]
        guessPe[1][iD] = newPe[1][iD]
        
        rho[0][iD] = gsRho
        rho[1][iD] = math.log(gsRho)
        mmw[iD] = gsMu * Useful.amu()
        
        #print("iD ", iD, " logT ", logE*temp[1][iD], " logNe ", logE*newNe[1][iD], " logRho ", logE*rho[1][iD], " mmw ", logE*math.log(mmw[iD]*Useful.amu()) )
        
        
        #Take neutral stage populations for atomic species from GAS: 
        for iElem in range(nelemAbnd):
            
            if (csp2gas[iElem] != -1):
                #element is in GAS package:
                #neutral stage only
                thisN = gsPp[csp2gas[iElem]] / Useful.k() / temp[0][iD]    
                masterStagePops[iElem][0][iD] = math.log(thisN)
            
            #print("iD ", iD, cname[19], gsName[csp2gas[19]], " logNCaI ", logE*masterStagePops[19][0][iD])
            
        for i in range(gsNumMols):
            thisN = gsPp[i+gsFirstMol] / Useful.k() / temp[0][iD]
            masterMolPops[i][iD] = math.log(thisN)
        
        #Needed  now GAS??  
        for iA in range(nelemAbnd):
            if (csp2gas[iA] != -1):
                #element is in GAS package:
                #neutral stage only
                logNz[iA][iD] = math.log10(gsPp[csp2gas[iA]]) - Useful.logK() - temp[1][iD]

    #end iD loop        

    #Catch species NOT in Phil's GAS Chem. Equil. package   
    for iElem in range(nelemAbnd):
        
        if (csp2gas[iElem] == -1):

            species = cname[iElem] + "I"
            chiIArr[0] = IonizationEnergy.getIonE(species)
            #//The following is a 2-element vector of temperature-dependent partitio fns, U,
            #// that are base e log_e U
            log10UwAArr[0] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "II"
            chiIArr[1] = IonizationEnergy.getIonE(species)
            log10UwAArr[1] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "III"
            chiIArr[2] = IonizationEnergy.getIonE(species)
            log10UwAArr[2] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "IV"
            chiIArr[3] = IonizationEnergy.getIonE(species)
            log10UwAArr[3]= PartitionFn.getPartFn2(species) #//base 1e log_e U
            species = cname[iElem] + "V"
            chiIArr[4] = IonizationEnergy.getIonE(species)
            log10UwAArr[4]= PartitionFn.getPartFn2(species) #//base 1e log_e U
            species = cname[iElem] + "VI"
            chiIArr[5] = IonizationEnergy.getIonE(species)
            log10UwAArr[5]= PartitionFn.getPartFn2(species) #//base e log_e U
    
        

            #Element NOT in GAS package - compute ionization equilibrium:
            logNums = LevelPopsGasServer.stagePops(logNz[iElem], guessNe, chiIArr, log10UwAArr, \
                                                   #thisNumMols, logNumBArr, dissEArr, log10UwBArr, logQwABArr, logMuABArr, \
                            numDeps, temp);

    #for iStage in range(numStages):
    #    for iTau in range(numDeps):
    #        masterStagePops[iElem][iStage][iTau] = logNums[iStage][iTau]
    #    #//save ion stage populations at tau = 1:
    #    #} //iTau loop
    #    tauOneStagePops[iElem][iStage] = logNums[iStage][iTauOne]
        
    #} //iStage loop
            masterStagePops[iElem] = [ [ logNums[iStage][iTau] for iTau in range(numDeps) ] for iStage in range(numStages) ]
            tauOneStagePops[iElem] = [ logNums[iStage][iTauOne] for iStage in range(numStages) ]
    #} //iElem loop

if (teff > GAStemp):
    
    for neIter2 in range(nInnerIter):
    
        for iElem in range(nelemAbnd):

            species = cname[iElem] + "I"
            chiIArr[0] = IonizationEnergy.getIonE(species)
            #//The following is a 2-element vector of temperature-dependent partitio fns, U,
            #// that are base e log_e U
            log10UwAArr[0] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "II"
            chiIArr[1] = IonizationEnergy.getIonE(species)
            log10UwAArr[1] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "III"
            chiIArr[2] = IonizationEnergy.getIonE(species)
            log10UwAArr[2] = PartitionFn.getPartFn2(species) #//base e log_e U
            species = cname[iElem] + "IV"
            chiIArr[3] = IonizationEnergy.getIonE(species)
            log10UwAArr[3]= PartitionFn.getPartFn2(species) #//base 1e log_e U
            species = cname[iElem] + "V"
            chiIArr[4] = IonizationEnergy.getIonE(species)
            log10UwAArr[4]= PartitionFn.getPartFn2(species) #//base 1e log_e U
            species = cname[iElem] + "VI"
            chiIArr[5] = IonizationEnergy.getIonE(species)
            log10UwAArr[5]= PartitionFn.getPartFn2(species) #//base e log_e U
    
#} //end Ne - ionzation fraction -molecular equilibrium iteration neIter2
            logNums = LevelPopsGasServer.stagePops(logNz[iElem], guessNe, chiIArr, log10UwAArr, \
                  numDeps, temp);

            #for iStage in range(numStages):
            #    for iTau in range(numDeps):
            #        masterStagePops[iElem][iStage][iTau] = logNums[iStage][iTau]
            #    #//save ion stage populations at tau = 1:
            #    #} //iTau loop
            #    tauOneStagePops[iElem][iStage] = logNums[iStage][iTauOne]
        
            #} //iStage loop
            masterStagePops[iElem] = [ [ logNums[iStage][iTau] for iTau in range(numDeps) ] for iStage in range(numStages) ]
            tauOneStagePops[iElem] = [ logNums[iStage][iTauOne] for iStage in range(numStages) ]
            #Fill in in PP report:
            if (csp2gas[iElem] != -1):
                log10MasterGsPp[csp2gas[iElem]] = [ logE*(logNums[0][iTau] + temp[1][iTau] + Useful.logK())\
                               for iTau in range(numDeps) ]
            if (csp2gasIon1[iElem] != -1):
                log10MasterGsPp[csp2gasIon1[iElem]] = [ logE*(logNums[1][iTau] + temp[1][iTau] + Useful.logK())\
                               for iTau in range(numDeps) ]
            if (csp2gasIon2[iElem] != -1):
                log10MasterGsPp[csp2gasIon2[iElem]] = [ logE*(logNums[2][iTau] + temp[1][iTau] + Useful.logK())\
                               for iTau in range(numDeps) ]
            

        log10UwA = [0.0 for i in range(numAtmPrtTmps)]
        newNe[0] = [ 0.0 for iTau in range(numDeps) ]
     
    #This is cumulative and not trivially pythonizable
        for iTau in range(numDeps):
            for iElem in range(nelemAbnd):
                #//1 e^- per ion, #//2 e^- per ion
                newNe[0][iTau] = newNe[0][iTau]   \
                + math.exp(masterStagePops[iElem][1][iTau])  \
                + 2.0 * math.exp(masterStagePops[iElem][2][iTau])   
            #//+ 3.0 * Math.exp(masterStagePops[iElem][3][iTau])   #//3 e^- per ion
            #//+ 4.0 * Math.exp(masterStagePops[iElem][4][iTau]);  #//3 e^- per ion
        #}
        #    newNe[1][iTau] = math.log(newNe[0][iTau])
        #    #// Update guess for iteration:
        #    guessNe[0][iTau] = newNe[0][iTau]
        #    guessNe[1][iTau] = newNe[1][iTau] 
        #newNe[0] = [ [ newNe[0][iTau]   \
        #        + math.exp(masterStagePops[iElem][1][iTau])  \
        #        + 2.0 * math.exp(masterStagePops[iElem][2][iTau]) \
        #        for iElem in range(nelemAbnd) ] for iTau in range(numDeps) ]
        newNe[1] = [ math.log(x) for x in newNe[0] ]
        guessNe[0] = [ x for x in newNe[0][:] ]
        guessNe[1] = [ x for x in newNe[1][:] ]

        log10pe = [ log10e * (newNe[1][i] + Useful.logK() + temp[1][i]) for i in range(numDeps) ]
        log10ne = [ log10e * x for x in newNe[1] ]

#//
#Some atmospheric structure output AGAIN after chemical equilibrium: 
#Convert everything to log_10 OR re-scaled units for plotting, printing, etc:


#log10mmw = [0.0 for i in range(numDeps)]
#for i in range(numDeps):
#    log10pe[i] = log10e * (newNe[1][i] + Useful.logK() + temp[1][i])
#    log10ne[i] = log10e * newNe[1][i]
log10pe = [ log10e * (newNe[1][i] + Useful.logK() + temp[1][i]) for i in range(numDeps) ]
log10ne = [ log10e * x for x in newNe[1] ]
 

# Create a restart module for use in spectrum synthesis mode:

 #outFile = outPath + strucFile
outFile = outPath + fileStem + "_restart.py"
#print vertical atmospheric structure as a python source file for re-import to ChromaStarPy
# Can be used as a converged model for an almost pure spectrum syntehsis run
#with open(outFile, 'w', encoding='utf-8') as strucHandle:
with open(outFile, 'w') as restartHandle:

    headerString = "# " + inputParamString
    restartHandle.write(headerString + "\n")
    
    restartHandle.write("\n")
    outLine = "teffRS = " + str(teff) + " # K\n"
    restartHandle.write(outLine)
    outLine = "loggRS = " + str(logg) + " #log (cm/^2)\n"
    restartHandle.write(outLine)
    outLine = "log10ZScaleRS = " + str(log10ZScale) + "\n"
    restartHandle.write(outLine)    
    outLine = "xiTRS = " + str(xiT) + " # (km/s) \n"
    restartHandle.write(outLine)
    outLine = "logKapFudgeRS = " + str(logKapFudge) + "\n"
    restartHandle.write(outLine)    
    outLine = "logHeFeRS = " + str(logHeFe) + "\n"
    restartHandle.write(outLine)
    outLine = "logCORS = " + str(logCO) + "\n"
    restartHandle.write(outLine)
    outLine = "logAlphaFeRS = " + str(logAlphaFe) + "\n"
    restartHandle.write(outLine) 

    restartHandle.write("\n")    
    numDepsStr = str(numDeps)
    outLine = "numDeps = " + numDepsStr + "\n"
    restartHandle.write(outLine)
    restartHandle.write("\n")    

    outLine = "tauRosRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("tauRosRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(tauRos[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(tauRos[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("tauRosRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(tauRos[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(tauRos[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine) 
    
    outLine = "tempRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("tempRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(temp[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(temp[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)
    ### This won't work: restartHandle.write( [ str( temp[0][i] ) + ', ' for i in range(numDeps-1) ]\
                         # + str(temp[0][numDeps-1]) + ']\n')

    restartHandle.write("tempRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(temp[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(temp[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    outLine = "pGasRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("pGasRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(pGas[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(pGas[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("pGasRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(pGas[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(pGas[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    outLine = "peRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("peRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(newPe[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(newPe[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("peRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(newPe[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(newPe[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)
    
    outLine = "pRadRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("pRadRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(pRad[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(pRad[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("pRadRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(pRad[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(pRad[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)    
    
    outLine = "rhoRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("rhoRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(rho[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(rho[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("rhoRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(rho[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(rho[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    outLine = "kappa500RS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("kappa500RS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(kappa500[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(kappa500[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("kappa500RS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(kappa500[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(kappa500[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)        

    outLine = "kappaRosRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("kappaRosRS[0] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(kappaRos[0][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(kappaRos[0][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)

    restartHandle.write("kappaRosRS[1] = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(kappaRos[1][i]) + ', '
        restartHandle.write(outLine)
    outLine = str(kappaRos[1][numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)        

    outLine = "mmwRS = [ [ 0.0 for i in range(" + numDepsStr + ") ] for j in range(2) ]\n"
    restartHandle.write(outLine)
    restartHandle.write("mmwRS = [\\\n") #continuation line '\' has to be escaped
    for i in range(numDeps-1):
        outLine = str(mmw[i]) + ', '
        restartHandle.write(outLine)
    outLine = str(mmw[numDeps-1]) + '\\\n]\n'
    restartHandle.write(outLine)
    
############################################################
#
#
#
# Surface radiation field
#
#  - flux distribution (SED)
#  - high resolution synthetic spectrum
#
#
###############################################################

#//Okay - Now all the emergent radiation stuff:
#// Set up theta grid
#//  cosTheta is a 2xnumThetas array:
#// row 0 is used for Gaussian quadrature weights
#// row 1 is used for cos(theta) values
#// Gaussian quadrature:
#// Number of angles, numThetas, will have to be determined after the fact
cosTheta = Thetas.thetas()
numThetas = len(cosTheta[0])

#//establish a phi grid for non-axi-symmetric situations (eg. spots, in situ rotation, ...)
#//    //number of phi values per quandrant of unit circle centered on sub-stellar point
#//        //    in plane of sky:
#//        //For geometry calculations: phi = 0 is direction of positive x-axis of right-handed
#//        // 2D Cartesian coord system in plane of sky with origin at sub-stellar point (phi
#//        // increases CCW)
numPhiPerQuad = 6
numPhi = 4 * numPhiPerQuad
numPhiD = float(numPhi)
phi = [0.0 for i in range(numPhi)]
#//Compute phi values in whole range (0 - 2pi radians):
delPhi = 2.0 * math.pi / numPhiD
#double ii
#for i in range(numPhi):
#    ii = float(i)
#    phi[i] = delPhi * ii
phi = [ delPhi * float(i) for i in range(numPhi) ]
    
    
#boolean lineMode;

#//
#// ************
#//
#//  Spectrum synthesis section:
#// Set up continuum info:
isCool = 7300.0  #//Class A0

#//Set up opacity:
#// lambda break-points and gray levels:
#// No. multi-gray bins = num lambda breakpoints +1
minLambda = 30.0  #//nm
maxLambda = 1.0e6  #//nm

#// JOLA molecular bands here:
#// Just-overlapping line approximation treats molecular ro-vibrational bands as pseudo-continuum
#//opacity sources by "smearing" out the individual rotational fine-structure lines
#//See 1982A&A...113..173Z, Zeidler & Koester, 1982

#double jolaOmega0;  //band origin ?? //Hz OR waveno in cm^-1 ??
#//double[] jolaLogF; //total vibrational band oscillator strength (f_v'v")
#double jolaRSqu; //needed for total vibrational band oscillator strength (f_v'v")
jolaB = [0.0 for i in range(2)] #// B' value of upper vibational state (energy in cm^-1)??
jolaLambda = [0.0 for i in range(2)]
jolaAlphP = 0.0 #// alpha_P - weight of P branch (Delta J = -1)
jolaAlphR = 0.0 #/ alpha_R - weight of R branch (Delta J = 1)
jolaAlphQ = 0.0 #// alpha_Q - weight of Q branch (Delta J = 0)
#//Allen's Astrophysical quantities, 4th Ed., 4.12.2 - 4.13.1:
#// Electronic transition moment, Re
#//"Line strength", S = |R_e|^2*q_v'v" or just |R_e|^2 (R_00 is for the band head)
#//Section 4.4.2 - for atoms or molecules:
#// then: gf = (8pi^2m_e*nu/3he^2) * S
#//
#// ^48Ti^16O systems: Table 4.18, p. 91
#//  C^3Delta - X^3Delta ("alpha system") (Delta Lambda = 0??, p. 84 - no Q branch??)
#//  c^1Phi - a^1Delta ("beta system") (Delta Lambda = 1??, p. 84)
#//  A^3Phi - X^3Delta ("gamma system") (Delta Lambda = 0??, p. 84 - no Q branch??)
#// //
#// Rotational & vibrational constants for TiO states:, p. 87, Table 4.17
#// C^3Delta, X^3Delta a^1Delta, -- No "c^1Phi" - ??
#//
#//General TiO molecular rotational & vibrational constants - Table 3.12, p. 47

#//Zeidler & Koester 1982 p. 175, Sect vi):
#//If Q branch (deltaLambda = +/-1): alpP = alpR = 0.25, alpQ = 0.5
#//If NO Q branch (deltaLambda = 0): alpP = alpR = 0.5, alpQ = 0.0

#//number of wavelength point sampling a JOLA band
jolaNumPoints = 30 
#//int jolaNumPoints = 10; 

#// branch weights for transitions of DeltaLambda = +/- 1
jolaAlphP_DL1 = 0.25
jolaAlphR_DL1 = 0.25
jolaAlphQ_DL1 = 0.5
#// branch weights for transitions of DeltaLambda = 0
jolaAlphP_DL0 = 0.5
jolaAlphR_DL0 = 0.5
jolaAlphQ_DL0 = 0.0 #//no Q branch in this case

#double jolaS; //line strength
#double jolaLogF; //line strength

logSTofHelp = math.log(8.0/3.0) + 2.0*math.log(math.pi) + Useful.logMe() - Useful.logH() - 2.0*Useful.logEe()
#//Hand-tuned for now - Maybe this is the "script S" factor in Allen 4th Ed., p. 88 (S = |R|^2*q_v'v"*scriptS)
jolaQuantumS = 1.0 #//default for multiplicative factor 
logNumJola = [0.0 for i in range(numDeps)]
jolaProfPR = [ [0.0 for i in range(numDeps)] for j in range(jolaNumPoints) ]  #// For unified P & R branch
jolaProfQ = [ [0.0 for i in range(numDeps)] for j in range(jolaNumPoints) ]  #//For Q branch
#//Differential cross-section - the main "product" of the JOLA approximation:
dfBydv = [ [0.0 for i in range(numDeps)] for j in range(jolaNumPoints) ]  

#//
dataPath = "InputData/"
#//
#//
#// **************  Atomic line list:
#//
#//NIST Atomic Spectra Database Lines Data
#//Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD Team (2015). NIST Atomic Spectra Database (ver. 5.3), [Online]. Available: http://physics.nist.gov/asd [2017, January 30]. National Institute of Standards and Technology, Gaithersburg, MD.
#//
#//Stuff for byte file method:
#//
#// *** NOTE: bArrSize must have been noted from the stadout of LineListServer and be consistent
#// with whichever line list is linked to gsLineListBytes.dat, and be st manually here:
lineListBytes = absPath + dataPath + "atomLineListFeb2017Bytes.dat"
#lineListBytes = "gsLineListBytes.dat"
#//

#//System.out.println(" *********************************************** ");
#//System.out.println("  ");
#//System.out.println("  ");
print("READING LINE LIST")
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println(" *********************************************** ");

with open(lineListBytes, 'rb') as fHandle:    
    #Java: barray = ByteFileRead.readFileBytes(lineListBytes, bArrSize);
    barray = fHandle.read()
    
#fHandle closed automatically when with: exited   

#Java: String decoded = new String(barray, 0, bArrSize);  // example for one encoding type 
decoded = barray.decode('utf-8')

#//System.out.println(" *********************************************** ");
#//System.out.println("  ");
#//System.out.println("  ");
print("LINE LIST READ")
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println(" *********************************************** ");

arrayLineString = decoded.split("%%")
#//Number of lines MUST be the ONLY entry on the first line 

numLineList = len(arrayLineString) - 1
#numLineList = 1 #//test


#//Atomic lines:
#//Okay, here we go:
list2Lam0 = [0.0 for i in range(numLineList)]  #// nm
list2Element = ["" for i in range(numLineList)] #//element
list2StageRoman = ["" for i in range(numLineList)] #//ion stage
list2Stage = [0 for i in range(numLineList)] #//ion stage
list2Mass = [0.0 for i in range(numLineList)] #// amu
list2LogGammaCol = [0.0 for i in range(numLineList)]
#//Einstein coefficient for spontaneous de-exciation:
list2LogAij = [0.0 for i in range(numLineList)] #//log base 10
#//Log of unitless oscillator strength, f 
list2Logf = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage I (eV) 
list2ChiI1 = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage II (eV)
list2ChiI2 = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage III (eV) 
list2ChiI3 = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage IV (eV)
list2ChiI4 = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage V (eV)
list2ChiI5 = [0.0 for i in range(numLineList)]
#//Ground state ionization E - Stage VI (eV)
list2ChiI6 = [0.0 for i in range(numLineList)]
#//Excitation E of lower E-level of b-b transition (eV)
list2ChiL = [0.0 for i in range(numLineList)]
#//Unitless statisital weight, Ground state - Stage I
#//double[] list2Gw1 = new double[numLineList];
#//Unitless statisital weight, Ground state - Stage II
#//double[] list2Gw2 = new double[numLineList];
#//Unitless statisital weight, Ground state - Stage III
#//double[] list2Gw3 = new double[numLineList];
#//Unitless statisital weight, Ground state - Stage IV
#//double[] list2Gw4 = new double[numLineList];
#//double[] list2Gw4 = new double[numLineList];
#//Unitless statisital weight, lower E-level of b-b transition                 
list2GwL = [0.0 for i in range(numLineList)]
#//double[] list2GwU For now we'll just set GwU to 1.0
#// Is stage II?

#//Atomic Data sources:
 
#double thisF;
list2_ptr = 0 #//pointer into line list2 that we're populating
numFields = 7 #//number of field per record 
#// 0: element, 1: ion stage, 2: lambda_0, 3: logf, 4: g_l, 5: chi_l
thisRecord = ["" for i in range(numFields)] 
    
#String myString;  //useful helper

for iLine in range(numLineList):

    
    #// "|" turns out to mean something in regexp, so we need to escape with '\\':
    thisRecord = arrayLineString[iLine].split("|")
    #//System.out.println("thisRecord[0] " + thisRecord[0]
    #//                 + "thisRecord[1] " + thisRecord[1] 
    #//                 + "thisRecord[2] " + thisRecord[2] 
    #//                 + "thisRecord[3] " + thisRecord[3] 
    #//                 + "thisRecord[4] " + thisRecord[4] 
    #//                 + "thisRecord[5] " + thisRecord[5]);
                 
       
    myString = thisRecord[0].strip() 
    list2Element[iLine] = myString
    myString = thisRecord[1].strip()
    list2StageRoman[iLine] = myString  
    myString = thisRecord[2].strip() 
    list2Lam0[iLine] = float(myString)
    myString = thisRecord[3].strip()
    list2LogAij[iLine] = float(myString)
    myString = thisRecord[4].strip()
    list2Logf[iLine] = float(myString)
    myString = thisRecord[5].strip()
    list2ChiL[iLine] = float(myString)
    #//// Currently not used
    #//        myString = thisRecord[6].trim();
    #//        list2ChiU = Double.parseDouble(myString);
    #//        myString = thisRecord[7].trim();
    #//        list2Jl = Double.parseDouble(myString);
    #//        myString = thisRecord[8].trim();
    #//        list2Ju = Double.parseDouble(myString);
    myString = thisRecord[9].strip()
    list2GwL[iLine] = float(myString)
    #//// Currently not used
    #//        myString = thisRecord[10].trim();
    #//        list2GwU = Double.parseDouble(myString);
        
    #//Get the chemical element symbol - we don't know if it's one or two characters
    if (list2StageRoman[list2_ptr] == "I"):
        list2Stage[list2_ptr] = 0
             
    if (list2StageRoman[list2_ptr] == "II"):
        list2Stage[list2_ptr] = 1
             
    if (list2StageRoman[list2_ptr] == "III"):
        list2Stage[list2_ptr] = 2
             
    if (list2StageRoman[list2_ptr] == "IV"):
        list2Stage[list2_ptr] = 3
             
    if (list2StageRoman[list2_ptr] == "V"):
        list2Stage[list2_ptr] = 4
             
    if (list2StageRoman[list2_ptr] == "VI"):
        list2Stage[list2_ptr] = 5
             
    if (list2StageRoman[list2_ptr] == "VII"):
        list2Stage[list2_ptr] = 6
             
#//wavelength in nm starts at position 23 and is in %8.3f format - we're not expecting anything greater than 9999.999 nm

#// Some more processing:
    list2Mass[list2_ptr] = AtomicMass.getMass(list2Element[list2_ptr])
    species = list2Element[list2_ptr] + "I"
    list2ChiI1[list2_ptr] = IonizationEnergy.getIonE(species) 
    species = list2Element[list2_ptr] + "II"
    list2ChiI2[list2_ptr] = IonizationEnergy.getIonE(species)
    species = list2Element[list2_ptr] + "III"
    list2ChiI3[list2_ptr] = IonizationEnergy.getIonE(species) 
    species = list2Element[list2_ptr] + "IV"
    list2ChiI4[list2_ptr] = IonizationEnergy.getIonE(species)
    species = list2Element[list2_ptr] + "V"
    list2ChiI5[list2_ptr] = IonizationEnergy.getIonE(species)
    species = list2Element[list2_ptr] + "VI"
    list2ChiI6[list2_ptr] = IonizationEnergy.getIonE(species)

    #//We're going to have to fake the ground state statistical weight for now - sorry:
    #//list2Gw1[list2_ptr] = 1.0;
    #//list2Gw2[list2_ptr] = 1.0; 
    #//list2Gw3[list2_ptr] = 1.0;
    #//list2Gw4[list2_ptr] = 1.0; 
    list2LogGammaCol[list2_ptr] = logGammaCol 

    #//We've gotten everything we need from the NIST line list:
    list2_ptr+=1
        
    #} //iLine loop 

numLines2 = list2_ptr
#numLines2 = 0  #test
#//
#
#//Okay - what kind of mess did we make...
#
#
#// END FILE I/O SECTION


#//System.out.println(" *********************************************** ");
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println("BEFORE TRIAGE");
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println(" *********************************************** ");
#//
#//Triage: For each line: Voigt, Gaussian, or neglect??

#//
gaussLineCntr = 0 #//initialize accumulator
#//int sedLineCntr = 0; //initialize accumulator
#//No! boolean[] ifThisLine = new boolean[numLines2]; //initialize line strength flag
gaussLine_ptr = [0 for i in range(numLines2)] #//array of pointers to lines that make the cut in the 
#//int sedLine_ptr[] = new int[numLines2]; //array of pointers to lines that make the cut in the 
                                                  #// master line list  
        
isFirstLine = True #//initialization
firstLine = 0 #//default initialization
#// This holds 2-element temperature-dependent base 10 logarithmic parition fn:
thisUwV = [0.0 for i in range(numAtmPrtTmps)]
#// Below created a loop to initialize each value to zero for the five temperatures lburns
#for i in range(len(thisUwV)):
#    thisUwV[i] = 0.0  #//default initialization



for iLine in range(numLines2):

    #//No! ifThisLine[iLine] = false;
    #//if H or He, make sure kappaScale is unity:
    if ((list2Element[iLine] == "H") \
    or (list2Element[iLine] == "He")):
        zScaleList = 1.0
        #//list2Gw1[iLine] = 2.0;  //fix for H lines
        if (list2Lam0[iLine] <= 657.0):
            list2GwL[iLine] = 8.0  #//fix for Balmer lines
        else:
            list2GwL[iLine] = 18.0  #//fix for Paschen lines        
    else: 
        zScaleList = zScale


    list2Lam0[iLine] = list2Lam0[iLine] * nm2cm  #// nm to cm
    iAbnd = 0 #//initialization
    logNums_ptr = 0
    #//System.out.println("iLine " + iLine + " list2Element[iLine] " + list2Element[iLine]);
    #Not trivially pythonizable:
    for jj in range(nelemAbnd):
        #//System.out.println("jj " + jj + " cname[jj]" + cname[jj]+"!");
        if (list2Element[iLine] == cname[jj]):
            if (list2Stage[iLine] == 0):
                 species = cname[jj] + "I"
                 logNums_ptr = 0
            
            if (list2Stage[iLine] == 1):
                 species = cname[jj] + "II"
                 logNums_ptr = 1
            
            if (list2Stage[iLine] == 2):
                 species = cname[jj] + "III"
                 logNums_ptr = 4
            
            if (list2Stage[iLine] == 3):
                 species = cname[jj] + "IV"
                 logNums_ptr = 5
            
            if (list2Stage[iLine] == 4):
                 species = cname[jj] + "V"
                 logNums_ptr = 6
            
            if (list2Stage[iLine] == 5):
                 species = cname[jj] + "VI"
                 logNums_ptr = 7
            
            thisUwV = PartitionFn.getPartFn2(species) #//base e log_e U
            break   #//we found it
        
        iAbnd+=1
    #} //jj loop
            
    list2LogNums = [ [ 0.0 for i in range(numDeps) ] for j in range(numStages+2) ]
    #for iTau in range(numDeps):
    #    list2LogNums[0][iTau] = masterStagePops[iAbnd][0][iTau]
    #    list2LogNums[1][iTau] = masterStagePops[iAbnd][1][iTau]
    #    list2LogNums[4][iTau] = masterStagePops[iAbnd][2][iTau]
    #    list2LogNums[5][iTau] = masterStagePops[iAbnd][3][iTau]
    #    list2LogNums[6][iTau] = masterStagePops[iAbnd][4][iTau]
    #    list2LogNums[7][iTau] = masterStagePops[iAbnd][5][iTau]
    list2LogNums[0] = [ x for x in masterStagePops[iAbnd][0] ]
    list2LogNums[1] = [ x for x in masterStagePops[iAbnd][1] ]
    list2LogNums[4] = [ x for x in masterStagePops[iAbnd][2] ]
    list2LogNums[5] = [ x for x in masterStagePops[iAbnd][3] ]
    list2LogNums[6] = [ x for x in masterStagePops[iAbnd][4] ]
    list2LogNums[7] = [ x for x in masterStagePops[iAbnd][5] ]
    
    #if ( ((list2Lam0[iLine]) > lambdaStart) and ((list2Lam0[iLine]) < lambdaStop) and species=="CaI"):
    #    print("iLine ", iLine, " species ", species, " logNums_ptr ", logNums_ptr, " list2Lam0 ", list2Lam0[iLine], \
    #          " list2Logf[iLine] ", list2Logf[iLine] , " list2ChiL ", list2ChiL[iLine], " thisUwV ", thisUwV, \
    #          " list2GwL ", list2GwL[iLine])
    
            
    numHelp = LevelPopsGasServer.levelPops(list2Lam0[iLine], list2LogNums[logNums_ptr], list2ChiL[iLine], thisUwV, \
                list2GwL[iLine], numDeps, temp)
    
            
    #for iTau in range(numDeps):
    #    list2LogNums[2][iTau] = numHelp[iTau]
    #    list2LogNums[3][iTau] = numHelp[iTau] / 2.0 #//fake for testing with gS3 line treatment
    list2LogNums[2] = [ x for x in numHelp ]
    list2LogNums[3] = [ x/2.0 for x in numHelp ]
   
    #if ( ((list2Lam0[iLine]) > lambdaStart) and ((list2Lam0[iLine]) < lambdaStop) and species=="CaI"):
    #    print("list2LogNums[2] ", list2LogNums[2])         

    #//linePoints: Row 0 in cm (will need to be in nm for Plack.planck), Row 1 in Doppler widths
    #//For now - initial strength check with delta fn profiles at line centre for triage:
    listNumPointsDelta = 1
    listLinePointsDelta = LineGrid.lineGridDelta(list2Lam0[iLine], list2Mass[iLine], xiT, numDeps, teff)
    listLineProfDelta = LineProf.delta(listLinePointsDelta, list2Lam0[iLine], numDeps, tauRos, list2Mass[iLine], xiT, teff) 
    listLogKappaLDelta = LineKappa.lineKap(list2Lam0[iLine], list2LogNums[2], list2Logf[iLine], listLinePointsDelta, listLineProfDelta,
                    numDeps, zScaleList, tauRos, temp, rho, logFudgeTune)
   

    
    """/* Let's not do this - too slow:
            // Low resolution SED lines and high res spectrum synthesis region lines are mutually
            // exclusive sets in wavelength space:
            //Does line qualify for inclusion in SED as low res line at all??
            // Check ratio of line centre opacity to continuum at log(TauRos) = -5, -3, -1
            if ( (logE*(listLogKappaLDelta[0][6] - kappa[1][6]) > sedThresh)  
              || (logE*(listLogKappaLDelta[0][18] - kappa[1][18]) > sedThresh)  
              || (logE*(listLogKappaLDelta[0][30] - kappa[1][30]) > sedThresh) ){ 
                   if ( ( list2Stage[iLine] == 0) || (list2Stage[iLine] == 1) 
                    ||  ( list2Stage[iLine] == 2) || (list2Stage[iLine] == 3) ){
                        if ( (list2Lam0[iLine] > lamUV) and (list2Lam0[iLine] < lamIR) ){
                           if ( (list2Lam0[iLine] < lambdaStart) || (list2Lam0[iLine] > lambdaStop) ){ 
                      //No! ifThisLine[iLine] = true;
                      sedLine_ptr[sedLineCntr] = iLine;
                      sedLineCntr++;
      //System.out.println("SED passed, iLine= " + iLine + " sedLineCntr " + sedLineCntr 
      //   + " list2Lam0[iLine] " + list2Lam0[iLine] 
      //   + " list2Element[iLine] " + list2Element[iLine]
      //   + " list2Stage[iLine] " + list2Stage[iLine]); 
                                 }
                            }
                      } 
                }
    */"""

    #//Does line qualify for inclusion in high res spectrum synthesis region??
    #// Check ratio of line centre opacity to continuum at log(TauRos) = -5, -3, -1
    #//Find local value of lambda-dependent continuum kappa - list2Lam0 & lambdaScale both in cm here: 
    thisLambdaPtr = ToolBox.lamPoint(numLams, lambdaScale, list2Lam0[iLine])
    if ( (logE*(listLogKappaLDelta[0][6] - logKappa[thisLambdaPtr][6]) > lineThresh)  
    or (logE*(listLogKappaLDelta[0][18] - logKappa[thisLambdaPtr][18]) > lineThresh)  
    or (logE*(listLogKappaLDelta[0][30] - logKappa[thisLambdaPtr][30]) > lineThresh) ): 
        if ( ( list2Stage[iLine] == 0) or (list2Stage[iLine] == 1) 
		  or ( list2Stage[iLine] == 2) or (list2Stage[iLine] == 3) 
        or  ( list2Stage[iLine] == 4) or (list2Stage[iLine] == 5) ):
            if ( (list2Lam0[iLine] > lambdaStart) and (list2Lam0[iLine] < lambdaStop) ): 
                #special test condition
                #if (list2Element[iLine] == "Na"):
			           #//No! ifThisLine[iLine] = true;
                    gaussLine_ptr[gaussLineCntr] = iLine
                    gaussLineCntr+=1
                    if (isFirstLine == True):
                        firstLine = iLine
                        isFirstLine = False

#//
#} //iLine loop

#//
#
#//We need to have at least one line in region:
areNoLines = False #//initialization
if (gaussLineCntr == 0):
    gaussLineCntr = 1
    gaussLine_ptr[0] = firstLine
    areNoLines = True
         

numGaussLines = gaussLineCntr
#//System.out.println(" *********************************************** ");
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println("AFTER TRIAGE");
#//System.out.println("  ");
#//System.out.println("  ");
#//System.out.println(" *********************************************** ");

#//Notes
#//if Hydrogen or Helium, kappaScale should be unity for these purposes:
#//double kappaScaleList = 1.0; //initialization                   
#//

listNumCore = 3  #//half-core //default initialization
listNumWing = 1  #//per wing
#//int sedNumWing = 1;  //per wing
#//int thisNumCore = sedNumCore; //default initialization
#//int thisNumWing = sedNumWing; //default initialization
if (sampling == "coarse"):
    listNumCore = 3  #//half-core
    listNumWing = 3  #//per wing
else: 
    listNumCore = 5  #//half-core
    listNumWing = 10  #//per wing
         
#//Delta fn - for testing and strength triage
#        //int listNumPoints = 1;
#//All gaussian
#        //int listNumPoints = 2 * listNumCore - 1; // + 1;  //Extra wavelength point at end for monochromatic continuum tau scale
#////All full voigt:
listNumPoints = (2 * (listNumCore + listNumWing) - 1) #// + 1;  //Extra wavelength point at end for monochromatic continuum tau scale
#//int sedNumPoints = (2 * (sedNumCore + sedNumWing) - 1); // + 1;  //Extra wavelength point at end for monochromatic continuum tau scale
#//int thisNumPoints = sedNumPoints; //default initialization
numNow = numLams  #//initialize dynamic counter of how many array elements are in use
#int numMaster;
if (ifMols == 1):
    numMaster = numLams + (numGaussLines * listNumPoints) + (numJola * jolaNumPoints) #// + (numSedLines * sedNumPoints); //total size (number of wavelengths) of master lambda & total kappa arrays 
else:
    numMaster = numLams + (numGaussLines * listNumPoints)
    
masterLams = [0.0 for i in range(numMaster)]
#//Line blanketed opacity array:

logMasterKaps = [ [ 0.0 for i in range(numDeps) ] for j in range(numMaster) ]
#//seed masterLams and logMasterKaps with continuum SED lambdas and kappas:
#//This just initializes the first numLams of the numMaster elements

#//Initialize monochromatic line blanketed opacity array:
#// Seed first numLams wavelengths with continuum wavelength and kappa values 
for iL in range(numLams):
    masterLams[iL] = lambdaScale[iL]
    for iD in range(numDeps):
        logMasterKaps[iL][iD] = logKappa[iL][iD] 
#This pythonization will not work
#masterLams[0: numLams] = [ lambdaScale[iL] for iL in range(numLams) ]
#logMasterKaps[0: numLams][:] = [ [ logKappa[iL][iD] for iD in range(numDeps) ] for iL in range(numLams) ]           

        
#//initialize the remainder with dummy values - these values will be clobbered as line wavelengths are inserted, 
#// and don't matter
for iL in range(numLams, numMaster):
    masterLams[iL] = lambdaScale[numLams - 1]
    for iD in range(numDeps):
        logMasterKaps[iL][iD] = logKappa[numLams-1][iD]
#This pythonization will not work        
#masterLams[numLams: numMaster-1] = [ lambdaScale[numLams - 1] for iL in range(numLams, numMaster) ]
#logMasterKaps[numLams: numMaster-1][:] = [ [ logKappa[numLams-1][iD] for iD in range(numDeps) ] for iL in range(numLams, numMaster) ] 
           
#stop
#//Stuff for the the Teff recovery test:
#double lambda1, lambda2, fluxSurfBol, logFluxSurfBol;
fluxSurfBol = 0
 
#//Get the components for the power series expansion approximation of the Hjerting function
#//for treating Voigt profiles:
hjertComp = HjertingComponents.hjertingComponents()

#// This holds 2-element temperature-dependent base 10 logarithmic parition fn:
#for k in range(numAtmPrtTmps):
#    thisUwV[k] = 0.0 #//default initialization
thisUwV = [ 0.0 for i in range(numAtmPrtTmps) ]



listLineProf = [ [ 0.0 for i in range(numDeps) ] for j in range(listNumPoints) ]

print("Beginning spectrum synthesis, numVoigtLines ", numGaussLines)
#// Put in high res spectrum synthesis lines:
for iLine in range(numGaussLines):


    #//if H or He, make sure kappaScale is unity:
    if ((list2Element[gaussLine_ptr[iLine]] == "H")
    or (list2Element[gaussLine_ptr[iLine]] == "He")):
        zScaleList = 1.0
        #//list2Gw1[gaussLine_ptr[iLine]] = 2.0;  //fix for H lines
        if (list2Lam0[gaussLine_ptr[iLine]] <= 657.0e-7):
            list2GwL[gaussLine_ptr[iLine]] = 8.0  #//fix for Balmer lines
        else:
            list2GwL[gaussLine_ptr[iLine]] = 18.0  #//fix for Paschen lines
    else:
        zScaleList = zScale;
    

    #//
    iAbnd = 0 #//initialization
    logNums_ptr = 0
    for jj in range(nelemAbnd):
        if (list2Element[gaussLine_ptr[iLine]] == cname[jj]):
            if (list2Stage[gaussLine_ptr[iLine]] == 0):
                species = cname[jj] + "I"
                logNums_ptr = 0
                
            if (list2Stage[gaussLine_ptr[iLine]] == 1):
                species = cname[jj] + "II"
                logNums_ptr = 1
                
            if (list2Stage[gaussLine_ptr[iLine]] == 2):
                species = cname[jj] + "III"
                logNums_ptr = 4
                
            if (list2Stage[gaussLine_ptr[iLine]] == 3):
                species = cname[jj] + "IV"
                logNums_ptr = 5
                
            if (list2Stage[gaussLine_ptr[iLine]] == 4):
                species = cname[jj] + "V"
                logNums_ptr = 6
                
            if (list2Stage[gaussLine_ptr[iLine]] == 5):
                species = cname[jj] + "VI"
                logNums_ptr = 7
                
            thisUwV = PartitionFn.getPartFn2(species) #//base e log_e U
            break   #//we found it
             #}
        iAbnd+=1
    #} //jj loop
        
    list2LogNums = [ [ 0.0 for i in range(numDeps) ] for j in range(numStages+2) ]
    #for iTau in range(numDeps):
    #    list2LogNums[0][iTau] = masterStagePops[iAbnd][0][iTau]
    #    list2LogNums[1][iTau] = masterStagePops[iAbnd][1][iTau]
    #    list2LogNums[4][iTau] = masterStagePops[iAbnd][2][iTau]
    #    list2LogNums[5][iTau] = masterStagePops[iAbnd][3][iTau]
    #    list2LogNums[6][iTau] = masterStagePops[iAbnd][4][iTau]
    #    list2LogNums[7][iTau] = masterStagePops[iAbnd][5][iTau]
    list2LogNums[0] = [ masterStagePops[iAbnd][0][iTau] for iTau in range(numDeps) ]
    list2LogNums[1] = [ masterStagePops[iAbnd][1][iTau] for iTau in range(numDeps) ]
    list2LogNums[4] = [ masterStagePops[iAbnd][2][iTau] for iTau in range(numDeps) ]
    list2LogNums[5] = [ masterStagePops[iAbnd][3][iTau] for iTau in range(numDeps) ]
    list2LogNums[6] = [ masterStagePops[iAbnd][4][iTau] for iTau in range(numDeps) ]
    list2LogNums[7] = [ masterStagePops[iAbnd][5][iTau] for iTau in range(numDeps) ]
            
    numHelp = LevelPopsGasServer.levelPops(list2Lam0[gaussLine_ptr[iLine]], list2LogNums[logNums_ptr], list2ChiL[gaussLine_ptr[iLine]], thisUwV,
                    list2GwL[gaussLine_ptr[iLine]], numDeps, temp)
                              

    #for iTau in range(numDeps):
    #    list2LogNums[2][iTau] = numHelp[iTau]
    #    list2LogNums[3][iTau] = -19.0 #//upper E-level - not used - fake for testing with gS3 line treatment
    list2LogNums[2] = [ x for x in numHelp ]
    list2LogNums[3] = [ -19.0 for i in range(numDeps) ] #//upper E-level - not used - fake for testing with gS3 line treatment
    #print("iLine ", iLine, " iAbnd ", iAbnd)
    #print("list2LogNums ", list2LogNums[2])    
        #if ( (list2Element[gaussLine_ptr[iLine]] == "Na") and (list2Stage[gaussLine_ptr[iLine]] == 0) ):
            #if (iTau%5 == 1):
            #    outline = ("iTau "+ str(iTau)+ " Na I list2LogNums[2]: "+ str(log10e*list2LogNums[2][iTau]) + "\n")
            #    outHandle.write(outline)
    #if ( ((list2Lam0[gaussLine_ptr[iLine]]) > lambdaStart) and ((list2Lam0[gaussLine_ptr[iLine]]) < lambdaStop) and species=="CaI"):
    #    print("iLine ", iLine , " gaussLine_ptr ", gaussLine_ptr[iLine] ," list2Lam0 ", list2Lam0[gaussLine_ptr[iLine]], " list2LogAij ", list2LogAij[gaussLine_ptr[iLine]], " list2Logf ", list2Logf[gaussLine_ptr[iLine]])
    #    print("list2Mass ", list2Mass[gaussLine_ptr[iLine]], " list2LogGammaCol ", list2LogGammaCol[gaussLine_ptr[iLine]])

    #if ( ((list2Lam0[gaussLine_ptr[iLine]]) > lambdaStart) and ((list2Lam0[gaussLine_ptr[iLine]]) < lambdaStop) and species=="CaI"):
    #    print("list2LogNums[2] ", list2LogNums[2])             

    #//Proceed only if line strong enough: 
    #// 
    #//ifThisLine[gaussLine_ptr[iLine]] = true; //for testing
    #//No! if (ifThisLine[gaussLine_ptr[iLine]] == true){
              
    #// Gaussian only approximation to profile (voigt()):
    #//            double[][] listLinePoints = LineGrid.lineGridGauss(list2Lam0[gaussLine_ptr[iLine]], list2Mass[gaussLine_ptr[iLine]], xiT, numDeps, teff, listNumCore);
    #//            double[][] listLineProf = LineProf.gauss(listLinePoints, list2Lam0[gaussLine_ptr[iLine]],
    #//                    numDeps, teff, tauRos, temp, tempSun);
    #// Gaussian + Lorentzian approximation to profile (voigt()):
    listLinePoints = LineGrid.lineGridVoigt(list2Lam0[gaussLine_ptr[iLine]], list2Mass[gaussLine_ptr[iLine]], xiT, 
                                            numDeps, teff, listNumCore, listNumWing, species)
    #print("species: ", species)
    #if ( (list2Element[gaussLine_ptr[iLine]] == "Na") and (list2Stage[gaussLine_ptr[iLine]] == 0) ):
    #    outline = ("iLine "+ str(iLine)+ " gaussLine_ptr "+ str(gaussLine_ptr[iLine])+ " list2Lam0 "+ str(list2Lam0[gaussLine_ptr[iLine]])+ " list2LogAij "+ 
    #      str(list2LogAij[gaussLine_ptr[iLine]])+ " list2LogGammaCol "+ str(list2LogGammaCol[gaussLine_ptr[iLine]])+ " list2Logf "+ 
    #      str(list2Logf[gaussLine_ptr[iLine]]) + "\n")
    #    outHandle.write(outline)
    if (species == "HI"):
 #//System.out.println("Calling Stark...");
        listLineProf = LineProf.stark(listLinePoints, list2Lam0[gaussLine_ptr[iLine]], list2LogAij[gaussLine_ptr[iLine]],
                      list2LogGammaCol[gaussLine_ptr[iLine]],
                      numDeps, teff, tauRos, temp, pGas, newNe, tempSun, pGasSun, hjertComp, species)
    else:
        #print("voigt branch called")
        listLineProf = LineProf.voigt(listLinePoints, list2Lam0[gaussLine_ptr[iLine]], list2LogAij[gaussLine_ptr[iLine]],
                      list2LogGammaCol[gaussLine_ptr[iLine]],
                      numDeps, teff, tauRos, temp, pGas, tempSun, pGasSun, hjertComp, dbgHandle)
                
        
    listLogKappaL = LineKappa.lineKap(list2Lam0[gaussLine_ptr[iLine]], list2LogNums[2], list2Logf[gaussLine_ptr[iLine]], listLinePoints, listLineProf,
                       numDeps, zScaleList, tauRos, temp, rho, logFudgeTune)
    #print("listLogKappaL ", listLogKappaL[:][16])
    #stop                        
    #if ( (list2Element[gaussLine_ptr[iLine]] == "Na") and (list2Stage[gaussLine_ptr[iLine]] == 0) ):
    #        for iTau in range(numDeps):
    #            if (iTau%5 == 1):
    #                for iL in range(listNumPoints):
    #                    if (iL%2 == 0):
    #                        print("iTau ", iTau, " iL ", iL, " listLinePoints[0]&[1] ", listLinePoints[0][iL], " ", listLinePoints[1][iL], 
    #                              " listLineProf ", listLineProf[iL][iTau],  " listLogKappaL ", log10e*listLogKappaL[iL][iTau])
    listLineLambdas = [0.0 for i in range(listNumPoints)]
    #for il in range(listNumPoints):
    #    #// // lineProf[gaussLine_ptr[iLine]][*] is DeltaLambda from line centre in cm
    #    listLineLambdas[il] = listLinePoints[0][il] + list2Lam0[gaussLine_ptr[iLine]]
    listLineLambdas = [ x + list2Lam0[gaussLine_ptr[iLine]] for x in listLinePoints[0] ]
            

    masterLamsOut = SpecSyn.masterLambda(numLams, numMaster, numNow, masterLams, listNumPoints, listLineLambdas)
    logMasterKapsOut = SpecSyn2.masterKappa(numDeps, numLams, numMaster, numNow, masterLams, masterLamsOut, \
                                           logMasterKaps, listNumPoints, listLineLambdas, listLogKappaL)

    numNow = numNow + listNumPoints
    #numNow = numNow + listNumPoints
    #plt.plot(masterLamsOut, [logMasterKapsOut[i][12] for i in range(numNow)]) 
    #plt.plot(masterLamsOut, [logMasterKapsOut[i][12] for i in range(numNow)], '.')      
    #//update masterLams and logMasterKaps:

    for iL in range(numNow):
        masterLams[iL] = masterLamsOut[iL]
        for iD in range(numDeps):
            #//Still need to put in multi-Gray levels here:
            logMasterKaps[iL][iD] = logMasterKapsOut[iL][iD]
    #This pythoniztion does not work:       
    #masterLams[0: numNow] = [ masterLamsOut[iL] for iL in range(numNow) ]
    #logMasterKaps[0: numNow][:] = [ [ logMasterKapsOut[iL][iD] for iD in range(numDeps) ] for iL in range(numNow) ]

    #print("iLine ", iLine, " gaussLine_ptr ", gaussLine_ptr[iLine])            
  
        #//No! } //ifThisLine strength condition
#//numLines loop
print("End spectrum synthesis")        
#print("logMasterKaps ", logMasterKaps[:][16])
   
#////

if (teff <= jolaTeff):
    #//Begin loop over JOLA bands - isert JOLA oapcity into opacity spectum...
    helpJolaSum = 0.0
  
    if (ifMols == 1):

        for iJola in range(numJola):

            #//Find species in molecule set:

            for iMol in range(gsFirstMol, gsNspec):
                if (gsName[iMol] == jolaSpecies[iJola]):
                    #//System.out.println("mname " + mname[iMol]);
                    #for iTau in range(numDeps):
                    #    logNumJola[iTau] = masterMolPops[iMol][iTau]
                    logNumJola = [ x for x in masterMolPops[iMol-gsFirstMol] ]          
                    #}
                #}
            #}


            
            jolaOmega0 = MolecData.getOrigin(jolaSystem[iJola])  #//band origin ?? //Freq in Hz OR waveno in cm^-1 ??
            jolaB = MolecData.getRotConst(jolaSystem[iJola]) #// B' and b" values of upper and lower vibational state
            jolaLambda = MolecData.getWaveRange(jolaSystem[iJola]) #//approx wavelength range of band
            jolaDeltaLambda = MolecData.getDeltaLambda
            
            jolaLogF = -99.0 #Default
            
            if (jolaWhichF[iJola] == "Allen"):
             
                #Band strength: Allen's Astrophysical Quantities approach
                jolaRSqu = MolecData.getSqTransMoment(jolaSystem[iJola]) #//needed for total vibrational band oscillator strength (f_v'v")
                #//Line strength factor from Allen's 4th Ed., p. 88, "script S":
                #This is practically the astrophysical tuning factor:
                jolaQuantumS = MolecData.getQuantumS(jolaSystem[iJola]) 

                #//Compute line strength, S, Allen, p. 88:
                jolaS = jolaRSqu * jolaQuantumS #//may not be this simple (need q?)
                #//Compute logf , Allen, p. 61 Section 4.4.2 - for atoms or molecules - assumes g=1 so logGf = logF:
                #//jolaLogF = logSTofHelp + Math.log(jolaOmega0) + Math.log(jolaS); //if omega0 is a freq in Hz
                #//Gives wrong result?? jolaLogF = logSTofHelp + Useful.logC() + Math.log(jolaOmega0) + Math.log(jolaS); //if omega0 is a waveno in cm^-1 
                checkgf = 303.8*jolaS/(10.0*jolaLambda[0]) #//"Numerical relation", Allen 4th, p. 62 - lambda in A
                jolaLogF = math.log(checkgf) #//better??
                #print("iJola ", iJola, " logF ", 10.0**(logE*jolaLogF+14) )
            
            if (jolaWhichF[iJola] == "Jorgensen"):
                #Band strength: Jorgensen, 1994, A&A, 284, 179 approach - we have the f values directly:
            
                #This is practically the astrophysical tuning factor:
                jolaQuantumS = MolecData.getQuantumS(jolaSystem[iJola])
            
                jolaRawF = MolecData.getFel(jolaSystem[iJola])
                jolaF = jolaRawF * jolaQuantumS
                #print(iJola, " jQS ", jolaQuantumS, " jRF ", jolaRawF, " jF ", jolaF)
                jolaLogF = math.log(jolaF)
                #print("iJola ", iJola, " logF ", 10.0**(logE*jolaLogF+14) )
            
            if (jolaDeltaLambda == 0): 
                jolaAlphP = jolaAlphP_DL0 #// alpha_P - weight of P branch (Delta J = 1)
                jolaAlphR = jolaAlphR_DL0 #// alpha_R - weight of R branch (Delta J = -1)
                jolaAlphQ = jolaAlphQ_DL0 #// alpha_Q - weight of Q branch (Delta J = 0)
        
            if (jolaDeltaLambda != 0): 
                jolaAlphP = jolaAlphP_DL1 #// alpha_P - weight of P branch (Delta J = 1)
                jolaAlphR = jolaAlphR_DL1 #// alpha_R - weight of R branch (Delta J = -1)
                jolaAlphQ = jolaAlphQ_DL1 #// alpha_Q - weight of Q branch (Delta J = 0)
        

            jolaPoints = Jola.jolaGrid(jolaLambda, jolaNumPoints)

            #//This sequence of methods might not be the best way, but it's based on the procedure for atomic lines
            #// Put in JOLA bands:

            #//P & R brnaches in every case:
            dfBydv = Jola.jolaProfilePR(jolaOmega0, jolaLogF, jolaB,
                                     jolaPoints, jolaAlphP, jolaAlphR, numDeps, temp)

            jolaLogKappaL = Jola.jolaKap(logNumJola, dfBydv, jolaPoints, 
                  numDeps, temp, rho)

#////Q branch if DeltaLambda not equal to 0
#//         if (jolaDeltaLambda != 0){ 
#//            dfBydv = Jola.jolaProfileQ(jolaOmega0, jolaLogF, jolaB,
#//                                      jolaPoints, jolaAlphQ, numDeps, temp);
#// //
#//            double[][] jolaLogKappaQL = Jola.jolaKap(logNumJola, dfBydv, jolaPoints, 
#//                   numDeps, temp, rho);
#//            //Now add it to the P & R branch opacity:
#//            for (int iW = 0; iW < jolaNumPoints; iW++){
#//               for (int iD = 0; iD < numDeps; iD++){
#//             //   //  if (iD%10 == 1){
#//              //       //System.out.println("iW " + iW + " iD " + iD + " jolaLogKappaL " + jolaLogKappaL[iW][iD]);
#//               //  // }
#//                   helpJolaSum = Math.exp(jolaLogKappaL[iW][iD]) + Math.exp(jolaLogKappaQL[iW][iD]);
#//                   jolaLogKappaL[iW][iD] = Math.log(helpJolaSum); 
#//               } //iD loop
#//            } //iW loop
#//         } //Q-branch if

            jolaLambdas = [0.0 for i in range(jolaNumPoints)]
            #for il in range(jolaNumPoints):
            #    #// // lineProf[gaussLine_ptr[iLine]][*] is DeltaLambda from line centre in cm
            #    jolaLambdas[il] = nm2cm * jolaPoints[il]
            jolaLambdas = [ nm2cm * x for x in jolaPoints ]
            #print("jolaLambdas[0] ", jolaLambdas[0], " jolaLambdas[jolaNumPoints] ", jolaLambdas[jolaNumPoints-1])
            

            masterLamsOut = SpecSyn.masterLambda(numLams, numMaster, numNow, masterLams, jolaNumPoints, jolaLambdas)
            logMasterKapsOut = SpecSyn2.masterKappa(numDeps, numLams, numMaster, numNow, masterLams, masterLamsOut, \
                                logMasterKaps, jolaNumPoints, jolaLambdas, jolaLogKappaL)
            numNow = numNow + jolaNumPoints
            #numNow = numNow + jolaNumPoints

            #//update masterLams and logMasterKaps:
            for iL in range(numNow):
                masterLams[iL] = masterLamsOut[iL]
                for iD in range(numDeps):
                    #//Still need to put in multi-Gray levels here:
                    logMasterKaps[iL][iD] = logMasterKapsOut[iL][iD]
            #This pythoniztion does not work:
            #masterLams[0: numNow] = [ masterLamsOut[iL] for iL in range(numNow) ]
            #logMasterKaps[0: numNow][:] = [ [ logMasterKapsOut[iL][iD] for iD in range(numDeps) ] for iL in range(numNow) ]
            #plt.xlim(500.0e-7, 820.0e-7)
            #plt.plot([masterLams[i] for i in range(numNow)],\
            #          [logMasterKaps[i][20] for i in range(numNow)] )    

        #} //iJola JOLA band loop

    #} //ifTiO condition

#} //jolaTeff condition
    
#//

#//Sweep the wavelength grid for line-specific wavelength points that are closer together than needed for
#//critical sampling:
#//equivalent spectral resolution of wavelength-dependent critical sampling interval
sweepRes = 500000.0 #//equivalent spectral resolution of wavelength-dependent critical sampling interval
#//cm //use shortest wavelength to avoid under-smapling:
sweepDelta = lambdaStart / sweepRes #//cm //use shortest wavelength to avoid under-smapling
sweepHelp = [ 0.0 for i in range(numMaster) ] #//to be truncated later
#//Initialize sweepHelp
#for iSweep in range(numMaster):
#    sweepHelp[iSweep] = 0.0
sweepHelp = [ 0.0 for iSweep in range(numMaster) ]
   
#//
sweepHelp[0] = masterLams[0] #//An auspicous start :-)
lastLam = 0 #//index of last masterLam wavelength NOT swept out
iSweep = 1 #//current sweepHelp index
#//

for iLam in range(1, numMaster):
    #print ( "In sweeping loop: ", (masterLams[iLam] - masterLams[lastLam]) )
    if ( (masterLams[iLam] - masterLams[lastLam]) >= sweepDelta):
        #//Kept - ie. NOT swept out:
        sweepHelp[iSweep] = masterLams[iLam]
        lastLam = iLam
        iSweep+=1
        #print("Kept condition passed, iSweep ", iSweep)
      

numKept = iSweep-1
#sweptLams = [x for x in sweepHelp]
sweptLams = [0.0 for i in range(numKept)]
#for iKept in range(numKept):
#    sweptLams[iKept] = sweepHelp[iKept]
sweptLams = [ sweepHelp[iKept] for iKept in range(numKept) ]

#stop
#//Interpolate the total extinction array onto the swept wavelength grid:
keptHelp = [0.0 for i in range(numKept)]
logSweptKaps = [ [ 0.0 for i in range(numDeps) ] for j in range(numKept) ]
logMasterKapsId = [0.0 for i in range(numMaster)]
#Not trivially pythonizable:
for iD in range(numDeps):
    #//extract 1D kappa vs lambda at each depth:
    for iL in range(numMaster):
        logMasterKapsId[iL] = logMasterKaps[iL][iD]
      
    #keptHelp = ToolBox.interpolV(logMasterKapsId, masterLams, sweptLams)
    keptHelp = numpy.interp(sweptLams, masterLams, logMasterKapsId)
    for iL in range(numKept):
        logSweptKaps[iL][iD] = keptHelp[iL]

#Won't work logSweptKaps = [ [ ToolBox.interpolV(logMasterKaps[iL][iD], masterLams, sweptLams) for iL in range()] ]

#} //iD loop
    

#Special code to test sweeper by forcing it to NOT sweep anything:
    # - IF this is uncommented, then sweeper above should be commented
"""for iLam in range(1, numMaster):
    #//Kept - ie. NOT swept out:
    sweepHelp[iSweep] = masterLams[iLam]
    iSweep+=1
numKept = iSweep-1
sweptLams = [0.0 for i in range(numKept)]
for iKept in range(numKept):
    sweptLams[iKept] = sweepHelp[iKept]
#//Interpolate the total extinction array onto the swept wavelength grid:
logSweptKaps = [ [ 0.0 for i in range(numDeps) ] for j in range(numKept) ]
for iD in range(numDeps):
    for iL in range(numKept):
        logSweptKaps[iL][iD] = logMasterKaps[iL][iD]
#end special sweeper test block"""
#//
#////
#//Continuum monochromatic optical depth array:
logTauCont = LineTau2.tauLambdaCont(numLams, logKappa,
                 kappa500, numDeps, tauRos, logTotalFudge)

#//Evaluate formal solution of rad trans eq at each lambda 
#// Initial set to put lambda and tau arrays into form that formalsoln expects
contIntens = [ [ 0.0 for i in range(numThetas) ] for j in range(numLams) ]
contIntensLam = [0.0 for i in range(numThetas)]

contFlux = [ [ 0.0 for i in range(numLams) ] for j in range(2) ]
contFluxLam = [0.0 for i in range(2)]
thisTau = [ [ 0.0 for i in range(numDeps) ] for j in range(2) ]
lineMode = False  #//no scattering for overall SED

for il in range(numLams):

    #for id in range(numDeps):
    #    thisTau[1][id] = logTauCont[il][id]
    #    thisTau[0][id] = math.exp(logTauCont[il][id])
    thisTau[1] = [ x for x in logTauCont[il] ]
    thisTau[0] = [ math.exp(x) for x in logTauCont[il] ]
    #} // id loop

    contIntensLam = FormalSoln.formalSoln(numDeps,
                    cosTheta, lambdaScale[il], thisTau, temp, lineMode)

    #for it in range(numThetas):
    #    contIntens[il][it] = contIntensLam[it]
    contIntens[il] = [ x for x in contIntensLam ]
    #} //it loop - thetas


    #//// Teff test - Also needed for convection module!:
    if (il > 1):
        lambda2 = lambdaScale[il] #// * 1.0E-7;  // convert nm to cm
        lambda1 = lambdaScale[il - 1] #// * 1.0E-7;  // convert nm to cm
        fluxSurfBol = fluxSurfBol + contFluxLam[0] * (lambda2 - lambda1)

#//il loop

contFlux = Flux.flux3(contIntens, lambdaScale, cosTheta, phi, cgsRadius, omegaSini, macroVkm)

logTauMaster = LineTau2.tauLambda(numKept, sweptLams, logSweptKaps,
                numDeps, kappa500, tauRos, logTotalFudge)

#//Line blanketed formal Rad Trans solution:
#//Evaluate formal solution of rad trans eq at each lambda throughout line profile
#// Initial set to put lambda and tau arrays into form that formalsoln expects
masterIntens = [ [ 0.0 for i in range(numThetas) ] for j in range(numKept) ]  
masterIntensLam = [0.0 for i in range(numThetas)]

masterFlux = [ [ 0.0 for i in range(numKept) ] for j in range(2) ]
masterFluxLam = [0.0 for i in range(2)]

lineMode = False  #//no scattering for overall SED

for il in range(numKept):

#//                        }
    #for id in range(numDeps):
    #    thisTau[1][id] = logTauMaster[il][id]
    #    thisTau[0][id] = math.exp(logTauMaster[il][id])
    #} // id loop
    thisTau[1] = [ x for x in logTauMaster[il] ]
    thisTau[0] = [ math.exp(x) for x in logTauMaster[il] ]

    masterIntensLam = FormalSoln.formalSoln(numDeps,
                cosTheta, sweptLams[il], thisTau, temp, lineMode)


    #for it in range(numThetas):
    #    masterIntens[il][it] = masterIntensLam[it]
    masterIntens[il] = [ x for x in masterIntensLam ]
#} //it loop - thetas


#} //il loop

masterFlux = Flux.flux3(masterIntens, sweptLams, cosTheta, phi, cgsRadius, omegaSini, macroVkm)

#pltb.plot(sweptLams, masterFlux[0])
#plt.plot(sweptLams, masterFlux[0], '.')

#Can we find a pythonic way to accumulate instead of this for loop??
for il in range(numKept):
    #//// Teff test - Also needed for convection module!:
    if (il > 1):
        lambda2 = sweptLams[il] #// * 1.0E-7;  // convert nm to cm
        lambda1 = sweptLams[il - 1] #// * 1.0E-7;  // convert nm to cm
        fluxSurfBol = fluxSurfBol + masterFlux[0][il] * (lambda2 - lambda1)
    #}

logFluxSurfBol = math.log(fluxSurfBol)
logTeffFlux = (logFluxSurfBol - Useful.logSigma()) / 4.0
teffFlux = math.exp(logTeffFlux)

print("Recovered Teff = %9.2f" % (teffFlux))

#//Extract linear monochromatic continuum limb darkening coefficients (LDCs) ("epsilon"s):
ldc = [0.0 for i in range(numLams)]
ldc = LDC.ldc(numLams, lambdaScale, numThetas, cosTheta, contIntens)


#
#
#
#
#   Post-processing
#
# *****   Post-processing ported from ChromaStarServerUI  *****
#
#
#
#
#
#



#logContFluxI = ToolBox.interpolV(contFlux[1], lambdaScale, sweptLams)
logContFluxI = numpy.interp(sweptLams, lambdaScale, contFlux[1])

#//Quality control:
tiny = 1.0e-19
logTiny = math.log(tiny)
#iStart = ToolBox.lamPoint(numMaster, masterLams, (nm2cm*lambdaStart))
#iStop = ToolBox.lamPoint(numMaster, masterLams, (nm2cm*lambdaStop))
iStart = ToolBox.lamPoint(numKept, sweptLams, lambdaStart);
iStop = ToolBox.lamPoint(numKept, sweptLams, lambdaStop);
   
#//Continuum rectification
numSpecSyn = iStop - iStart + 1
specSynLams = [0.0 for i in range(numSpecSyn)]
specSynFlux = [ [ 0.0 for i in range(numSpecSyn) ] for j in range(2) ]
#js specSynFlux.length = 2;
#specSynFlux[0] = [];
#specSynFlux[1] = [];
#specSynFlux[0].length = numSpecSyn; 
#specSynFlux[1].length = numSpecSyn;
#for iCount in range(numSpecSyn):
#    specSynLams[iCount] = sweptLams[iStart+iCount]
#    specSynFlux[1][iCount] = masterFlux[1][iStart+iCount] - logContFluxI[iStart+iCount]
#   specSynFlux[0][iCount] = math.exp(specSynFlux[1][iCount])
    
specSynLams = [ x for x in sweptLams[iStart: iStart+numSpecSyn] ]
specSynFlux[1] = [ masterFlux[1][iStart+iCount] - logContFluxI[iStart+iCount] for iCount in range(numSpecSyn) ]
specSynFlux[0] = [math.exp(x) for x in specSynFlux[1] ]

#//
#// * eqWidthSynth will try to return the equivalenth width of EVERYTHING in the synthesis region
#// * as one value!  Isolate the synthesis region to a single line to a clean result
#// * for that line!
#// *
Wlambda = PostProcess.eqWidthSynth(specSynFlux, specSynLams)

#//
#//Radial velocity correction:
#//We have to correct both masterLams AND specSynLams to correct both the overall SED and the spectrum synthesis region:

masterLams2 = [ 0.0 for i in range(numKept) ]
specSynLams2 = [ 0.0 for i in range(numSpecSyn) ]

#//refresh default each run:
#for i in range(numKept):
#    masterLams2[i] = sweptLams[i]
masterLams2 = [ x for x in sweptLams ]
     
#for i in range(numSpecSyn):
#    specSynLams2[i] = specSynLams[i]
specSynLams2 = [ x for x in specSynLams ] 
    
deltaLam = 0.0
c = 2.9979249E+10 #// light speed in vaccuum in cm/s
RVfac = RV / (1.0e-5*c)
if (RV != 0.0):
    #for i in range(numKept):
    #    deltaLam = RVfac * sweptLams[i]
    #    masterLams2[i] = masterLams2[i] + deltaLam
    masterLams2 = [ masterLams2[i] + (RVfac * sweptLams[i]) for i in range(numKept) ]
      
    #for i in range(numSpecSyn):
    #    deltaLam = RVfac * specSynLams[i]
    #    specSynLams2[i] = specSynLams2[i] + deltaLam 
    specSynLams2 = [ specSynLams2[i] + (RVfac * specSynLams[i])  ]   
     
invnAir = 1.0 / 1.000277 #// reciprocal of refractive index of air at STP 
if (vacAir == "air"):
    #for i in range(numKept):
    #    masterLams2[i] = invnAir * masterLams2[i]
    masterLams2 = [ invnAir * x for x in masterLams2 ]
       
    #for i in range(numSpecSyn):
    #    specSynLams2[i] = invnAir * specSynLams2[i]
    specSynLams2 = [ invnAir * x for x in specSynLams2 ]   
     

colors =  PostProcess.UBVRI(masterLams2, masterFlux, numDeps, tauRos, temp)
#print("U-V: ", colors[0], " B-V: ", colors[1], " V-R ", colors[2], " V-I: ", colors[3],\
#      " R-I ", colors[4], " V- K ", colors[5], " J-K: ", colors[6])
print("U-B: %6.2f B-V: %6.2f V-R: %6.2f V-I: %6.2f R-I: %6.2f V-K: %6.2f J-K: %6.2f" %\
      (colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6]))
#// UBVRI band intensity annuli - for disk rendering:
bandIntens = PostProcess.iColors(masterLams2, masterIntens, numThetas, numKept) 
    
gaussFilter = PostProcess.gaussian(masterLams2, numKept, diskLambda, diskSigma, lamUV, lamIR) 
#//Use *shifted* wavelength scale (masterLams2) for user-filter integration of spectrum:
tuneBandIntens = PostProcess.tuneColor(masterLams2, masterIntens, numThetas, numKept, \
                                       gaussFilter, lamUV, lamIR) 

#//Fourier transform of narrow band image:
ft = PostProcess.fourier(numThetas, cosTheta, tuneBandIntens)
numK = len(ft[0])


    
#
#
# Report 1:
#
#
#Atmospheric structure output: 
#Convert everything to log_10 OR re-scaled units for plotting, printing, etc:
    

log10temp = [0.0 for i in range(numDeps)]
log10rho = [0.0 for i in range(numDeps)]
log10kappaRos = [0.0 for i in range(numDeps)]
log10kappa500 = [0.0 for i in range(numDeps)]
mmwAmu = [0.0 for i in range(numDeps)]
depthsKm = [0.0 for i in range(numDeps)]
#log10mmw = [0.0 for i in range(numDeps)]
#for i in range(numDeps):
#    log10tauRos[i] = log10e * tauRos[1][i]
#    log10temp[i] = log10e * temp[1][i]
#    log10pgas[i] = log10e * pGas[1][i]
#    log10pe[i] = log10e * (newNe[1][i] + Useful.logK() + temp[1][i])
#    log10prad[i] = log10e * pRad[1][i]
#    log10ne[i] = log10e * newNe[1][i]
#    log10rho[i] = log10e * rho[1][i]
#    log10NH[i] = log10e * logNH[i]
#    log10kappaRos[i] = log10e * kappaRos[1][i]
#    log10kappa500[i] = log10e * kappa500[1][i]
#    mmwAmu[i] = mmw[i] / Useful.amu()
#    depthsKm[i] = 1.0e-5 * depths[i]

log10tauRos = [ round(log10e * x, 4) for x in tauRos[1] ]
log10temp = [ round(log10e * x, 4) for x in temp[1] ]
log10pgas = [ round(log10e * x, 4) for x in pGas[1] ]
log10pe = [ round(log10e * (newNe[1][i] + Useful.logK() + temp[1][i]), 4) for i in range(numDeps) ]
log10prad = [ round(log10e * x, 4) for x in pRad[1] ]
log10ne = [ round(log10e * x, 4) for x in newNe[1] ]
log10rho = [ round(log10e * x, 4) for x in rho[1] ]
log10NH = [ round(log10e * x, 4) for x in logNH ]
log10kappaRos = [ round(log10e * x, 4) for x in kappaRos[1] ]
log10kappa500 = [ round(log10e * x, 4) for x in kappa500[1] ]
mmwAmu = [ round(x / Useful.amu(), 4) for x in mmw ]
depthsKm = [ round(1.0e-5 * x, 4) for x in depths ]

#outFile = outPath + strucFile
outFile = outPath + fileStem + ".struc.txt"
#print vertical atmospheric structure
#with open(outFile, 'w', encoding='utf-8') as strucHandle:
with open(outFile, 'w') as strucHandle:
#with open(strucFile, 'w') as strucHandle:    
    strucHandle.write(inputParamString + "\n")
    strucHandle.write("cgs units, unless otherwise noted" + "\n")
    strucHandle.write("logTauRos   depth   temp   logPgas   logPe  logPRad   logNe   logNH   logRho   mu(amu)   logKapRos   logKap500" + "\n")
    #NOt trivially pythonizable - each time through it writes a line to an output file
    for i in range(numDeps):
        outLine = str(log10tauRos[i]) + "   " + str(depthsKm[i]) + "   " + str(round(temp[0][i], 4)) + "   " + str(log10pgas[i]) +\
        "   " + str(log10pe[i]) + "   " + str(log10prad[i]) + "   " + str(log10ne[i]) + "   " + str(log10NH[i]) + "   " + str(log10rho[i]) +\
        "   " + str(mmwAmu[i]) + "   " + str(log10kappaRos[i]) + "   " + str(log10kappa500[i]) + "\n"
        strucHandle.write(outLine)
    #This doesn't work...
    #outLine = ""
    #outLine = [ outLine + str(log10tauRos[i]) + " " + str(depthsKm[i]) + " " + str(temp[0][i]) + " " + str(log10pgas[i]) + " " + str(log10pe[i]) +   \
    #                  " " + str(log10prad[i]) + " " + str(log10ne[i]) + " " + str(log10NH[i]) + " " + str(log10rho[i]) + " " + str(mmwAmu[i]) +   \
    #                  str(log10kappaRos[i]) + " " + str(log10kappa500[i]) + "\n" for i in range(numDeps) ]
    #strucHandle.write(outLine)
    
if makePlot == "structure":

    #Initialplot set-up
    plt.title = "T_kin vs log(tau)"
    plt.xlabel(r'$\log_{10} \tau_{\rm ROs}$')
    plt.ylabel(r'$T_{\rm kin}$ (K)')
    xMin = -6.5
    xMax = 2.5
    plt.xlim(xMin, xMax)
    yMax = max(temp[0]) + 1000.0
    yMin = min(temp[0]) - 500.0
    plt.ylim(yMin, yMax)
    plt.plot(log10tauRos, temp[0])    
    
    


#
#
# Report 2: 
#
#
#Print absolute spectral energy distribution (SED)

    
numWave = numKept
wave = [0.0 for i in range(numWave)]
log10Wave = [0.0 for i in range(numWave)]
log10Flux = [0.0 for i in range(numWave)]
#for i in range(numWave):
#    wave[i] = cm2nm * masterLams2[i]
#    log10Wave[i] = math.log10(masterLams2[i])
#    log10Flux[i] = log10e * masterFlux[1][i]
wave = [ round(cm2nm * x, 4) for x in masterLams2 ]
log10Wave = [ round(math.log10(x), 4) for x in masterLams2 ]
log10Flux = [ round(log10e * x, 4) for x in masterFlux[1] ]


if makePlot == "sed":

    #Initial plt plot set-up
    plt.title = "Spectral energy distribution (SED)"
    plt.xlabel(r'$\log_{10} \lambda$ (nm)')
    plt.ylabel(r'$\log_{10} F_\lambda$ (erg s$^{-1}$ cm$^{-2}$ cm$^{-1}$')
    xMin = min(log10Wave) - 0.1
    xMax = max(log10Wave) + 0.1
    plt.xlim(xMin, xMax)
    yMax = max(log10Flux) + 0.5
    yMin = min(log10Flux) - 0.5
    plt.ylim(yMin, yMax)
    plt.plot(log10Wave, log10Flux)    

#outFile = outPath + sedFile
outFile = outPath + fileStem + ".sed.txt"
#with open(outFile, 'w', encoding='utf-8') as sedHandle:
with open(outFile, 'w') as sedHandle:
#with open(sedFile, 'w') as sedHandle:
    sedHandle.write(inputParamString)
    sedHandle.write("Number of lines treated with Voigt profiles: " + str(numGaussLines) + "\n")
    sedHandle.write("Number of wavelength points: " + str(numKept) + "\n")
    sedHandle.write("wave (nm)    log10(flux) (cgs) \n")
    for i in range(numKept):
        flux = log10Flux[i]
        outLine = str(wave[i]) + "   " + str(flux) + "\n"
        sedHandle.write(outLine)

   

 
#
#
# Report 3:       
#synthetic spectrum quantities
#
#

waveSS = [0.0 for i in range(numSpecSyn)]
#for i in range(numSpecSyn):
#    waveSS[i] = cm2nm * specSynLams2[i]
waveSS = [ round(cm2nm * x, 4) for x in specSynLams2 ]
    
print("Number of lines treated with Voigt profiles: ", numGaussLines)

#Print rectified high resolution spectrum of synthesis region
#outFile = outPath + specFile
outFile = outPath + fileStem + ".spec.txt"
#with open(outFile, 'w', encoding='utf-8') as specHandle:
with open(outFile, 'w') as specHandle:
#with open(specFile, 'w') as specHandle:    
    specHandle.write(inputParamString + "\n")
    specHandle.write("Number of lines treated with Voigt profiles: " + str(numGaussLines) + "\n")
    specHandle.write("Number of wavelength points: " + str(numSpecSyn) + "\n")
    specHandle.write("wave (nm)     normalized flux \n")
    for i in range(numSpecSyn):
        outLine = str(waveSS[i]) + "   " + str(round(specSynFlux[0][i], 4)) + "\n"
        specHandle.write(outLine)
#With line ID labels:
    specHandle.write(" ")
    specHandle.write("lambda_0 species\n")
    for i in range(numGaussLines):
        thisLam = cm2nm * list2Lam0[gaussLine_ptr[i]]
        thisLam = round(thisLam, 2)
        thisLbl = list2Element[gaussLine_ptr[i]] + " " + \
        list2StageRoman[gaussLine_ptr[i]] + " " + str(thisLam)
        outLine = str(thisLam) + "   " + thisLbl + "\n"
        specHandle.write(outLine)    


if makePlot == "spectrum":

    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel(r'$F_\lambda/F^C_\lambda$')
    plt.xlim(-6.5, 2.5)
    plt.title = "Synthetic spectrum"
    xMin = min(waveSS)
    xMax = max(waveSS)
    plt.xlim(xMin, xMax)
    plt.ylim(0.0, 2.0)
    plt.plot(waveSS, specSynFlux[0])
    #Add spectral line labels:
    for i in range(numGaussLines):
        thisLam = cm2nm * list2Lam0[gaussLine_ptr[i]]
        thisLam = round(thisLam, 2)
        thisLbl = list2Element[gaussLine_ptr[i]] + " " + \
        list2StageRoman[gaussLine_ptr[i]] + " " + str(thisLam)
        xPoint = [thisLam, thisLam]
        yPoint = [1.05, 1.1]
        plt.plot(xPoint, yPoint, color='black')
        plt.text(thisLam, 1.7, thisLbl, rotation=270)
    


#
#
# Report 4:
#
#
#Print narrow band Gaussian filter quantities: 
#    limb darkening curve (LDC) and discrete fourier cosine transform of LDC

normTuneBandIntens = [ x / tuneBandIntens[0] for x in tuneBandIntens ] 
#outFile = outPath + ldcFile
outFile = outPath + fileStem + ".ldc.txt"
#with open(outFile, 'w', encoding='utf-8') as ldcHandle:
with open(outFile, 'w') as ldcHandle:
#with open(ldcFile, 'w') as ldcHandle:    
    ldcHandle.write(inputParamString)
    ldcHandle.write("Narrow band limb darkening curve (LDC) \n")
    ldcHandle.write("cos(theta)     I(mu)/I(0) \n")
    for i in range(numThetas):
        outLine = str(round(cosTheta[1][i], 4)) + "   " + str(round(normTuneBandIntens[i], 4)) + "\n" 
        ldcHandle.write(outLine)
    
    ldcHandle.write("\n ")    
    ldcHandle.write("Discrete fourier cosine transform of LDC \n")
    ldcHandle.write("k (RAD/RAD)     I(k) \n")
    for i in range(numK):
        outLine = str(round(ft[0][i], 4)) + "   " + str(round(ft[1][i], 4)) + "\n"
        ldcHandle.write(outLine)
        
    ldcHandle.write("\n ")    
    ldcHandle.write("Monochromatic continuum linear limb darkening coefficients (LDCs) \n")
    ldcHandle.write("Wavelength (nm)     LDC \n")
    for i in range(numK):
        outLine = str(wave[i]) + "   " + str(round(ldc[i], 4)) + "\n"
        ldcHandle.write(outLine)
        
#narrow band limb darkening curve (LDC)
if makePlot == "ldc":        

    plt.title = "Narrow band limb darkening"
    plt.xlabel(r'$cos\theta$ (RAD)')
    plt.ylabel(r'$I^{\rm C}_{\rm band}/I^{\rm C}_{\rm band}(0)$')
    plt.xlim(-0.1, 1.1)
    plt.ylim(0, 1.1)
    plt.plot(cosTheta[1], normTuneBandIntens)
    
#discrete fourier cosine transform of LDC
if makePlot == "ft":
    
    plt.title = "Fourier cosine transform of I_lambda(theta)"
    plt.xlabel('Angular frequency (RAD/RAD)')
    plt.ylabel(r'$I^{\rm C}_{\rm band}(\theta)$')
    xMin = 0.9 * min(ft[0])
    xMax = 1.1 * max(ft[0])
    plt.xlim(xMin, xMax)
    yMin = 0.9 * min(ft[1])
    yMax = 1.1 * max(ft[1])
    plt.ylim(yMin, yMax)
    plt.plot(ft[0], ft[1])
    
#
#
# Report 6:
#
#   
#//
#//"""
#Print partial pressures of atomic and molecular species
    #Mostly now from Phil Bennett's GAS apckage
#outFile = outPath + lineFile
#print(" **** Report 6!!!! **** ")
outFile = outPath + fileStem + ".ppress.txt"
#with open(outFile, 'w', encoding='utf-8') as tlaHandle:
with open(outFile, 'w') as ppHandle:    
#with open(tlaFile, 'w') as tlaHandle:
    ppHandle.write(inputParamString + "\n")
    ppHandle.write("Log_10 partial pressures every 10th depth: \n")
    for iD in range(0, numDeps, 4): 
        ppHandle.write("log_10(Tau_Ros) " + str(log10tauRos[iD]) + " T_Kin " + str(log10temp[iD]) +\
                               " (K) log_10(P_Gas) " + str(log10pgas[iD]) +\
                               " (dynes/cm^2) log_10(P_e) " + str(log10pe[iD]) + "\n" )
        for iSpec in range(gsNspec):
            ppHandle.write(gsName[iSpec] + " " + \
                               str(round(log10MasterGsPp[iSpec][iD], 4)) + " ")
        ppHandle.write("\n")
        #print("R6 ", (10.0**log10MasterGsPp[0][iD])/(10.0**log10pgas[iD]))
        
#spectral line of user-defined 2-level atom
if makePlot == "ppress":

    whichSpec = Input.plotSpec
    for thisSpec in range(gsNspec):
        if (gsName[thisSpec].strip() == whichSpec.strip()):
            break;
            
    plt.title = "Log_10 Partial pressure: " + gsName[thisSpec]
    plt.xlabel(r'$\log\tau$')
    plt.ylabel(r'$\log P$ (dynes cm$^{-2}$')
    xMin = logE * min(tauRos[1])
    xMax = logE * max(tauRos[1])
    yMin = min(log10MasterGsPp[thisSpec])
    yMax = max(log10MasterGsPp[thisSpec])
    plt.xlim(xMin, xMax)
    plt.ylim(yMin, yMax)
    plt.plot(log10tauRos, log10MasterGsPp[thisSpec])
    #print(log10tauRos)
    #print(log10MasterGsPp[thisSpec])     

#print(" ")       
#print(" ************** ")
#print(" ")
#print("STOP!!!!")
#print(" ")
#print(" ************** ")
#print(" ")                       
#// *****************************
#// 
#//
#//
#// User-defined two-level atom and line profile section:
#//
#//
#//
#//

#    // Set up grid of line lambda points sampling entire profile (cm):
numCore = 5 #//half-core
numWing = 10 #//per wing 
numPoints = 2 * (numCore + numWing) - 1 #// + 1;  //Extra wavelength point at end for monochromatic continuum tau scale
#//linePoints: Row 0 in cm (will need to be in nm for Plack.planck), Row 1 in Doppler widths
species = "Ca"  #Anything but Hydrogen - doesn't matter for now - ??
linePoints = LineGrid.lineGridVoigt(userLam0, userMass, xiT, numDeps, teff, numCore, numWing, species) #//cm

#// Get Einstein coefficient for spontaneous de-excitation from f_ij to compute natural 
#// (radiation) roadening:  Assumes ration of statisitcal weight, g_j/g_i is unity
#logAij = math.log(6.67e13) + math.log(10.0)*userLogF - 2.0*math.log(cm2nm*userLam0)
log10Aij = math.log10(6.67e13) + userLogF - 2.0*math.log10(cm2nm*userLam0)
#////
#//Compute area-normalized depth-independent line profile "phi_lambda(lambda)"
if (ifVoigt == True):
    lineProf = LineProf.voigt2(linePoints, userLam0, log10Aij, userLogGammaCol,
                numDeps, teff, tauRos, temp, pGas, tempSun, pGasSun)
else: 
    lineProf = LineProf.voigt(linePoints, userLam0, log10Aij, userLogGammaCol, \
                      numDeps, teff, tauRos, temp, pGas, tempSun, pGasSun, hjertComp, dbgHandle)
    

#//
#// Level population now computed in LevelPops.levelPops()

#//
#// This holds 2-element temperature-dependent base 10 logarithmic parition fn:

#for k in range(len(thisUwV)):
#    thisUwV[k] = 0.0 #//default initialization
thisUwV = [ 0.0 for i in range(numAtmPrtTmps) ]        

logNums = [ [ 0.0 for i in range(numDeps) ] for j in range(numStages+2) ]

thisLogN = [0.0 for i in range(numDeps)] 
#for i in range(numDeps):
#    thisLogN[i] = logE10*(userA12 - 12.0) + logNH[i]
thisLogN = [ logE10*(userA12 - 12.0) + x for x in logNH ]
   
#//load arrays for stagePops2():
#//Default is to set both temperature-dependent values to to the user-input value:
    
chiIArr[0] = userChiI1
chiIArr[1] = userChiI2
chiIArr[2] = userChiI3
chiIArr[3] = userChiI4
log10UwAArr[0][0] = math.log10(userGw1)
log10UwAArr[0][1] = math.log10(userGw1)
log10UwAArr[1][0] = math.log10(userGw2)
log10UwAArr[1][1] = math.log10(userGw2)
log10UwAArr[2][0] = math.log10(userGw3)
log10UwAArr[2][1] = math.log10(userGw3)
log10UwAArr[3][0] = math.log10(userGw4)
log10UwAArr[3][1] = math.log10(userGw4)

#//One phantom molecule:
fakeNumMols = 1
fakeLogNumB = [ [ 0.0 for i in range(numDeps) ] for j in range(1) ]

#for i in range(numDeps):
#    fakeLogNumB[0][i] = -49.0
fakeLogNumB[0] = [ -49.0 for i in range(numDeps) ] 
    
fakeDissEArr = [ 0.0 for i in range(1) ]
fakeDissEArr[0] = 29.0 #//eV
fakeLog10UwBArr = [ [ 0.0 for i in range(numAtmPrtTmps) ] for j in range(1) ]
#for kk in range(len(fakeLog10UwBArr)):
#    fakeLog10UwBArr[0][kk] = 0.0
fakeLogQwABArr = [ [ 0.0 for i in range(numMolPrtTmps) ] for j in range(fakeNumMols) ]

#for im in range(fakeNumMols):
#    for kk in range(numMolPrtTmps):
#        fakeLogQwABArr[im][kk] = math.log(300.0)
fakeLogQwABArr = [ [ log300 for kk in range(numMolPrtTmps) ] for im in range(fakeNumMols) ]

fakeLogMuABArr = [0.0 for i in range(1)]
fakeLogMuABArr[0] = math.log(2.0) + Useful.logAmu() #//g 
logN = LevelPopsGasServer.stagePops2(thisLogN, newNe, chiIArr, log10UwAArr,   \
                fakeNumMols, fakeLogNumB, fakeDissEArr, fakeLog10UwBArr, fakeLogQwABArr, fakeLogMuABArr, \
                numDeps, temp)

#for iTau in range(numDeps):
#    logNums[0][iTau] = logN[0][iTau]
#    logNums[1][iTau] = logN[1][iTau]
#    logNums[4][iTau] = logN[2][iTau]
#    logNums[5][iTau] = logN[3][iTau]
#    logNums[6][iTau] = logN[4][iTau]
    #//logNums[6][iTau] = logN[4][iTau];
logNums[0] = [ x for x in logN[0] ]
logNums[1] = [ x for x in logN[1] ]
logNums[4] = [ x for x in logN[2] ]
logNums[5] = [ x for x in logN[3] ]
logNums[6] = [ x for x in logN[4] ]  

stage_ptr = 0 #//default initialization is neutral stage
if (userStage == 0):
    stage_ptr = 0
    
if (userStage == 1):
    stage_ptr = 1
    
if (userStage == 2):
    stage_ptr = 4
    
if (userStage == 3):
    stage_ptr = 5
    
numHelp = LevelPopsGasServer.levelPops(userLam0, logN[stage_ptr], userChiL, thisUwV, \
                    userGwL, numDeps, temp);
          
#for iTau in range(numDeps):
#    logNums[2][iTau] = numHelp[iTau]
    #//Log of line-center wavelength in cm
logNums[2] = [ x for x in numHelp ] 
    
logLam0 = math.log(userLam0)
#// energy of b-b transition
logTransE = Useful.logH() + Useful.logC() - logLam0 - Useful.logEv() #// last term converts back to cgs units
#// Energy of upper E-level of b-b transition
chiU = userChiL + math.exp(logTransE)
numHelp = LevelPopsGasServer.levelPops(userLam0, logN[stage_ptr], chiU, thisUwV, userGwL, \
         numDeps, temp)
#for iTau in range(numDeps):
#    logNums[3][iTau] = numHelp[iTau] #//upper E-level - not used - fake for testing with gS3 line treatment
logNums[3] = [ x for x in numHelp ] #//upper E-level - not used - fake for testing with gS3 line treatment   
#//
#//Compute depth-dependent logarithmic monochromatic extinction co-efficient, kappa_lambda(lambda, tauRos):

lineLambdas = [0.0 for i in range(numPoints)]   
#for il in range(numPoints):
#    lineLambdas[il] = linePoints[0][il] + userLam0
lineLambdas = [ x + userLam0 for x in linePoints[0] ]
            
logKappaL = LineKappa.lineKap(userLam0, logNums[2], userLogF, linePoints, lineProf, \
                       numDeps, zScale, tauRos, temp, rho, logFudgeTune)

logTotKappa = LineKappa.lineTotalKap(lineLambdas, logKappaL, numDeps, logKappa, \
             numLams, lambdaScale)
#//
#//Compute monochromatic optical depth scale, Tau_lambda throughout line profile
#//CAUTION: Returns numPoints+1 x numDeps array: the numPoints+1st row holds the line centre continuum tau scale
logTauL = LineTau2.tauLambda(numPoints, lineLambdas, logTotKappa, \
               numDeps, kappa500, tauRos, logTotalFudge)

#//Evaluate formal solution of rad trans eq at each lambda throughout line profile
#// Initial set to put lambda and tau arrays into form that formalsoln expects

lineIntens = [ [ 0.0 for i in range(numThetas) ] for j in range(numPoints) ]

lineIntensLam = [0.0 for i in range(numThetas)]

lineFlux = [ [ 0.0 for i in range(numPoints) ] for j in range(2) ]
lineFluxLam = [0.0 for i in range(2)]

if (ifScatt == True):
    lineMode = True
else:
    lineMode = False
    
for il in range(numPoints):

    #for id in range(numDeps):
    #    thisTau[1][id] = logTauL[il][id]
    #    thisTau[0][id] = math.exp(logTauL[il][id])
        #//console.log("il " + il + " id " + id + " logTauL[il][id] " + logE*logTauL[il][id]);
    thisTau[1] = [ x for x in logTauL[il] ]
    thisTau[0] = [ math.exp(x) for x in logTauL[il] ]    

    lineIntensLam = FormalSoln.formalSoln(numDeps, \
                cosTheta, lineLambdas[il], thisTau, temp, lineMode)
    #//lineFluxLam = flux2(lineIntensLam, cosTheta);
    #for it in range(numThetas):
    #    lineIntens[il][it] = lineIntensLam[it]
    lineIntens[il] = [ x for x in lineIntensLam ]
        #//console.log("il " + il + " it " + it + "lineIntensLam[it] " + lineIntensLam[it]);
    #} //it loop - thetas
#} //il loop
lineFlux = Flux.flux3(lineIntens, lineLambdas, cosTheta, phi, cgsRadius, omegaSini, macroVkm)

#//Continuum rectify line spectrum:
#//
#contFlux2 = ToolBox.interpolV(contFlux[0], lambdaScale, lineLambdas)
contFlux2 = numpy.interp(lineLambdas, lambdaScale, contFlux[0])

lineFlux2 = [ [ 0.0 for i in range(numPoints) ] for j in range(2) ]
#for i in range(numPoints):
#    lineFlux2[0][i] = lineFlux[0][i] / contFlux2[i]
#    lineFlux2[1][i] = math.log(lineFlux2[0][i])
lineFlux2[0] = [ lineFlux[0][i] / contFlux2[i] for i in range(numPoints) ]
lineFlux2[1] = [ math.log(x) for x in lineFlux2[0] ]
   

#//Get equivalent width, W_lambda, in pm - picometers:
#//Wlambda = eqWidth(lineFlux2, linePoints, lam0); //, fluxCont);

WlambdaLine = PostProcess.eqWidthSynth(lineFlux2, lineLambdas) 

#
#
# Report 5:
#
#   
#//
#//"""
#Print rectified high resolution spectrum of synthesis region
lineWave = [0.0 for i in range(numPoints)]
#outFile = outPath + lineFile
outFile = outPath + fileStem + ".tla.txt"
#with open(outFile, 'w', encoding='utf-8') as tlaHandle:
with open(outFile, 'w') as tlaHandle:    
#with open(tlaFile, 'w') as tlaHandle:
    tlaHandle.write(inputParamString + "\n")
    tlaHandle.write("User-defined two-level atom and line: Equivalent width: " + str(WlambdaLine) + " pm \n")
    tlaHandle.write("wave (nm)   normalized flux \n")
    for i in range(numPoints):
        lineWave[i] = cm2nm*lineLambdas[i]
        outLine = str(round(lineWave[i], 4)) + "   " + str(round(lineFlux2[0][i], 4)) + "\n"
        tlaHandle.write(outLine)
    tlaHandle.write("\n")
    tlaHandle.write("log_10 energy level populations (cm^-3) \n")
    tlaHandle.write("tauRos    n_l    n_I    n_II    N_III   N_IV")
    for i in range(numDeps):
        nI = round(log10e * logNums[0][i], 4)
        nII = round(log10e * logNums[1][i], 4)
        nl = round(log10e * logNums[2][i], 4)
        nIII = round(log10e * logNums[4][i], 4)
        nIV = round(log10e * logNums[5][i], 4)
        outLine = str(log10tauRos[i]) + "   " + str(nl) + "   " + str(nI) + "   " + str(nII) + "   " + str(nIII) + "   " + str(nIV) + "\n" 
        tlaHandle.write(outLine)


#spectral line of user-defined 2-level atom
if makePlot == "tlaLine":

    plt.title = "Fourier cosine transform of I_lambda(theta)"
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel(r'$F_\lambda/F^{\rm C}_\lambda$')
    xMin = min(lineWave)
    xMax = max(lineWave)
    plt.xlim(xMin, xMax)
    plt.ylim(0, 1.2)
    plt.plot(lineWave, lineFlux2[0])
    

     
dbgHandle.close()
        
        
    
