#
#
#Custom filename tags to distinguish from other runs
project = "Check"
runVers = "Run3"

#Default plot
#Select ONE only:

#makePlot = "structure"
#makePlot = "sed"
#makePlot = "spectrum"
#makePlot = "ldc"
#makePlot = "ft"
#makePlot = "tlaLine" 

#Chemical species for partial rpessure plot:
plotSpec = "TiO"

#Spectrum synthesis mode
# - uses model in Restart.py with minimal structure calculation
#specSynMode = False
specSynMode = True

if (specSynMode):
    runVers += "SS"

#Model atmosphere
teff = 5777.0  #,    K
logg = 4.44 #,      cgs
log10ZScale = 0.0     # [A/H]
massStar = 1.0 #,      solar masses
xiT = 1.0  #,       km/s
logHeFe = 0.0  #,   [He/Fe]
logCO = 0.0  #,   [C/O]
logAlphaFe = 0.0   #,   [alpha-elements/Fe]


#Spectrum synthesis
lambdaStart = 712.0  #,       nm    
lambdaStop = 713.0  #,     nm

fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers  

lineThresh = -3.0  #,    min log(KapLine/kapCnt) for inclusion at all - areally, being used as "lineVoigt" for now
voigtThresh = -3.0  #,     min log(KapLine/kapCnt) for treatment as Voigt - currently not used - all lines get Voigt
logGammaCol = 0.5
logKapFudge = 0.0
macroV = 1.0  #,     km/s
rotV = 2.0  #,   km/s
rotI = 89.7 #,    degrees
RV = 0.0 #,   km/s
vacAir = "vacuum"    
sampling = "fine"

#Performance vs realism
nOuterIter = 20   #,     no of outer Pgas(HSE) - EOS - kappa iterations
nInnerIter = 20  #,    no of inner (ion fraction) - Pe iterations
ifMols = 1   #,     where to include TiO JOLA bands in synthesis 

#Gaussian filter for limb darkening curve, fourier transform
diskLambda = 1000.0  #,      nm
diskSigma = 0.01  #,     nm

#Two-level atom and spectral line
userLam0 = 589.592  #,   nm 
userA12 = 6.24  #,    A_12 logarithmic abundance = log_10(N/H_H) = 12
userLogF = -0.495   #,  log(f) oscillaotr strength // saturated line
userStage = 0  #,   ionization stage of user species (0 (I) - 3 (IV)
userChiI1 = 5.139   #,  ground state chi_I, eV
userChiI2 = 47.29   #,  1st ionized state chi_I, eV
userChiI3 = 71.62   #,  2nd ionized state chi_I, eV
userChiI4 = 98.94   #,  3rd ionized state chi_I, eV
userChiL = 0.0  #,   lower atomic E-level, eV
userGw1 = 2   #,  ground state state. weight or partition fn (stage I) - unitless
userGw2 = 1   #,  ground state state. weight or partition fn (stage II) - unitless
userGw3 = 1   #,   ground state state. weight or partition fn (stage III) - unitless
userGw4 = 1  #,  ground state state. weight or partition fn (stage IV) - unitless
userGwL = 2  #,   lower E-level state. weight - unitless
userMass = 22.9   #,  amu
userLogGammaCol = 1.0   #,  log_10 Lorentzian broadening enhancement factor

#Planetary transit parameters for transit light curve modelling
# ** Also depends on rotI chosen above!!
# Oribital period is not a free parameter - it is set by the 
# size of the orbit and the planet's mass by basic form of 
#Kepler's 3rd law
ifTransit = True
rOrbit = 1.0 # AU
rPlanet = 1.0 #Earth radii
#mPlanet = 1.0 #Earth masses #not needed (yet?)
