# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:04:33 2019

@author: 
"""

#Try this
#global pi, sbcon, kbol, cvel, gcon, hpl, hmass, t0, everg #/consts/
global kbol, hmass, t0 #/consts/
global name, ip, comp, awt, nspec, natom, itab, ntab, indx, iprint, gsinit, print0 #/gasp/
global ipr, nch, nel, ntot, nat, zat, neut, idel, indsp, indzat, iat, natsp, iatsp #/gasp2/
global nlin1, lin1, linv1, nlin2, lin2, linv2 #/lin/
#global xg,wtrp,dfflag,fqhead,nxg,ixgp,nxgp,iper #/fqgrid/
#global msol,lsol,rsol #/solar/
#global nit,nmit,itcon,mitcon,jtcorr,outfg #/iters/
#global nblock,nline #/output/
#global epsper,ftlim,fplim,frlim,restol,updatj,updatx, aconv,taups,irfact,ipverb,itaups #/flags/
#global chix, nix, nopac, ixa, ixn, opinit, opflag, opchar, iopt #/opacty
global chix, nix, ixa, ixn #/opacty

#pi = 3.1415926536e0
#sbcon = 5.66956e-5
kbol = 1.3806e-16
#cvel = 2.997925e+10
#gcon = 6.670e-8
#hpl = 6.62620e-27
hmass = 1.66053e-24
t0 = 5039.93e0
#everg = 1.60219e-12
     
#c
ip = [0.0e0 for i in range(150)]
comp = [0.0e0 for i in range(40)]
awt = [0.0e0 for i in range(150)]
      
#itab = [0 for i in range(83)]
#ntab = [0 for i in range(5)]
indx = [ [ [ [ [149 for i in range(2)] for j in range(5) ] for k in range(7) ] for l in range(26) ] for m in range(4) ]    
     
name = [' ' for i in range(150)]
    
#gsinit = False
#print0 = False
gsinit = True
print0 = False
    
#common /gasp/ name,ip,comp,awt,nspec,natom,itab,ntab,indx,
     #    iprint,gsinit,print0
"""
itab = [2,  8,  0,  0,  0,  3,  4,  5,  0,  9,\
        10, 11, 12, 13,  0,  6,  7,  0, 14, 15,\
        16, 17, 18, 19, 20, 21, 22, 23,  0,  0,\
        0,  0,  0,  0,  0,  0,  0, 24, 25, 26,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0] 
"""
itab = [1,  7,  0,  0,  0,  2,  3,  4,  0,  8,\
        9,  10, 11, 12, 0,  5,  6,  0, 13, 14,\
        15, 16, 17, 18, 19, 20, 21, 22,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  23, 24, 25,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
        0,  0,  0] 

#ntab = [4, 26, 7, 5, 2]
ntab = [3, 25, 6, 4, 1]


#c
ipr = [0 for i in range(150)]
nch = [0 for i in range(150)]
nel = [0 for i in range(150)]
ntot = [0 for i in range(150)]
nat = [ [0 for i in range(150)] for j in range(5) ]
zat = [ [0 for i in range(150)] for j in range(5) ]
neut = [0 for i in range(150)]
idel = [0 for i in range(150)]
#indsp = [0 for i in range(40)]
#indzat = [0 for i in range(100)]
#iat = [0 for i in range(150)]
natsp = [0 for i in range(40)]
iatsp = [ [0 for i in range(40)] for j in range(40) ]
    
#common /gasp2/ ipr,nch,nel,ntot,nat,zat,neut,idel,indsp,
#    indzat,iat,natsp,iatsp

    
#iat = 150*40
#indsp = 40*150
#indzat = 100*40
iat = [39 for i in range(150)]
indsp = [149 for i in range(40)]
indzat = [39 for i in range(100)]
    
#c
lin1 = [0 for i in range(40)]
lin2 = [0 for i in range(40)]
linv1 = [0 for i in range(40)]
linv2 = [0 for i in range(40)]
    
#common /lin/ nlin1,lin1,linv1,nlin2,lin2,linv2
#c
#dfflag = [0.0e0 for i in range(120)]
#wtrp = [0.0e0 for i in range(120)]
#xg = [0.0e0 for i in range(120)]
#ixgp = [0 for i in range(120)]
    
"""
fqhead = ['' for i in range(120)]  
#common /fqgrid/ xg,wtrp,dfflag,fqhead,nxg,ixgp,nxgp,iper
nxg = 116
xg = [7.550, 7.050, 6.547, 6.545, 6.350, 6.159, 6.157, 5.940, 5.938, 5.600,\
      5.300, 5.000, 4.831, 4.829, 4.600, 4.400, 4.200, 3.972, 3.970, 3.800,\
      3.600, 3.401, 3.399, 3.200, 3.000, 2.896, 2.894, 2.800, 2.700, 2.600,\
      2.500, 2.450, 2.400, 2.350, 2.300, 2.250, 2.200, 2.150, 2.100, 2.050,\
      2.000, 1.960, 1.920, 1.880, 1.840, 1.800, 1.760, 1.720, 1.680, 1.640,\
      1.600, 1.560, 1.520, 1.480, 1.440, 1.400, 1.360, 1.330, 1.300, 1.270,\
      1.240, 1.210, 1.180, 1.150, 1.120, 1.009, 1.006, 1.003, 1.000, 0.980,\
      0.960, 0.940, 0.920, 0.900, 0.880, 0.860, 0.840, 0.820, 0.800, 0.780,\
      0.760, 0.740, 0.720, 0.700, 0.680, 0.660, 0.640, 0.620, 0.600, 0.580,\
      0.560, 0.540, 0.520, 0.500, 0.480, 0.460, 0.440, 0.420, 0.400, 0.380,\
      0.360, 0.340, 0.320, 0.300, 0.280, 0.260, 0.240, 0.220, 0.200, 0.180,\
      0.160, 0.140, 0.120, 0.100, 0.080, 0.060]
#c
    
#common /solar/ msol,lsol,rsol
msol = 1.989e+33
lsol = 3.826e+33
rsol = 6.9599e+10
    
#c
#common /iters/  nit,nmit,itcon,mitcon,jtcorr,outfg
nit = 0
nmit = 0
itcon = False
mitcon = False
jtcorr = False
outfg = False
    
#c
#common /output/ nblock,nline

nblock = 10
nline = 1
    
    
#c
#common /flags/ epsper,ftlim,fplim,frlim,restol,updatj,updatx,
#    aconv,taups,irfact,ipverb,itaups
irfact = 0
epsper = 1.0e-4
restol = 1.0e-6
updatj = 0.0e0
updatx = 0.0e0
ftlim = 0.10e0
fplim = 0.10e0
frlim = 0.10e0
aconv = 1.6e0
taups = 6.66667e-01
ipverb = 2
"""
#c
    
#chix = ['' for i in range(70)]
#opchar = ['' for i in range(25)]
#opch1 = ['' for i in range(18)]
#opch2 = ['' for i in range(7)]
    
#******
#
#I don't know what we do about this FORTRAN "equivalence"...
#equivalence (opch1(1),opchar(1)),(opch2(1),opchar(19))
#
#
#*******
    
#opflag = [False for i in range(25)]
    
#common /opacty/ chix,nix,nopac,ixa,ixn,opinit,opflag,opchar,iopt
#c
#c Initialize block of flags and control parameters.
#c
#c  The list of species for which partial pressures are
#c  explicitly referenced (for opacity calculations and general
#c  interest) are defined by the array IXA below. These are:
#c
#c    1. H      2. H+     3. H-     4. H2     5. H2+    6. He
#c    7. He+    8. C      9. C+    10. N     11. N+    12. O
#c   13. O+    14. Ne    15. Na    16. Na+   17. Mg    18. Mg+
#c   19. Mg++  20. Al    21. Al+   22. Si    23. Si+   24. S
#c   25. S+    26. K     27. K+    28. Ca    29. Ca+   30. Ca++
#c   31. Ti    32. Ti+   33. V     34. V+    35. Fe    36. Fe+
#c   37. CO    38. N2    39. OH    40. H2O   41. SiO   42. TiO
#c   43. VO    44. CN    45. CH    46. NH    47. HCO   48. HCN
#c   49. C2H2  50. HS    51. MgH   52. AlH   53. SiH   54. CaH
#c   55. C2    56. C3    57. CS    58. SiS   59. SiC   60. SiC2
#c

nix = 60
#nopac = 23
#opinit = True
    
ixa = [ [0 for i in range(70)] for j in range(5) ]
ixn = [0 for i in range(70)]    

"""
ixaTranspose = [[2, 2,1,1,1],  [3, 2,1,1,1],  [1, 2,1,1,1],  [2, 2,2,1,1],\
                [3, 2,2,1,1],  [2, 8,1,1,1],  [3, 8,1,1,1],  [2, 3,1,1,1],\
                [3, 3,1,1,1],  [2, 4,1,1,1],  [3, 4,1,1,1],  [2, 5,1,1,1],\
                [3, 5,1,1,1],  [2, 9,1,1,1],  [2,10,1,1,1],  [3,10,1,1,1],\
                [2,11,1,1,1],  [3,11,1,1,1],  [4,11,1,1,1],  [2,12,1,1,1],\
                [3,12,1,1,1],  [2,13,1,1,1],  [3,13,1,1,1],  [2, 6,1,1,1],\
                [3, 6,1,1,1],  [2,14,1,1,1],  [3,14,1,1,1],  [2,15,1,1,1],\
                [3,15,1,1,1],  [4,15,1,1,1],  [2,17,1,1,1],  [3,17,1,1,1],\
                [2,18,1,1,1],  [3,18,1,1,1],  [2,21,1,1,1],  [3,21,1,1,1],\
                [2, 5,3,1,1],  [2, 4,4,1,1],  [2, 5,2,1,1],  [2, 5,2,2,1],\
                [2,13,5,1,1],  [2,17,5,1,1],  [2,18,5,1,1],  [2, 4,3,1,1],\
                [2, 3,2,1,1],  [2, 4,2,1,1],  [2, 5,3,2,1],  [2, 4,3,2,1],\
                [2, 3,3,2,2],  [2, 6,2,1,1],  [2,11,2,1,1],  [2,12,2,1,1],\
                [2,13,2,1,1],  [2,15,2,1,1],  [2, 3,3,1,1],  [2, 3,3,3,1],\
                [2, 6,3,1,1],  [2,13,6,1,1],  [2,13,3,1,1],  [2,13,3,3,1]]
"""
ixaTranspose = [[1, 1,0,0,0],  [2, 1,0,0,0],  [0, 1,0,0,0],  [1, 1,1,0,0],\
                [2, 1,1,0,0],  [1, 7,0,0,0],  [2, 7,0,0,0],  [1, 2,0,0,0],\
                [2, 2,0,0,0],  [1, 3,0,0,0],  [2, 3,0,0,0],  [1, 4,0,0,0],\
                [2, 4,0,0,0],  [1, 8,0,0,0],  [1, 9,0,0,0],  [2, 9,0,0,0],\
                [1,10,0,0,0],  [2,10,0,0,0],  [3,10,0,0,0],  [1,11,0,0,0],\
                [2,11,0,0,0],  [1,12,0,0,0],  [2,12,0,0,0],  [1, 5,0,0,0],\
                [2, 5,0,0,0],  [1,13,0,0,0],  [2,13,0,0,0],  [1,14,0,0,0],\
                [2,14,0,0,0],  [3,14,0,0,0],  [1,16,0,0,0],  [2,16,0,0,0],\
                [1,17,0,0,0],  [2,17,0,0,0],  [1,20,0,0,0],  [2,20,0,0,0],\
                [1, 4,2,0,0],  [1, 3,3,0,0],  [1, 4,1,0,0],  [1, 4,1,1,0],\
                [1,12,4,0,0],  [1,16,4,0,0],  [1,17,4,0,0],  [1, 3,2,0,0],\
                [1, 2,1,0,0],  [1, 3,1,0,0],  [1, 4,2,1,0],  [1, 3,2,1,0],\
                [1, 2,2,1,1],  [1, 5,1,0,0],  [1,10,1,0,0],  [1,11,1,0,0],\
                [1,12,1,0,0],  [1,14,1,0,0],  [1, 2,2,0,0],  [1, 2,2,2,0],\
                [1, 5,2,0,0],  [1,12,5,0,0],  [1,12,2,0,0],  [1,12,2,2,0]]
    
for i in range(5):
    for j in range(60):
        ixa[i][j] = ixaTranspose[j][i]
            

            
chix = ['H       ','H+      ','H-      ','H2      ',\
        'H2+     ','He      ','He+     ','C       ',\
        'C+      ','N       ','N+      ','O       ',\
        'O+      ','Ne      ','Na      ','Na+     ',\
        'Mg      ','Mg+     ','Mg++    ','Al      ',\
        'Al+     ','Si      ','Si+     ','S       ',\
        'S+      ','K       ','K+      ','Ca      ',\
        'Ca+     ','Ca++    ','Ti      ','Ti+     ',\
        'V       ','V+      ','Fe      ','Fe+     ',\
        'CO      ','N2      ','OH      ','H2O     ',\
        'SiO     ','TiO     ','VO      ','CN      ',\
        'CH      ','NH      ','HCO     ','HCN     ',\
        'C2H2    ','HS      ','MgH     ','AlH     ',\
        'SiH     ','CaH     ','C2      ','C3      ',\
        'CS      ','SiS     ','SiC     ','SiC2    ']
    
"""
opch1 = ['Neutral H bound-free and free-free      ',\
         'H- ion bound-free and free-free         ',\
         'He- ion free-free                       ',\
         'H2- free-free                           ',\
         'H2+ bound-free and free-free            ',\
         'Neutral Si bound-free                   ',\
         'Neutral Mg bound-free                   ',\
         'Neutral Ca bound-free                   ',\
         'Neutral Al bound-free                   ',\
         'Neutral Na bound-free                   ',\
         'Neutral K bound-free                    ',\
         'Neutral C bound-free                    ',\
         'Neutral H Rayleigh scattering           ',\
         'Molecular H2 Rayleigh scattering        ',\
         'Neutral He Rayleigh scattering          ',\
         'Free electron scattering                ',\
         'Analytic opacity defined by TESTOPAC cmd',\
         'Grey hydrogen test opacity              ']
    
opch2 = ['CN red system (straight mean)           ',\
         'CO vibration-rotation                   ',\
         'H2O vibration-rotation (straight mean)  ',\
         'H2O vibration-rotation (harmonic mean)  ',\
         'TiO electronic (straight mean)          ']
"""

