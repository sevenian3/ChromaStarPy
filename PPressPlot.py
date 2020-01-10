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

from functools import reduce
import subprocess
import os
import sys

#General file for printing ad hoc quantities
#dbgHandle = open("debug.out", 'w')

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


#Now get the synthetic spectrum pre-computed with ChromaStarPy
modelPath = absPath + "Outputs/"
#outPath = absPath + "Outputs/"


project = "Project"
runVers = "RunGas"
teff = 3600.0
logg = 1.0
log10ZScale = 0.0 
lambdaStart = 695.0  
lambdaStop = 700.0 
fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers    
inFile = modelPath + fileStem + ".ppress.txt"


#whichSpec = "Ca+"
whichSpec = ["C", "N", "O", "Na", "Mg", "Si", "S", "K", "Ca", "Fe"]
colrSpec = ["black", "brown", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "gray"]
whichIon = ["H-", "Na+", "Mg+", "Si+", "S+", "K+", "Ca+", "Fe+"]
colrIon = ["black", "orange", "yellow", "green", "blue", "indigo", "violet", "gray"]
thisSpec = 0 #default initialization (H)

numSampleDepths = 48 
#numSampleDepths = 2  #debug
numSpecies = 105
#numSpecies = 3 #debug

#numStr = fields[0].strip()   #first field is number of following records
#num = int(numStr)
species = [0.0 for i in range(numSpecies)]
logTau = [0.0 for i in range(numSampleDepths)]
logTkin = [0.0 for i in range(numSampleDepths)]
logPGas = [0.0 for i in range(numSampleDepths)]
logPe = [0.0 for i in range(numSampleDepths)]
logPP = [ [ 0.0 for j in range(numSpecies) ] for i in range(numSampleDepths)]


fileTeff = 0.0
fileLogg = 0.0
fileLogZ = 0.0


with open(inFile, 'r') as inputHandle:    
    
    #Expects number of records on first lines, then white space delimited columns of
    #wavelengths in nm and continuum rectified fluxes
    inLine = inputHandle.readline()   #line of header
    print(inLine)
    fields = inLine.split()
    fileTeff = float(fields[1].strip())
    fileLogg = float(fields[3].strip())
    fileZ = float(fields[5].strip())
    if ( (fileTeff != teff) or
         (fileLogg != logg) or
         (fileLogZ != log10ZScale) ):
        print(" ")
        print("  !!!!!!!!!!!!!!!!!!!!!!")
        print(" ")
        print("Mismatch between input file name and stellar paramters in input file!")
        print(" ")
        print("  !!!!!!!!!!!!!!!!!!!!!!")
        print(" ")            

#Header line    
    inLine = inputHandle.readline()
    print(inLine)
    
    
    #Get the synthetic spectrum
    for i in range(numSampleDepths):
        #Begin reading data - each depthwise record is two lines:
        #line 1 has depth and environmental paramters
        #line 2 has specieswise partial pressures
        inLine1 = inputHandle.readline()
        #print(inLine1)
        fields = inLine1.split()
        logTau[i] = float(fields[1].strip())
        logTkin[i] = float(fields[3].strip())
        logPGas[i] = float(fields[6].strip())
        logPe[i] = float(fields[9].strip())  
        #Relative to total gas pressure for plot:
        logPe[i] = logPe[i] - logPGas[i]
        
        inLine2 = inputHandle.readline()
        #print(inLine2)
        fields = inLine2.split()
        for j in range(numSpecies):
            species[j] = fields[2*j].strip()
            #if (species[j] == whichSpec):
            #    thisSpec = j
            logPP[i][j] = float(fields[(2*j) + 1].strip())
            #Relative to total gas pressure for plot:
            logPP[i][j] = logPP[i][j] - logPGas[i]
            #print("j ", j, " 2*j ", 2*j, " 2*j+1 ", (2*j)+1, " species ", species[j], " pp ", logPP[i][j])
        
    
#plot some partial pressures     
#plt.title('Synthetic spectrum')
plt.figure()
plt.subplot(1, 1, 1)                
#plt.ylabel(r'$\log P$ dynes cm$^{\rm -2}$')
plt.ylabel(r'$\log_{10} (P/P_{\rm H})$', fontsize=14)
plt.xlabel(r'$\log_{10}\tau_{\rm Ros}$', fontsize=14)            
xMin = min(logTau)
xMax = max(logTau)
pylab.xlim(xMin, xMax)
pylab.ylim(-10.0, -1.0)            
#thisSpec = 3
colr = 0

for wS in whichSpec:
          
    for i in range(numSpecies):
        if (species[i] == wS):
            thisSpec = i
    print("Species: ", species[thisSpec])

    #print("At plot:")
    #print ("logPP ", [logPP[i][0] for i in range(numSampleDepths)]) 
    # skip first depth point [i=0] - upper boundary condition:     
    pylab.plot( [logTau[i] for i in range(1, numSampleDepths)],\
               [logPP[i][thisSpec] for i in range(1, numSampleDepths)],\
               color=colrSpec[colr], linewidth=2 )
    pylab.text(logTau[4], logPP[4][thisSpec], species[thisSpec],\
               color=colrSpec[colr], fontsize=13, weight='bold')
    colr+=1
    
# skip first depth point [i=0] - upper boundary condition:
pylab.plot( [logTau[i] for i in range(1, numSampleDepths)],\
           [logPe[i] for i in range(1, numSampleDepths)],\
               'o', color='black')
pylab.text(logTau[numSampleDepths-8], logPe[numSampleDepths-8], 'e-',\
           color='black', fontsize=13, weight='bold')

colr = 0    
for wI in whichIon:
          
    for i in range(numSpecies):
        if (species[i] == wI):
            thisSpec = i
    print("Species: ", species[thisSpec])

    # skip first depth point [i=0] - upper boundary condition:
    pylab.plot( [logTau[i] for i in range(1, numSampleDepths)],\
               [logPP[i][thisSpec] for i in range(1, numSampleDepths)],\
               '--', color=colrIon[colr], linewidth=2)
    pylab.text(logTau[numSampleDepths-4], logPP[numSampleDepths-4][thisSpec],\
               species[thisSpec], color=colrIon[colr], fontsize=13, weight='bold')
    colr+=1

#Save as encapsulated postscript (eps) for LaTex
epsName = fileStem + ".eps"
plt.savefig(epsName, format='eps', dpi=1000)