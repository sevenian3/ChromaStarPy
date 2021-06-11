#
#
#Custom filename tags to distinguish from other runs
project = "SunEarth"
runVers = "Test"

#Project specific notes:
# Test case:  
# Star:  Sun 
# Spectrum:  Na I D region
# Lightcurve: Earth, in plane of ecliptic


#Default plot
#Select ONE only if plotting 'inline' - 

makePlotStruc = True
makePlotSED = True
makePlotSpec = True
makePlotLDC = True
makePlotFT = True
makePlotTLA = True
makePlotTrans = True

makePlotPPress = False
#Chemical species for partial rpessure plot:
plotSpec = "H"

#Spectrum synthesis mode
# - uses model in Restart.py with minimal structure calculation
specSynMode = True

if (specSynMode):
    runVers += "SS"

#Model atmosphere
teff = 5777.0  #,    K
logg = 4.44 #,      cgs
log10ZScale = -0.0     # [A/H]
massStar = 1.00 #,      solar masses
xiT = 1.0  #,       km/s
logHeFe = 0.0  #,   [He/Fe]
logCO = 0.0  #,   [C/O]
logAlphaFe = 0.0   #,   [alpha-elements/Fe]


#Spectrum synthesis
lambdaStart = 588.5  #,       nm    
lambdaStop = 589.5  #,     nm

fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers  

lineThresh = -3.0  #,    min log(KapLine/kapCnt) for inclusion at all - areally, being used as "lineVoigt" for now
voigtThresh = -3.0  #,     min log(KapLine/kapCnt) for treatment as Voigt - currently not used - all lines get Voigt
logGammaCol = 0.5  #      Logarithmic VdW damping enhancement
logKapFudge = 0.0  #     continuum opacity fudge factor
macroV = 1.0  #,      macroscopic broadening dispersion  km/s
rotV = 2.0  #,      equatorial surface rotational velocity   km/s
rotI = 90.0 #,      inclination of rotational axis AND orbital axis   degrees
RV = 0.0 #,         system radial velocity    km/s
vacAir = "vacuum"   # wavelength scale ('air' OR 'vacuum')      
sampling = "fine"   # density of freq points in spectrum synthesis ('fine' is useful, 'coarse' for quick checking)

#Performance vs realism
nOuterIter = 12   #,     no of outer Pgas(HSE) - EOS - kappa iterations
nInnerIter = 12   #,    no of inner (ion fraction) - Pe iterations
ifMols = 1   #,     whether to include TiO JOLA bands in synthesis 

#Gaussian filter for limb darkening curve (LDC), fourier transform (FT)
diskLambda = 500.0  #,  Band centre wavelength     nm
diskSigma = 0.01  #,   Band dispersion   nm

#Two-level atom and spectral line
#Example: NaI D lambda 5896:
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
rJupiter = 11.21 # Earth radii - handy reference
ifTransit = True   # set to True if we want an exoplanet lightcurve
#Data source:  Wikipedia for now...
rOrbit = 1.00 # AU
rPlanet = 1.00 #Earth radii
#mPlanet = 1.0 #Earth masses #not needed (yet?)
