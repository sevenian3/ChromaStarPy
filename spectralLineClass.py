# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:58:23 2017

@author: ishort
"""

class SpectralLine:
    
    """The spectral line class"""
    
    def __init__(self, lam0In = 500.0, fijIn = 0.100, AijIn = 1.0e8):
        
        self.lam0 = lam0In   #nm
        self.fij = fijIn
        self.Aij = AijIn
        
    def showLine(self):
        
        print("lam0 " + self.lam0 + " fij " + self.fij + " Aij " + self.Aij)
        
    def __str__(self):
        return ("({0}, {1}, {2})".format(self.lam0, self.fij, self.Aij))
        

thisLine = SpectralLine(393.34, 0.67, 1.0e10)

isinstance(thisLine, SpectralLine)
