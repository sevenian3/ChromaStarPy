# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:41:34 2019

@author: 
"""

import math

"""
*> \brief \b IDAMAX
*
*  =========== DOCUMENTATION ===========
*
* Online html documentation available at
*            http://www.netlib.org/lapack/explore-html/
*
*  Definition:
*  ===========
*
*       INTEGER FUNCTION IDAMAX(N,DX,INCX)
*
*       .. Scalar Arguments ..
*       INTEGER INCX,N
*       ..
*       .. Array Arguments ..
*       DOUBLE PRECISION DX(*)
*       ..
*
*
*> \par Purpose:
*  =============
*>
*> \verbatim
*>
*>    IDAMAX finds the index of the first element having maximum
*absolute value.
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
*> \param[in] DX
*> \verbatim
*>          DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1
*)*abs( INCX ) )
*> \endverbatim
*>
*> \param[in] INCX
*> \verbatim
*>          INCX is INTEGER
*>         storage spacing between elements of SX
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
*> \ingroup aux_blas
*
*> \par Further Details:
*  =====================
*>
*> \verbatim
*>
*>     jack dongarra, linpack, 3/11/78.
*>     modified 3/93 to return if incx .le. 0.
*>     modified 12/3/93, array(1) declarations changed to array(*)
*> \endverbatim
*>
*  =====================================================================
"""

#INTEGER FUNCTION idamax(N,DX,INCX)
def idamax(n, dx, incx):
    
    #*
    #*  -- Reference BLAS level1 routine (version 3.8.0) --
    #*  -- Reference BLAS is a software package provided by Univ. of
    #*  Tennessee,    --
    #*  -- Univ. of California Berkeley, Univ. of Colorado Denver and NAG
    #*  Ltd..--
    #*     November 2017
    #*
    #*     .. Scalar Arguments ..
    #INTEGER INCX,N
    #*     ..
    #*     .. Array Arguments ..
    #DOUBLE PRECISION DX(*)
    #*     ..
    #*
    #*  =====================================================================
    #*
    #*     .. Local Scalars ..
    dmax = 0.0e0
    i = 0
    ix = 0

    #*     ..
    #*     .. Intrinsic Functions ..
    #INTRINSIC dabs
    #*     ..
    #idamax = 0
    returnValue = 0
      
    #IF (n.LT.1 .OR. incx.LE.0) RETURN
    if ( (n >= 1) and (incx > 0) ):
        
        #idamax = 1
        returnValue = 0
      
        #IF (n.EQ.1) RETURN
        if (n != 1):
      
            #IF (incx.EQ.1) THEN
            if (incx == 1):
                #*
                #*        code for increment equal to 1
                #*
                dmax = abs(dx[0])
                #print("dmax ", dmax)
                #DO i = 2,n
#                print("IDAMAX: n ", n)
                for i in range(1, n):
                    #IF (dabs(dx(i)).GT.dmax) THEN
                    #print("abs(dx[i]) ", abs(dx[i]))
                    if (abs(dx[i]) > dmax):
                        #idamax = i
                        #print("Condition triggered")
                        returnValue = i
                        dmax = abs(dx[i])
                    #print("i ", i, " dx ", dx[i], " returnValue ", returnValue)

            else:
                #*
                #*        code for increment not equal to 1
                #*
                #ix = 1
                print("Road not taken, right?")
                ix = 0
                dmax = abs(dx[0])
                ix = ix + incx
         
                #DO i = 2,n
                for i in range(1, n):
                    
                    #IF (dabs(dx(ix)).GT.dmax) THEN
                    if (abs(dx[ix]) > dmax):
                        #idamax = i
                        returnValue = i
                        dmax = abs(dx[ix])
            
                    ix = ix + incx
         
    
    #print("IDAMAX: ", returnValue)
    return returnValue
      
