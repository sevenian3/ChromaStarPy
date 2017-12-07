#
#
#Custom filename tags to distinguish from other runs
project = "Project"
runVers = "Run"

#Default plot
#Select ONE only:

#makePlot = "structure"
#makePlot = "sed"
makePlot = "spectrum"
#makePlot = "ldc"
#makePlot = "ft"
#makePlot = "tlaLine" 

#Spectrum synthesis mode
# - uses model in Restart.py with minimal structure calculation
specSynMode = False

#Griffin, R. E. M., Lynas-Gray, A. E., 1999, \aj, 117, 2998
#Decin, L., Vandenbussche, B., Waelkens, C., Decin, G., Eriksson, K., Gustafsson, B., Plez, B., Sauval, A. J., 2003a, \aap, 400, 709

#Model atmosphere
teff = 4300.0  #,    K
logg = 2.0 #,      cgs
log10ZScale = -0.7     # [A/H]
massStar = 0.75 #,      solar masses
xiT = 2.0  #,       km/s
logHeFe = 0.0  #,   [He/Fe]
logCO = 0.0  #,   [C/O]
logAlphaFe = 0.0   #,   [alpha-elements/Fe]


#Spectrum synthesis
lambdaStart = 390.0  #,       nm    
lambdaStop = 400.0  #,     nm

fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers  
 
lineThresh = -3.0  #,    min log(KapLine/kapCnt) for inclusion at all - areally, being used as "lineVoigt" for now
voigtThresh = -3.0  #,     min log(KapLine/kapCnt) for treatment as Voigt - currently not used - all lines get Voigt
logGammaCol = 0.5
logKapFudge = 0.0
macroV = 1.0  #,     km/s
rotV = 1.0  #,   km/s
rotI = 90.0 #,    degrees
RV = 0.0 #,   km/s
vacAir = "vacuum"    
sampling = "fine"

#Performance vs realism
nOuterIter = 12   #,     no of outer Pgas(HSE) - EOS - kappa iterations
nInnerIter = 12   #,    no of inner (ion fraction) - Pe iterations
ifTiO = 1   #,     where to include TiO JOLA bands in synthesis 

#Gaussian filter for limb darkening curve, fourier transform
diskLambda = 500.0  #,      nm
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
