# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:28:47 2017

@author: Ian
"""
import math

def thetas(): 

    #//int numThetas = 10; // guess
    #//double[] cosTheta = new double[numThetas];
    #// Try equal distribution in cos(theta) space (rather than Gaussian quadrature)
    """ /* 
    double ii;
    for (int i = 0; i < numThetas; i++){
            
        ii = (double) i;
        cosTheta[i] = 1.0 - ii/numThetas;
            
    }
         */  """
    #//  cosTheta is a 2xnumThetas array:
    #/ row 0 is used for Gaussian quadrature weights
    #// row 1 is used for cos(theta) values
    #// Gaussian quadrature:
    """/*
         "n = 21" Gaussian quadrature weights, w_i, and abscissae from 
         http://pomax.github.io/bezierinfo/legendre-gauss.html
         - ie. 11 point among 0 and positive abcissae
        
         This 11/21 of a 21-point formula: 0 plus the positive abscissae ,
         so I *think* it represents *half* the integral on the interval [-1,1],
         ie., on the interval[0,1].   SO: Divide the first weight (x=0) by 2 so 
         that the quadrature sum is exactly half the integral on [-1,1]. 
         */"""
    nGauss = 11
    #//int nGauss = 7;
    #//int nGauss = 21;
    theta = [0.0 for i in range(nGauss)]
    weight = [0.0 for i in range(nGauss)]
    cosTheta = [ [ 0.0 for i in range(nGauss) ] for j in range(2) ]
    #// I *think* the "thetas" being assigned here (abcissae) are fractional
    #// angles, theta/(pi/2).
    #// 11 points on [0,1] from 21 point Gaussian quadrature on [-1,1]
    #//weight[0] = 0.5 * 0.1460811336496904;  // Divide the weight of the x=0 point by 2!  
    """
//        weight[0] = 0.1460811336496904; 
//        theta[0] = 0.0000000000000000;  //disk centre
//        weight[1] = 0.1445244039899700;
//        theta[1] = 0.1455618541608951;
//        weight[2] = 0.1398873947910731;
//        theta[2] = 0.2880213168024011;
//        weight[3] = 0.1322689386333375;
//        theta[3] = 0.4243421202074388;
//        weight[4] = 0.1218314160537285;
//        theta[4] = 0.5516188358872198;
//        weight[5] = 0.1087972991671484;
//        theta[5] = 0.6671388041974123;
//        weight[6] = 0.0934444234560339;
//        theta[6] = 0.7684399634756779;
//        weight[7] = 0.0761001136283793;
//        theta[7] = 0.8533633645833173;
//        weight[8] = 0.0571344254268572;
//        theta[8] = 0.9200993341504008;
//        weight[9] = 0.0369537897708525;
//        theta[9] = 0.9672268385663063;
//        weight[10] = 0.0160172282577743;
//        theta[10] = 0.9937521706203895;  //limb
    """
    """    
               // 7 points on [0,1] from 13 point Gaussian quadrature on [-1,1]
//               weight[0] = 0.2325515532308739;  // disk center
//               theta[0] = 0.0000000000000000;
//               weight[1] = 0.2262831802628972; 
//               theta[1] = 0.2304583159551348;
//               weight[2] = 0.2078160475368885; 
//               theta[2] = 0.4484927510364469;
//               weight[3] = 0.1781459807619457; 
//               theta[3] = 0.6423493394403402;
//               weight[4] = 0.1388735102197872; 
//               theta[4] = 0.8015780907333099;
//               weight[5] = 0.0921214998377285; 
//               theta[5] = 0.9175983992229779;
//               weight[6] = 0.0404840047653159; 
//               theta[6] = 0.9841830547185881;  //limb
    """
    """
//              // 9 points on [0,1] from 17 point Gaussian quadrature on [-1,1]    
//        weight[0] = 0.1794464703562065;  //disk center
//        theta[0] = 0.0000000000000000;
//        weight[1] = 0.1765627053669926;
//        theta[1] = 0.1784841814958479;
//        weight[2] = 0.1680041021564500;
//        theta[2] = 0.3512317634538763;
//        weight[3] = 0.1540457610768103;
//        theta[3] = 0.5126905370864769;
//        weight[4] = 0.1351363684685255;
//        theta[4] = 0.6576711592166907;
//        weight[5] = 0.1118838471934040;
//        theta[5] = 0.7815140038968014;
//        weight[6] = 0.0850361483171792;
//        theta[6] = 0.8802391537269859;
//        weight[7] = 0.0554595293739872;
//        theta[7] = 0.9506755217687678;
//        weight[8] = 0.0241483028685479;
//        theta[8] = 0.9905754753144174;  //limb
    """
    #// For nGauss = 11;
    #// 11 points on [0,1] from 21 point Gaussian quadrature on [-1,1]
    #// // No? weight[0] = 0.5 * 0.1460811336496904;  // Divide the weight of the x=0 point by 2!
    weight[0] = 0.1460811336496904
    theta[0] = 0.0000000000000000 #//disk centre
    weight[1] = 0.1445244039899700
    theta[1] = 0.1455618541608951
    weight[2] = 0.1398873947910731
    theta[2] = 0.2880213168024011
    weight[3] = 0.1322689386333375
    theta[3] = 0.4243421202074388
    weight[4] = 0.1218314160537285
    theta[4] = 0.5516188358872198
    weight[5] = 0.1087972991671484
    theta[5] = 0.6671388041974123
    weight[6] = 0.0934444234560339
    theta[6] = 0.7684399634756779
    weight[7] = 0.0761001136283793
    theta[7] = 0.8533633645833173
    weight[8] = 0.0571344254268572
    theta[8] = 0.9200993341504008
    weight[9] = 0.0369537897708525
    theta[9] = 0.9672268385663063
    weight[10] = 0.0160172282577743
    theta[10] = 0.9937521706203895 #//limb

    """
    /*
    // For nGauss = 21;
    // 21 points on [0,1] from 41 point Gaussian quadrature on [-1,1]
    weight[0] = 0.0756955356472984;
    theta[0] = 0.0000000000000000;
    weight[1] = 0.0754787470927158;
    theta[1] = 0.0756232589891630;
    weight[2] = 0.0748296231762215;
    theta[2] = 0.1508133548639922;
    weight[3] = 0.0737518820272235;
    theta[3] = 0.2251396056334228;
    weight[4] = 0.0722516968610231;
    theta[4] = 0.2981762773418249;
    weight[5] = 0.0703376606208175;
    theta[5] = 0.3695050226404815;
    weight[6] = 0.0680207367608768;
    theta[6] = 0.4387172770514071;
    weight[7] = 0.0653141964535274;
    theta[7] = 0.5054165991994061;
    weight[8] = 0.0622335425809663;
    theta[8] = 0.5692209416102159;
    weight[9] = 0.0587964209498719;
    theta[9] = 0.6297648390721963;
    weight[10] = 0.0550225192425787;
    theta[10] = 0.6867015020349513;
    weight[11] = 0.0509334542946175;
    theta[11] = 0.7397048030699261;
    weight[12] = 0.0465526483690143;
    theta[12] = 0.7884711450474093;
    weight[13] = 0.0419051951959097;
    theta[13] = 0.8327212004013613;
    weight[14] = 0.0370177167035080;
    theta[14] = 0.8722015116924414;
    weight[15] = 0.0319182117316993;
    theta[15] = 0.9066859447581012;
    weight[16] = 0.0266358992071104;
    theta[16] = 0.9359769874978539;
    weight[17] = 0.0212010633687796;
    theta[17] = 0.9599068917303463;
    weight[18] = 0.0156449384078186;
    theta[18] = 0.9783386735610834;
    weight[19] = 0.0099999387739059;
    theta[19] = 0.9911671096990163;
    weight[20] = 0.0043061403581649;
    theta[20] = 0.9983215885747715;
    */
    """
#// Fill cosTheta[][]

    for it in range(nGauss):
        cosTheta[0][it] = weight[it]
        theta[it] = theta[it] * math.pi / 2.0
        cosTheta[1][it] = math.cos(theta[it])
        

#// Try equal distribution in cos(theta) space (rather than Gaussian quadrature)
    """/* 
         double ii;
         for (int i = 0; i < numThetas; i++){
            
         ii = (double) i;
         cosTheta[i] = 1.0 - ii/numThetas;
            
         }
    */"""
    return cosTheta