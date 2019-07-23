# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:00:46 2019

@author: Philip D. Bennett
Port from FORTRAN to Python: Ian Short
"""

"""
This is the main source file for GAS.

"""

"""
/*
 * The openStar project: stellar atmospheres and spectra
 *
 * ChromaStarPy/GAS
 *
 * Version 2019-05-02
 * Use date based versioning with ISO 8601 date (YYYY-MM-DD)
 *
 * May 2019
 * 
 * C. Ian Short
 * Philip D. Bennett
 *
 * Saint Mary's University
 * Department of Astronomy and Physics
 * Institute for Computational Astrophysics (ICA)
 * Halifax, NS, Canada
 *  * ian.short@smu.ca
 * www.ap.smu.ca/~ishort/
 *
 *
 * Ported from FORTRAN77
 *
 *
 * Code provided "as is" - there is no formal support 
 *
 */

"""

"""/*
 * The MIT License (MIT)
 * Copyright (c) 2019 C. Ian Short 
 *
 * Permission is hereby granted, free of charge, to any person 
 obtaining a copy of this software and associated documentation 
 files (the "Software"), to deal in the Software without 
 restriction, including without limitation the rights to use, 
 copy, modify, merge, publish, distribute, sublicense, and/or 
 sell copies of the Software, and to permit persons to whom the 
 Software is furnished to do so, subject to the following 
 conditions:
 *
 * The above copyright notice and this permission notice shall 
 be included in all copies or substantial portions of the 
 Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY 
 KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
 WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
 AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
 OTHER DEALINGS IN THE SOFTWARE.
*
 */
"""

#from decimal import Decimal as D

#plotting:
#import matplotlib
#import matplotlib.pyplot as plt
#%matplotlib inline
import math
import numpy
#from scipy.linalg.blas import daxpy
#from scipy.linalg.blas import ddot
#from scipy.linalg.blas import dscal
#from scipy.linalg.blas import idamax

#from Documents.ChromaStarPy.linpack.Dgesl import dgesl
#from Documents.ChromaStarPy.linpack.Dgefa import dgefa
import Dgesl
import Dgefa
#from Documents.ChromaStarPy.GAS.blas.Daxpy import daxpy
#from Documents.ChromaStarPy.GAS.blas.Ddot import ddot
#from Documents.ChromaStarPy.GAS.blas.Dscal import dscal
#from Documents.ChromaStarPy.GAS.blas.Idamax import idamax
 
#from Documents.ChromaStarPy.GAS.BlockData import *
#from Documents.ChromaStarPy.GAS.GsRead2 import 
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
            
    

def gas(isolv, temp, pt, pe0, p0, neq, tol, maxit):
    
    #Returned structure
    # a, ngit, pe, pd, pp, ppix, gmu, rho
    
    #c cis: parameter tol is argument GTOL
    #c cis: parameter * is argument PRINT - !!??
    #c cis: INPUT: ISOLV,T,P, PE0,P0,NEQ, GTOL,MAXGIT, PRINT (??)
    #c cis: OUTPUT: A, NGIT, PE,PD,PP,PPIX,GMU,RHO (??)
    #c
    #c GAS: Calculates the equilibrium abundances of each molecular and ionic
    #c species specified in "gsread", at the given temperature T and
    #c pressure P.
    #c

    
    #FORTRAN commons - needed
    #common /consts/ pi,sbcon,kbol,cvel,gcon,hpl,hmass,t0,everg
    #common /gasp/ name,ip,comp,awt,nspec,natom,itab,ntab,indx,
     #    iprint,gsinit,print1
    #common /gasp2/ ipr,nch,nel,ntot,nat,zat,neut,idel,indsp,
     #    indzat,iat,natsp,iatsp
    #common /lin/ nlin1,lin1,linv1,nlin2,lin2,linv2
    #common /equil/ logk,logwt,it,kt,type
    #common /opacty/ chix,nix,nopac,ixa,ixn,opinit,opflag,opchar,iopt
    
    #Try this:
    #global pi, sbcon, kbol, cvel, gcon, hpl, hmass, t0, everg # /consts/
    global kbol, hmass, t0 # /consts/
    global name, ip, comp, awt, nspec, natom, itab, ntab, indx, iprint, gsinit, print0 #/gasp/
    global ipr, nch, nel, ntot, nat, zat, neut, idel, indsp, indzat, iat, natsp, iatsp #/gasp2/
    global nlin1, lin1, linv1, nlin2, lin2, linv2 #/lin/
    global logk, logwt, it, kt, type0 #equil
    #global chix, nix, nopac, ixa, ixn, opinit, opflag, opchar, iopt #/opacty/
    global chix, nix, ixa, ixn  #/opacty/
    
#c
    outString=""
      
    kbol = CSBlockData.kbol
    hmass = CSBlockData.hmass
    t0 = CSBlockData.t0
#c
      
    #ip = [0.0e0 for i in range(150)]
    #ip = GsRead.ip
    ip = CSGsRead2.ip
    #comp = [0.0e0 for i in range(40)]
    #comp = GsRead.comp
    comp = CSGsRead2.comp
    #awt = [0.0e0 for i in range(150)]
    #awt = GsRead.awt
    awt = CSGsRead2.awt
    
    #itab = [0 for i in range(83)]
    itab = CSBlockData.itab
    #ntab = [0 for i in range(5)]
    #indx = [ [ [ [ [0 for i in range(2)] for j in range(5) ] for k in range(7) ] for l in range(26) ] for m in range(4) ]
    #indx = GsRead.indx
    indx = CSGsRead2.indx

    #name = [' ' for i in range(150)]
    #name = GsRead.name
    name = CSGsRead2.name
    
    #gsinit = False
    #print0 = False
    print0 = CSBlockData.print0
    #iprint = GsRead.iprint
    iprint = CSGsRead2.iprint
     
    #ipr = [0 for i in range(150)]
    #ipr = GsRead.ipr
    ipr = CSGsRead2.ipr
    #nch = [0 for i in range(150)]
    #nch = GsRead.nch
    nch = CSGsRead2.nch
    #nel = [0 for i in range(150)]
    #nel = GsRead.nel
    nel = CSGsRead2.nel
    #ntot = [0 for i in range(150)]
    #ntot = GsRead.ntot
    ntot = CSGsRead2.ntot
    #nat = [ [0 for i in range(150)] for j in range(5) ]
    #nat = GsRead.nat
    nat = CSGsRead2.nat
    #zat = [ [0 for i in range(150)] for j in range(5) ]
    #zat = GsRead.zat
    zat = CSGsRead2.zat
    #neut = [0 for i in range(150)]
    #neut = GsRead.neut
    neut = CSGsRead2.neut
    #idel = [0 for i in range(150)]
    #indsp = [0 for i in range(40)]
    #indsp = GsRead.indsp
    indsp = CSGsRead2.indsp
    #indzat = [0 for i in range(100)]
    #indzat = GsRead.indzat
    indzat = CSGsRead2.indzat
    #iat = [0 for i in range(150)]
    #iat = GsRead.iat
    iat = CSGsRead2.iat
    #natsp = [0 for i in range(40)]
    #natsp = GsRead.natsp
    natsp = CSGsRead2.natsp
    #iatsp = [ [0 for i in range(40)] for j in range(40) ]
    #iatsp = GsRead.iatsp
    iatsp = CSGsRead2.iatsp
#c
      
    #lin1 = [0 for i in range(40)]
    #lin1 = GsRead.lin1
    lin1 = CSGsRead2.lin1
    #lin2 = [0 for i in range(40)]
    #lin2 = GsRead.lin2
    lin2 = CSGsRead2.lin2
    #linv1 = [0 for i in range(40)]
    #linv1 = GsRead.linv1
    linv1 = CSGsRead2.linv1
    #linv2 = [0 for i in range(40)]
    #linv2 = GsRead.linv2
    linv2 = CSGsRead2.linv2
    
    #nlin1 = GsRead.nlin1
    nlin1 = CSGsRead2.nlin1
    #nlin2 = GsRead.nlin2
    nlin2 = CSGsRead2.nlin2
#c
    #logk = [ [0.0e0 for i in range(150)] for j in range(5) ]
    #logwt = [0.0e0 for i in range(150)]
    it = [0.0e0 for i in range(150)]
    kt = [0.0e0 for i in range(150)]
    
    #type0 = [0 for i in range(150)]
    #type0 = GsRead.type0
    type0 = CSGsRead2.type0
    
#c
    #ixa = [ [0 for i in range(70)] for j in range(5) ]
    #ixn = [0 for i in range(70)]
    #ixn = GsRead.ixn
    ixn = CSGsRead2.ixn
    #chix = [' ' for i in range(70)]
    #opchar = [' ' for i in range(25)]
    #opflag = [False for i in range(25)]
    #opinit = False    
    nix = CSBlockData.nix
    
    #natom = GsRead.natom
    natom = CSGsRead2.natom
    #nspec = GsRead.nspec
    nspec = CSGsRead2.nspec
    
    #logk = GsRead.logk
    logk = CSGsRead2.logk
    #logwt = GsRead.logwt
    logwt = CSGsRead2.logwt

#c
    #print("GAS: neq ", neq, " nlin1 ", nlin1, " nlin2 ", nlin2)
    
    a = [ [0.0e0 for i in range(neq)] for j in range(neq) ]
    b = [0.0e0 for i in range(40)]
    p = [0.0e0 for i in range(40)]
    pp = [0.0e0 for i in range(150)]
    pp0 = [0.0e0 for i in range(150)]
    al = [0.0e0 for i in range(25)]
    ppix = [0.0e0 for i in range(70)]
    #p0 = [0.0e0 for i in range(40)]
    nd = 0.0e0
    logt = 0.0e0
    logit = 0.0e0
    logkt = 0.0e0
   
    namet = ''
    namemx = ''

    iperm = [0 for i in range(180)]
       
    metals = 'Z'
    ename = 'e-'
    blank = ' '
    rhs = 'rhs'
    job = 0
    
    #c
    #c Calculate equilibrium constants for each species in table.
    #c N.B. Freeze the chemical equilibrium for T < 1200K.
    #c
    t = temp
    if (t < 1200.0e0):
        t = 1200.0e0
        
    th = t0/t
    logt = 2.5e0*math.log10(t)
    
    for n in range(0, nspec):
        
        ityp = type0[n]
        nq = nch[n]
        ich = isign(1, nq)
        
        if (ityp == 3 or ityp == 4):
            
            kt[n] = kt[neut[n]]
            if ( ((nch[n] - nch[n-1]) != ich) or (nch[n-1] == 0) ):
                logit = 0.0e0
            logit = logit + ich*(-th*ip[n] + logt + logwt[n] - 0.48e0)
            it[n] = ten(logit)
        elif (ityp == 2):
            logkt = ( ((logk[4][n]*th + logk[3][n])*th + logk[2][n])*th + logk[1][n] )*th + logk[0][n]
            kt[n] = ten(logkt)
            it[n] = 1.0e0
        else:
            kt[n] = 1.0e0
            it[n] = 1.0e0

#c
#c Update main arrays 
#c
    pe = pe0
    #print("pe0 ", pe0)
    for j in range(0, natom):
        p[j] = p0[j]
        #print("j ", j, " p0 ", p0[j])

    ngit = 0
    namemx = blank
    delmax = 0.0e0
    
    if (isolv != 0):
        
        if (isolv == 1):
        
            compz = 0.0e0
            pzs = 0.0e0
            
            for j in range(natom):

                nn = indsp[j]
                if (ipr[nn] == 2):
                
                    nnp = indx[2][itab[zat[0][nn]-1]][0][0][0]
                    compz = compz + comp[j]
                    
                    if (pe > 0.0e0):
                        pzs = pzs + (1.0e0 + it[nnp]/pe) * p[j]
                    else:
                        pzs = pzs + p[j]
                     
        #print("print0 ", print0)
        if (print0):
            
            #print("T ", "P ", t, pt)
            
            if (isolv == 1):
                
                print("0 #  Name     Delmax   ")
                for k in range(0, nlin1):
                    print(name[indsp[linv1[k]]])
                print("ngit ", "namemx ", "delmax ", ngit, namemx, delmax)
                for k in range(0, nlin1):
                    print(p[linv1[k]])
                    
            elif (isolv == 2):
                
                print("0 #  Name     Delmax   ")
                for k in range(0, nlin2):
                    print(name[indsp[linv2[k]]])
                print("ngit ", "namemx ", "delmax ", ngit, namemx, delmax)
                for k in range(0, nlin2):
                    print(p[linv2[k]])
        

        """        
        c
        c Main loop: fill linearized coefficient matrix and rhs vector, and
        c solve system for partial pressure corrections. 
        c ISOLV = 1: Linearize only the partial pressures of the neutral atoms
        c for which IPR(j) = 1 (major species). The electron pressure Pe is
        c assumed to be given in this case, and so is not included in the
        c linearization. this is necessary since most of these electrons
        c (at cool temps.) originate from elements not considered in the
        c linearization. In order to obtain a good value for Pe in the first
        c place, it is necessary to call GAS with ISOLV = 2.
        c ISOLV = 2: This linearizes the partial pressures of the neutraL atoms
        c for which IPR(j) = 1 OR 2. This list of elements should include all
        c the significant contributors to the total pressure Pt, as well as the
        c electon pressure Pe. Any element (IPR(j) = 3) not included is assumed
        c to have a negligible effect on both P and Pe.
        c In both cases, the partial pressures of the neutral atoms for elements
        c not included in the linearization are calculated directly from the now
        c determined pressures of the linearized elements.
        c
        """
    
        #316   
        firstTime = True
        
        while( (delmax > tol) or (firstTime == True) ):
            
            firstTime = False
        
            if (ngit >= maxit):
                print('(" *15 Error: Too many iterations in routine GAS")')
                print('(" for Isolv, T, P, Pe0= " ')
                print(isolv, t, pt, pe0)
                #return 1
        
            ngit = ngit + 1
    
        #c
        #c Zero coefficient matrix and rhs vector
        #c
            if (isolv == 1):
                nlin = nlin1
            elif (isolv == 2):
                nlin = nlin2

            for jj in range(neq):
                for j in range(neq):

                    a[j][jj] = 0.0e0

                b[jj] = 0.0e0

            if (isolv == 2):
        
                #c
                #c Here the isolv = 2 case is handled. This includes linearization of Pe.
                #c
        
                #a[neq][neq] = -1.0e0
                a[neq-1][neq-1] = -1.0e0
                b[0] = pt
                #b[neq] = pe
                b[neq-1] = pe
        
                for n in range(nspec):
            
                    if (ipr[n] <= 2):
                
                        nq = nch[n]
                        pf = 1.0e0
                        nelt = nel[n]
                
                        for i in range(nelt):
                            j = indzat[zat[i][n]-1]
                            pf = pf * p[j]**nat[i][n]

                        penq = 1.0e0
                        if (pe > 0.0e0):
                            penq = pe**nq
                        pn = it[n]*pf/kt[n]/penq

                        #c
                        #c Now fill the matrix and rhs vector of linearized equations
                        #c

                        for i in range(nelt):
                            jj = indzat[zat[i][n]-1]
                            at = pn*nat[i][n]/p[jj]
                            kk = lin2[jj]
                    
                            #if (kk == 0):
                            if (kk < 0):    
                                print('(" *16 Error: Inconsistency in priority ", "tables")')
                                print('(" for Isolv, T, P, Pe0= ")')
                                print(isolv, t, pt, pe0)
                                #return 1
                            a[0][kk] = a[0][kk] + (nq + 1)*at
                            #print("n ", n, " i ", i, " jj ", jj, " kk ", kk)
                            #print("zat ", zat[i][n]-1, " nat ", nat[i][n], " p ", p[jj], " at ", at, " nq ", nq)
                            #print("a ", a[0][kk])
                            if (nlin2 >= 1):    
                                #for k in range(1, nlin2+1):
                                for k in range(1, nlin2):    
                                    j = linv2[k]
                                    a[k][kk] = a[k][kk] + comp[j]*ntot[n]*at
                                    #print("n ", n, " k ", k, " j ", j, " comp ", comp[j], " ntot ", ntot[n], " at ", at)
                                    #print("a ", a[k][kk])
                            
                            for ii in range(nelt):
                                jjj = indzat[zat[ii][n]-1]
                                kkk = lin2[jjj]
                                if (kkk != 0):
                                    a[kkk][kk] = a[kkk][kk] - nat[ii][n]*at
                                    #print("n ", n, " kk ", kk, " ii ", ii, " jjj ", jjj, " kkk ", kkk, " nat ", nat[ii][n], " at ", at)
                                    #print("a ", a[kkk][kk])
                            #a[neq][kk] = a[neq][kk] + nq*at
                            a[neq-1][kk] = a[neq-1][kk] + nq*at
                            
                        at = 0.0e0
                        if (pe > 0.0e0):
                            at = nq*pn/pe
                        a[0][neq-1] = a[0][neq-1] - (nq + 1)*at
                        b[0] = b[0] - (nq + 1)*pn
                
                        if (nlin2 >= 1):
                            #for k in range(1, nlin2+1):
                            for k in range(1, nlin2):    
                                j = linv2[k]
                                a[k][neq-1] = a[k][neq-1] - comp[j]*ntot[n]*at
                                b[k] = b[k] - comp[j]*ntot[n]*pn
                                #print("b ", b[k])

                        for ii in range(nelt):
                            jjj = indzat[zat[ii][n]-1]
                            kkk = lin2[jjj]
                    
                            if (kkk != 0):
                                a[kkk][neq-1] = a[kkk][neq-1] + nat[ii][n]*at
                                b[kkk] = b[kkk] + nat[ii][n]*pn
                                #print("b ", b[kkk])

                        #a[neq][neq] = a[neq][neq] - nq*at
                        a[neq-1][neq-1] = a[neq-1][neq-1] - nq*at
                        b[neq-1] = b[neq-1] - nq*pn
                        #print("a ", a[neq-1][neq-1], " b ", b[neq-1])
 
            else:
        
                #c
                #c Here the isolv = 1 case is treated. the electron pressure Pe
                #c is assumed gven and is not included in the linearization. 
                #c
                #print("******  isolve ne 2 brnach! isolv ", isolv)
                sum1 = 0.0e0
                sum2 = 0.0e0
        
                for j in range(natom):
                    nn = indsp[j]
                    #print("j ", j, " nn ", nn)
                    if (ipr[nn] == 2):
                        nnp = indx[2][itab[zat[0][nn]-1]][0][0][0]
                        #print("zat ", zat[0][nn]-1, " itab ", itab[zat[0][nn]-1],\
                        #     " nnp ", nnp)
                        fact = it[nnp] + pe
                        sum1 = sum1 + comp[j]*it[nnp]/fact
                        sum2 = sum2 + comp[j]*it[nnp]/fact/fact
                        #print("comp ", comp[j], " it ", it[nnp],\
                        #      " fact ", fact, " sum1 ", sum1)
                
                b[0] = pt - pzs - pe
                a[0][nlin1] = 1.0e0
                a[0][nlin1+1] = 1.0e0
                #print("pt ", pt, " pzs ", pzs, " pe ", pe)
                #print("nlin1 ", nlin1, " b[0] ", b[0], " a[0][] ", a[0][nlin1+1], a[0][nlin1+2])
        
                if (nlin1 >= 1):
                    #for k in range(1, nlin1+1):
                    for k in range(1, nlin1):    
                        j = linv1[k]
                        a[k][nlin1] = comp[j]
                        b[k] = -1.0*comp[j]*pzs
                        #print("k ", k, " j ", j, " comp ", comp[j], " a () ", a[k][nlin1+1])

                pzsrat = 0.0e0
                if (compz > 0.0e0):
                    pzsrat = pzs/compz
                a[nlin1][nlin1] = compz - 1.0e0
                b[nlin1] = (1.0e0 - compz)*pzs
                a[nlin1+1][nlin1] = 0.0e0
                if (compz > 0.0e0):
                    a[nlin1+1][nlin1] = sum1/compz
                a[nlin1+1][nlin1+1] = -1.0e0 - sum2*pzsrat
                b[nlin1+1] = pe - sum1*pzsrat
                #print("compz ", compz, " sum1 ", sum1, " sum2 ", sum2,\
                #      " pzsrat ", pzsrat)
                #print("nlin1+1 ", nlin1+1, " nlin1+2 ", nlin1+2)
                #print("a(nlin1+1,nlin1+1) ", a[nlin1+1][nlin1+1],\
                #      " b(nlin1+1) ", b[nlin1+1],\
                #      " a(nlin1+2,nlin1+1) ", a[nlin1+2][nlin1+1],\
                #      " a(nlin1+2,nlin1+2) ", a[nlin1+2][nlin1+2],\
                #      " b(nlin1+2) ", b[nlin1+2])
                

                for n in range(nspec):
            
                    if (ipr[n] <= 1):
                
                        nq = nch[n]
                        pf = 1.0e0
                        nelt = nel[n]
                
                        for i in range(nelt):
                            j = indzat[zat[i][n]-1]
                            pf = pf*p[j]**nat[i][n]

                        penq = 1.0e0
                        if (pe > 0.0e0):
                            penq = pe**nq
                        pn = it[n]*pf/kt[n]/penq
                
                        #c
                        #c Fill the coefficient matrix and rhs vector of linearized eqns
                        #c

                        for i in range(nelt):
                            jj = indzat[zat[i][n]-1]
                            #print("GAS: n ", n, " name ", name[n], " i ", i," jj ", jj, " p ", p[jj])
                            at = pn*nat[i][n]/p[jj]
                            kk = lin1[jj]
                            #print("i ", i, " jj ", jj, " kk ", kk, " at ", at)
                            #if (kk == 0):
                            if (kk < 0):
                                print('(" *17 Error: Inconsistency in priority tables")')
                                print('(" for Isolv, T, P, Pe0 = ")', isolv, t, pt, pe0)
                                #return 1
                        
                            #print("Before: n ", n, " i ", i, " kk ", kk, " a[0][kk] ", a[0][kk])
                            a[0][kk] = a[0][kk] + at
                            #print("a[0][kk] ", a[0][kk])
                            #print("n ", n, " ntot[n] ", ntot[n])
                            if (nlin1 >= 1):
                                #for k in range(1,nlin1+1):
                                for k in range(1,nlin1):
                                    j = linv1[k]
                                    a[k][kk] = a[k][kk] + comp[j]*ntot[n]*at

                            for ii in range(nelt):
                                jjj = indzat[zat[ii][n]-1]
                                kkk = lin1[jjj]
                                if (kkk != 0):
                                    a[kkk][kk] = a[kkk][kk] - nat[ii][n]*at

                            a[nlin1][kk] = a[nlin1][kk] + compz*ntot[n]*at
                            a[nlin1+1][kk] = a[nlin1+1][kk] + nq*at
                
                        at = 0.0e0
                        if (pe > 0.0e0): 
                            at = nq*pn/pe
                        a[0][nlin1+1] = a[0][nlin1+1] - at
                        b[0] = b[0] - pn
                
                        if (nlin1 >= 1):
                            #for k in range(1, nlin1+1):
                            for k in range(1, nlin1):    
                                j = linv1[k]
                                a[k][nlin1+1] = a[k][nlin1+1] - comp[j]*ntot[n]*at
                                b[k] = b[k] - comp[j]*ntot[n]*pn
                        
                        for ii in range(nelt):
                            jjj = indzat[zat[ii][n]-1]
                            kkk = lin1[jjj]
                            if (kkk != 0):
                                a[kkk][nlin1+1] = a[kkk][nlin1+1] + nat[ii][n]*at
                                b[kkk] = b[kkk] + nat[ii][n]*pn

                        a[nlin1][nlin1+1] = a[nlin1][nlin1+1] - compz*ntot[n]*at
                        b[nlin1] = b[nlin1] - compz*ntot[n]*pn
                        a[nlin1+1][nlin1+1] = a[nlin1+1][nlin1+1] - nq*at
                        b[nlin1+1] = b[nlin1+1] - nq*pn

        
            if (print0):
                
                print('("0 Log of coefficient matrix at iteration #")', ngit)
                if (isolv == 1): 
                    for k in range(nlin1):
                        print(name[indsp[linv1[k]]])
                    print(metals, ename, rhs)
                if (isolv == 2):
                    #       (name(indsp(linv2(k))),k = 1,nlin2),ename,rhs
                    for k in range(nlin2):
                        print(name[indsp[linv2[k]]])
                    print(ename, rhs)
            
                print('(" ")')
                
                neq1 = neq + 1
          
                for i in range(neq):            
                    for j in range(neq): 
                        al[j] = math.log10(abs(a[j][i]) + 1.0e-70)
                    al[neq1] = math.log10(abs(b[i]) + 1.0e-70)
                    if (isolv == 1):
                        if (i <= nlin1):
                            namet = name[indsp[linv1[i]]]
                        if (i == nlin1+1):
                            namet = metals
                        if (i == nlin1+2): 
                            namet = ename
           
                    if (isolv == 2):
                        if (i <= nlin2):
                            namet = name[indsp[linv2[i]]]
                        if (i == nlin2+1):
                            namet = ename
           
                    #print('(" ")', namet)
                    #for j in range(neq1):
                        #print(al[j])

                #print('(" ")')
        
            #c
            #c Now solve the linearized equations.
            #c
            #FORTRAN subroutine dgefa(a, neq, neq, iperm, info)
            #pythonized dgefa returns a tuple:
            #print("Before dgefa, a is:")
            #for idum in range(neq):
                #print("idum ", idum, [a[idum][jdum] for jdum in range(neq)])
            #print("b ", [b[kk] for kk in range(neq)])

            dgefaReturn = Dgefa.dgefa(a, neq, neq)
            a = dgefaReturn[0]
            iperm = dgefaReturn[1]
            info = dgefaReturn[2]
            
            #print("After dgefa, a is:")
            #for idum in range(neq):
                #print("idum ", idum, [a[idum][jdum] for jdum in range(neq)])
            #print("b ", [b[kk] for kk in range(neq)])
            #print("iperm ", [iperm[kk] for kk in range(neq)])
            #print("info ", info, " iperm ", iperm)
            

            if (info != 0):
                print('(" Info = ",i5," returned from DGEFA in GAS")', info)
            #return 1
        
            #Fortanized call call dgesl(a,neq,neq,iperm,b,job)
            #print("Before ddgesl, b is:")
            #print("b ", b)
            b = Dgesl.dgesl(a, neq, neq, iperm, b, job)
            #print("After dgesl, a is:")
            #for idum in range(neq):
                #print("idum ", idum, [a[idum][jdum] for jdum in range(neq)])
            #print("b ", [b[kk] for kk in range(neq)])
            #print("iperm ", [iperm[kk] for kk in range(neq)])            
            
            #print("After ddgesl, b is:")
            #print("b ", b)            
            delmax = 0.0e0
        
            #c
            #c First, update the partial pressures for the major species by adding
            #c the pressure corrections obtained for each atom from the linearization
            #c procedure.
            #c
            for k in range(nlin):
                if (isolv == 1): 
                    j = linv1[k]
                if (isolv == 2):
                    j = linv2[k]
                n = indsp[j]
                pnew = p[j] + b[k]
                if (pnew < 0.0e0):
                    pnew = abs(pnew)
                dp = pnew - p[j]
                #print("GAS: k ", k, " j ", j, " n ", n,\
                #      " b ", b[k], " pnew ", pnew, " p ", p[j], " dp ", dp)
                p[j] = pnew
                #print("j ", j, " p ", p[j])
                if (abs(p[j]/pt) >= 1.0e-15):
                    delp = abs(dp/p[j])
                    if (delp > delmax):
                        namemx = name[n]
                        delmax = delp
         
            if (isolv == 2):
            
                penew = pe + b[nlin2]
                if (penew < 0.0e0):
                    penew = abs(penew)
                dpe = penew - pe
                pe = penew
                if (abs(pe/pt) >= 1.0e-15):
                    delpe = abs(dpe/pe)
                    if (delpe > delmax):
                        namemx = ename
                        delmax = delpe
            
          
            elif (isolv == 1):
        
                pznew = pzs + b[nlin1]
                if (pznew < 0.0e0): 
                    pznew = abs(pznew)
                dpz = pznew - pzs
                pzs = pznew
                if (abs(pzs/pt) >= 1.0e-15):
                    delpz = abs(dpz/pzs)
                    if (delpz > delmax):
                        namemx = metals
                        delmax = delpz

                penew = pe + b[nlin1+1]
                if (penew < 0.0e0): 
                    penew = abs(penew)
                dpe = penew - pe
                pe = penew
                if (abs(pe/pt) >= 1.0e-15):
                    delpe = abs(dpe/pe)
                    if (delpe > delmax):
                        namemx = ename
                        delmax = delpe

            #c
            #c Print out summary line  for each iteration
            #c
            
            if (print0):
                if (isolv == 1): 
                    print('(" ",)', ngit, namemx, delmax, pzs, pe)
                    for k in range(nlin1):
                        print(p[linv1[k]])
                if (isolv == 2):
                    print('(" ",)', ngit, namemx, delmax, pe)
                    for k in range(nlin2):
                        print(p[linv2[k]])                  
            
            #print("firstTime ", firstTime)
            #print("*** !!! *** ngit ", ngit, " delmax ", delmax, " tol ", tol)
    #End while loop 316
            
        #c
        #c Calculate the partial pressures of the species included in the above
        #c linearization, and also the fictitious total pressure Pd of the gas.
        #c


        
        if (isolv == 1):
            for j in range(natom):
                n = indsp[j]
                if (ipr[n] == 2):
                    np = indx[2][itab[zat[0][n]-1]][0][0][0]
                    p[j] = comp[j]*pzs*pe/compz/(it[np] + pe)
                    #print("GAS: j ", j, " n ", n, " np ", np, " comp ", comp[j],\
                    #     " pzs ", pzs, " pe ", pe, " compz ", compz, " it ", it[np])
        # I *think* this ends the (isolv != 0) condition on line 290
    
    pd = 0.0e0
    pu = 0.0e0
    ptot = pe
    
    #print("GAS: pe ", pe)
    for n in range(nspec):
        
        ppt = 0.0e0
        if (ipr[n] <= 2):
            nelt = nel[n]
            nq = nch[n]
            pf = 1.0e0
            for i in range(nelt):
                j = indzat[zat[i][n]-1]
                pf = pf*p[j]**nat[i][n]

            penq = 1.0e0
            if (pe > 0.0e0):
                penq = pe**nq
            ppt = it[n]*pf/kt[n]/penq
            #print("1: n ", n, " it ", it[n], " kt ", kt[n], " penq ", penq, " pf ", pf, " ppt ", ppt)
            ptot = ptot + ppt
            pd = pd + ntot[n]*ppt
            pu = pu + awt[n]*ppt

        #print("GAS: 1st pp: n ", n, " name ", name[n], " ppt ", ppt, " it ", it[n], " pf ", pf, " kt ", kt[n], " penq ", penq) 
        pp[n] = ppt
        

    gmu = pu/ptot
    nd = ptot/kbol/t
    rho = nd*gmu*hmass
 
    """
    c
    c     return
    c
    c  The following ENTRY point has been removed for the time being,
    c  so that the partial pressures of all species are always 
    c  calculated automatically, as needed for opacity calculations.
    c                                                     29 June/90
    c                                                            PDB
    c
    c Entry point "GASPP" calculates partial pressures of all
    c species present in the gas.
    c
    c     entry gaspp(pp)
    c cis
    c      entry gaspp(pp)
    c
    c Now  calculate the partial pressure of the remaining atomic
    c species. some restrictions apply here. these are:
        c  1) Each element being considered here is restricted to a
    c     single atom per species.
    c  2) The other elements appearing in a given species must all
    c     be major elements, that is, the partial pressure for each 
    c     has already been found by the preceding linearization
    c     procedure.
    c
    """
    
    for j in range(natom):
        
        n = indsp[j]
        #print("j ", j, " n ", n, " ipr ", ipr[n])
        if (ipr[n] >= 3):
            nsp = natsp[j]
            #print("nsp ", nsp)
            denom = 0.0e0

            for k in range(nsp+1):
                nn = iatsp[j][k]
                nq = nch[nn]
                nelt = nel[nn]
                pfp = 1.0e0
                #print(" k ", k, " nn ", nn, " nq ", nq, " nelt ", nelt)
                for i in range(nelt):
                    jj = indzat[zat[i][nn]-1]
                    #print(" i ", i, " zat ", zat[i][nn]-1, " jj ", jj)
                    if (jj == j):
                        #print("jj == j")
                        if (nat[i][nn] > 1):
                            print('(" *18 Error: 2 or more atoms of same element in species")')
                            print('(" for Isolv, T, P, Pe0= ",i3,2x,1p3d12.4)', isolv, t, pt, pe0)
                            #return 1
             
            
                    else:
                        
                        #print("jj !=j")
                        
                        #if (ipr[indsp[jj]] >= 3):
                            #print("Going to 363")
                        if (ipr[indsp[jj]] < 3):
                            #print("pfp=")
                            pfp = pfp*p[jj]**nat[i][nn]
                            #print(" nat ", nat[i][nn], " p ", p[jj])
                #print("jj ", jj, " indsp ", indsp[jj], " ipr ", ipr[indsp[jj]])
                if ( (ipr[indsp[jj]] < 3) or (jj == j) ):
                    #print("penq, psp denom=")
                    penq = 1.0e0

                    if (pe > 0.0e0): 
                        penq = pe**nq
                    psp = it[nn]*pfp/kt[nn]/penq
                    denom = denom + psp

            #print("FINAL: j ", j, " comp ", comp[j], " pd ", pd, " denom ", denom)
            p[j] = comp[j]*pd/denom
            #print("GAS 2: n ", n, " name ", name[n], " j ", j, " comp ", comp[j], " pd ", pd, " denom ", denom, " p ", p[j])
            #print("pfp ", pfp, " psp ", psp)

    #c
    #c Calculate final partial pressures after convergence obtained
    #c
    ptot = pe
    pd = 0.0e0
    pu = 0.0e0
    pq = 0.0e0

    for n in range(nspec):
        
        nelt = nel[n]
        nq = nch[n]
        pf0 = 1.0e0
        pf = 1.0e0

        for i in range(nelt):
            
            j = indzat[zat[i][n]-1]
            pf0 = pf0*p0[j]**nat[i][n]
            pf = pf*p[j]**nat[i][n]
            #print("GAS 2: n ", n, " j ", j, " p ", p[j], " i ", i, " nat ", nat[i][n])

        penq = 1.0e0

        if (pe > 0.0e0):
            penq = pe**nq
        pp[n] = it[n]*pf/kt[n]/penq
        #print("GAS: 2nd pp: n ", n, " name ", name[n], " pp ", pp[n], " it ", it[n], " pf ", pf, " kt ", kt[n], " penq ", penq)
        penq = 1.0e0
            
        if (pe0 > 0.0e0):
            penq = pe0**nq
        pp0[n] = it[n]*pf0/kt[n]/penq
        ptot = ptot + pp[n]
        pd = pd + ntot[n]*pp[n]
        pq = pq + nq*pp[n]
        pu = pu + awt[n]*pp[n]

    pdtot = pd + pe
    dptot = abs(ptot - pt)/pt
    dpq = abs(pq - pe)/pt
    gmu = pu/ptot
    nd = ptot/kbol/t
    rho = nd*gmu*hmass

    #c
    #c Fill the array "PPIX" with the partial pressures of the
    #c specified species.
    #c
    if (nix > 0):
        for i in range(nix):
            ppix[i] = 0.0e0
            ii = ixn[i]
            #print("i ", i, " ixn ", ixn[i])
            if (ii < 150):
                ppix[i] = pp[ixn[i]]

    #c
    #c Write out final partial pressures 
    #c
    """
    print0 = True
    
    if (print0):    
        #print('("1After ",i3," iterations, with ISOLV =",i2,":", "0T=","   P=", "   Pdtot=","   dPtot=","   dPq="," Number Dens.="," /cm**3    Mean At.Wt.=","   Density="," g/cm**3"/, "0  #  Species      Abundance   Initial P     Final P", "      iT           kT     "//)',\
        #        ngit, isolv, t, pt, pdtot, dptot, dpq, nd, gmu, rho)
        outString = ("%6s %4d %25s %2d %1s\n"\
              %("1After ", ngit, " iterations, with ISOLV =", isolv, ":"))
        outFile.write(outString)
        outString =("%3s %12.3e %3s %12.3e %7s %12.3e %7s %12.3e %5s %10.3e\n"\
              %("0T=", t, "   P=", pt, "   Pdtot=", pdtot, "   dPtot=", dptot, "   dPq=", dpq))
        outFile.write(outString)
        outString = ("%14s %10.3e %24s %8.3f %9s %10.3e %8s\n"\
              %(" Number Dens.=", nd, " /cm**3    Mean At.Wt.=", gmu, "   Density=", rho, "g/cm**3"))
        outFile.write(outString)
        nsp1 = nspec + 1

        outString = ("%4s %14s %12s %11s %13s %12s %10s\n"\
              %("0  #", "  Species     ", " Abundance  ", "   Initial P    ", "    Final P ", "     iT     ", "     kT    "))
        outFile.write(outString)
        for n in range(nspec):
            #if (pp[n] <= 0.0e0):
            #    pp[n] = 1.0e-19
            if (type0[n] != 1):
                #print(n, name[n], pp0[n], math.log10(abs(pp[n])/pt) ,it[n], kt[n])
                outString = ("%4d %14s %24.3e %12.3e %12.3e %12.3e\n"\
                      %(n, name[n], pp0[n], pp[n] ,it[n], kt[n]))
                outFile.write(outString)
            else:
                j = iat[n]
                #print(n, name[n], comp[j], pp0[n], math.log10(abs(pp[n])/pt), it[n], kt[n])
                outString = ("%4d %14s %12.3e %12.3e %12.3e %12.3e %12.3e\n"\
                      %(n, name[n], comp[j], pp0[n], pp[n], it[n], kt[n]))
                outFile.write(outString)

        if (iprint < 0):
            print0 = False
        #print(nsp1, ename, pe0, pe)
        outString = ("%4d %14s %24.3e %12.3e\n" %(nsp1, ename, pe0, pe))
        outFile.write(outString)
        """
    #Try returning a tuple:
    return a, ngit, pe, pd, pp, ppix, gmu, rho