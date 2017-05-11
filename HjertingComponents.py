# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:21:01 2017

@author: Ian
"""

def hjertingComponents():

    """//Hjerting function components (expansion coefficients in Voigt fn "a" parameter):
    // Observation and Analysis of Stellar Photospehres -, 3rd. Ed., Tab 11.5, p. 256
    // David F. Gray"""
    
    #//Note: "u" is the Voigt fn "v" parameter

    numV = 81
    #//Row 0 containt abscissae (Voigt fn "v" parameter)
    hjertComp = [ [ 0.0 for i in range(numV) ] for j in range(6) ]

    #//u    H_0(u)    H_1(u)     H_2(u)    H_3(u)    H_4(u)

    hjertComp[0][0] = 0.0; hjertComp[1][0] =   1.000000 ; hjertComp[2][0] = -1.12838 ; hjertComp[3][0] =   1.0000 ; hjertComp[4][0] =  -0.752 ; hjertComp[5][0] =    0.50;
    hjertComp[0][1] = 0.1; hjertComp[1][1] =   0.990050 ; hjertComp[2][1] = -1.10596 ; hjertComp[3][1] =   0.9702 ; hjertComp[4][1] =  -0.722 ; hjertComp[5][1] =    0.48;
    hjertComp[0][2] = 0.2; hjertComp[1][2] =   0.960789 ; hjertComp[2][2] = -1.04048 ; hjertComp[3][2] =   0.8839 ; hjertComp[4][2] =  -0.637 ; hjertComp[5][2] =    0.40;
    hjertComp[0][3] = 0.3; hjertComp[1][3] =   0.913931 ; hjertComp[2][3] = -0.93703 ; hjertComp[3][3] =   0.7494 ; hjertComp[4][3] =  -0.505 ; hjertComp[5][3] =    0.30;
    hjertComp[0][4] = 0.4; hjertComp[1][4] =   0.852144 ; hjertComp[2][4] = -0.80346 ; hjertComp[3][4] =   0.5795 ; hjertComp[4][4] =  -0.342 ; hjertComp[5][4] =    0.17;
    hjertComp[0][5] = 0.5; hjertComp[1][5] =   0.778801 ; hjertComp[2][5] = -0.64945 ; hjertComp[3][5] =   0.3894 ; hjertComp[4][5] =  -0.165 ; hjertComp[5][5] =    0.03;
    hjertComp[0][6] = 0.6; hjertComp[1][6] =   0.697676 ; hjertComp[2][6] = -0.48582 ; hjertComp[3][6] =   0.1953 ; hjertComp[4][6] =   0.007 ; hjertComp[5][6] =   -0.09;
    hjertComp[0][7] = 0.7; hjertComp[1][7] =   0.612626 ; hjertComp[2][7] = -0.32192 ; hjertComp[3][7] =   0.0123 ; hjertComp[4][7] =   0.159 ; hjertComp[5][7] =   -0.20;
    hjertComp[0][8] = 0.8; hjertComp[1][8] =   0.527292 ; hjertComp[2][8] = -0.16772 ; hjertComp[3][8] =  -0.1476 ; hjertComp[4][8] =   0.280 ; hjertComp[5][8] =   -0.27;
    hjertComp[0][9] = 0.9; hjertComp[1][9] =   0.444858 ; hjertComp[2][9] = -0.03012 ; hjertComp[3][9] =  -0.2758 ; hjertComp[4][9] =   0.362 ; hjertComp[5][9] =   -0.30;

    hjertComp[0][10] = 1.0; hjertComp[1][10] =   0.367879 ; hjertComp[2][10] =  0.08594 ; hjertComp[3][10] =  -0.3679 ; hjertComp[4][10] =   0.405 ; hjertComp[5][10] =   -0.31;
    hjertComp[0][11] = 1.1; hjertComp[1][11] =   0.298197 ; hjertComp[2][11] =  0.17789 ; hjertComp[3][11] =  -0.4234 ; hjertComp[4][11] =   0.411 ; hjertComp[5][11] =   -0.28;
    hjertComp[0][12] = 1.2; hjertComp[1][12] =   0.236928 ; hjertComp[2][12] =  0.24537 ; hjertComp[3][12] =  -0.4454 ; hjertComp[4][12] =   0.386 ; hjertComp[5][12] =   -0.24;
    hjertComp[0][13] = 1.3; hjertComp[1][13] =   0.184520 ; hjertComp[2][13] =  0.28981 ; hjertComp[3][13] =  -0.4392 ; hjertComp[4][13] =   0.339 ; hjertComp[5][13] =   -0.18;
    hjertComp[0][14] = 1.4; hjertComp[1][14] =   0.140858 ; hjertComp[2][14] =  0.31394 ; hjertComp[3][14] =  -0.4113 ; hjertComp[4][14] =   0.280 ; hjertComp[5][14] =   -0.12;
    hjertComp[0][15] = 1.5; hjertComp[1][15] =   0.105399 ; hjertComp[2][15] =  0.32130 ; hjertComp[3][15] =  -0.3689 ; hjertComp[4][15] =   0.215 ; hjertComp[5][15] =   -0.07;
    hjertComp[0][16] = 1.6; hjertComp[1][16] =   0.077305 ; hjertComp[2][16] =  0.31573 ; hjertComp[3][16] =  -0.3185 ; hjertComp[4][16] =   0.153 ; hjertComp[5][16] =   -0.02;
    hjertComp[0][17] = 1.7; hjertComp[1][17] =   0.055576 ; hjertComp[2][17] =  0.30094 ; hjertComp[3][17] =  -0.2657 ; hjertComp[4][17] =   0.097 ; hjertComp[5][17] =    0.02;
    hjertComp[0][18] = 1.8; hjertComp[1][18] =   0.039164 ; hjertComp[2][18] =  0.28027 ; hjertComp[3][18] =  -0.2146 ; hjertComp[4][18] =   0.051 ; hjertComp[5][18] =    0.04;
    hjertComp[0][19] = 1.9; hjertComp[1][19] =   0.027052 ; hjertComp[2][19] =  0.25648 ; hjertComp[3][19] =  -0.1683 ; hjertComp[4][19] =   0.015 ; hjertComp[5][19] =    0.05;

    hjertComp[0][20] = 2.0; hjertComp[1][20] =   0.0183156; hjertComp[2][20] =  0.231726; hjertComp[3][20] =  -0.12821; hjertComp[4][20] =  -0.0101; hjertComp[5][20] =    0.058;
    hjertComp[0][21] = 2.1; hjertComp[1][21] =   0.0121552; hjertComp[2][21] =  0.207528; hjertComp[3][21] =  -0.09505; hjertComp[4][21] =  -0.0265; hjertComp[5][21] =    0.056;
    hjertComp[0][22] = 2.2; hjertComp[1][22] =   0.0079071; hjertComp[2][22] =  0.184882; hjertComp[3][22] =  -0.06863; hjertComp[4][22] =  -0.0355; hjertComp[5][22] =    0.051;
    hjertComp[0][23] = 2.3; hjertComp[1][23] =   0.0050418; hjertComp[2][23] =  0.164341; hjertComp[3][23] =  -0.04830; hjertComp[4][23] =  -0.0391; hjertComp[5][23] =    0.043;
    hjertComp[0][24] = 2.4; hjertComp[1][24] =   0.0031511; hjertComp[2][24] =  0.146128; hjertComp[3][24] =  -0.03315; hjertComp[4][24] =  -0.0389; hjertComp[5][24] =    0.035;
    hjertComp[0][25] = 2.5; hjertComp[1][25] =   0.0019305; hjertComp[2][25] =  0.130236; hjertComp[3][25] =  -0.02220; hjertComp[4][25] =  -0.0363; hjertComp[5][25] =    0.027;
    hjertComp[0][26] = 2.6; hjertComp[1][26] =   0.0011592; hjertComp[2][26] =  0.116515; hjertComp[3][26] =  -0.01451; hjertComp[4][26] =  -0.0325; hjertComp[5][26] =    0.020;
    hjertComp[0][27] = 2.7; hjertComp[1][27] =   0.0006823; hjertComp[2][27] =  0.104739; hjertComp[3][27] =  -0.00927; hjertComp[4][27] =  -0.0282; hjertComp[5][27] =    0.015;
    hjertComp[0][28] = 2.8; hjertComp[1][28] =   0.0003937; hjertComp[2][28] =  0.094653; hjertComp[3][28] =  -0.00578; hjertComp[4][28] =  -0.0239; hjertComp[5][28] =    0.010;
    hjertComp[0][29] = 2.9; hjertComp[1][29] =   0.0002226; hjertComp[2][29] =  0.086005; hjertComp[3][29] =  -0.00352; hjertComp[4][29] =  -0.0201; hjertComp[5][29] =    0.007;

    hjertComp[0][30] = 3.0; hjertComp[1][30] =   0.0001234; hjertComp[2][30] =  0.078565; hjertComp[3][30] =  -0.00210; hjertComp[4][30] =  -0.0167; hjertComp[5][30] =    0.005;
    hjertComp[0][31] = 3.1; hjertComp[1][31] =   0.0000671; hjertComp[2][31] =  0.072129; hjertComp[3][31] =  -0.00122; hjertComp[4][31] =  -0.0138; hjertComp[5][31] =    0.003;
    hjertComp[0][32] = 3.2; hjertComp[1][32] =   0.0000357; hjertComp[2][32] =  0.066526; hjertComp[3][32] =  -0.00070; hjertComp[4][32] =  -0.0115; hjertComp[5][32] =    0.002;
    hjertComp[0][33] = 3.3; hjertComp[1][33] =   0.0000186; hjertComp[2][33] =  0.061615; hjertComp[3][33] =  -0.00039; hjertComp[4][33] =  -0.0096; hjertComp[5][33] =    0.001;
    hjertComp[0][34] = 3.4; hjertComp[1][34] =   0.0000095; hjertComp[2][34] =  0.057281; hjertComp[3][34] =  -0.00021; hjertComp[4][34] =  -0.0080; hjertComp[5][34] =    0.001;
    hjertComp[0][35] = 3.5; hjertComp[1][35] =   0.0000048; hjertComp[2][35] =  0.053430; hjertComp[3][35] =  -0.00011; hjertComp[4][35] =  -0.0068; hjertComp[5][35] =    0.000;
    hjertComp[0][36] = 3.6; hjertComp[1][36] =   0.0000024; hjertComp[2][36] =  0.049988; hjertComp[3][36] =  -0.00006; hjertComp[4][36] =  -0.0058; hjertComp[5][36] =    0.000;
    hjertComp[0][37] = 3.7; hjertComp[1][37] =   0.0000011; hjertComp[2][37] =  0.046894; hjertComp[3][37] =  -0.00003; hjertComp[4][37] =  -0.0050; hjertComp[5][37] =    0.000;
    hjertComp[0][38] = 3.8; hjertComp[1][38] =   0.0000005; hjertComp[2][38] =  0.044098; hjertComp[3][38] =  -0.00001; hjertComp[4][38] =  -0.0043; hjertComp[5][38] =    0.000;
    hjertComp[0][39] = 3.9; hjertComp[1][39] =   0.0000002; hjertComp[2][39] =  0.041561; hjertComp[3][39] =  -0.00001; hjertComp[4][39] =  -0.0037; hjertComp[5][39] =    0.000;

    hjertComp[0][40] = 4.0; hjertComp[1][40] =   0.0000000; hjertComp[2][40] =  0.039250; hjertComp[3][40] =   0.00000; hjertComp[4][40] =  -0.00329; hjertComp[5][40] =   0.000;
    hjertComp[0][41] = 4.2; hjertComp[1][41] =   0.0000000; hjertComp[2][41] =  0.035195; hjertComp[3][41] =   0.00000; hjertComp[4][41] =  -0.00257; hjertComp[5][41] =   0.000;
    hjertComp[0][42] = 4.4; hjertComp[1][42] =   0.0000000; hjertComp[2][42] =  0.031762; hjertComp[3][42] =   0.00000; hjertComp[4][42] =  -0.00205; hjertComp[5][42] =   0.000;
    hjertComp[0][43] = 4.6; hjertComp[1][43] =   0.0000000; hjertComp[2][43] =  0.028824; hjertComp[3][43] =   0.00000; hjertComp[4][43] =  -0.00166; hjertComp[5][43] =   0.000;
    hjertComp[0][44] = 4.8; hjertComp[1][44] =   0.0000000; hjertComp[2][44] =  0.026288; hjertComp[3][44] =   0.00000; hjertComp[4][44] =  -0.00137; hjertComp[5][44] =   0.000;
    hjertComp[0][45] = 5.0; hjertComp[1][45] =   0.0000000; hjertComp[2][45] =  0.024081; hjertComp[3][45] =   0.00000; hjertComp[4][45] =  -0.00113; hjertComp[5][45] =   0.000;
    hjertComp[0][46] = 5.2; hjertComp[1][46] =   0.0000000; hjertComp[2][46] =  0.022146; hjertComp[3][46] =   0.00000; hjertComp[4][46] =  -0.00095; hjertComp[5][46] =   0.000;
    hjertComp[0][47] = 5.4; hjertComp[1][47] =   0.0000000; hjertComp[2][47] =  0.020441; hjertComp[3][47] =   0.00000; hjertComp[4][47] =  -0.00080; hjertComp[5][47] =   0.000;
    hjertComp[0][48] = 5.6; hjertComp[1][48] =   0.0000000; hjertComp[2][48] =  0.018929; hjertComp[3][48] =   0.00000; hjertComp[4][48] =  -0.00068; hjertComp[5][48] =   0.000;
    hjertComp[0][49] = 5.8; hjertComp[1][49] =   0.0000000; hjertComp[2][49] =  0.017582; hjertComp[3][49] =   0.00000; hjertComp[4][49] =  -0.00059; hjertComp[5][49] =   0.000;

    hjertComp[0][50] = 6.0; hjertComp[1][50] =   0.0000000; hjertComp[2][50] =  0.016375;  hjertComp[3][50] =  0.00000; hjertComp[4][50] =  -0.00051; hjertComp[5][50] =   0.000;
    hjertComp[0][51] = 6.2; hjertComp[1][51] =   0.0000000; hjertComp[2][51] =  0.015291;  hjertComp[3][51] =  0.00000; hjertComp[4][51] =  -0.00044; hjertComp[5][51] =   0.000;
    hjertComp[0][52] = 6.4; hjertComp[1][52] =   0.0000000; hjertComp[2][52] =  0.014312;  hjertComp[3][52] =  0.00000; hjertComp[4][52] =  -0.00038; hjertComp[5][52] =   0.000;
    hjertComp[0][53] = 6.6; hjertComp[1][53] =   0.0000000; hjertComp[2][53] =  0.013426;  hjertComp[3][53] =  0.00000; hjertComp[4][53] =  -0.00034; hjertComp[5][53] =   0.000;
    hjertComp[0][54] = 6.8; hjertComp[1][54] =   0.0000000; hjertComp[2][54] =  0.012620;  hjertComp[3][54] =  0.00000; hjertComp[4][54] =  -0.00030; hjertComp[5][54] =   0.000;
    hjertComp[0][55] = 7.0; hjertComp[1][55] =   0.0000000; hjertComp[2][55] =  0.0118860; hjertComp[3][55] =  0.00000; hjertComp[4][55] =  -0.00026; hjertComp[5][55] =   0.000;
    hjertComp[0][56] = 7.2; hjertComp[1][56] =   0.0000000; hjertComp[2][56] =  0.0112145; hjertComp[3][56] =  0.00000; hjertComp[4][56] =  -0.00023; hjertComp[5][56] =   0.000;
    hjertComp[0][57] = 7.4; hjertComp[1][57] =   0.0000000; hjertComp[2][57] =  0.0105990; hjertComp[3][57] =  0.00000; hjertComp[4][57] =  -0.00021; hjertComp[5][57] =   0.000;
    hjertComp[0][58] = 7.6; hjertComp[1][58] =   0.0000000; hjertComp[2][58] =  0.0100332; hjertComp[3][58] =  0.00000; hjertComp[4][58] =  -0.00019; hjertComp[5][58] =   0.000;
    hjertComp[0][59] = 7.8; hjertComp[1][59] =   0.0000000; hjertComp[2][59] =  0.0095119; hjertComp[3][59] =  0.00000; hjertComp[4][59] =  -0.00017; hjertComp[5][59] =   0.000;

    hjertComp[0][60] = 8.0; hjertComp[1][60] =   0.0000000; hjertComp[2][60] =  0.0090306; hjertComp[3][60] =  0.00000; hjertComp[4][60] =  -0.00015; hjertComp[5][60] =   0.000;
    hjertComp[0][61] = 8.2; hjertComp[1][61] =   0.0000000; hjertComp[2][61] =  0.0085852; hjertComp[3][61] =  0.00000; hjertComp[4][61] =  -0.00013; hjertComp[5][61] =   0.000;
    hjertComp[0][62] = 8.4; hjertComp[1][62] =   0.0000000; hjertComp[2][62] =  0.0081722; hjertComp[3][62] =  0.00000; hjertComp[4][62] =  -0.00012; hjertComp[5][62] =   0.000;
    hjertComp[0][63] = 8.6; hjertComp[1][63] =   0.0000000; hjertComp[2][63] =  0.0077885; hjertComp[3][63] =  0.00000; hjertComp[4][63] =  -0.00011; hjertComp[5][63] =   0.000;
    hjertComp[0][64] = 8.8; hjertComp[1][64] =   0.0000000; hjertComp[2][64] =  0.0074314; hjertComp[3][64] =  0.00000; hjertComp[4][64] =  -0.00010; hjertComp[5][64] =   0.000;
    hjertComp[0][65] = 9.0; hjertComp[1][65] =   0.0000000; hjertComp[2][65] =  0.0070985; hjertComp[3][65] =  0.00000; hjertComp[4][65] =  -0.00009; hjertComp[5][65] =   0.000;
    hjertComp[0][66] = 9.2; hjertComp[1][66] =   0.0000000; hjertComp[2][66] =  0.0067875; hjertComp[3][66] =  0.00000; hjertComp[4][66] =  -0.00008; hjertComp[5][66] =   0.000;
    hjertComp[0][67] = 9.4; hjertComp[1][67] =   0.0000000; hjertComp[2][67] =  0.0064967; hjertComp[3][67] =  0.00000; hjertComp[4][67] =  -0.00008; hjertComp[5][67] =   0.000;
    hjertComp[0][68] = 9.6; hjertComp[1][68] =   0.0000000; hjertComp[2][68] =  0.0062243; hjertComp[3][68] =  0.00000; hjertComp[4][68] =  -0.00007; hjertComp[5][68] =   0.000;
    hjertComp[0][69] = 9.8; hjertComp[1][69] =   0.0000000; hjertComp[2][69] =  0.0059688; hjertComp[3][69] =  0.00000; hjertComp[4][69] =  -0.00007; hjertComp[5][69] =   0.000;

    hjertComp[0][70] = 10.0; hjertComp[1][70] =  0.000000 ; hjertComp[2][70] =  0.0057287; hjertComp[3][70] =  0.00000; hjertComp[4][70] =  -0.00006; hjertComp[5][70] =   0.000;
    hjertComp[0][71] = 10.2; hjertComp[1][71] =  0.000000 ; hjertComp[2][71] =  0.0055030; hjertComp[3][71] =  0.00000; hjertComp[4][71] =  -0.00006; hjertComp[5][71] =   0.000;
    hjertComp[0][72] = 10.4; hjertComp[1][72] =  0.000000 ; hjertComp[2][72] =  0.0052903; hjertComp[3][72] =  0.00000; hjertComp[4][72] =  -0.00005; hjertComp[5][72] =   0.000;
    hjertComp[0][73] = 10.6; hjertComp[1][73] =  0.000000 ; hjertComp[2][73] =  0.0050898; hjertComp[3][73] =  0.00000; hjertComp[4][73] =  -0.00005; hjertComp[5][73] =   0.000;
    hjertComp[0][74] = 10.8; hjertComp[1][74] =  0.000000 ; hjertComp[2][74] =  0.0049006; hjertComp[3][74] =  0.00000; hjertComp[4][74] =  -0.00004; hjertComp[5][74] =   0.000;
    hjertComp[0][75] = 11.0; hjertComp[1][75] =  0.000000 ; hjertComp[2][75] =  0.0047217; hjertComp[3][75] =  0.00000; hjertComp[4][75] =  -0.00004; hjertComp[5][75] =   0.000;
    hjertComp[0][76] = 11.2; hjertComp[1][76] =  0.000000 ; hjertComp[2][76] =  0.0045526; hjertComp[3][76] =  0.00000; hjertComp[4][76] =  -0.00004; hjertComp[5][76] =   0.000;
    hjertComp[0][77] = 11.4; hjertComp[1][77] =  0.000000 ; hjertComp[2][77] =  0.0043924; hjertComp[3][77] =  0.00000; hjertComp[4][77] =  -0.00003; hjertComp[5][77] =   0.000;
    hjertComp[0][78] = 11.6; hjertComp[1][78] =  0.000000 ; hjertComp[2][78] =  0.0042405; hjertComp[3][78] =  0.00000; hjertComp[4][78] =  -0.00003; hjertComp[5][78] =   0.000;
    hjertComp[0][79] = 11.8; hjertComp[1][79] =  0.000000 ; hjertComp[2][79] =  0.0040964; hjertComp[3][79] =  0.00000; hjertComp[4][79] =  -0.00003; hjertComp[5][79] =   0.000;

    hjertComp[0][80] = 12.0; hjertComp[1][80] =  0.000000 ; hjertComp[2][80] =  0.0039595; hjertComp[3][80] =  0.00000; hjertComp[4][80] =  -0.00003; hjertComp[5][80] =   0.000;


    return hjertComp