# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:32:00 2019

@author:  Phil Bennett 
- ported to python and integrated with ChromaStarPy (CSPy) by Ian Short  
"""

#FORTRAN unit 4 with data about species to include:
# No! import Fort4

#import Documents.ChromaStarPy.GAS.BlockData
import CSBlockData
import CSGasData   # with H2O - causes problems
#import GasData2   # Without H2O
#from ..GAS.BlockData import *
#from ..GAS.GasData import *


def gsread(cname, eheu):
    
    #print("GsRead called")
    
    #Try this:
    global name, ip, comp, awt, nspec, natom, itab, ntab, indx, iprint, gsinit, print0 #/gasp/
    global ipr, nch, nel, ntot, nat, zat, neut, idel, indsp, indzat, iat, natsp, iatsp #/gasp2/
    global nlin1, lin1, linv1, nlin2, lin2, linv2 #/lin/
    global logk, logwt, it, kt, type0 #equil
    #global chix, nix, nopac, ixa, ixn, opinit, opflag, opchar, iopt #/opacty/  
    global chix, nix, ixa, ixn #/opacty/
    
    outString = ""
    
    #BlockData.block_data()
    
    #ip = [0.0e0 for i in range(150)]
    ip = CSGasData.ip
    #ip = GasData2.ip
    #comp = [0.0e0 for i in range(40)]
    comp = CSGasData.comp
    #comp = GasData2.comp
    name = CSGasData.name
    #name = GasData2.name
    

    
    #awt = [0.0e0 for i in range(150)]
    awt = CSGasData.awt
    #awt = GasData2.awt
    
    #itab = [0 for i in range(83)]
    itab = CSBlockData.itab
    #ntab = [0 for i in range(5)]
    ntab = CSBlockData.ntab
    #indx = [ [ [ [ [0 for i in range(2)] for j in range(5) ] for k in range(7) ] for l in range(26) ] for m in range(4) ]
    indx = CSBlockData.indx

    #name = [' ' for i in range(150)]
    #name = BlockData.name
    
    #gsinit = False
    #print0 = False
    print0 = CSBlockData.print0
    
    #ipr = [0 for i in range(150)]
    ipr = CSGasData.ipr
    #ipr = GasData2.ipr
    #nch = [0 for i in range(150)]
    nch = CSGasData.nch
    #nch = GasData2.nch
    #nel = [0 for i in range(150)]
    nel = CSGasData.nel
    #nel = GasData2.nel
    #ntot = [0 for i in range(150)]
    ntot = CSBlockData.ntot
    #nat = [ [0 for i in range(150)] for j in range(5) ]
    nat = CSGasData.nat
    #nat = GasData2.nat
    #zat = [ [0 for i in range(150)] for j in range(5) ]
    zat = CSGasData.zat
    #zat = GasData2.zat
    #neut = [0 for i in range(150)]
    neut = CSBlockData.neut
    #idel = [0 for i in range(150)]
    idel = CSBlockData.idel
    #indsp = [0 for i in range(40)]
    indsp = CSBlockData.indsp
    
    #indzat = [0 for i in range(100)]
    indzat = CSBlockData.indzat
    #iat = [0 for i in range(150)]
    iat = CSBlockData.iat
    #natsp = [0 for i in range(40)]
    natsp = CSBlockData.natsp
    #iatsp = [ [0 for i in range(40)] for j in range(40) ]
    iatsp = CSBlockData.iatsp
      
    #lin1 = [0 for i in range(40)]
    lin1 = CSBlockData.lin1
    #lin2 = [0 for i in range(40)]
    lin2 = CSBlockData.lin2
    #linv1 = [0 for i in range(40)]
    linv1 = CSBlockData.linv1
    #linv2 = [0 for i in range(40)]
    linv2 = CSBlockData.linv2
    
   
    
    #logk = [ [0.0e0 for i in range(150)] for j in range(5) ]
    #logwt = [0.0e0 for i in range(150)]
    logk = CSGasData.logk
    #logk = GasData2.logk
    logwt = CSGasData.logwt
    #logwt = GasData2.logwt
    it = [0.0e0 for i in range(150)]
    kt = [0.0e0 for i in range(150)]
    
    type0 = [0 for i in range(150)]
    
    #ixa = [ [0 for i in range(70)] for j in range(5) ]
    ixa = CSBlockData.ixa
    #ixn = [0 for i in range(70)]
    ixn = CSBlockData.ixn
    #chix = [' ' for i in range(70)]
    chix = CSBlockData.chix
    #opchar = [' ' for i in range(25)]
    #opflag = [False for i in range(25)]
    #opinit = False
    nix = CSBlockData.nix

    #gsline = ""
    #namet = ""
    iprt = 0
    ncht = 0
    #nnz = [0 for i in range(4)]
    ix = [0 for i in range(5)]
    
    #blank = ' '
    ename = 'e-'
    mxatom = 30
    mxspec = 150
    
    #c
    #c The first line specifies whether intermediate results are outputted.
    #c  iprint .eq. 0 - No.
    #c  iprint .ne. 0 - Yes.
    #c
    #with open("", 'r', encoding='utf-8') as inputHandle:
    #dataPath = "./"
    #inFile = dataPath + "fort.4"
    
    n = 0   #record counter
    np = 0
    natom = -1   #neutral atomic species counter
    nlin1 = -1
    nlin2 = -1
    tcomp = 0.0e0
    
    """
    with open(inFile, 'r') as inputHandle:
        
        
    gsline = inputHandle.readline()
    lineLength = len(gsline)
    #Should be only onen field, but to be on the safe side - assume iprint is first field:
    fields = gsline.split()
    iprint = int(fields[0].strip())
    #iprint = gsline.strip()
    """
    iprint = 0
#c
#c The first line specifies whether intermediate results are outputted.
#c  iprint .eq. 0 - No.
#c  iprint .ne. 0 - Yes.
#c
           
    if (iprint == 0):
        print0 = False
    else:
        print0 = True

    """
    lineLength = 1 #initialization
    #Get first line of data:
    gsline = inputHandle.readline()
    lineLength = len(gsline)
    """
    
    #nspec = len(name)
    #print("nspec ", nspec)
    while (name[n] != ' '):
    #for n in range(nspec):    
        #c
        #c Each following input line specifies a distinct chemical species.
        #c
    
    #1 
        """
        #print("1: gsline: ", gsline)
        namet = gsline[0:4].strip()
        iprt = int(gsline[4:6].strip())
        ncht = int(gsline[6:9].strip())
        #print("1: namet ", namet, " iprt ", iprt, " ncht ", ncht)
        """    
        #if (namet != blank):
        """
        n = n + 1
                
        if (n >= mxspec-1):
            print('(" *19 Error: Too many species specified. Limit is")', mxspec)
                    
        name[n] = namet
        ipr[n] = iprt #class (1, 2, or 3, p. 34-35 of P. Bennett M.Sc. thesis)
        nch[n] = ncht #electronic charge in fcu
        """
        #namet = name[n]
        iprt = ipr[n]
        ncht = nch[n]
        idel[n] = 1  
        #print("iprt ", iprt, " ncht ", ncht)
    #c
    #c Determine the species type:
    #c TYPE(N) = 1 --> Neutral atom
    #c         = 2 --> Neutral molecule
    #c         = 3 --> Negative ion
    #c         = 4 --> Positive ion
    #c
           
        if (nch[n] == 0):
#c
#c Species is neutral
#c
            np = n
            """
            nelt = int(gsline[9:11].strip())  
            nat1 = int(gsline[11:13].strip())
            zat1 = int(gsline[13:16].strip())
            #print("2: nelt ", nelt, " nat1 ", nat1, " zat1 ", zat1)
            nel[n] = nelt #no. of distinct elements in species
            nat[0][n] = nat1  #no. of recurrences of most numerous element in species
            zat[0][n] = zat1  #atomic number of heaviest element in species
            #print("GsRead: n ", n, " zat[0] ", zat[0][n])
            """
            nelt = nel[n]
            nat1 = nat[0][n]
            #zat1 = zat[0][n]
            #print("nch = 0 nelt ", nelt, " nat1 ", nat1)
        
            if (nelt <= 1 and nat1 <= 1):
#c
#c Neutral atom (one atom of single element Z present)
#c
                type0[n] = 1
                natom = natom + 1
                if (natom >= mxatom):
                    print('(" *20 Error: Too many elements specified.", "  Limit is")', mxatom)
              
        
                iat[n] = natom
                #print("Setting indsp, n: ", n, " natom ", natom)
                indsp[natom] = n  #pointer to iat[], etc....
                indzat[zat[0][n]-1] = natom   #indzat's index is atomic number - 1
                ntot[n] = 1
                neut[n] = n

                #awt[n] = float(gsline[16:23].strip()) #atomic weight in amu
                #comp[natom] = float(gsline[23:32].strip()) #abundance as N/N_H
                #print("3: n ", n, " awt ", awt[n], " comp ", comp[natom])
                    
                tcomp = tcomp + comp[natom]
                iprt = ipr[n]
                if (iprt == 1):
                    nlin1 = nlin1 + 1
                    lin1[natom] = nlin1
                    linv1[nlin1] = natom

                if ( (iprt == 1) or (iprt == 2) ):
                    nlin2 = nlin2 + 1
                    lin2[natom] = nlin2
                    linv2[nlin2] = natom
                        
            else:
                    
#c
#c Neutral molecule ( >1 atom present in species)
#c
                type0[n] = 2
                ntot[n] = nat1
                neut[n] = n
                
                nleft = (nelt - 1)*2
                #print("Neutral mol: n ", n, " name ", name[n], " nelt ", nelt, " nleft ", nleft)
                    
                if (nleft > 0):
                    """
                    nnz[0] = int(gsline[16:18].strip())
                    nnz[1] = int(gsline[18:21].strip())
                    nnzTest = gsline[21:23].strip()
                    if (nnzTest != ''):
                        nnz[2] = int(nnzTest)
                    else:
                        nnz[2] = 0
                    nnzTest = gsline[23:26].strip()
                    if (nnzTest != ''):
                        nnz[3] = int(nnzTest)
                    else:
                        nnz[3] = 0                            
                    #print("4: nnz ", nnz[0], " ", nnz[1], " ", nnz[2], " ", nnz[3])
        
                    for i in range(0, nleft, 2):
                        ii = int((i + 1)/2 + 1)
                        nat[ii][n] = nnz[i]
                        zat[ii][n] = nnz[i+1]
                        print("i ", i, " ii ", ii, " nat ", nat[ii][n], " zat ", zat[ii][n])
                        ntot[n] = ntot[n] + nat[ii][n]
                    """
                    for ii in range(1, 3):
                        ntot[n] = ntot[n] + nat[ii][n]
                
                """
                logk[0][n] = float(gsline[26:33].strip())
                logk[1][n] = float(gsline[33:41].strip())
                logk[2][n] = float(gsline[41:50].strip())
                logk[3][n] = float(gsline[50:62].strip())
                logk[4][n] = float(gsline[62:74].strip())
                """
            #print("5: n ", n, " logk ", logk[0][n], " ", logk[1][n], " ", logk[2][n], " ", logk[3][n], " ", logk[4][n])

        else:    
#c
#c Ionic species (nch .ne. 0)
#c
            
            if (np <= -1):
                print('(" *** error: ionic species encountered out of", " sequence")')
            
            if (ncht < 0):
                type0[n] = 3
            elif (ncht > 0):
                type0[n] = 4
          
            neut[n] = np
            nel[n] = nel[np]
            nelt = nel[n]
            for i in range(nelt):
                nat[i][n] = nat[i][np]
                zat[i][n] = zat[i][np]

            ntot[n] = ntot[np]
            #ip[n] = float(gsline[9:16].strip())   #ground state ionization potential (eV)
            #logwt[n] = float(gsline[16:23].strip())  #log partition fn??
#print("6: n ", n, " ip ", ip[n], " logwt ", logwt[n])
        
#c
#c Generate master array tying chemical formula of species to
#c its table index. A unique index is generated for a given
#c (possibly charged) species containing up to 4 atoms.
#c
#c Index #1 <--  Ionic charge + 2  (dim. 4, allows chg -1 to +2) 
#c       #2 <--> Index to Z of 1st atom in species (23 allowed Z)
#c       #3 <-->    "          2nd        "        ( 6 allowed Z)
#c       #4 <-->    "          3rd        "        ( 4 allowed Z)
#c       #5 <-->    "          4th        "        ( 1 allowed Z)
#c

        #ix[0] = nch[n] + 2
        ix[0] = nch[n] + 1
        nelt = nel[n]
        #k = 1
        k = 0
        
        #print("n ", n, " name ", name[n])
        for i in range(nelt):
                
            nats = nat[i][n]
            for j in range(nats):
                    
                k = k + 1
                if (k > 4):
                    print('(" *21 Error: species ",a8," contains > 4 atoms")', name[n])

                ix[k] = itab[zat[i][n]-1]
                #print("i ", i, " j ", j, " k ", k, " ix ", ix[k], "ntab ", ntab[k])
                #print("zat-1 ", zat[i][n]-1, "itab ", itab[zat[i][n]-1])
                if ( (ix[k] <= 0) or (ix[k] > ntab[k]) ):
                    print('(" *22 Error: species atom z= not in allowed element list")', name[n], zat[i][n]-1)

        if (k < 4):
            kp = k + 1
            for kk in range(kp, 5):
                ix[kk] = 0
            #print("kk ", kk, " ix ", ix[kk])
                

        indx[ix[0]][ix[1]][ix[2]][ix[3]][ix[4]] = n
        n = n + 1
            #print("n ", n, " name ", name[n], " ix ", ix[0], ix[1], ix[2], ix[3], ix[4],\
            #      " indx ", indx[ix[0]][ix[1]][ix[2]][ix[3]][ix[4]])
                    
    #go to 1
    #Ends if namet != ''??
        
    #Get next line of data and test of end-of-file:
    #gsline = inputHandle.readline()
    #lineLength = len(gsline)
            #print("lineLength = ", lineLength)
    #Ends file read loop "with open(infile...??)
        
    #After read loop:
    
#c
#c Normalize abundances such that SUM(COMP) = 1
#c
    nspec = n
    #name[nspec+1] = ename
    name[nspec] = ename
    iat[mxspec-1] = mxatom
    comp[mxatom-1] = 0.0e0
    neut[mxspec-1] = mxspec
    nsp1 = nspec + 1

    for n in range(nsp1-1, mxspec):
        idel[n] = 0
        
        
    #print("GsRead: nspec ", nspec, " natom ", natom)
    if (nspec != 0):
        
        for j in range(natom):
            natsp[j] = - 1
            comp[j] = comp[j]/tcomp

#c
#c Calculate the atomic (molecular) weight of each constituent
#c
        for n in range(nspec):
            
            #print("name ", name[n], " nel ", nel[n])
            nelt = nel[n]
            sum0 = 0.0e0
            iprt = ipr[n]
            
            for i in range(nelt):
                
                #print("i ", i, " n ", n, " zat ", zat[i][n]-1, " indzat ", indzat[zat[i][n]-1])
                j = indzat[zat[i][n]-1]
                #print("j ", j)
                nn = indsp[j]
                #print(" nn ", nn)
                natsp[j] = natsp[j] + 1
                iatsp[j][natsp[j]] = n
                sum0 = sum0 + nat[i][n]*awt[nn]
                if (ipr[nn] > iprt): 
                    iprt = ipr[nn]

            awt[n] = sum0
            ipr[n] = iprt
            
#c
#c Fill array of direct indices of species needed for opacity
#c calculations.
#c
        if (nix > 0):
            for i in range(nix):
                ixn[i] = indx[ixa[0][i]][ixa[1][i]][ixa[2][i]][ixa[3][i]][ixa[4][i]]
                if (ixn[i] == 149):
                    print('("0*** Warning: Opacity source ", " not included in GAS data tables")', chix[i])

        """
#c
#c Output species table
#c
        #print("I am here!")
        for j in range(1, 5):
            #outString = "j " + str(j) + "\n"
            #outFile.write(outString)
            if (j == 1):
                outString = "1 %5s %10s %8s %5s %7s\n" %("#", "Name", "At.Weight", "Z", "Abundance") 
                #outFile.write("1  #  Name      At.Weight   Z   Abundance\n")
                outFile.write(outString)
            elif (j == 2):
                outString = "0 %5s %10s %8s %5s" %("#", "Name", "At.Weight", "Nel")
                outString = outString + " n1   Z1   n2   Z2 ...\n"
                #outFile.write("0  #  Name      At.Weight Nel   n1   Z1   n2   Z2 ...\n")
                outFile.write(outString)
            elif (j == 3):
                outFile.write("0  #  Name      At.Weight Chg  Natom    I.P.   Log(2*g1/g0)\n")

            for i in range(nspec):
                ityp = type0[i]
                #outString = "i " + str(i) + " type " + str(type0[i]) + "\n"
                #outFile.write(outString)
                if (ityp == j):
                    if (ityp == 1):
                        ii = iat[i]
                        #print("i ", i, " iat ", iat[i])
                        #outString = str(i) + " " + str(name[i]) + " " + str(awt[i]) + " " + str(zat[0][i]) + " " + str(comp[ii]) + "\n"
                        outString = "%5d %10s %8.3f %5d %7.2e\n" %(i, name[i], awt[i], zat[0][i], comp[ii])
                        outFile.write(outString)
                    elif (ityp == 2):
                        nelt = nel[i]
                        #outString = str(i) + " " + str(name[i]) + " " + str(awt[i]) + " " + str(nelt) + "\n"
                        outString = "%5d %10s %8.3f %5d" %(i, name[i], awt[i], nelt)
                        #outFile.write(outString)
                        for k in range(nelt):
                            outString = outString + "  " + str(nat[k][i]) + "  " + str(zat[k][i])
                        outString += "\n"
                        outFile.write(outString)
                    else:
                        outString = "%5d %10s %8.3f %6d %6d %10.3f %7.3f\n" %(i, name[i], awt[i], nch[i], neut[i], ip[i], logwt[i])
                        #outString = str(i) + " " + str(name[i]) + " " + str(awt[i]) + " " + str(nch[i]) + " " + str(neut[i]) + " " + str(ip[i]) + " " + str(logwt[i]) + "\n"
                        outFile.write(outString)
        """
        # Replace Gas abundnaces with the ones from CSPy
        for i in range(natom):
            for j in range(len(cname)):
                if (name[i].strip() == cname[j].strip()):
                    comp[i] = 10.0**(eheu[j]-12.0)
        #cis: Try this:
        nlin1+=1
        nlin2+=1
        natom+=1

    return

       
        
    

