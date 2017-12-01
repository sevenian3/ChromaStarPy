# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:39:41 2017

/**
 * Initializes and re-scales a Phoenix LTE spherical reference model of 
 * Teff=5000K, log(g)=4.5, [Fe/H]=0.0, xi=1.0 km/s, l=1.0H_p, M=1M_Sun, R=6.4761D+10cm
 *
 * @author Ian
 */


@author: ishort
"""

import math
import ToolBox
import Useful

def phxRefTeff():
    return 5000.0

def phxRefLogEg(): 
    return math.log(10.0) * 4.5  #//base e!

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
        
    logPhxRefTau64[0] = logPhxRefTau64[1] - (logPhxRefTau64[numPhxDep - 1] - logPhxRefTau64[1]) / numPhxDep
    return logPhxRefTau64
    
def phxRefTemp(teff, numDeps, tauRos):

    logE = math.log10(math.e)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefTemp64 = [
    3.15213572679982190e+03, 3.15213572679982190e+03, 3.17988621810632685e+03,
    3.21012887128011243e+03, 3.24126626267038500e+03, 3.27276078893546673e+03,
    3.30435725697820226e+03, 3.33589185632140106e+03, 3.36724151725549154e+03,
    3.39831714195318273e+03, 3.42906935013664861e+03, 3.45949368388945595e+03,
    3.48962758169505923e+03, 3.51953742647688796e+03, 3.54929791042697934e+03,
    3.57896962155466872e+03, 3.60858205550851335e+03, 3.63812646699481775e+03,
    3.66755983657917068e+03, 3.69681905522719444e+03, 3.72583932497757132e+03,
    3.75457006928661031e+03, 3.78298372918123914e+03, 3.81109104721021231e+03,
    3.83893072914395862e+03, 3.86656355962043835e+03, 3.89408059675027425e+03,
    3.92160316230741546e+03, 3.94927225929978204e+03, 3.97726284805320847e+03,
    4.00584847611869327e+03, 4.03531360317989993e+03, 4.06591896438200047e+03,
    4.09802860937899732e+03, 4.13221207874272022e+03, 4.16915227717330799e+03,
    4.20937593060261861e+03, 4.25369220113429128e+03, 4.30330739566306784e+03,
    4.36035870964639616e+03, 4.42601579216115442e+03, 4.50281614584142153e+03,
    4.59386420090837146e+03, 4.70448179136501403e+03, 4.83727710376560208e+03,
    4.99516189027659129e+03, 5.19102132587796405e+03, 5.40505223548941285e+03,
    5.67247302987449984e+03, 5.95695843497286933e+03, 6.27957483223234703e+03,
    6.71365960956718118e+03, 7.06828382342861460e+03, 7.34157936910693206e+03,
    7.56939938735570740e+03, 7.77138428264261165e+03, 7.95656000812699585e+03,
    8.13006721530056711e+03, 8.29523535580475982e+03, 8.45429779465689171e+03,
    8.60879260449185131e+03, 8.75981713693203528e+03, 8.90838141718757288e+03,
    9.05361290415211806e+03]

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
        

    return scaleTemp

def phxRefPGas(grav, zScale, logAHe, numDeps, tauRos):

    #//System.out.println("ScaleT5000.phxRefPGas called");

    logE = math.log10(math.e)
    logEg = math.log(grav) #//base e!
    AHe = math.exp(logAHe)
    refAHe = math.exp(phxRefLogAHe())
    logZScale = math.log(zScale)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefPGas64 = [
    1.00000000000000005e-04, 1.03770217591881035e+02, 1.24242770084417913e+02,
    1.47686628640383276e+02, 1.74578854906314291e+02, 2.05506972274478784e+02,
    2.41168221287605292e+02, 2.82385081738383917e+02, 3.30127686150304896e+02,
    3.85540773715381306e+02, 4.49974446823229414e+02, 5.25018679681323647e+02,
    6.12542265074691159e+02, 7.14737800095933608e+02, 8.34175243666085407e+02,
    9.73867213356324669e+02, 1.13734973870022168e+03, 1.32878148706864113e+03,
    1.55306409432270971e+03, 1.81598529465124716e+03, 2.12438618583220841e+03,
    2.48635477283421324e+03, 2.91145034581766595e+03, 3.41095942605562823e+03,
    3.99819276314161607e+03, 4.68883438023894087e+03, 5.50134310662684311e+03,
    6.45741052408807354e+03, 7.58249196327514983e+03, 8.90641248566333525e+03,
    1.04639741154490002e+04, 1.22956502717452295e+04, 1.44484787849992390e+04,
    1.69769301182948657e+04, 1.99435621814443475e+04, 2.34195796692420117e+04,
    2.74860930366683497e+04, 3.22351125605895031e+04, 3.77699103578024442e+04,
    4.42033085085744533e+04, 5.16616495136288213e+04, 6.02879692077906366e+04,
    7.02475218656768702e+04, 8.17365047611011832e+04, 9.50146489805318997e+04,
    1.10441316485543124e+05, 1.28451318144638804e+05, 1.49415613553191157e+05,
    1.72877372164747008e+05, 1.96852852539717947e+05, 2.18808320050485723e+05,
    2.35794833242603316e+05, 2.48716041541587241e+05, 2.59902150512206339e+05,
    2.70560370352023339e+05, 2.81251297069544089e+05, 2.92310802132537181e+05,
    3.03988239352240635e+05, 3.16495216131040419e+05, 3.30029076402488339e+05,
    3.44786943994771456e+05, 3.60975297786138486e+05, 3.78815092131546407e+05,
    3.98560549755298765e+05]

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
        #//if (i%10 == 0){
        #//System.out.println("i " + i);
        #//}
        #logPhxRefPGas[i] = ToolBox.interpol(logPhxRefTau64, logPhxRefPGas64, tauRos[1][i])
        #//if (i%10 == 0){
        #//System.out.println("After tau interpolation: pGas " + logE*logPhxRefPGas[i]);
        #//}
        thisGexp = gexpTop + gexpRange * (tauRos[1][i] - tauRos[1][0]) / tauLogRange
        #//scaling with g 
        #//if (i%10 == 0){
        #//System.out.println("thisGexp " + thisGexp);
        #//}
        scalePGas[1][i] = thisGexp*logEg + logPhxRefPGas[i] - thisGexp*phxRefLogEg()
        #//if (i%10 == 0){
        #//System.out.println("After scaling with g: pGas " + logE*scalePGas[1][i]);
        #//}
        #//scaling with zscl:
        #//if (i%10 == 0){
        #//System.out.println("logZScale " + logZScale);
        #//}
        #scalePGas[1][i] = -0.333333*logZScale + scalePGas[1][i]
        #//if (i%10 == 0){
        #//System.out.println("After scaling with z: pGas " + logE*scalePGas[1][i]);
        #//}
        #//scaling with A_He:
        #//if (i%10 == 0){
        #//System.out.println("Math.log(1.0 + 4.0*AHe) - logHeDenom " + (0.666667*Math.log(1.0 + 4.0*AHe) - logHeDenom));
        #//}
        #scalePGas[1][i] = 0.666667 * math.log(1.0 + 4.0*AHe) + scalePGas[1][i] - logHeDenom
        #//if (i%10 == 0){
        #//System.out.println("After scaling with AHe: pGas " + logE*scalePGas[1][i]);
        #//}
        #scalePGas[0][i] = math.exp(scalePGas[1][i])
        #//if (i%10 == 0){
        #//System.out.println("logPhxRefPGas " + logE*logPhxRefPGas[i] + " scalePGas[1][i] " + logE * scalePGas[1][i]);
        #//}        
    scalePGas[1] = [ -0.333333*logZScale + x for x in scalePGas[1] ]
    scalePGas[1] = [ 0.666667 * math.log(1.0 + 4.0*AHe) + x - logHeDenom for x in scalePGas[1] ]
    scalePGas[0] = [ math.exp(x) for x in scalePGas[1] ]

    return scalePGas

def phxRefPe(teff, grav, numDeps, tauRos, zScale, logAHe):

    logE = math.log10(math.e)
    logEg = math.log(grav) #//base e!
    AHe = math.exp(logAHe)
    refAHe = math.exp(phxRefLogAHe())
    logZScale = math.log(zScale)

    #//Theoretical radiative/convective model from Phoenix V15:
    phxRefPe64 = [
    1.17858427569630401e-08, 1.73073837795169436e-03, 2.13762360059438538e-03,
    2.64586145846806451e-03, 3.26749020460433354e-03, 4.02219945676032288e-03,
    4.93454747856481805e-03, 6.03357965110110344e-03, 7.35319802933484621e-03,
    8.93306098318919460e-03, 1.08200092390451780e-02, 1.30700158082515377e-02,
    1.57505131367194594e-02, 1.89428593874781982e-02, 2.27446519479000651e-02,
    2.72716961646799864e-02, 3.26596927620770305e-02, 3.90659173672675136e-02,
    4.66713907010225318e-02, 5.56843086932707065e-02, 6.63452384304821230e-02,
    7.89341909634427297e-02, 9.37792909747245523e-02, 1.11270186635302790e-01,
    1.31870014183696899e-01, 1.56130489360824298e-01, 1.84715397349025645e-01,
    2.18428766543559472e-01, 2.58245610307223983e-01, 3.05363622257444900e-01,
    3.61311333509324040e-01, 4.27990544717643029e-01, 5.07743853690445168e-01,
    6.03604039632526179e-01, 7.19674246257567152e-01, 8.61422066803848585e-01,
    1.03568172049434559e+00, 1.25187412720684454e+00, 1.52336996895144261e+00,
    1.87078029858400652e+00, 2.31893413667797388e+00, 2.90597658045488094e+00,
    3.68566481623166187e+00, 4.74110273402785865e+00, 6.16546324347510222e+00,
    8.08486709272609971e+00, 1.07959796585076546e+01, 1.46390000057528482e+01,
    2.17273927465764913e+01, 3.56194058574816239e+01, 6.57361652682183575e+01,
    1.48468954779851543e+02, 2.80489497081349555e+02, 4.46587250419467807e+02,
    6.46784311972032128e+02, 8.86744838282462069e+02, 1.17244960918767083e+03,
    1.51089748714632174e+03, 1.91050957850908458e+03, 2.38115682377229541e+03,
    2.93426662234414562e+03, 3.58305801646245618e+03, 4.34379670059742239e+03,
    5.22642525609140284e+03]

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

    return scalePe

def phxRefNe(numDeps, scaleTemp, scalePe):

    logE = math.log10(math.e)

    scaleNe = [ [0.0 for i in range(numDeps) ] for j in range(2) ]

    #for i in range(numDeps):
    #    scaleNe[1][i] = scalePe[1][i] - scaleTemp[1][i] - Useful.logK()
    #    scaleNe[0][i] = math.exp(scaleNe[1][i])
    scaleNe[1] = [ scalePe[1][i] - scaleTemp[1][i] - Useful.logK() for i in range(numDeps) ]
    scaleNe[0] = [ math.exp(x) for x in scaleNe[1] ]        
        

    return scaleNe
