# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:42:29 2019

@author: 
"""

import math
import numpy
#from scipy.linalg.blas import daxpy
#from scipy.linalg.blas import ddot
#from scipy.linalg.blas import dscal
#from scipy.linalg.blas import idamax
#from Documents.ChromaStarPy.GAS.blas.Daxpy import daxpy
#from Documents.ChromaStarPy.GAS.blas.Ddot import ddot
#from Documents.ChromaStarPy.GAS.blas.Dscal import dscal
#from Documents.ChromaStarPy.GAS.blas.Idamax import idamax
import Daxpy
import Ddot
import Dscal
import Idamax

def dgesl(a, lda, n, ipvt, b, job):
    
    
    #integer lda,n,ipvt(1),job
    #double precision a(lda,1),b(1)
    
    """
c
c     dgesl solves the double precision system
c     a * x = b  or  trans(a) * x = b
c     using the factors computed by dgeco or dgefa.
c
c     on entry
c
c        a       double precision(lda, n)
c                the output from dgeco or dgefa.
c
c        lda     integer
c                the leading dimension of the array  a .
c
c        n       integer
c                the order of the matrix  a .
c
c        ipvt    integer(n)
c                the pivot vector from dgeco or dgefa.
c
c        b       double precision(n)
c                the right hand side vector.
c
c        job     integer
c                = 0         to solve  a*x = b ,
c                = nonzero   to solve  trans(a)*x = b  where
c                            trans(a)  is the transpose.
c
c     on return
c
c        b       the solution vector  x .
c
c     error condition
c
c        a division by zero will occur if the input factor contains a
c        zero on the diagonal.  technically this indicates singularity
c        but it is often caused by improper arguments or improper
c        setting of lda .  it will not occur if the subroutines are
c        called correctly and if dgeco has set rcond .gt. 0.0
c        or dgefa has set info .eq. 0 .
c
c     to compute  inverse(a) * c  where  c  is a matrix
c     with  p  columns
c           call dgeco(a,lda,n,ipvt,rcond,z)
c           if (rcond is too small) go to ...
c           do 10 j = 1, p
c              call dgesl(a,lda,n,ipvt,c(1,j),0)
c        10 continue
c
c     linpack. this version dated 08/14/78 .
c     cleve moler, university of new mexico, argonne national lab.
c
c     subroutines and functions
c
c     blas daxpy,ddot
c
c     internal variables
c
    """
    
    #double precision ddot,t
    #integer k,kb,l,nm1
    
    #c
    nm1 = n - 1
    if (job == 0):
        #c
        #c        job = 0 , solve  a * x = b
        #c        first solve  l*y = b
        #c
        if (nm1 >= 1):
              
            for k in range(nm1):
                l = ipvt[k]
                t = b[l]
                if (l != k):
                    #print("DGESL if triggered")
                    b[l] = b[k]
                    b[k] = t
                #print("DGESL 1: l ", l, " k, ", k, " b ", b[k])

                #FORTRAN call call daxpy(n-k, t, a[k+1][k], 1, b[k+1], 1)
                #5th parameter is in/out:
                #b[k+1] = daxpy(n-k, t, a[k+1][k], 1, b[k+1], 1)
                #[b[kk+1] for kk in range(k, n)] = daxpy(n-k, t,\
                # [a[k+1][kk] for kk in range(k, n)], 1, [b[kk+1] for kk in range(k, n)], 1)
                daxpyOut =\
                Daxpy.daxpy(n-k-1, t, [a[kk][k] for kk in range(k+1, n)], 1, [b[kk] for kk in range(k+1, n)], 1)
                daxpyCount = 0
                for kk in range(k+1, n):
                    b[kk] = daxpyOut[daxpyCount]
                    daxpyCount+=1
                #print("DGESL 2: k ", k, " b ", b[k])
                #scipy: b[k+1] = daxpy(t, a[k+1][k], n-k, 1, 1)
        
          #c
          #c        now solve  u*x = y
          #c
        #print("DGESL: Before 2nd DAXPY call n ", n)
        for kb in range(n):
            #k = n + 1 - kb
            k = (n-1) - kb
            #print("DGESL: kb ", kb, " k ", k, " b ", b[k], " a ", a[k][k])
            b[k] = b[k]/a[k][k]
            t = -b[k]
            #FORTRAN call: call daxpy(k-1, t, a[1][k], 1, b[1], 1)
            #b[1] = daxpy(k-1, t, a[1][k], 1, b[1], 1)
            #[b[kk] for kk in range(1, k)] = daxpy(k-1, t,\
            # [a[1][kk] for kk in range(1, k)], 1, [b[kk] for kk in range(1, k)], 1)
            #print("DGESL: Before DAPXPY 2:")
            #print("a ", [a[kk][k] for kk in range(0, k+1)])
            #print("b ", [b[kk] for kk in range(0, k+1)])
            daxpyOut =\
            Daxpy.daxpy(k, t, [a[kk][k] for kk in range(0, k+1)], 1, [b[kk] for kk in range(0, k+1)], 1)
            daxpyCount = 0
            for kk in range(0, k+1):
                b[kk] = daxpyOut[daxpyCount]
                daxpyCount+=1 
            #print("DGESL: After DAPXPY 2:")
            #print("b ", [b[kk] for kk in range(0, k+1)])             
            #scipy: b[0] = daxpy(t, a[0][k], k-1, 1, 1)
              
          # **** goto 100 !!!  Oh-oh!!
          
    #c
    #c        job = nonzero, solve  trans(a) * x = b
    #c        first solve  trans(u)*y = b
    #c
    
    if (job != 0):
        
        for k in range(n):
            #t = ddot(k-1, a[1][k], 1, b[1], 1)
            t = Ddot.ddot(k, [a[kk][k] for kk in range(0, k)],\
                             1, [b[kk] for kk in range(0, k)], 1)
            b[k] = (b[k] - t)/a[k][k]
            #print("DDOT 1: t ", t)
        
            #c
            #c        now solve trans(l)*x = y
            #c
        if (nm1 >= 1):
            for kb in range(nm1):
                #k = n - kb
                k = n - kb - 1
                #b[k] = b[k] + ddot(n-k, a[k+1][k], 1, b[k+1], 1)
                b[k] = b[k] + Ddot.ddot(n-k, [a[kk][k] for kk in range(k, n)],\
                  1, [b[kk] for kk in range(k, n)], 1)
                #print("DDOT 2: t ", t)
                l = ipvt[k]
                if (l != k):
                    t = b[l]
                    b[l] = b[k]
                    b[k] = t

    return b