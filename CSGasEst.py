# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:25:12 2019

@author: Philip D. Bennett
Port from FORTRAN to Python: Ian Short
"""

import math
import numpy
#from scipy.linalg.blas import daxpy
#from scipy.linalg.blas import ddot
#from scipy.linalg.blas import dscal
#from scipy.linalg.blas import idamax

#import Documents.ChromaStarPy.GAS.BlockData
#from Documents.ChromaStarPy.GAS.GsRead import gsread
import CSBlockData
#import GsRead
import CSGsRead2


def ten(xdum):
    x = 2.302585093e0*xdum
    x2 = math.exp(x)
    return x2

def isign(a, b):
    
    #default:
    c = a
    
    if ( (numpy.sign(b) == -1) and (numpy.sign(a) == 1) ):
        c = -1 * a
            
    if ( (numpy.sign(b) == 1) and (numpy.sign(a) == -1) ):
        c = -1 * a
        
    if ( (numpy.sign(b) == 0) and (numpy.sign(a) == -1) ):
        c = -1 * a    
        
    return c
            

#def gasest(isolv, temp, pt, peIn):
def gasest(isolv, temp, pt):
    
    """
    #c
    #c cis: Inputs: isolv, temp, pt, pe
    #c cis: Ouput: p, neq  ??
    #
    #c
    #c GASEST: Returns an estimate of the fractional abundances of
    #c each chemical species for a given T, P, and composition.
    #c ISOLV=1: Calculate initial estimates only for species with
    #c          IPR=1, ie. major species. 
    #c      =2: Calculate initial estimates for species with IPR=1
    #c          or 2, ie. major and minor constituents.
    #c Initial estimates are not calculated for IPR=3 species since
    #c these are never needed. 
    #c
    """
    #Try this:
    #global pi, sbcon, kbol, cvel, gcon, hpl, hmass, t0, everg # /consts/
    global kbol, hmass, t0 # /consts/
    global name, ip, comp, awt, nspec, natom, itab, ntab, indx, iprint, gsinit, print0 #/gasp/
    global ipr, nch, nel, ntot, nat, zat, neut, idel, indsp, indzat, iat, natsp, iatsp #/gasp2/
    global nlin1, lin1, linv1, nlin2, lin2, linv2 #/lin/
    global logk, logwt, it, kt, type0 #equil
    
#c
      
#c
    t0 = CSBlockData.t0
    
    #ip = [0.0e0 for i in range(150)]
    #ip = GsRead.ip
    ip = CSGsRead2.ip
    #comp = [0.0e0 for i in range(40)]
    #comp = GsRead.comp
    comp = CSGsRead2.comp
    #awt = [0.0e0 for i in range(150)]
    
    #itab = [0 for i in range(83)]
    itab = CSBlockData.itab
    #ntab = [0 for i in range(5)]
    #indx = [ [ [ [ [0 for i in range(2)] for j in range(5) ] for k in range(7) ] for l in range(26) ] for m in range(4) ]
    #indx = GsRead.indx
    indx = CSGsRead2.indx
    #name = [' ' for i in range(150)]
    
    #gsinit = False
    #print0 = False
    
#c
    #ipr = [0 for i in range(150)]
    #ipr = GsRead.ipr
    ipr = CSGsRead2.ipr
    #nch = [0 for i in range(150)]
    #nch = GsRead.nch
    nch = CSGsRead2.nch
    #nel = [0 for i in range(150)]
    #ntot = [0 for i in range(150)]
    #nat = [ [0 for i in range(150)] for j in range(5) ]
    #zat = [ [0 for i in range(150)] for j in range(5) ]
    #zat = GsRead.zat
    zat = CSGsRead2.zat
    #neut = [0 for i in range(150)]
    #neut = GsRead.neut
    neut = CSGsRead2.neut
    #idel = [0 for i in range(150)]
    #idel = GsRead.idel
    idel = CSGsRead2.idel
    #indsp = [0 for i in range(40)]
    #indsp = GsRead.indsp
    indsp = CSGsRead2.indsp
    #indzat = [0 for i in range(100)]
    #iat = [0 for i in range(150)]
    #iat = GsRead.iat
    iat = CSGsRead2.iat
    #natsp = [0 for i in range(40)]
    #iatsp = [ [0 for i in range(40)] for j in range(40) ]
    
#c
    #lin1 = [0 for i in range(40)]
    #lin2 = [0 for i in range(40)]
    #linv1 = [0 for i in range(40)]
    #linv2 = [0 for i in range(40)]
    
    #natom = GsRead.natom
    natom = CSGsRead2.natom
    #nspec = GsRead.nspec
    nspec = CSGsRead2.nspec
    #nlin1 = GsRead.nlin1
    nlin1 = CSGsRead2.nlin1
    #nlin2 = GsRead.nlin2
    nlin2 = CSGsRead2.nlin2
    
#c
    #logk = [ [0.0e0 for i in range(150)] for j in range(5) ]
    #logwt = [0.0e0 for i in range(150)]
    #logk = GsRead.logk
    logk = CSGsRead2.logk
    #logwt = GsRead.logwt
    logwt = CSGsRead2.logwt

    it = [0.0e0 for i in range(150)]
    kt = [0.0e0 for i in range(150)]
    
    #type0 = [0 for i in range(150)]
    #type0 = GsRead.type0
    type0 = CSGsRead2.type0
    
#c
    
    p = [0.0e0 for i in range(40)]
    logt = 0.0e0
    logit = 0.0e0
    logkt = 0.0e0
    ipeff = 0.0e0
    imp = 0.0e0
    ihp = 0.0e0
    ihm = 0.0e0
    icp = 0.0e0
    inp = 0.0e0
    iop = 0.0e0
    isip = 0.0e0
    isp = 0.0e0
    iclm = 0.0e0
    iscp = 0.0e0
    itip = 0.0e0
    ivp = 0.0e0
    iyp = 0.0e0
    izrp = 0.0e0
    kh2 = 0.0e0
    kch = 0.0e0
    koh = 0.0e0
    knh = 0.0e0
    kco = 0.0e0
    kn2 = 0.0e0
    kh2o = 0.0e0
    ksio = 0.0e0
    ksis = 0.0e0
    ksih = 0.0e0
    khs = 0.0e0
    kh2s = 0.0e0
    khcl = 0.0e0
    ksco = 0.0e0
    ksco2 = 0.0e0
    ktio = 0.0e0
    kvo = 0.0e0
    kyo = 0.0e0
    kyo2 = 0.0e0
    kzro = 0.0e0
    kzro2 = 0.0e0
    
    
    #izmet = [1, 2, 6, 11, 12, 13, 14, 19, 20, 26]
    izmet = [0, 1, 5, 10, 11, 12, 13, 18, 19, 25]
    nummet = 10
    mxspec = 150
    
    #c
    #c Calculate equilibrium constants for each species in table
    #c N.B. Freeze the chemical equilibrium for T < 1200K.
    #c
    
    t = temp

    if (t < 1200.0e0):
        t = 1200.0e0
        
    th = t0/t
    logt = 2.5e0*math.log10(t)
    
    for n in range(nspec):
        
        if (ipr[n] <= 2):
            
            ityp = type0[n]
            nq = nch[n]
            ich = isign(1, nq)
            
            if ( (ityp == 3) or (ityp == 4) ):

                kt[n] = kt[neut[n]]
                if ( ((nch[n] - nch[n-1]) != ich) or (nch[n-1] == 0) ):
                    logit = 0.0e0
                logit = logit + ich*(-th*ip[n] + logt + logwt[n] - 0.48e0)
                it[n] = ten(logit)
            elif (ityp == 2):
                logkt = (((logk[4][n]*th + logk[3][n])*th + logk[2][n])*th + logk[1][n])*th + logk[0][n]
                kt[n] = ten(logkt)
                it[n] = 1.0e0
            else:
                kt[n] = 1.0e0
                it[n] = 1.0e0
            


    kt[mxspec-1] = 1.0e0
    it[mxspec-1] = 1.0e0
    
    #c
    #c ISOLV=1: Calculate initial estimates of major species 
    #c          and for a fictitous electron donor Z as well as Pe
    #c ISOLV=2: Calculate initial estimates of both major and minor
    #c          species as well as for pe.
    #c
    jh = iat[indx[1][1][0][0][0]]
    comph = comp[jh]
    ihp = it[indx[2][1][0][0][0]]
    dhp = idel[indx[2][1][0][0][0]]
    kh2 = kt[indx[1][1][1][0][0]]
    dh2 = idel[indx[1][1][1][0][0]]
    #print("jh ", jh, " comph ", comph, " kh2 ", kh2, " dh2 ", dh2)
    
    peh = 0.0e0
    if (dhp != 0.0e0):
        term = (1.0e0 + comph)*ihp
        rat = -4.0e0*comph*ihp*pt/term/term
        omrat = 1.0e0 - rat
        if (omrat < 0.0e0): 
            omrat = 0.0e0
        if (abs(rat) >= 1.0e-10):
            peh = (-term + abs(term)*math.sqrt(omrat))/2.0e0
        else:
            peh = comph*ihp*pt/term
        
    
    ipeff = 7.3e0
    imp = ten(-ipeff*th + logt - 0.48e0)
    
    #c
    #c Estimate PH2 since Pd = PH + PH2 in the cool temperature
    #c limit where the metals provide most of the electrons. We
    #c then use this Pd value to estimate this electron pressure.
    #c
    ph2 = 0.0e0
    if (dh2 != 0.0e0):
        fact = 2.0e0 - comph
        terma = fact*fact
        termb = 2.0e0*comph*pt*fact + kh2
        fact2 = comph*pt
        termc = fact2*fact2
        rat = 4.0e0*terma*termc/termb/termb
        omrat = 1.0e0 - rat
        if (omrat < 0.0e0): 
            omrat = 0.0e0
        ph2 = termb*(1.0e0 - math.sqrt(omrat))/2.0e0/terma
        
    #c
    #c Include metals with low ionization potential in initial guess
    #c Na (Z=11), Mg (Z=12), Al (Z=13), K (Z=19), Ca (Z=20), Fe(Z=26)
    #c also Si (Z=14)
    #c
    compm = 0.0e0
    for i in range(2, nummet):
        ind = itab[izmet[i]]
        j = iat[indx[1][ind][0][0][0]]
        compm = compm + comp[j]*idel[indx[2][ind][0][0][0]]
        
    pem2 = imp*imp + 4.0e0*compm*(pt + ph2)*imp
    if (pem2 < 0.0e0):
        pem2 = 0.0e0
    pem = (math.sqrt(pem2) - imp)/2.0e0

    #c
    #c Estimate total electron pressure
    #c
    pe0 = max(peh, pem)
    #print("peh ", peh, " pem ", pem, " pe0 ", pe0)
    #c
    #c Having obtained a crude estimate of electron pressure,
    #c we now use a linearization approach to obtain a good value.
    #c
    firstTime = True
    neit = 0
    
    #215
    #sum1 = 0.0e0
    #sum2 = 0.0e0
    #pd = pt + ph2 - pe0
    #dpe = (pd*sum1 - pe0)/(1.0e0 + sum1 + pd*sum2)
    #pe0 = pe0 + dpe
    dpe = 1.1e-3 * pe0 #initial dummy value
    
    #print("pt ", pt, " pe0 ", pe0, " peh ", peh, " pem ", pem)
    while( ( (neit <= 15) and (abs(pe0/pt) > 1.0e-20) and (abs(dpe/pe0) > 1.0e-3) ) or firstTime == True):
    
        firstTime = False
    
        neit = neit + 1
        sum1 = 0.0e0
        sum2 = 0.0e0
    
        #c
        #c Consider H, He, C, Na, Mg, Al, Si, K, Ca and Fe as electron donors
        #c
        for i in range(nummet):
            ind = itab[izmet[i]]
            j = iat[indx[1][ind][0][0][0]]
            ii = indx[2][ind][0][0][0]
            #print("i ", i, " ind ", ind, " j ", j, " ii ", ii, " idel ", idel[ii])
            if (idel[ii] == 1):
                fact3 = it[ii] + pe0
                #print("it ", it[ii], " fact3 ", fact3)
                sum1 = sum1 + comp[j]*it[ii]/fact3
                sum2 = sum2 + comp[j]*it[ii]/fact3/fact3
       
        pd = pt + ph2 - pe0
        dpe = (pd*sum1 - pe0)/(1.0e0 + sum1 + pd*sum2)
        #print("sum1 ", sum1, " sum2 ", sum2, " pd ", pd)
        pe0 = pe0 + dpe
        #print("neit ", neit, " dpe ", dpe, " pe0 ", pe0)
        #Original FORTRAN go to logic replaced by while condition above
        #if (neit .le. 15 .AND. dabs(pe0/pt) .gt. 1.0d-20
        #    .AND. dabs(dpe/pe0) .gt. 1.0e-3) go to 215

    pe = pe0
    #print("Final pe0 ", pe0)
    if (abs(pe/pt) < 1.0e-20):
        pe = pt*1.0e-20
    #c
    #c Estimate partial pressures of major atomic species, ie.
    #c H, C, N, O, S, and Si.
    #c These are the only initial estimates required if ISOLV=1.
    #c
    #c First estimate partial pressure of atomic hydrogen
    #c
    ihm = it[indx[0][1][0][0][0]]
    dhm = idel[indx[0][1][0][0][0]]
    terma = (2.0e0 - comph)*dh2/kh2
    termb = 1.0e0
    if (pe > 0.0e0):
        #print("dhp ", dhp, " ihp ", ihp, " dhm ", dhm, " ihm ", ihm, " pe ", pe)
        termb = 1.0e0 + dhp*ihp/pe + dhm*ihm*pe
    termc = -(pt - pe)*comph
    rat = 4.0e0*terma*termc/termb/termb
    omrat = 1.0e0 - rat
    if (omrat < 0.0e0):
        omrat = 0.0e0
    #print("abs(rat) ", abs(rat))
    if (abs(rat) >= 1.0e-10):
        ph = ( (-1.0*termb) + abs(termb)*math.sqrt(omrat))/2.0e0/terma
        #print("terma ", terma, " termb ", termb, " omrat ", omrat, " ph ", ph)
    else:
        ph = -1.0*termc/termb
        #print(" termb ", termb, " termc ", termc, " ph ", ph)
      
    ph2 = dh2*ph*ph/kh2
    pd = pt + ph2 - pe
    
    #c
    #c Now that Pd, the total fictitious pressure is known, we can
    #c estimate the partial pressure of the other major
    #c atomic species C,N,O,Si,S
    #c
    jc = iat[indx[1][2][0][0][0]]
    jn = iat[indx[1][3][0][0][0]]
    jo = iat[indx[1][4][0][0][0]]
    jsi = iat[indx[1][12][0][0][0]]
    js = iat[indx[1][5][0][0][0]]
    compc = comp[jc]
    compn = comp[jn]
    compo = comp[jo]
    compsi = comp[jsi]
    comps = comp[js]
    icp = it[indx[2][2][0][0][0]]
    inp = it[indx[2][3][0][0][0]]
    iop = it[indx[2][4][0][0][0]]
    isip = it[indx[2][12][0][0][0]]
    isp = it[indx[2][5][0][0][0]]
    kch = kt[indx[1][2][1][0][0]]
    koh = kt[indx[1][4][1][0][0]]
    knh = kt[indx[1][3][1][0][0]]
    kco = kt[indx[1][4][2][0][0]]
    kn2 = kt[indx[1][3][3][0][0]]
    kh2o = kt[indx[1][4][1][1][0]]
    ksio = kt[indx[1][12][4][0][0]]
    ksis = kt[indx[1][12][5][0][0]]
    #c   ksih = kt[indx[1][12][1][0][0]]
    khs = kt[indx[1][5][1][0][0]]
    kh2s = kt[indx[1][5][1][1][0]]
    dcp = idel[indx[2][2][0][0][0]]
    dnp = idel[indx[2][3][0][0][0]]
    dop = idel[indx[2][4][0][0][0]]
    dsip = idel[indx[2][12][0][0][0]]
    dsp = idel[indx[2][5][0][0][0]]
    dch = idel[indx[1][2][1][0][0]]
    doh = idel[indx[1][4][1][0][0]]
    dnh = idel[indx[1][3][1][0][0]]
    dco = idel[indx[1][4][2][0][0]]
    dn2 = idel[indx[1][3][3][0][0]]
    dh2o = idel[indx[1][4][1][1][0]]
    dsio = idel[indx[1][12][4][0][0]]
    dsis = idel[indx[1][12][5][0][0]]
    #c     dsih = idel[indx[1][12][1][0][0]]
    dhs = idel[indx[1][5][1][0][0]]
    dh2s = idel[indx[1][5][1][1][0]]
    ksih = 1.0e0
    dsih = 0.0e0
      
    #c
    #c Estimate C and O partial pressures
    #c
    fact1 = 1.0e0 + doh*ph/koh + dh2o*ph*ph/kh2o + dop*iop/pe
    fact2 = 1.0e0 + dch*ph/kch + dcp*icp/pe
    terma = fact1*dco/kco
    termb = fact1*fact2 + (compc - compo)*pd*dco/kco
    termc = -compo*pd*fact2
    rat = 4.0e0*terma*termc/termb/termb
    omrat = 1.0e0 - rat
    
    if (omrat < 0.0e0):
        omrat = 0.0e0
    if (abs(rat) >= 1.0e-10):
        po = (-termb + abs(termb)*math.sqrt(omrat))/(2.0e0*terma)
    else:
        if (termb <= 0.0e0):
            po = -termb/terma
        else:
            po = -termc/termb
    
     
    pc = compc*pd/(fact2 + dco*po/kco)

    #c
    #c Estimate N partial pressure 
    #c
    terma = 2.0e0*dn2/kn2
    termb = 1.0e0 + dnh*ph/knh + dnp*inp/pe
    termc = -compn*pd
    pn = compn*pd/termb
    if ( (dn2 != 0.0e0) and (kn2 < 1.0e6) ):
        pnnn = termb*termb - 4.0e0*terma*termc
        if (pnnn < 0.0e0): 
            pnnn = 0.0e0
        pn = (-termb + math.sqrt(pnnn))/2.0e0/terma

    #c
    #c Estimate Si and S partial pressures
    #c
    fact1 = 1.0e0 + dsio*po/ksio + dsih*ph/ksih + dsip*isip/pe
    fact2 = 1.0e0 + dhs*ph/khs + dh2s*ph*ph/kh2s + dsp*isp/pe
    terma = fact1*dsis/ksis
    termb = fact1*fact2 + (comps - compsi)*pd*dsis/ksis
    termc = -compsi*pd*fact2
    rat = 4.0e0*terma*termc/termb/termb
    omrat = 1.0e0 - rat
    
    if (omrat < 0.0e0):
        omrat = 0.0e0
    if (abs(rat) >= 1.0e-10):
        psi = (-termb + abs(termb)*math.sqrt(omrat))/2.0e0/terma
    else:
        if (termb <= 0.0e0):
            psi = -termb/terma
        else:
            psi = -termc/termb
    
     
    ps = comps*pd/(fact2 + dsis*psi/ksis)

    #c
    #c Fill array of initial partial pressure estimates for H, C, N, O 
    #c
    p[jh] = ph
    p[jc] = pc
    p[jn] = pn
    p[jo] = po
    p[jsi] = psi
    p[js] = ps
    
    #print("jh ", jh, " p[jh] ", p[jh])

    #c
    #c Make initial estimates for any other elements to be
    #c included in linearizaton.
    #c
    for j in range(natom):
        n = indsp[j]
        if (ipr[n] > 2):
            p[j] = 0.0e0
        else:
            #iz = zat[0][indsp[j]]
            iz = zat[0][indsp[j]]-1
            
            #Original FORTRAN "computed go to":
            #  go to (230, 400, 400, 400, 400, 230, 230, 230, 400, 400,
            #         400, 400, 400, 230, 400, 230, 317, 400, 400, 400,
            #         321, 322, 323, 400, 400, 400, 400, 400, 400, 400,
            #         400, 400, 400, 400, 400, 400, 400, 400, 339, 340), iz

            if ( iz==1 or iz==2 or iz==3 or iz==4\
                or iz==8 or iz==9 or iz==10 or iz==11 or iz==12\
                or iz==14 or iz==17 or iz==18 or iz==19\
                or (iz>=23 and iz<=37) ):
                
                #c
                #c Estimate partial pressure of neutral atomic species considering all
                #c atoms are present only as neutral atoms or singly charged ions.
                #c Elements for which the above statement is inaccurate
                #c (eg., molecular association is appreciable) are treated
                #c separately below. These elements are He,Ne,Cl,Sc,Ti,V,Y,Zr.
                #c
                
                #400    
                n = indx[2][itab[iz]][0][0][0]
                p[j] = pd*comp[j]/(1.0e0 + idel[n]*it[n]/pe)
                #go to 230
                
            elif(iz == 16):
                
                #c
                #c Estimate Cl partial pressure 
                #c
                #317    
                jcl = iat[indx[1][6][0][0][0]]
                iclm = it[indx[0][6][0][0][0]]
                khcl = kt[indx[1][6][1][0][0]]
                dclm = idel[indx[0][6][0][0][0]]
                dhcl = idel[indx[1][6][1][0][0]]
                p[jcl] = comp[jcl]*pd/(1.0e0 + dhcl*ph/khcl + dclm*iclm*pe)
                #go to 230
                
#c
#c Estimate Sc partial pressure
#c
#  321   
            elif(iz == 20):
                jsc = iat[indx[1][15][0][0][0]]
                iscp = it[indx[2][15][0][0][0]]
                dscp = idel[indx[2][15][0][0][0]]
                ksco = kt[indx[1][15][4][0][0]]
                dsco = idel[indx[1][15][4][0][0]]
                ksco2 = kt[indx[1][15][4][4][0]]
                dsco2 = idel[indx[1][15][4][4][0]]
                p[jsc] = comp[jsc]*pd/(1.0e0 + dsco*po/ksco + dsco2*po*po/ksco2 + dscp*iscp/pe)
                #go to 230
            #c
            #c Estimate Ti partial pressure 
            #c
  #322    
            elif(iz == 21):          
                jti = iat[indx[1][16][0][0][0]]
                itip = it[indx[2][16][0][0][0]]
                dtip = idel[indx[2][16][0][0][0]]
                ktio = kt[indx[1][16][4][0][0]]
                dtio = idel[indx[1][16][4][0][0]]
                p[jti] = comp[jti]*pd/(1.0e0 + dtio*po/ktio + dtip*itip/pe)
                #go to 230
            #c
            #c Estimate V partial pressure 
            #c
  #323    
            elif(iz == 21):          
                jv = iat[indx[1][17][0][0][0]]
                ivp = it[indx[2][17][0][0][0]]
                dvp = idel[indx[2][17][0][0][0]]
                kvo = kt[indx[1][17][4][0][0]]
                dvo = idel[indx[1][17][4][0][0]]
                p[jv] = comp[jv]*pd/(1.0e0 + dvo*po/kvo + dvp*ivp/pe)
                #go to 230
            #c
            #c Estimate Y partial pressure
            #c
  #339    
            elif(iz == 38):          
                jy = iat[indx[1][24][0][0][0]]
                iyp = it[indx[2][24][0][0][0]]
                dyp = idel[indx[2][24][0][0][0]]
                kyo = kt[indx[1][24][4][0][0]]
                dyo = idel[indx[1][24][4][0][0]]
                kyo2 = kt[indx[1][24][4][4][0]]
                dyo2 = idel[indx[1][24][4][4][0]]
                p[jy] = comp[jy]*pd/(1.0e0 + dyo*po/kyo + dyo2*po*po/kyo2 + dyp*iyp/pe)
                #go to 230
                
                #c
                #c Estimate Zr partial pressure
                #c
  #340    
            elif(iz == 39):     
                jzr = iat[indx[1][25][0][0][0]]
                izrp = it[indx[2][25][0][0][0]]
                dzrp = idel[indx[2][25][0][0][0]]
                kzro = kt[indx[1][25][4][0][0]]
                dzro = idel[indx[1][25][4][0][0]]
                kzro2 = kt[indx[1][25][4][4][0]]
                dzro2 = idel[indx[1][25][4][4][0]]
                p[jzr] = comp[jzr]*pd/(1.0e0 + dzro*po/kzro + dzro2*po*po/kzro2 + dzrp*izrp/pe)


    if (isolv == 0):
        #neq = 1
        neq = 1 + 1
    elif (isolv == 1):
        neq = nlin1 + 2
        #neq = nlin1 + 2 + 1
    elif (isolv == 2):
        neq = nlin2 + 1
        #neq = nlin2 + 1 + 1
        
    #print("GasEst: isolv ", isolv, " nlin2 ", nlin2, " neq ", neq)
#Try returning a tuple:
    return pe, p, neq


            
        

    
    
    
    


    
    
    
    
    
    
    

