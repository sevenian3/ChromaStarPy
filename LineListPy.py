# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:07:45 2017

@author: ishort


/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2016 C. Ian Short
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */"""
 
import math
 
#// Argument 0: Name of ascii input line list
#// Argument 1: Name of byte data output line list
#asciiListStr = args[0]
#byteListStr = args[1]
asciiListStr = "atomLineListFeb2017"
byteListStr = "atomLineListFeb2017Bytes"

logE = math.log10(math.e) #// for debug output
logE10 = math.log(10.0) #//natural log of 10
#//
#//These atomic and molecular data are really just here for the human reader's
#// reference - they're not actually used by the code:
#////
#////Abundance table adapted from PHOENIX V. 15 input bash file
#////Solar abundances:
#//// c='abundances, Anders & Grevesse',
#//

nelemAbnd = 41
nome = [0 for i in range(nelemAbnd)]
cname = ["" for i in range(nelemAbnd)]
#//nome is the Kurucz code - in case it's ever useful
nome[0]=   100
nome[1]=   200
nome[2]=   300
nome[3]=   400
nome[4]=   500
nome[5]=   600
nome[6]=   700
nome[7]=   800
nome[8]=   900
nome[9]=  1000
nome[10]=  1100
nome[11]=  1200
nome[12]=  1300
nome[13]=  1400
nome[14]=  1500
nome[15]=  1600
nome[16]=  1700
nome[17]=  1800
nome[18]=  1900
nome[19]=  2000
nome[20]=  2100
nome[21]=  2200
nome[22]=  2300
nome[23]=  2400
nome[24]=  2500
nome[25]=  2600
nome[26]=  2700
nome[27]=  2800
nome[28]=  2900
nome[29]=  3000
nome[30]=  3100
nome[31]=  3600
nome[32]=  3700
nome[33]=  3800
nome[34]=  3900
nome[35]=  4000
nome[36]=  4100
nome[37]=  5600
nome[38]=  5700
nome[39]=  5500
nome[40]=  3200

cname[0]="H"
cname[1]="He"
cname[2]="Li"
cname[3]="Be"
cname[4]="B"
cname[5]="C"
cname[6]="N"
cname[7]="O"
cname[8]="F"
cname[9]="Ne"
cname[10]="Na"
cname[11]="Mg"
cname[12]="Al"
cname[13]="Si"
cname[14]="P"
cname[15]="S"
cname[16]="Cl"
cname[17]="Ar"
cname[18]="K"
cname[19]="Ca"
cname[20]="Sc"
cname[21]="Ti"
cname[22]="V"
cname[23]="Cr"
cname[24]="Mn"
cname[25]="Fe"
cname[26]="Co"
cname[27]="Ni"
cname[28]="Cu"
cname[29]="Zn"
cname[30]="Ga"
cname[31]="Kr"
cname[32]="Rb"
cname[33]="Sr"
cname[34]="Y"
cname[35]="Zr"
cname[36]="Nb"
cname[37]="Ba"
cname[38]="La"
cname[39]="Cs"
cname[40]="Ge"

#String species;


#//
#//     FILE I/O Section
#//
#//External line list input file approach:

dataPath = "./InputData/"
lineListFile = dataPath + asciiListStr + ".dat"


#//Put entire line list into one big string - we'll sort it out later
masterLineString = "" #//initialize
#may not need splitChar is we can split string on end-of-line character, "\n"
#splitChar = "%%" #//character separating new lines

#System.out.println(" *********************************************** ");
#System.out.println("  ");
#System.out.println("  ");
#System.out.println("BEFORE FILE READ");
#System.out.println("  ");
#System.out.println("  ");
#System.out.println(" *********************************************** ");

try:
    fHandle = open(lineListFile, 'r', encoding='utf-8')

    thisLine = fHandle.readline()
    masterLineString = masterLineString + thisLine
    while (thisLine != ""):
        thisLine = fHandle.readline()
        #masterLineString = masterLineString + splitChar + thisLine
        #may not need splitChar is we can split string on end-of-line character, "\n"
        masterLineString = masterLineString + thisLine
        
finally:
    fHandle.close()
        
#System.out.println(" *********************************************** ");
#System.out.println("  ");
#System.out.println("  ");
#System.out.println("AFTER FILE READ");
#System.out.println("  ");
#System.out.println("  ");
#System.out.println(" *********************************************** ");

#Split string on new line character "\n":
arrayLineString = masterLineString.split("\n") 
#//Number of lines MUST be the ONLY entry on the first line

numLineList = int(arrayLineString[0])
#//System.out.println("arrayLineString[0] " + arrayLineString[0]);
list2Length = len(arrayLineString) - 1 #//useful for checking if something's wrong?
#System.out.println("numLineList " + numLineList + " list2Length " + list2Length); 
#//        for (int i = 0; i < 5; i++){
#//           System.out.println(arrayLineString[i]);
#//        }

#// In general there will be header information.  The first block of six lines (blank separartor line
#//followed by five data lines) must be immediately preceded by a line whose first six columns contain 
#//the string "START:", followed by the correct pipe symbol ("|") separators  
  
startKey = "START:"
testField= ""
startLine = 1 #//initialization
for i in range(1, list2Length):
    #print("i " + i + " arrayLineString[i] " + arrayLineString[i]); 
    print(arrayLineString[i]) 
    #testField = arrayLineString[i].substring(0, 6);
    testField = arrayLineString[i][0:6]
    if (testField == startKey):
        break  #//We found it
                
    startLine+=1

#//  startLine++; //one more
#System.out.println("list2Length " + list2Length + " numLineList " + numLineList + " startLine " + startLine); 

#//// Find seven field separators ("|"):
#//int lastBound = 0; //initialization
#//int[] bounds = new int[7];
#//for (int i = 0; i < 7; i++){
#//   bounds[i] = arrayLineString[startLine].indexOf("|", lastBound);
#//   lastBound = bounds[i]+1;
#//   //System.out.println("i " + i + " bounds[i] " + bounds[i]);
#//   }


#//Okay, here we go:
print("numLineList ", numLineList)
#String list2Element; // = new String[numLineList]; //element
#String list2LogGammaCol; // = new double[numLineList];
#//Log of unitless oscillator strength, f 
#double list2Logf; // = new double[numLineList];
#//Einstein coefficinet for spontaneous de-excitation
#double list2LogAij; // = new double[numLineList];
#//Unitless statisital weight, lower E-level of b-b transition                 
#double list2GwL; // = new double[numLineList];

#//Atomic Data sources:
 

list2_ptr = 0 #//pointer into line list2 that we're populating
#int array_ptr; //pointer into array containing line list2 data file line-by-line Strings
    
#//First line in block of six is always a blank separator line:
numBlocks = int((list2Length - (startLine+1))/6) - 1
#// int rmndr = (list2Length - (startLine+1)) % 6
rmndr = 0 #//for now - something's wrong
#System.out.println("numBlocks " + numBlocks + " rmndr " + rmndr); 
#String myString, myStringUp, elName;  //useful helper
#double log10gf, Jnumer, Jdenom, Jfinal;
#int testLength, thisUpperBound;
#boolean blankFlag;

newField = " | " #//field separator - consistent with NIST ascii output 
newRecord = "%%" #//record separator
masterStringOut = "" #//initialize master string for output 
numFields = 12 #//number of "|"-separated INPUT fields in NIST ascii dump
#// Input filds:
#// 0: element + ion stage, 1: lambda_0, 2: A_ij, 3: f, 4: log(gf), 5: "Acc." - ??, 6: E_i - E_j, 7: J_i, 8: J_j
thisRecord = ["" for i in range(numFields)]
subFields = ["" for i in range(2)]

for iBlock in range(numBlocks):

    offset = startLine + 6 * iBlock + 1
    for i in range(1, 6):

        array_ptr = offset + i
        #//System.out.println("i " + i + " array_ptr " + array_ptr);
        #//System.out.println("arrayLineString " + arrayLineString[array_ptr]); 
        #//"|" turns out to mean something in regexp, so we need to escape with '\\':
        #//Get the chemical element symbol - we don't know if it's one or two characters
        thisRecord = arrayLineString[array_ptr].split("|") 

        #//
        #// "|"-separated field [0] is the species - element AND ion. stage
        #//
        testField = thisRecord[0]
        #//Contains both chemical symbol and ionization stage, so have to "sub-split":
        testField = testField.strip()
        subFields = testField.split(" ")
        myString = subFields[0]
        #//System.out.println("element " + myString);
        list2Element = myString.strip()
        masterStringOut = masterStringOut + list2Element + newField
        myString = subFields[1]
        #//System.out.println("ion " + myString.trim());
        #//list2StageRoman[list2_ptr] = myString.trim();
        masterStringOut = masterStringOut + myString.strip() + newField
        #//
        #// "|"-separated field [1] is wavelength in nm
        #//
        myString = thisRecord[1]
        #//We need to be ready for blank fields - checking for this in Java is hard!
        #//testLength = bounds[1] - bounds[0];
        blankFlag = True
        if (len(myString.strip()) > 0):
            blankFlag = False 
                 
        if (blankFlag):
            myString = " " 
        #// else { 
        #//  myString.trim();
        #//  list2Lam0[list2_ptr] = Double.parseDouble(myString);
        #// }
        #//System.out.println("lambda " + myString.trim());
        masterStringOut = masterStringOut + myString.strip() + newField
#//
#// "|"-separated field [2] is Einstein A_ij coeffcient for spontaneous de-excitation: 
#//
        myString = thisRecord[2];
        #//We need to be ready for blank fields - checking for this in Java is hard!
        #//testLength = bounds[1] - bounds[0];
        blankFlag = True
        if (len(myString.strip()) > 0):
            blankFlag = False 
                 
        if (blankFlag):
            myString = "-19.0" 
        else: 
            myString.strip()
            list2LogAij = math.log10(float(myString)) #//careful - base 10 log of f
            myString = str(list2LogAij)
             
        #//System.out.println("logAji " + myString.trim());
        masterStringOut = masterStringOut + myString.strip() + newField;
        #//
        #// "|"-separated field [3] is oscillator strength f_ij: 
        #//
        myString = thisRecord[3] 
        #//We need to be ready for blank fields - checking for this in Java is hard!
        #//testLength = bounds[3] - bounds[2];
        blankFlag = True
        if (len(myString.strip()) > 0):
            blankFlag = False 
                 
        if (blankFlag == True):
            list2Logf =  -9.0 #//careful - base 10 log of f
            myString = "-9.0" 
        else: 
            myString.strip()
            list2Logf = math.log10(float(myString)) #//careful - base 10 log of f
            myString = str(list2Logf)
             
            #//System.out.println("log(f) " + myString.trim());
        masterStringOut = masterStringOut + myString.strip() + newField
#////
#//// "|"-separated field [4] is log_10 gf_ij ("log gf") - 
#////
#//// Originally needed to recover "g_i" from f_ij and log(gf)
#////  - We may not need this anymore - latest line list has "g_i" values
#////
#//           //process this so we can back out the statistical weight, g_l of the lower E-level (heh-heh!)
#//           myString = thisRecord[4]; 
#//           //We need to be ready for blank fields - checking for this in Java is hard!
#//           //testLength = bounds[4] - bounds[3];
#//           blankFlag = true;
#//               if (myString.trim().length() > 0){
#//                  blankFlag = false; 
#//                 }
#//           if (blankFlag){
#//               list2GwL = 1.0; 
#//               myString = "1.0"; 
#//             } else { 
#//               myString.trim();
#//               log10gf = Double.parseDouble(myString); // log_10 of gf
#//               //Lower E level statistical weight
#//               list2GwL = 2.0 * ( Math.exp(log10gf - list2Logf) ); 
#//               list2GwL = (double) ( (int) list2GwL );
#//               myString = Double.toString(list2GwL);
#//             }
#//           //System.out.println("g_i " + myString.trim());
#//           masterStringOut = masterStringOut + myString.trim() + newField;
#//
#// "|"-separated field [5] is a quality control indicator 
#//
#//
#// "|"-separated field [6] is BOTH the Lower & Upper E-level excitation energy in eV 
#//
        testField = thisRecord[6] 
        #//System.out.println("list2Element " + list2Element + " testField " + testField + " testField.trim().length() " + testField.trim().length());
        #//testLength = bounds[6] - bounds[5];
        blankFlag = True
        #//for (int kk = 0; kk < testLength-2; kk++){
        #//testChar = testField.substring(kk, kk+2);
        testField = testField.strip()
        if (len(testField) > 0):
            blankFlag = False 
                 
        #//   }  
        if (blankFlag):
            myString = "0.0"
            myStringUp = "0.0"
            #//System.out.println("blankFlag triggered, myString = " + myString); 
        else:
            #// chi_L and chi_U separated by "-" - revise upper boundary to isolate chi_L:
            subFields = testField.split("-")
            myString = subFields[0].strip() #//lower E level 
            myStringUp = subFields[1].strip() #//upper E level 
            #//Some values are in square brackets ("[ ]"):
            sqbr1 = myString.find("[")
            if (sqbr1 != -1):
                sqbr2 = myString.find("]")
                myString = myString[sqbr1+1: sqbr2] 
                    
            sqbr1 = myStringUp.find("[")
            if (sqbr1 != -1):
                sqbr2 = myStringUp.find("]")
                myStringUp = myStringUp[sqbr1+1: sqbr2] 
                   
            #//Or it could be round brackets ("( )"):
            sqbr1 = myString.find("(")
            if (sqbr1 != -1):
                sqbr2 = myString.find(")")
                myString = myString[sqbr1+1: sqbr2] 
                   
            sqbr1 = myStringUp.find("(")
            if (sqbr1 != -1):
                sqbr2 = myStringUp.find(")")
                myStringUp = myStringUp[sqbr1+1: sqbr2] 
                   
            #//**Or** Some values have "+x" appended (NIST code):
            plusX = myString.find("+x")
            if (plusX != -1):
                myString = myString[0: plusX]
                  
            plusX = myStringUp.find("+x")
            if (plusX != -1):
                myStringUp = myStringUp[0: plusX]
                  
            #//**Or** Some values have "?" appended (NIST code):
            questn = myString.find("?")
            if (questn != -1):
                myString = myString[0: questn]
                  
            questn = myStringUp.find("?")
            if (questn != -1):
                myStringUp = myStringUp[0: questn]
                  
            #//myString.trim();
            #//list2ChiL[list2_ptr] = Double.parseDouble(myString);
             
        #//System.out.println("final myString = " + myString); 
        #//System.out.println("loggf " + myString.trim());
        #//System.out.println("chi_i " + myString.trim() + " chi_j " + myStringUp.trim());
        masterStringOut = masterStringOut + myString.strip() + newField + myStringUp.strip() + newField
        #//
        #// "|"-separated field [7] is the term designation of the lower level - needed? 
        #//
        #//
        #// "|"-separated field [8] is Lower E-level J quantum number
        #//
        testField = thisRecord[8]
        #//System.out.println("list2Element " + list2Element + " testField " + testField + " testField.trim().length() " + testField.trim().length());
        #//testLength = bounds[6] - bounds[5];
        blankFlag = True
        #//for (int kk = 0; kk < testLength-2; kk++){
        #//testChar = testField.substring(kk, kk+2);
        testField = testField.strip()
        if (len(testField) > 0):
            blankFlag = False 
                 
        #//   } 
        #//initialize subfields so we're ready for both whole and rational number Js
        subFields[0] = "1" 
        subFields[1] = "1" 
        if (blankFlag):
            myString = "1"
            myStringUp = "1"
            #//System.out.println("blankFlag triggered, myString = " + myString); 
        else:
            #// chi_L and chi_U separated by "-" - revise upper boundary to isolate chi_L:
            slash = testField.find("/")
            if (slash != -1):
                subFields = testField.split("/")
                myString = subFields[0].strip() #//numerator OR entire value, as case may be 
                myStringUp = subFields[1].strip() #//denominator OR default value of unity as case may be
            else:
                myString = testField
                myStringUp = "1"
               
            Jnumer = float(myString) #// log_10 of gf
            Jdenom = float(myStringUp) #// log_10 of gf
            #//Lower E level statistical weight
            Jfinal = Jnumer / Jdenom
            myString = str(Jfinal)
             

        #//System.out.println("J_i " + myString.trim());
        masterStringOut = masterStringOut + myString.strip() + newField;
        #//
        #// "|"-separated field [9] is the term designation of the upper level - needed? 
        #//
        #//
        #// "|"-separated field [10] is Upper E-level J quantum number
        #//
        #//Upper J quantum number 
        testField = thisRecord[10] 
        #//System.out.println("list2Element " + list2Element + " testField " + testField + " testField.trim().length() " + testField.trim().length());
        #//testLength = bounds[6] - bounds[5];
        blankFlag = True
        #//for (int kk = 0; kk < testLength-2; kk++){
        #//testChar = testField.substring(kk, kk+2);
        testField = testField.strip()
        if (len(testField) > 0):
            blankFlag = False 
                 
        #//   } 
        #//initialize subfields so we're ready for both whole and rational number Js
        subFields[0] = "1" 
        subFields[1] = "1" 
        if (blankFlag):
            myString = "1"
            myStringUp = "1";
            #//System.out.println("blankFlag triggered, myString = " + myString); 
        else:
            #// chi_L and chi_U separated by "-" - revise upper boundary to isolate chi_L:
            slash = testField.find("/")
            if (slash != -1):
                subFields = testField.split("/")
                myString = subFields[0].strip() #//numerator OR entire value, as case may be 
                myStringUp = subFields[1].strip() #//denominator OR default value of unity as case may be
            else:
                myString = testField
                myStringUp = "1.0"
               
            Jnumer = float(myString) #// log_10 of gf
            Jdenom = float(myStringUp) #// log_10 of gf
            #//Lower E level statistical weight
            Jfinal = Jnumer / Jdenom
            myString = str(Jfinal)
             

        #//System.out.println("J_j " + myString.trim());
        masterStringOut = masterStringOut + myString.strip() + newField
        #//
        #// "|"-separated field [11] is the statistical weight, g_i of BOTH the lower and upper level 
        #//
        testField = thisRecord[11] 
        #//System.out.println("list2Element " + list2Element + " testField " + testField + " testField.trim().length() " + testField.trim().length());
        #//testLength = bounds[6] - bounds[5];
        blankFlag = True
        #//for (int kk = 0; kk < testLength-2; kk++){
        #//testChar = testField.substring(kk, kk+2);
        testField = testField.strip()
        if (len(testField) > 0):
            blankFlag = False 
                 
        #//   }  
        if (blankFlag):
            myString = "0.0"
            myStringUp = "0.0"
            #//System.out.println("blankFlag triggered, myString = " + myString); 
        else:
            #// chi_L and chi_U separated by "-" - revise upper boundary to isolate chi_L:
            subFields = testField.split("-")
            myString = subFields[0].strip() #//lower E level 
            myStringUp = subFields[1].strip() #//upper E level 
            #//myString.trim()
            #//list2ChiL[list2_ptr] = Double.parseDouble(myString);
             
        #//System.out.println("final myString = " + myString); 
        #//System.out.println("loggf " + myString.trim());
        #//System.out.println("chi_i " + myString.trim() + " chi_j " + myStringUp.trim());
        masterStringOut = masterStringOut + myString.strip() + newField + myStringUp.strip() + newRecord
        #//

        #//We've gotten everything we need from the closed blocks of the NIST line list:
        list2_ptr+=1
        
    #} //i loop 

#} //iBlock loop

#//now get the remaining lines:
iBlock = numBlocks
offset = startLine + 6 * iBlock + 1
for i in range(1, rmndr):
    pass

####
numLines2 = list2_ptr

#//check:
#//System.out.println("masterStringOut " + masterStringOut);
#
#//Okay - what kind of mess did we make...
#// System.out.println("We processed " +  numLines2 + " lines");
#// System.out.println("list2Element  list2Stage  list2Lam0  list2Logf  list2GwL  list2ChiL  list2ChiI1  list2ChiI2  list2Mass");
#
#// WARNING: The line list is expected to be in the format printed out by the NIST Atomic Spectra Database (ver. 5.3), [Online]. 
#//Available: http://physics.nist.gov/asd [2015, November 21] * when ascii output is selected *   
#// Ie. blocks of five lines sepeareted by a lineof blank fields, fields separated by '|', etc.    
#// NOTE: "START:" MUST be added by hand after retrieving a NIST list
#//NIST database Print-out options MUST be selected so as to produce the following header, headings and sample data lines:
#//117
#Spectrum  |                           Ritz    |     Aki    |     fik    | log_gf   | Acc. |                 Ei           Ek                  | Lower level  |  Upper level   |  gi   gk  |Type|
#          |                        Wavelength |     s^-1   |            |          |      |                (eV)         (eV)                 |--------------|----------------|           |    |
#          |                         Vac (nm)  |            |            |          |      |                                                  | Term  | J    | Term    | J    |           |    |
#

#Java: byte[] barray = masterStringOut.getBytes();
barray = masterStringOut.encode('utf-8')
#//byte[] barray = masterStringOut.getBytes("UTF-8")
#// what do I do with this??   throws UnsupportedEncodingException; 
#System.out.println(" ");
#System.out.println("*************************");
#System.out.println(" ");
#System.out.println("This needs to be detected by GrayStar3Server.java: ");
#System.out.println(" ");
#System.out.println("size of barray " + barray.length);
#System.out.println(" ");
#System.out.println("*************************");
#System.out.println(" ");
# // System.out.println("barray " + barray);
# //
#Java: ByteFileWrite.writeFileBytes(byteListStr, barray); 
with open(byteListStr, 'wb') as fHandle:
    fHandle.write(barray)

#fHandle closed automatically upon exit from with:
#//
#    } // end main()