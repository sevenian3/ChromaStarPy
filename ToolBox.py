# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:41:24 2017

Collection of useful utilities

@author: ishort
"""

import math

def interpol(x, y, newX): 

    """Linear interpolation to a new abscissa """
    
    #// Bracket newX:
    p1 = 0 
    p2 = 1
    x1 = x[p1]
    x2 = x[p2]

    for i in range(1, len(x)):
        if (x[i] >= newX): 
            #// Found upper bracket
            p2 = i
            p1 = i - 1
            x2 = x[p2]
            x1 = x[p1]
            break
            
        

    step = x2 - x1

    #//Interpolate
    #//First order Lagrange formula
    #//   newY = y[1][p2] * (newX - x1) / step
    #//           + y[1][p1] * (x2 - newX) / step;
    
    newY = y[p2] * (newX - x1) / step  \
    + y[p1] * (x2 - newX) / step

    #//System.out.println("Interpol: p1, p2, x1, x2, y1, y2, newX, newY: " + 
    #//        p1 + " " + p2 + " " + x1 + " " + x2 + " " + y[1][p1] + " " + y[1][p2] + " " + newX + " " + newY + " ");
    return newY


def interpolV(y, x, newX):

    """vectorized version of simple linear 1st order interpolation
    Caution: Assumes new and old abscissae are in monotonic increasing order"""
    
    num = len(x)
    #if (num != len(y)):
        #//System.out.println("Toolbox.interpolV(): Old x and y must be same length");  
        
    newNum = len(newX)
    #//System.out.println("interpolV: newNum " + newNum + " num " + num); 
    #newY = [0.0 for i in range(newNum)]

#//Renormalize ordinates:
    
    iMinAndMax = minMax(y)
    norm = y[iMinAndMax[1]]
    #//System.out.println("norm " + norm);
    #yNorm = [0.0 for i in range(num)]
    newYNorm = [0.0 for i in range(newNum)] 
    #for i in range(num):
    #    yNorm[i] = y[i] / norm 
    yNorm = [ x / norm for x in y ]

#// Set any newX elements that are *less than* the first x element to th first 
#// x element - "0th order extrapolation"
#//
    start = 0
    for i in range(newNum):
        if (newX[i] <= x[1]):
            newYNorm[i] = yNorm[0]
            start += 1
            
        if (newX[i] > x[1]):
            break
            
        
#//System.out.println("start " + start);
#//System.out.println("x[0] " + x[0] + " x[1] " + x[1] + " newX[start] " + newX[start]);
#double jWght, jm1Wght, denom;


    if (start < newNum-1):

        j = 1 #//initialize old abscissae index
        #//outer loop over new abscissae
        for i in range(start, newNum):

            #//System.out.println("i " + i + " j " + j);

#// break out if current element newX is *greater* that last x element
            if ( (newX[i] > x[num-1]) or (j > (num-1)) ):
                break 
            

            while (x[j] < newX[i]): 
                j += 1
            
            #//System.out.println("i " + i + " newX[i] " + newX[i] + " j " + j + " x[j-1] " + x[j-1] + " x[j] " + x[j]);
            #//1st order Lagrange method:
            jWght = newX[i] * (1.0 - (x[j-1]/newX[i])) #//(newX[i]-x[j-1])
            jm1Wght = x[j] * (1.0 - (newX[i]/x[j])) #//(x[j]-newX[i])
            denom = x[j] * (1.0 - (x[j-1]/x[j])) #//(x[j]-x[j-1])
            jWght = jWght / denom
            jm1Wght = jm1Wght / denom
            #//newYNorm[i] = (yNorm[j]*(newX[i]-x[j-1])) + (yNorm[j-1]*(x[j]-newX[i]));
            newYNorm[i] = (yNorm[j]*jWght) + (yNorm[j-1]*jm1Wght)
            #//System.out.println("i " + i + " newYNorm[i] " + newYNorm[i] + " j " + j + " yNorm[j-1] " + yNorm[j-1] + " yNorm[j] " + yNorm[j]);
        

#// Set any newX elements that are *greater than* the first x element to the last 
#// x element - "0th order extrapolation"
#//
    for i in range(newNum):
        if (newX[i] >= x[num-1]):
            newYNorm[i] = yNorm[num-1]
            
            

    #//Restore orinate scale
    #for i in range(newNum):
    #    newY[i] = newYNorm[i] * norm 
    newY = [ x * norm for x in newYNorm ]


    return newY

def lamPoint(numLams, lambdas, lam):

    """Return the array index of the wavelength array (lambdas) closest to a desired
     value of wavelength (lam)"""
    
    help = [0.0 for i in range(numLams)]
    for i in range(numLams):

        help[i] = lambdas[i] - lam;
        help[i] = abs(help[i]);

        
    index = 0
    min = help[index]

    for i in range(1, numLams):

        if (help[i] < min): 
            min = help[i]
            index = i

    return index

def minMax(x): 
    
    """Return the minimum and maximum values of an input 1D array CAUTION; Will
  return the *first* occurence if min and/or max values occur in multiple
  places iMinMax[0] = first occurence of minimum iMinMax[1] = first occurence
  of maximum"""

    iMinMax = [0 for i in range(2)]

    num = len(x)
    #//System.out.println("MinMax: num: " + num);

    iMin = 0
    iMax = 0
    min = x[iMin]
    max = x[iMax]

    for i in range(1, num):

        #//System.out.println("MinMax: i , current min, x : " + i + " " + min + " " + x[i]);
        if (x[i] < min): 
            #//System.out.println("MinMax: new min: if branch triggered" );
            min = x[i]
            iMin = i
            
        #//System.out.println("MinMax: new min: " + min);

        if (x[i] > max): 
            max = x[i]
            iMax = i
            

        
    #//System.out.println("MinMax: " + iMin + " " + iMax);

    iMinMax[0] = iMin
    iMinMax[1] = iMax

    return iMinMax

def minMax2(x): 
    
    """Version of MinMax.minMax for 2XnumDep & 2XnumLams arrays where row 0 is
  linear and row 1 is logarithmic
 
  Return the minimum and maximum values of an input 1D array CAUTION; Will
  return the *first* occurence if min and/or max values occur in multiple
  places iMinMax[0] = first occurence of minimum iMinMax[1] = first occurence
  of maximum"""

    iMinMax = [0 for i in range(2)]
    num = len(x)[0]

    iMin = 0
    iMax = 0

    #// Search for minimum and maximum in row 0 - linear values:
    min = x[0][iMin]
    max = x[0][iMax]

    for i in range(1, num):

        if (x[0][i] < min): 
            min = x[0][i]
            iMin = i
            

        if (x[0][i] > max): 
            max = x[0][i]
            iMax = i
            
    iMinMax[0] = iMin
    iMinMax[1] = iMax

    return iMinMax

def tauPoint(numDeps, tauRos, tau): 
    
    """Return the array index of the optical depth arry (tauRos) closest to a
  desired value of optical depth (tau) Assumes the use wants to find a *lienar*
  tau value , NOT logarithmic"""

    #int index;

    help = [0.0 for i in range(numDeps)]

    for i in range(0, numDeps):

        help[i] = tauRos[0][i] - tau
        help[i] = abs(help[i])

        
    index = 0
    min = help[index]

    for i in range(1, numDeps):

        if (help[i] < min): 
            min = help[i]
            index = i
                    

    return index





