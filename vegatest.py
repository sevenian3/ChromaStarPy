# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:54:21 2017

@author: ishort
"""

#plotting:
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
import pylab

from astropy.io import fits
import numpy

import Gauss2

#General file for printing ad hoc quantities
#dbgHandle = open("debug.out", 'w')

#Get the data
dataPath = "VegaAtlas/"
#outPath = absPath + "Outputs/"





#If reading FITS file (from STELIB) 
#http://www.ast.obs-mip.fr/users/leborgne/stelib/fits_files.html
#A&A 402, 433–442 (2003) J.-F. Le Borgne1, G. Bruzual2, R. Pell´o1, A. Lanc¸on3, B. Rocca-Volmerange4 , B. Sanahuja5, D. Schaerer1,
#C. Soubiran6, and R. V´ılchez-G´omez

wav = 0.0

inFile = dataPath + "HD172167_V3.2.fits"
hdulist = fits.open(inFile)

#Get the coefficients for the wavelength array
naxis1 = hdulist[0].header['NAXIS1']
crval1 = hdulist[0].header['CRVAL1']
cdelt = hdulist[0].header['CDELT1']
vhelio = hdulist[0].header['VHELIO']
vlsr = hdulist[0].header['VLSR']
radvel = hdulist[0].header['RADVEL']

flux = hdulist[0].data
#Continuum rectification - here a divisor:
cy0 = 1.3e-8

wave = [0.0 for i in range(naxis1)]
for i in range(naxis1):
    ii = float(i)
    wav = crval1 + cdelt*ii
    wave[i] = 0.1 * wav
    flux[i] = flux[i] / cy0


""" If reading ascii data
#with open("", 'r', encoding='utf-8') as inputHandle:
       
numStr = ""
num = 0.0
wav = 0.0
flx = 0.0
wavStr = ""
flxStr = ""
inLine = ""
fields = [" " for i in range(2)] 

inFile = dataPath + "vega.dat"

#Continuum rectification - here a factor:
cy0 = 0.65
with open(inFile, 'r') as inputHandle:    
    
    #No header - we'll figure out number of records on fly
    wave = []
    flux = []
      
    #for i in range(num):
    inLine = inputHandle.readline()
    while (inLine != ""):
        inLine = inputHandle.readline()
        #print(inLine)
        if not inLine:
            break    
        inLine = inputHandle.readline()  
        fields = inLine.split()
        wavStr = fields[0].strip(); flxStr = fields[1].strip()
        wav = 0.1 * float(wavStr)
        wave.append(wav)
        flx = cy0 * float(flxStr)
        flux.append(flx)
"""        
        
pylab.plot(wave, flux, color='black')

#Now get the synthetic spectrum pre-computed with ChromaStarPy
modelPath = "Outputs/"
#outPath = absPath + "Outputs/"

numStr = ""
num = 0.0
wavStr = ""
flxStr = ""
inLine = "   "
#fields = [" " for i in range(2)] 

"""
runVers = "pyLoop"
#Model atmosphere
teffStr = "9550.0"
loggStr = "3.95"
logZStr = "-0.5"     
massStarStr = "2.0"
xiTStr = "2.0"
logHeFeStr = "0.0"
logCOStr = "0.0" 
logAlphaFeStr = "0.0"
#Spectrum synthesis
lambdaStartStr = "429.0"  
lambdaStopStr = "439.0"
lineThreshStr = "-3.0" 
voigtThreshStr = "-3.0" 
logGammaColStr = "0.0"
logKapFudgeStr = "0.0"
macroVStr = "2.0"
#rotVStr = "275.0"
#rotIStr = "5.0"
rotVStr = "20.0"
rotIStr = "0.0"
RVStr = "0.0"

strucStem = "Teff" + teffStr + "Logg" + loggStr + "Z" + logZStr + "M" + massStarStr+"xiT"+xiTStr + \
"HeFe" + logHeFeStr + "CO" + logCOStr + "AlfFe" + logAlphaFeStr + "v" + runVers
strucFile = "struc." + strucStem + ".out"
specFile = "spec." + strucStem + "L"+lambdaStartStr+"-"+lambdaStopStr+"xiT"+xiTStr+"LThr"+lineThreshStr+ \
"GamCol"+logGammaColStr+"Mac"+macroVStr+"Rot"+rotVStr+"-"+rotIStr+"RV"+RVStr + ".out"
#with open("", 'r', encoding='utf-8') as inputHandle:
inFile = modelPath + specFile; 
"""

project = "Project"
runVers = "Run"
teff = 9550.0
logg = 3.95
log10ZScale = -0.5 
lambdaStart = 429.0  
lambdaStop = 439.0 
fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers    
inFile = modelPath + fileStem + ".spec.txt"

invnAir = 1.0 / 1.000277 #// reciprocal of refractive index of air at STP 

#numStr = fields[0].strip()   #first field is number of following records
#num = int(numStr)
waveMod = []
fluxMod = []
wav = 0.0 #//initialization
wavStr = ""
lblStr = ""

with open(inFile, 'r') as inputHandle:    
    
    #Expects number of records on first lines, then white space delimited columns of
    #wavelengths in nm and continuum rectified fluxes
    inLine = inputHandle.readline()   #line of header
    print(inLine)
    inLine = inputHandle.readline()
    print(inLine)
    fields = inLine.split()
    #number of line IDs is last field:
    numLineIdsStr = fields[len(fields)-1]
    numLineIds = int(numLineIdsStr) - 1  # to be on safe side
    print("Recovered that there are " +  numLineIdsStr + " lines to ID")
    inLine = inputHandle.readline()
    print(inLine)
    fields = inLine.split()
    #number of wavelengths in spectrum is last field:
    numWavsStr = fields[len(fields)-1]
    numWavs = int(numWavsStr)  # to be on safe side
    print("Recovered that there are " +  numWavsStr + " wavelengths")
    #One more line of header
    inLine = inputHandle.readline()   #line of header
    print(inLine)    
    
    waveMod = [0.0 for i in range(numWavs)]
    fluxMod = [0.0 for i in range(numWavs)]
    
    #Get the synthetic spectrum
    for i in range(numWavs):
        inLine = inputHandle.readline()
        fields = inLine.split()
        wavStr = fields[0].strip(); flxStr = fields[1].strip()
        wav = invnAir * float(wavStr)
        waveMod[i] = wav
        fluxMod[i] = float(flxStr)
        
    waveIds = [0.0 for i in range(numLineIds)]
    lblIds = ["" for i in range(numLineIds)]
    
    #Get the line IDs
    #Expects four white-space-delimited fields:
    # wavelength, element, ion. stage, and rounded wavelength
    #Another line of header for line id section
    inLine = inputHandle.readline()   #line of header
    print(inLine)  
    
    for i in range(numLineIds):
        inLine = inputHandle.readline()
        fields = inLine.split()
        wavStr = fields[0].strip()
        wav = invnAir * float(wavStr)
        waveIds[i] = wav
        lblStr = fields[1].strip() + " " + fields[2].strip() + " " + fields[3].strip()
        lblIds[i] = lblStr
        
    
    """
    #If we do NOT know number of records:  
    #for i in inputHandle: #doesn't work - 0 iterations
    while (inLine != ""):
        inLine = inputHandle.readline()
        if not inLine:
            break
        #print(inLine)
        fields = inLine.split()
        wavStr = fields[0].strip(); flxStr = fields[1].strip()
        wav = invnAir * float(wavStr)
        waveMod.append(wav)
        fluxMod.append(float(flxStr))
    """
    

#Interpolate syntehtic spectrum onto uniform wavelength grid and convolve with
#instrumental profile accounting for finite spectral resolving power, R
delLam = 0.01 #sampling in nm

numWavs2 = (waveMod[numWavs-1] - waveMod[0]) / delLam
numWavs2 = int(numWavs2)
wave2 = [0.0 for i in range(numWavs2)]
for i in range(numWavs2):
    ii = float(i)
    wave2[i] = waveMod[0] + ii*delLam
    
#necessary?? flux2 = [0.0 for i in range(numWavs2)]

#interpolate the flux onto the new wavelength scale
flux2 = numpy.interp(wave2, waveMod, fluxMod)

specR = 2000   #approximate STELIB value
midWave = (waveMod[numWavs-1] + waveMod[0]) / 2.0
deltaR = midWave / specR  #resolution element in nm
sigma = deltaR /delLam #resolution element in array elements
fwhm = 2.0 * sigma
#length of array holding Gaussian in array element space if computing Gaussian from -3.5 to +3.5 sigma
length = int(7.0 * sigma) 

#Make a Gaussian instrumental profile
gaussian = Gauss2.gauss2(fwhm, length)

#Convolve the uniformly sampled synthetic spectrum with the instrumental profile
flux2s = numpy.convolve(flux2, gaussian, mode='same')


#plot the spectrum        
#plt.title('Synthetic spectrum')
plt.ylabel('$F_\lambda/F^C_\lambda$')
plt.xlabel('$\lambda$ (nm)')
xMin = min(waveMod)
xMax = max(waveMod)
pylab.xlim(xMin, xMax)
pylab.ylim(0.0, 1.2)        
#pylab.plot(waveMod, fluxMod, color="gray")
pylab.plot(wave2, flux2, color=(0.6, 0.6, 0.6))
pylab.plot(wave2, flux2s, color=(0.3, 0.3, 0.3))

#add the line IDs
foundOne = False # work around H I line components being multiply labeled in line list
for i in range(numLineIds):
    if "H I" in lblIds[i] and foundOne == False:
        foundOne = True
        thisLam = waveIds[i]
        thisLbl = lblIds[i]
        xPoint = [thisLam, thisLam]
        yPoint = [0.75, 0.8]
        pylab.plot(xPoint, yPoint, color='black')
        pylab.text(thisLam, 1.1, thisLbl, rotation=270)

#Save as encapsulated postscript (eps) for LaTex
epsName = fileStem + ".eps"
plt.savefig(epsName, format='eps', dpi=1000)