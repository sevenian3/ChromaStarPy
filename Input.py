#
#
#Custom filename tags to distinguish from other runs
project = "Project"
runVers = "Run"

#Default plot
#Select ONE only:

#makePlot = "none"
#makePlot = "structure"
#makePlot = "sed"
#makePlot = "spectrum"
#makePlot = "ldc"
#makePlot = "ft"
#makePlot = "tlaLine"
###The following two plot variables refer to the partial pressure outpue ("Report 6")
makePlot = "ppress"
plotSpec = "H"

#Spectrum synthesis mode
# - uses model in Restart.py with minimal structure calculation
#specSynMode = True
specSynMode = False

#Model atmosphere
teff = 6100.0  #,    K
logg = 4.5 #,      cgs
#teff = 5777.0  #,    K
#logg = 4.44 #,      cgs
log10ZScale = 0.0     # [A/H]
massStar = 1.0 #,      solar masses
xiT = 1.0  #,       km/s
logHeFe = 0.0  #,   [He/Fe]
logCO = 0.0  #,   [C/O]
logAlphaFe = 0.0   #,   [alpha-elements/Fe]


#Spectrum synthesis
#Test
#TiO beta 
#lambdaStart = 560.0  #,       nm    
#lambdaStop = 564.0  #,     nm
#TiO gamma 
#lambdaStart = 708.0  #,       nm    
#lambdaStop = 712.0  #,     nm
#lambdaStart = 715.0  #,       nm    
#lambdaStop = 719.0  #,     nm

#TiO gamma prime
#lambdaStart = 617.0  #,       nm    
#lambdaStop = 621.0  #,     nm
#TiO epsilon
#lambdaStart = 839.0  #,       nm    
#lambdaStop = 843.0  #,     nm
#TiO delta
#lambdaStart = 882.0  #,       nm    
#lambdaStop = 892.0  #,     nm
#TiO phi
#lambdaStart = 1100.0  #,       nm    
#lambdaStop = 1110.0  #,     nm

#CH A2Delta_X2Pi ("G-band" at 4314 A)
lambdaStart = 395.0  #,       nm    
lambdaStop = 400.0  #,     nm


fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers  

lineThresh = -3.0  #,    min log(KapLine/kapCnt) for inclusion at all - areally, being used as "lineVoigt" for now
voigtThresh = -3.0  #,     min log(KapLine/kapCnt) for treatment as Voigt - currently not used - all lines get Voigt
logGammaCol = 0.0
logKapFudge = 0.0
macroV = 1.0  #,     km/s
rotV = 1.0  #,   km/s
rotI = 90.0 #,    degrees
RV = 0.0 #,   km/s
vacAir = "vacuum"    
sampling = "fine"

#Performance vs realism
nOuterIter = 12   #,     no of outer Pgas(HSE) - EOS - kappa iterations
nInnerIter = 12  #,    no of inner (ion fraction) - Pe iterations
ifMols = 1   #,     where to include TiO JOLA bands in synthesis
ifTiO = 0 #Soon to be deprecated 

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
