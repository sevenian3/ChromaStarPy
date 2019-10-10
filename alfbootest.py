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

#General file for printing ad hoc quantities
#dbgHandle = open("debug.out", 'w')

#Get the data
dataPath = "AlfBooAtlas/"
#outPath = absPath + "Outputs/"

numStr = ""
num = 0.0
wav = 0.0
wavStr = ""
flxStr = ""
inLine = ""
fields = [" " for i in range(2)] 

#with open("", 'r', encoding='utf-8') as inputHandle:
inFile = dataPath + "ar3900"
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
        flux.append(float(flxStr))
        
        
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
runVers = "Run"
teff = 4300.0
logg = 2.0
log10ZScale = -0.7 
lambdaStart = 390.0  
lambdaStop = 400.0 
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