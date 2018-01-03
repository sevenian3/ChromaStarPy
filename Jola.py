# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:10:08 2017

@author: ishort
"""

#/**
# * Collection of methods for computing molecular band opacity in the
# * Just-overlapping-line approximation (JOLA)
# * Just-overlapping line approximation treats molecular ro-vibrational bands as pseudo-continuum
# * opacity sources by "smearing" out the individual rotational fine-structure lines
# *See 1982A&A...113..173Z, Zeidler & Koestler, 1982
# */

import math
import Useful

def jolaGrid(jolaLambda, jolaNumPoints):

    #//Try linear wavelength sampling of JOLA band for now...
    
    jolaPoints = [0.0 for i in range(jolaNumPoints)]

    iLambD = 0.0
    deltaLamb = (jolaLambda[1] - jolaLambda[0]) / jolaNumPoints

    for iL in range(jolaNumPoints):
        iLambD = float(iL)
        jolaPoints[iL] = jolaLambda[0] + iLambD*deltaLamb #//nm
        #//System.out.println("iL: " + iL + " jolaPoints " + jolaPoints[iL]);
      
  
    return jolaPoints #//nm

#} //end method jolaGrid



def jolaProfilePR(omega0, logf, vibConst,
                  jolaPoints, alphP, alphR, numDeps, temp):

    """//
//JOLA profile for P (Delta J = 1) and R (Delta J = -1) branches
//Equation 19 from Zeidler & Koestler"""

    nm2cm = 1.0e-7
    log10E = math.log10(math.e)

    numPoints = len(jolaPoints)
    #// derivative of rotational-line oscillator strength with respect to frequency
    dfBydw = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    fvv = math.exp(logf)

    logHcBbyK = Useful.logH() + Useful.logC() + math.log(vibConst[0]) \
                                - Useful.logK()

    #//System.out.println("omega0 " + omega0 + " logf " + log10E*logf + " vibConst " + vibConst[0] + " " + vibConst[1] + " alphP " + alphP + " alphR " + alphR);

    Bsum = vibConst[1] + vibConst[0] 
    Bdiff = vibConst[1] - vibConst[0]

#//value of J-related "m" at band-head:
    mH = -1.0 * Bsum / (2.0*Bdiff) #//Eq. 14
    #//Frequency (or wavenumber??) at band head:
    wH = ( -1.0 * Bdiff * mH*mH ) + omega0 #//Eq. 15  
    #//System.out.println("1.0/wH " + 1.0/wH + " 1.0/omega0 " + 1.0/omega0);

    mTheta1 = 1.0 #//R branch?
    mTheta2 = 1.0 #//P branch?

    #double m1, m2; // related to J, for R & P branches, respectively
    alpha1 = 1.0
    alpha2 = 1.0

    #//value of m is closely related to rotational quantum number J,
    #//Near band origin, frequency, w, range should correspond to -1 <= m <= 1 - ???:
    #//double wMin = Useful.c / (1.0e-7*jolaPoints[numPoints-1]); //first frequency omega
    #//double wMax = Useful.c / (1.0e-7*jolaPoints[0]); //last frequency omega
    #//double deltaW = 0.02;
    #double w, logW, m1Fctr, m2Fctr, mHelp, wMinuswHOverBDiff;
    #double denom1, denom2, m1Term, m2Term; 
    #double help1, logHcBbyKt, hcBbyKt;
 
    #//Outer loop over frequency omega 
    #// for (int iW = -1; iW <= 1; iW++){
    #for (int iW = numPoints-1; iW >= 0; iW--){
    for iW in range(numPoints-1, 0, -1):
        #//dW = (double) iW; 
        #//w = wMin + (dW*deltaW); 
        #//logW = Useful.logC() - Math.log(1.0e-7*jolaPoints[iW]); //if w is freq in Hz
        logW = 0.0 - math.log(nm2cm*jolaPoints[iW]) #//if w is waveno in cm^-1 
        w = math.exp(logW)
        #//System.out.println("logW " + log10E*logW);
        #//I have no idea if this is right...
        wMinuswHOverBDiff = (w - wH) / Bdiff 
        mHelp = math.sqrt(abs(wMinuswHOverBDiff))  #//Eq. 17
        m1 = mH + mHelp
        m2 = mH - mHelp #//Eq. 18
        #//System.out.println("mH " + mH + " m1 " + m1 + " m2 " + m2);
        m1Fctr = (m1*m1 - m1) 
        m2Fctr = (m2*m2 - m2)
        #//The following association between the sign of m1 or m2 and whether 
        #//it's the P or the R branch might be backwards:
        if (m1 < 0):
            alpha1 = alphP
             
        if (m1 >= 0):
            alpha1 = alphR
             
        if (m2 < 0):
            alpha2 = alphP
             
        if (m2 >= 0):
            alpha2 = alphR
             
             
        denom1 = abs(Bsum + 2.0*m1*Bdiff) 
        denom2 = abs(Bsum + 2.0*m2*Bdiff)

        for iD in range(numDeps):

            if (wMinuswHOverBDiff > 0):
 
                logHcBbyKt = logHcBbyK - temp[1][iD] 
                hcBbyKt = math.exp(logHcBbyKt)

                help1 = -1.0 * hcBbyKt * m1Fctr
                m1Term = alpha1 * mTheta1 * math.exp(help1) / denom1  
                              
                help1 = -1.0 * hcBbyKt * m2Fctr
                m2Term = alpha2 * mTheta2 * math.exp(help1) / denom2                
            
                #//Can this be used like a differential cross-section (once converted to sigma)?  
                #// System.out.println("fvv " + fvv + " hcBbyKt " + hcBbyKt + " m1Term " + m1Term + " m2Term " + m2Term);
                dfBydw[iW][iD] = fvv * hcBbyKt * ( m1Term + m2Term )  #// Eq. 19     

            else:

                dfBydw[iW][iD] = 0.0

            #}
            #// if (iD%10 == 1){
            #//   System.out.println("PR iD " + iD + " iW " + iW + " dfBydw " + dfBydw[iW][iD]);
            #// }
    
        #} //iD - depth loop 
              
    #} //iW - frequency loop
    
    return dfBydw      

#} //end method jolaProfilePR 
#//

def jolaProfileQ(omega0, logf, vibConst,
                    jolaPoints, alphQ, numDeps, temp):
    
    """//JOLA profile for Q (Delta J = 0) branch
//Equation 24 from Zeidler & Koestler"""

    nm2cm = 1.0e-7
    numPoints = len(jolaPoints)
    #// derivative of rotational-line oscillator strength with respect to frequency
         
    dfBydw = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    fvv = math.exp(logf)
    logHcBbyK = Useful.logH() + Useful.logC() + math.log(vibConst[0]) \
                                - Useful.logK()

    Bsum = vibConst[1] + vibConst[0] 
    Bdiff = vibConst[1] - vibConst[0]

    #double mQ; #// related to J, for R & P branches, respectively

    #//value of m is closely related to rotational quantum number J,
    #//Near band origin, frequency, w, range should correspond to -1 <= m <= 1 - ???:
    #//      double wMin = Useful.c / (1.0e-7*lambda[1]); //first frequency omega
    #//     double wMax = Useful.c / (1.0e-7*lambda[0]); //last frequency omega
    #//    double deltaW = 0.02;
    #double w, logW, mQFctr, mHelp;
    #double denom, mQTerm, wMinusw0OverBDiff; 
    #double help1, logHcBbyKt, hcBbyKt;
 
    #//Outer loop over frequency omega 
    #//for (int iW = -1; iW <= 1; iW++){
    #for (int iW = numPoints-1; iW >= 0; iW--){
    for iW in range(numPoints-1, 0, -1):
        #//dW = (double) iW; 
        #//w = wMin + (dW*deltaW); 
        #//logW = Useful.logC() - Math.log(1.0e-7*jolaPoints[iW]); //if w is freq in Hz
        logW = 0.0 - math.log(nm2cm*jolaPoints[iW]) #//if w is waveno in cm^-1 
        w = math.exp(logW)

        #//I have no idea if this is right...
        wMinusw0OverBDiff = (w - omega0) / Bdiff 
        mHelp = 0.25 + math.abs(wMinusw0OverBDiff)
        mHelp = math.sqrt(mHelp)  #//Eq. 17
        mQ = -0.5 + mHelp
        mQFctr = (mQ*mQ - mQ) 
        denom = math.abs(Bdiff); 

        for iD in range(numDeps):

            if (wMinusw0OverBDiff > 0): 

                logHcBbyKt = logHcBbyK - temp[1][iD] 
                hcBbyKt = math.exp(logHcBbyKt)

                help1 = -1.0 * hcBbyKt * mQFctr
                mQTerm = math.exp(help1) / denom  
                              
            
                #//Can this be used like a differential cross-section (once converted to sigma)?  
                #//System.out.println("alphQ " + alphQ + " fvv " + " logHcBbyKt " + logHcBbyKt + " mQTerm " + mQTerm);
                dfBydw[iW][iD] = alphQ * fvv * hcBbyKt * mQTerm  #// Eq. 24      
            
            else:
              
                dfBydw[iW][iD] = 0.0;
         
               

            #//if (iD%10 == 1){
            #//System.out.println("Q iD " + iD + " iW " + iW + " dfBydw " + dfBydw[iW][iD]);
            #//}
 
        #//iD - depth loop 
             
    #} //iW - frequency loop
          
    return dfBydw      
         

#} //end method jolaProfileQ 
#  //

def jolaKap(jolaLogNums, dfBydw, jolaPoints,
                    numDeps, temp, rho):

    log10E = math.log10(math.e)
    nm2cm = 1.0e-7

    numPoints = len(jolaPoints)
 
    logKappaJola = [ [ 0.0 for i in range(numDeps) ] for j in range(numPoints) ]
    #//Initialize this carefully:

    for iD in range(numDeps):
        for iW in range(numPoints):
            logKappaJola[iW][iD] = -999.0
       
     

    #double stimEmExp, stimEmLogExp, stimEmLogExpHelp, stimEm;
    #double freq, lastFreq, w, lastW, deltaW, thisDeltaF;
    logSigma = -999.0    
    logFreq = Useful.logC() - math.log(nm2cm * jolaPoints[0])
    logW = 0.0 - math.log(nm2cm * jolaPoints[0]) #//if w is waveno in cm^-1
    #//lastFreq = Math.exp(logFreq) 
    lastW = math.exp(logW) 

    #//try accumulating oscillator strenth, f, across band - assumes f = 0 at first (largest) lambda- ??
    thisF = 0.0

    #//If f is cumulative in wavenumber, then we have to make the wavenumber loop the inner one even if it
    #//means re-calculating depth-independent quantities each time:
    for iD in range(numDeps):

        thisF = 0.0 #//re-set accumulator

        #//loop in order of *increasing* wavenumber
        #for (int iW = numPoints-1; iW >=1; iW--){
        for iW in range(numPoints-1, 1, -1):

            #//df/dv is a differential oscillator strength in *frequency* space:
            logFreq = Useful.logC() - math.log(nm2cm*jolaPoints[iW])
            freq = math.exp(logFreq)
            logW = 0.0 - math.log(nm2cm * jolaPoints[iW]) #//if w is waveno in cm^-1
            w = math.exp(logW) #//if w is waveno in cm^-1
            #//System.out.println("w " + w);
            #//deltaW = Math.abs(freq - lastFreq);
            deltaW = abs(w - lastW)

            #//For LTE stimulated emission correction:
            stimEmLogExpHelp = Useful.logH() + logFreq - Useful.logK();

#//        for (int iD = 0; iD < numDeps; iD++){

            thisDeltaF = deltaW * dfBydw[iW][iD]
            if (thisDeltaF > 0.0):
                thisF += thisDeltaF #//cumulative version
                #//thisF = thisDeltaF; //non-cumulative version
                logSigma = math.log(thisF) + math.log(math.pi) + 2.0*Useful.logEe() - Useful.logMe() - Useful.logC()
            else:
                logSigma = -999.0
          

            #// LTE stimulated emission correction:
            stimEmLogExp = stimEmLogExpHelp - temp[1][iD]
            stimEmExp = -1.0 * math.exp(stimEmLogExp)
            stimEm = ( 1.0 - math.exp(stimEmExp) )

            #//extinction coefficient in cm^2 g^-1:
            logKappaJola[iW][iD] = logSigma + jolaLogNums[iD] - rho[1][iD] + math.log(stimEm) 
            #//logKappaJola[iW][iD] = -999.0; 
            #//if (iD%10 == 1){
            #//System.out.println("iD " + iD + " iW " + iW + " logFreq " + log10E*logFreq + " logW " + log10E*logW + " logStimEm " + log10E*Math.log(stimEm));
            #//System.out.println("iD " + iD + " iW " + iW + " thisDeltaF " + thisDeltaF + " logSigma " + log10E*logSigma + " jolaLogNums " + log10E*jolaLogNums[iD] + " rho " + log10E*rho[1][iD] + " logKappaJola " + log10E*logKappaJola[iW][iD]);
#//} 

#//        } //iD loop - depths

            lastFreq = freq;
        #} //iW loop - wavelength

    #} //iD loop - depths

    return logKappaJola

#} //end method jolaKap
