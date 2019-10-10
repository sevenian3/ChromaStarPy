# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:54:21 2017

@author: ishort

Compare arbitrary phoenix spectra to CSGPy spectra 
- mainly to "astrophyscially tune" molecular band oscillator strenths

"""

#plotting:
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
import pylab

#From: https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/
def sort_list(list1, list2): 
  
    zipped_pairs = zip(list2, list1) 
  
    z = [x for _, x in sorted(zipped_pairs)] 
      
    return z 

#General file for printing ad hoc quantities
#dbgHandle = open("debug.out", 'w')

#Get the data
dataPath = "PHX/"
#outPath = absPath + "Outputs/"

numStr = ""
num = 0.0
wav = 0.0
wavStr = ""
flxStr = ""
inLine = ""
fields = [" " for i in range(2)] 

#with open("", 'r', encoding='utf-8') as inputHandle:
inFile = dataPath + "ltePy-3750-2.0-0.0.sph.ames.spec.7"
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
        wav = 0.1 * float(wavStr)  # A to nm
        wave.append(wav)
        flx = 10.0**float(flxStr)
        flx = 1.0e8 * flx  # erg/s/cm^2/cm to ergs/s/cm^2/nm
        flx = 1.5e-22 * flx # crude normalization
        flux.append(flx)
        
print("wave ", [wave[x] for x in range(10)])
print("flux ", [flux[x] for x in range(10)])
#; Parallel version produces unsorted wavelengths!!    ;MPI
flux2 = sort_list(flux, wave) #This *first!!*
wave.sort()
      
pylab.plot(wave, flux2, color='black')

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
teffStr = "4300.0"
loggStr = "2.0"
logZStr = "-0.7"     
massStarStr = "0.75"
xiTStr = "2.0"
logHeFeStr = "0.0"
logCOStr = "0.0" 
logAlphaFeStr = "0.3"
#Spectrum synthesis
lambdaStartStr = "390.0"  
lambdaStopStr = "400.0"
lineThreshStr = "-3.0" 
voigtThreshStr = "-3.0" 
logGammaColStr = "0.5"
logKapFudgeStr = "0.0"
macroVStr = "1.0"
rotVStr = "1.0"
rotIStr = "90.0"
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
runVers = "RunGas"
teff = 3750.0
logg = 2.0
log10ZScale = 0.0 
#TiO alpha system
#lambdaStart = 515.0  
#lambdaStop = 519.0
#TiO beta system
#lambdaStart = 560.0  
#lambdaStop = 564.0 
#TiO gamma system
#lambdaStart = 715.0  
#lambdaStop = 719.0 
#TiO gamma prime system
#lambdaStart = 617.0  
#lambdaStop = 621.0 
#TiO epsilon system
#lambdaStart = 839.0  
#lambdaStop = 843.0 
#TiO delta system
#lambdaStart = 882.0  
#lambdaStop = 892.0 
#TiO phi system
#lambdaStart = 1100.0  
#lambdaStop = 1110.0 

#CH A2Delta_X2Pi ("G-band" at 4314 A)
lambdaStart = 430.5  
lambdaStop = 431.5 

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
    
    
#plot the spectrum        
#plt.title('Synthetic spectrum')
plt.ylabel('$F_\lambda/F^C_\lambda$')
plt.xlabel('$\lambda$ (nm)')
xMin = min(waveMod)
xMax = max(waveMod)
pylab.xlim(xMin, xMax)
print(xMin, xMax)
#pylab.xlim(708, xMax)
pylab.ylim(0.0, 1.6)        
pylab.plot(waveMod, fluxMod, color="gray")

#add the line IDs
for i in range(numLineIds):
    if "Ca II" in lblIds[i]:
        thisLam = waveIds[i]
        thisLbl = lblIds[i]
        xPoint = [thisLam, thisLam]
        yPoint = [1.05, 1.1]
        pylab.plot(xPoint, yPoint, color='black')
        pylab.text(thisLam, 1.5, thisLbl, rotation=270)

#Save as encapsulated postscript (eps) for LaTex
epsName = fileStem + '.eps'
plt.savefig(epsName, format='eps', dpi=1000)
