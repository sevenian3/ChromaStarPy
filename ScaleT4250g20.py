# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:39:41 2017

/**
 * Initializes and re-scales a Phoenix LTE spherical reference model of 
 * Teff=4250K, log(g)=2.0, [Fe/H]=0.0, xi=1.0 km/s, l=1.0H_p, M=1M_Sun, R=6.4761e+10cm
 *
 * @author Ian
 */


@author: ishort
"""

import math
import ToolBox
import Useful

def phxRefTeff():
    return 4250.0

def phxRefLogEg(): 
    return math.log(10.0) * 2.0  #//base e!

#//He abundance from  Grevesse Asplund et al 2010
def phxRefLogAHe(): 
    return math.log(10.0) * (10.93 - 12.0)  #//base e "A_12" logarithmic abundance scale!

def getphxRefTau64():
    
#//Corresponding Tau_12000 grid (ie. lambda_0 = 1200 nm):    
    phxRefTau64 = [
 0.00000000000000000e+00, 9.99999999999999955e-07, 1.34596032415536424e-06,
 1.81160919420041334e-06, 2.43835409826882661e-06, 3.28192787251147086e-06,
 4.41734470314007309e-06, 5.94557070854439435e-06, 8.00250227816105150e-06,
 1.07710505603676914e-05, 1.44974067037263169e-05, 1.95129342263596216e-05,
 2.62636352765333530e-05, 3.53498110503010939e-05, 4.75794431400941383e-05,
 6.40400427119728238e-05, 8.61953566475303262e-05, 1.16015530173997159e-04,
 1.56152300600049659e-04, 2.10174801133248699e-04, 2.82886943462596935e-04,
 3.80754602122237182e-04, 5.12480587696093125e-04, 6.89778537938765847e-04,
 9.28414544519474451e-04, 1.24960914129198684e-03, 1.68192432488086874e-03,
 2.26380340952144670e-03, 3.04698957090350801e-03, 4.10112707055130046e-03,
 5.51995432128156785e-03, 7.42963950759494875e-03, 1.00000000000000002e-02,
 1.34596032415536422e-02, 1.81160919420041318e-02, 2.43835409826882663e-02,
 3.28192787251147047e-02, 4.41734470314006436e-02, 5.94557070854439401e-02,
 8.00250227816105275e-02, 1.07710505603676912e-01, 1.44974067037263149e-01,
 1.95129342263596212e-01, 2.62636352765332981e-01, 3.53498110503010221e-01,
 4.75794431400941464e-01, 6.40400427119728333e-01, 8.61953566475303190e-01,
 1.16015530173997150e+00, 1.56152300600049654e+00, 2.10174801133248712e+00,
 2.82886943462596641e+00, 3.80754602122236818e+00, 5.12480587696092638e+00,
 6.89778537938765801e+00, 9.28414544519474383e+00, 1.24960914129198670e+01,
 1.68192432488086894e+01, 2.26380340952144650e+01, 3.04698957090350540e+01,
 4.10112707055129562e+01, 5.51995432128157333e+01, 7.42963950759495049e+01,
 1.00000000000000000e+02]

    
    return phxRefTau64


def getLogPhxRefTau64():

    logE = math.log10(math.e)

    phxRefTau64 = getphxRefTau64()
    numPhxDep = len(phxRefTau64)
    logPhxRefTau64 = [0.0 for i in range(numPhxDep)]    
    #for i in range(1, numPhxDep):
    #    logPhxRefTau64[i] = math.log(phxRefTau64[i])
    logPhxRefTau64[1: numPhxDep] = [ math.log(phxRefTau64[i]) for i in range(1, numPhxDep) ]
    #print("*********")
    #print(logPhxRefTau64)
    #print("*********")
    #stop    
    logPhxRefTau64[0] = logPhxRefTau64[1] - (logPhxRefTau64[numPhxDep - 1] - logPhxRefTau64[1]) / numPhxDep
    return logPhxRefTau64
    
def phxRefTemp(teff, numDeps, tauRos):

    logE = math.log10(math.e)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefTemp64 = [
 2.55177189467776134e+03, 2.55177189467776134e+03, 2.57792125655286191e+03,
 2.60758002435901381e+03, 2.64012742898025908e+03, 2.67432875475946230e+03,
 2.70893891273552163e+03, 2.74308870598832664e+03, 2.77632383320681129e+03,
 2.80848811483166946e+03, 2.83959882227651724e+03, 2.86975658734314266e+03,
 2.89908813206188461e+03, 2.92771359779851400e+03, 2.95573102630948051e+03,
 2.98321198037901013e+03, 3.01020749755630777e+03, 3.03675606855582828e+03,
 3.06288810300240721e+03, 3.08862982043339889e+03, 3.11400422160098924e+03,
 3.13903037085205142e+03, 3.16372090154785838e+03, 3.18810905092703479e+03,
 3.21223709737028685e+03, 3.23616013487906321e+03, 3.25997011697764810e+03,
 3.28379847029234497e+03, 3.30779792957306154e+03, 3.33215641253420881e+03,
 3.35718199939999613e+03, 3.38317056293436599e+03, 3.41035215459581877e+03,
 3.43904544965103469e+03, 3.46977882782005645e+03, 3.50316432370656776e+03,
 3.53952093749718961e+03, 3.57938756282554868e+03, 3.62358876591721355e+03,
 3.67390373594475159e+03, 3.73057002905895024e+03, 3.79526239264127798e+03,
 3.87014190881368677e+03, 3.96034605960104500e+03, 4.06785077337546363e+03,
 4.19530126018311603e+03, 4.35807101922509446e+03, 4.53128152603078979e+03,
 4.75647877892966608e+03, 4.99815140831592271e+03, 5.29640554819846147e+03,
 5.60111278999269234e+03, 6.01099379170666271e+03, 6.36043009619938857e+03,
 6.87521615935859882e+03, 7.26044412747461593e+03, 7.50448146936407466e+03,
 7.68547260686038317e+03, 7.83660366095023619e+03, 7.97031461253075395e+03,
 8.09288613904806061e+03, 8.20796577074222841e+03, 8.31800144917403668e+03,
 8.42235419676150195e+03]


    logPhxRefTau64 = getLogPhxRefTau64();
    #// interpolate onto gS3 tauRos grid and re-scale with Teff:
        
    phxRefTemp = [0.0 for i in range(numDeps)]
    scaleTemp = [ [0.0 for i in range(numDeps)] for j in range(2)]
    #for i in range(numDeps):
    #    phxRefTemp[i] = ToolBox.interpol(logPhxRefTau64, phxRefTemp64, tauRos[1][i])
    #    scaleTemp[0][i] = teff * phxRefTemp[i] / phxRefTeff()
    #    scaleTemp[1][i] = math.log(scaleTemp[0][i]);
    phxRefTemp = [ ToolBox.interpol(logPhxRefTau64, phxRefTemp64, x) for x in tauRos[1] ]
    scaleTemp[0] = [ teff * x / phxRefTeff() for x in phxRefTemp ]
    scaleTemp[1] = [ math.log(x) for x in scaleTemp[0] ]
        #//System.out.println("tauRos[1][i] " + logE * tauRos[1][i] + " scaleTemp[1][i] " + logE * scaleTemp[1][i]);
    #print("*********")
    #print(phxRefTemp)
    #print("*********")
    #print(scaleTemp[0])
    #stop        

    return scaleTemp

def phxRefPGas(grav, zScale, logAHe, numDeps, tauRos):

    #//System.out.println("ScaleT4250g20.phxRefPGas called");

    logE = math.log10(math.e)
    logEg = math.log(grav) #//base e!
    AHe = math.exp(logAHe)
    refAHe = math.exp(phxRefLogAHe())
    logZScale = math.log(zScale)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefPGas64 = [
 1.00000000000000005e-04, 4.30797022881529035e+00, 5.23633209862413107e+00,
 6.35110679837766412e+00, 7.68415255320091806e+00, 9.26944725328996455e+00,
 1.11437944000671951e+01, 1.33486175933519231e+01, 1.59320732110696728e+01,
 1.89510405786159843e+01, 2.24729535630686001e+01, 2.65776121702747155e+01,
 3.13591521574494898e+01, 3.69283427891380711e+01, 4.34153596323810476e+01,
 5.09731596421035889e+01, 5.97815115471393099e+01, 7.00515965533140843e+01,
 8.20320988196306047e+01, 9.60157114466986172e+01, 1.12346894715709283e+02,
 1.31431137235228107e+02, 1.53746059612369663e+02, 1.79853925611152988e+02,
 2.10416068512255976e+02, 2.46209759085281831e+02, 2.88146638387011080e+02,
 3.37292455489998588e+02, 3.94889455574428723e+02, 4.62381218232488322e+02,
 5.41431239027500510e+02, 6.33944346680425951e+02, 7.42101436711750239e+02,
 8.68388258638872003e+02, 1.01559408923251908e+03, 1.18679360231291594e+03,
 1.38539626183849145e+03, 1.61516883770226173e+03, 1.88020120421177171e+03,
 2.18463232976707104e+03, 2.53293658371589027e+03, 2.93000255565556563e+03,
 3.38117288723951515e+03, 3.89194415900473678e+03, 4.46986439959823201e+03,
 5.12776215162745939e+03, 5.88482548647403291e+03, 6.77685699601984379e+03,
 7.85508152689431518e+03, 9.16793034379196797e+03, 1.06499829584269464e+04,
 1.20573723930509423e+04, 1.31104385587741126e+04, 1.38632723386838443e+04,
 1.43359336214159030e+04, 1.46332769212074945e+04, 1.48729928730357842e+04,
 1.50999078995603995e+04, 1.53309455833121519e+04, 1.55753421735992888e+04,
 1.58400487938745937e+04, 1.61313349003330495e+04, 1.64553234176194455e+04,
 1.68190844909027946e+04]

    numPhxDeps = len(phxRefPGas64) #//yeah, I know, 64, but that could change!
    logPhxRefPGas64 = [0.0 for i in range(numPhxDeps)]
    #for i in range(numPhxDeps):
    #    logPhxRefPGas64[i] = math.log(phxRefPGas64[i])
    logPhxRefPGas64 = [ math.log(x) for x in phxRefPGas64 ]
            
    logPhxRefTau64 = getLogPhxRefTau64();

    #// interpolate onto gS3 tauRos grid and re-scale with grav, metallicity and He abundance
    #// From Gray 3rd Ed. Ch.9, esp p. 189, 196:
    phxRefPGas = [0.0 for i in range(numDeps)]
    logPhxRefPGas = [0.0 for i in range(numDeps)]
    scalePGas = [ [0.0 for i in range(numDeps)] for j in range(2) ]
#//exponents in scaling with g:
    gexpTop = 0.54 #//top of model
    gexpBottom = 0.64 #//bottom of model
    gexpRange = (gexpBottom - gexpTop)
    tauLogRange =  tauRos[1][numDeps-1] -  tauRos[1][0] 
    #double thisGexp;
#// factor for scaling with A_He:
    logHeDenom = 0.666667 * math.log(1.0 + 4.0*refAHe)
    logPhxRefPGas = [ ToolBox.interpol(logPhxRefTau64, logPhxRefPGas64, x) for x in tauRos[1] ]
    for i in range(numDeps):
    #    #//if (i%10 == 0){
    #    #//System.out.println("i " + i);
    #    #//}
    #    logPhxRefPGas[i] = ToolBox.interpol(logPhxRefTau64, logPhxRefPGas64, tauRos[1][i])
    #    #//if (i%10 == 0){
    #    #//System.out.println("After tau interpolation: pGas " + logE*logPhxRefPGas[i]);
    #    #//}
        thisGexp = gexpTop + gexpRange * (tauRos[1][i] - tauRos[1][0]) / tauLogRange
    #    #//scaling with g 
    #    #//if (i%10 == 0){
    #   #//System.out.println("thisGexp " + thisGexp);
    #    #//}
        scalePGas[1][i] = thisGexp*logEg + logPhxRefPGas[i] - thisGexp*phxRefLogEg()
    #    #//if (i%10 == 0){
    #    #//System.out.println("After scaling with g: pGas " + logE*scalePGas[1][i]);
    #    #//}
    #    #//scaling with zscl:
    #    #//if (i%10 == 0){
    #    #//System.out.println("logZScale " + logZScale);
    #    #//}
    #    scalePGas[1][i] = -0.333333*logZScale + scalePGas[1][i]
    #    #//if (i%10 == 0){
    #    #//System.out.println("After scaling with z: pGas " + logE*scalePGas[1][i]);
    #    #//}
    #    #//scaling with A_He:
    #    #//if (i%10 == 0){
    #    #//System.out.println("Math.log(1.0 + 4.0*AHe) - logHeDenom " + (0.666667*Math.log(1.0 + 4.0*AHe) - logHeDenom));
    #    #//}
    #    scalePGas[1][i] = 0.666667 * math.log(1.0 + 4.0*AHe) + scalePGas[1][i] - logHeDenom
    #    #//if (i%10 == 0){
    #    #//System.out.println("After scaling with AHe: pGas " + logE*scalePGas[1][i]);
    #   #//}
    #    scalePGas[0][i] = math.exp(scalePGas[1][i])
    #    #//if (i%10 == 0){
    #    #//System.out.println("logPhxRefPGas " + logE*logPhxRefPGas[i] + " scalePGas[1][i] " + logE * scalePGas[1][i]);
    #    #//}        

    #logPhxRefPGas = [ ToolBox.interpol(logPhxRefTau64, logPhxRefPGas64, x) for x in tauRos[1] ]
    #No! scalePGas[1] = [ logEg*(gexpTop + gexpRange * (tauRos[1][i] - tauRos[1][0]) / tauLogRange)\
    #No!         + logPhxRefPGas[i] - thisGexp*phxRefLogEg() for i in range(numDeps) ]
    scalePGas[1] = [ -0.333333*logZScale + x for x in scalePGas[1] ]
    scalePGas[1] = [ 0.666667 * math.log(1.0 + 4.0*AHe) + x - logHeDenom for x in scalePGas[1] ]
    scalePGas[0] = [ math.exp(x) for x in scalePGas[1] ]
    #SOMETHING WRONG!!
    #print("*********")
    #print("logPhxRefPGas ", logPhxRefPGas)
    #print("*********")
    #print("scalePGas[1] ", scalePGas[1])
    #print("*********")
    #stop        

    return scalePGas


def phxRefPe(teff, grav, numDeps, tauRos, zScale, logAHe):

    logE = math.log10(math.e)
    logEg = math.log(grav) #//base e!
    AHe = math.exp(logAHe)
    refAHe = math.exp(phxRefLogAHe())
    logZScale = math.log(zScale)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefPe64 = [
 8.82107332460937786e-09, 2.78937385278448721e-05, 3.47576301038577686e-05,
 4.35832572659463317e-05, 5.49376619037973015e-05, 6.94409656870532439e-05,
 8.77707903792445917e-05, 1.10693651821575575e-04, 1.39104108185757799e-04,
 1.74066374927776200e-04, 2.16859921028963076e-04, 2.69028731246404777e-04,
 3.32432061837431244e-04, 4.09296056659801003e-04, 5.02267654306449442e-04,
 6.14473664793957226e-04, 7.49597452349998888e-04, 9.11974871131562793e-04,
 1.10671154087655646e-03, 1.33981929191927902e-03, 1.61837137445693482e-03,
 1.95067571498008536e-03, 2.34645801822358068e-03, 2.81730972458459810e-03,
 3.37701527100230971e-03, 4.04206883240371042e-03, 4.83264944868273382e-03,
 5.77375902899801303e-03, 6.89635454260574543e-03, 8.23939377538898503e-03,
 9.85478499694628605e-03, 1.18084450314643753e-02, 1.41821928408006545e-02,
 1.70844502273588689e-02, 2.06675266544882504e-02, 2.51401461738746321e-02,
 3.07601652353682656e-02, 3.78883555684116358e-02, 4.70434551509077148e-02,
 5.90737609051253110e-02, 7.49278881219457016e-02, 9.61506501246208595e-02,
 1.25001054449255633e-01, 1.65469764331727026e-01, 2.21877141054763416e-01,
 2.99471993844184214e-01, 4.09463450124863737e-01, 5.44807309494293679e-01,
 7.32622090968494066e-01, 1.00147011151172505e+00, 1.61234892801148755e+00,
 3.05928587566573817e+00, 7.65951702544590596e+00, 1.63896549667325182e+01,
 4.47471354140328827e+01, 8.76262151753557248e+01, 1.30080006341931238e+02,
 1.72013432855285373e+02, 2.15462867458483203e+02, 2.61494582627386649e+02,
 3.10959654478989705e+02, 3.64658419590852475e+02, 4.23480004219150715e+02,
 4.87036243289867400e+02]

    logPhxRefTau64 = getLogPhxRefTau64()

    numPhxDeps = len(phxRefPe64) #//yeah, I know, 64, but that could change!
    logPhxRefPe64 = [0.0 for i in range(numPhxDeps)]
    #for i in range(numPhxDeps):
    #    logPhxRefPe64[i] = math.log(phxRefPe64[i])
    logPhxRefPe64 = [ math.log(x) for x in phxRefPe64 ]
        

    #// interpolate onto gS3 tauRos grid and re-scale with Teff:
    phxRefPe = [0.0 for i in range(numDeps)]
    logPhxRefPe = [0.0 for i in range(numDeps)]
    scalePe = [ [0.0 for i in range(numDeps) ] for j in range(2) ]    
#//exponents in scaling with Teff ONLY VALID FOR Teff < 10000K:
    omegaTaum1 = 0.0012 #//log_10(tau) < 0.1
    omegaTaup1 = 0.0015 #//log_10(tau) > 1.0
    omegaRange = (omegaTaup1-omegaTaum1)
    lonOfM1 = math.log(0.1)
#//exponents in scaling with g:
    gexpTop = 0.48 #//top of model
    gexpBottom = 0.33 #//bottom of model
    gexpRange = (gexpBottom - gexpTop)
    tauLogRange =  tauRos[1][numDeps-1] -  tauRos[1][0] 
    #double thisGexp
    thisOmega = omegaTaum1 #//default initialization
#// factor for scaling with A_He:
    logHeDenom = 0.333333 * math.log(1.0 + 4.0*refAHe)
    
    logPhxRefPe = [ ToolBox.interpol(logPhxRefTau64, logPhxRefPe64, x) for x in tauRos[1] ]
    for i in range(numDeps):
        #//if (i%10 == 0){
        #//System.out.println("i " + i);
        #//}
        #logPhxRefPe[i] = ToolBox.interpol(logPhxRefTau64, logPhxRefPe64, tauRos[1][i])
        thisGexp = gexpTop + gexpRange * (tauRos[1][i] - tauRos[1][0]) / tauLogRange
        if (tauRos[0][i] < 0.1):
            thisOmega =  omegaTaum1
            
        if (tauRos[0][i] > 10.0):
            thisOmega =  omegaTaup1
            
        if ( (tauRos[0][i] >= 0.1) and (tauRos[0][i] <= 10.0) ):
            thisOmega = omegaTaum1 + omegaRange * (tauRos[1][i] - lonOfM1) / tauLogRange
            
        #//if (i%10 == 0){
        #//System.out.println("thisGexp " + thisGexp + " thisOmega " + thisOmega);
        #//}
        #//scaling with g 
        scalePe[1][i] = thisGexp*logEg + logPhxRefPe[i] - thisGexp*phxRefLogEg()
        #//if (i%10 == 0){
        #//System.out.println("After g scaling: pe " + logE*scalePe[1][i]);
        #//}
        #//scale with Teff:
        scalePe[1][i] = thisOmega*teff + scalePe[1][i] - thisOmega*phxRefTeff()
        #//if (i%10 == 0){
        #//System.out.println("After Teff scaling: pe " + logE*scalePe[1][i]);
        #//}
        #//scaling with zscl:
        #scalePe[1][i] = 0.333333*logZScale + scalePe[1][i]
        #//if (i%10 == 0){
        #//System.out.println("After z scaling: pe " + logE*scalePe[1][i]);
        #//}
        #//scaling with A_He:
        #scalePe[1][i] = 0.333333 * math.log(1.0 + 4.0*AHe) + scalePe[1][i] - logHeDenom
        #//if (i%10 == 0){
        #//System.out.println(" logPhxRefPe " + logE*logPhxRefPe[i] + " After A_He scaling: pe " + logE*scalePe[1][i]);
        #//}
        #scalePe[0][i] = math.exp(scalePe[1][i]);

    scalePe[1] = [ 0.333333*logZScale + x for x in scalePe[1] ]
    scalePe[1] = [ 0.333333 * math.log(1.0 + 4.0*AHe) + x - logHeDenom for x in scalePe[1] ]
    scalePe[0] = [ math.exp(x) for x in scalePe[1] ]
    #print("*********")
    #print("logPhxRefPe ", logPhxRefPe)
    #print("*********")
    #print("scalePe[1] ", scalePe[1])
    #print("*********")
    #print("scalePe[0] ", scalePe[0])
    #print("*********")
    #stop        
    return scalePe

def phxRefNe(numDeps, scaleTemp, scalePe):

    logE = math.log10(math.e)

    scaleNe = [ [0.0 for i in range(numDeps) ] for j in range(2) ]

    #for i in range(numDeps):
    #    scaleNe[1][i] = scalePe[1][i] - scaleTemp[1][i] - Useful.logK()
    #    scaleNe[0][i] = math.exp(scaleNe[1][i])
    scaleNe[1] = [ scalePe[1][i] - scaleTemp[1][i] - Useful.logK() for i in range(numDeps) ]
    scaleNe[0] = [ math.exp(x) for x in scaleNe[1] ]    
    #print("*********")
    #print("scaleNe[1] ", scaleNe[1])
    #print("*********")
    #print("scaleNe[0] ", scaleNe[0])
    #print("*********")
    #stop        
    return scaleNe
