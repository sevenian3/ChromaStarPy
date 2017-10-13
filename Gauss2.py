# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:29:34 2017

@author: ishort
"""

import math

""" procedure to generate Gaussian of unit area when passed a FWHM"""

        #IDL: PRO GAUSS2,FWHM,LENGTH,NGAUS
def gauss2(fwhm, length):

    #length=length*1l & FWHM=FWHM*1l
    #NGAUS=FLTARR(LENGTH)
    ngaus = [0.0 for i in range(length)]

#This expression for CHAR comes from requiring f(x=0.5*FWHM)=0.5*f(x=0):

    #CHAR=-1d0*ALOG(0.5d0)/(0.5d0*0.5d0*FWHM*FWHM)
    char = -1.0 * math.log(0.5) / (0.5*0.5*fwhm*fwhm)

#This expression for AMP (amplitude) comes from requiring that the
#area under the gaussian is unity:

    #AMP=SQRT(CHAR/PI)
    amp = math.sqrt(char/math.pi)

    #FOR CNT=0l,(LENGTH-1) DO BEGIN
    #   X=(CNT-LENGTH/2)*1.d0
    #   NGAUS(CNT)=AMP*EXP(-CHAR*X^2)
    #ENDFOR

    for cnt in range(length):
        x = 1.0 * (cnt - length/2)
        ngaus[cnt] = amp * math.exp(-1.0*char*x*x)
        
    return ngaus

        
