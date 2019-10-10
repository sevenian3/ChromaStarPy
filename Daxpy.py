# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:38:28 2019

@author:
"""
import math

"""
*> \brief \b DAXPY
*
*  =========== DOCUMENTATION ===========
*
* Online html documentation available at
*            http://www.netlib.org/lapack/explore-html/
*
*  Definition:
*  ===========
*
*       SUBROUTINE DAXPY(N,DA,DX,INCX,DY,INCY)
*
*       .. Scalar Arguments ..
*       DOUBLE PRECISION DA
*       INTEGER INCX,INCY,N
*       ..
*       .. Array Arguments ..
*       DOUBLE PRECISION DX(*),DY(*)
*       ..
*
*
*> \par Purpose:
*  =============
*>
*> \verbatim
*>
*>    DAXPY constant times a vector plus a vector.
*>    uses unrolled loops for increments equal to one.
*> \endverbatim
*
*  Arguments:
*  ==========
*
*> \param[in] N
*> \verbatim
*>          N is INTEGER
*>         number of elements in input vector(s)
*> \endverbatim
*>
*> \param[in] DA
*> \verbatim
*>          DA is DOUBLE PRECISION
*>           On entry, DA specifies the scalar alpha.
*> \endverbatim
*>
*> \param[in] DX
*> \verbatim
*>          DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1
*)*abs( INCX ) )
*> \endverbatim
*>
*> \param[in] INCX
*> \verbatim
*>          INCX is INTEGER
*>         storage spacing between elements of DX
*> \endverbatim
*>
*> \param[in,out] DY
*> \verbatim
*>          DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1)*abs( INCY ) )
*> \endverbatim
*>
*> \param[in] INCY
*> \verbatim
*>          INCY is INTEGER
*>         storage spacing between elements of DY
*> \endverbatim
*
*  Authors:
*  ========
*
*> \author Univ. of Tennessee
*> \author Univ. of California Berkeley
*> \author Univ. of Colorado Denver
*> \author NAG Ltd.
*
*> \date November 2017
*
*> \ingroup double_blas_level1
*
*> \par Further Details:
*  =====================
*>
*> \verbatim
*>
*>     jack dongarra, linpack, 3/11/78.
*>     modified 12/3/93, array(1) declarations changed to array(*)
*> \endverbatim
*>
*  =====================================================================
"""
#SUBROUTINE daxpy(N,DA,DX,INCX,DY,INCY)
def daxpy(n, da, dx, incx, dy, incy):
    """
*
*  -- Reference BLAS level1 routine (version 3.8.0) --
*  -- Reference BLAS is a software package provided by Univ. of
*  Tennessee,    --
*  -- Univ. of California Berkeley, Univ. of Colorado Denver and NAG
*  Ltd..--
*     November 2017
*
    """
    #*     .. Scalar Arguments ..
    #DOUBLE PRECISION DA
    #INTEGER INCX,INCY,N
    #*     ..
    #*     .. Array Arguments ..
    #DOUBLE PRECISION DX(*),DY(*)
    #dySize = 1 + (n-1)*abs(incy)
    #dyOut = [0.0e0 for i in range(dySize)]
    #*     ..
    #*
    #*  =====================================================================
    #*
    #*     .. Local Scalars ..
    #INTEGER I,IX,IY,M,MP1
    i = 0
    ix = 0
    iy = 0
    m = 0
    mp1 = 0
    #*     ..
    #*     .. Intrinsic Functions ..
    #INTRINSIC mod
    #*     ..
    #IF (n.LE.0) RETURN
    #IF (da.EQ.0.0d0) RETURN
    if ( (n > 0) and (da != 0.0e0) ):
      
        #IF (incx.EQ.1 .AND. incy.EQ.1) THEN
        if ( (incx == 1) and (incy == 1) ): 
            #*
            #*        code for both increments equal to 1
            #*
            #*
            #*        clean-up loop
            #*
            m = n % 4
            #IF (m.NE.0) THEN
            if (m != 0):
            
                #DO i = 1,m
                for i in range(m):
                
                    dy[i] = dy[i] + da*dx[i]
            
                #END DO
                
            #END IF
            
            #IF (n.LT.4) RETURN
            if (n >= 4):
                
                mp1 = m + 1
                
                #DO i = mp1,n,4
                #print("DAXPY: n ", n, " m ", m, " mp1 ", mp1, " da ", da)                
                for i in range(mp1-1, n, 4):
                    #print("DAXPY 2: i ", i, " dx(i... i+4) ",\
                    #      dx[i], dx[i+1], dx[i+2], dx[i+3])
                    #print("DAXPY 2: i ", i, " dy(i... i+3) ",\
                    #      dy[i], dy[i+1], dy[i+2], dy[i+3])                    
                    dy[i] = dy[i] + da*dx[i]
                    dy[i+1] = dy[i+1] + da*dx[i+1]
                    dy[i+2] = dy[i+2] + da*dx[i+2]
                    dy[i+3] = dy[i+3] + da*dx[i+3]
                    #print("DAXPY 3: i ", i, " dy(i... i+3) ",\
                    #      dy[i], dy[i+1], dy[i+2], dy[i+3])                    
                #END DO
        else:
            #*
            #*        code for unequal increments or equal increments
            #*          not equal to 1
            #*
            ix = 1
            iy = 1
            if (incx < 0):
                ix = ((-1*n)+1)*incx + 1
            if (incy < 0):
                iy = ((-1*n)+1)*incy + 1
            for i in range(n):
                #print("DAXPY 4: iy ", iy, " dy ", dy[iy],\
                #     " ix ", ix, " dx ", dx[ix])
                dy[iy] = dy[iy] + da*dx[ix]
                #print("DAXPY 5: iy ", iy, " dy ", dy[iy],\
                #      " ix ", ix, " dx ", dx[ix])                
                ix = ix + incx
                iy = iy + incy
         
      
      
    return dy
      
