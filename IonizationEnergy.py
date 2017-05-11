# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:12:02 2017

@author: ishort
"""

def getIonE(species):

    """// Ground state ionization energies in eV 
//From NIST Atomic Spectra Database
//Ionization Energies Data """

#//Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD Team (2014). NIST Atomic Spectra Database (ver. 5.2), [Online]. Available: http://physics.nist.gov/asd [2015, November 23]. National Institute of Standards and Technology, Gaithersburg, MD.
#//Heaviest element treatable: La

#//Ionization stages that don't exist (eg. "HIII") are given extremely large ioization energies (999 ev)

    ionE = 999999.0 #//default initialization

    if ("HI" == species):
         ionE = 13.598434005136

    if ("HII" == species):
         ionE = 999999.0

    if ("HIII" == species):
         ionE = 999999.0

    if ("HIV" == species):
         ionE = 999999.0

    if ("HV" == species):
         ionE = 999999.0

    if ("HVI" == species):
         ionE = 999999.0

    if ("HeI" == species):
         ionE = 24.587387936

    if ("HeII" == species):
         ionE = 54.417763110

    if ("HeIII" == species):
         ionE = 999999.0

    if ("HeIV" == species):
         ionE = 999999.0

    if ("HeV" == species):
         ionE = 999999.0

    if ("HeVI" == species):
         ionE = 999999.0

    if ("LiI" == species):
         ionE = 5.391714761

    if ("LiII" == species):
         ionE = 75.6400937

    if ("LiIII" == species):
         ionE = 122.45435380

    if ("LiIV" == species):
         ionE = 999999.0

    if ("LiV" == species):
         ionE = 999999.0

    if ("LiVI" == species):
         ionE = 999999.0

    if ("BeI" == species):
         ionE = 9.3226990

    if ("BeII" == species):
         ionE = 18.211153

    if ("BeIII" == species):
         ionE = 153.8961980

    if ("BeIV" == species):
         ionE = 217.7185766

    if ("BeV" == species):
         ionE = 999999.0

    if ("BeVI" == species):
         ionE = 999999.0

    if ("BI" == species):
         ionE = 8.2980190

    if ("BII" == species):
         ionE = 25.154830

    if ("BIII" == species):
         ionE = 37.930580

    if ("BIV" == species):
         ionE = 259.3715

    if ("BV" == species):
         ionE = 340.2260080

    if ("BVI" == species):
         ionE = 999999.0

    if ("CI" == species):
         ionE = 11.260300

    if ("CII" == species):
         ionE = 24.38450

    if ("CIII" == species):
         ionE = 47.88778

    if ("CIV" == species):
         ionE = 64.49351

    if ("CV" == species):
         ionE = 392.090500

    if ("CVI" == species):
         ionE = 489.9931770

    if ("NI" == species):
         ionE = 14.534130

    if ("NII" == species):
         ionE = 29.601250

    if ("NIII" == species):
         ionE = 47.4453

    if ("NIV" == species):
         ionE = 77.47350

    if ("NV" == species):
         ionE = 97.89013

    if ("NVI" == species):
         ionE = 552.067310

    if ("OI" == species):
         ionE = 13.6180540

    if ("OII" == species):
         ionE = 35.121110

    if ("OIII" == species):
         ionE = 54.93554

    if ("OIV" == species):
         ionE = 77.41350

    if ("OV" == species):
         ionE = 113.89890

    if ("OVI" == species):
         ionE = 138.1189

    if ("FI" == species):
         ionE = 17.422820

    if ("FII" == species):
         ionE = 34.97081

    if ("FIII" == species):
         ionE = 62.70800

    if ("FIV" == species):
         ionE = 87.175

    if ("FV" == species):
         ionE = 114.2490

    if ("FVI" == species):
         ionE = 157.16310

    if ("NeI" == species):
         ionE = 21.5645400

    if ("NeII" == species):
         ionE = 40.962960

    if ("NeIII" == species):
         ionE = 63.42331

    if ("NeIV" == species):
         ionE = 97.1900

    if ("NeV" == species):
         ionE = 126.247

    if ("NeVI" == species):
         ionE = 157.9340

    if ("NaI" == species):
         ionE = 5.13907670

    if ("NaII" == species):
         ionE = 47.28636

    if ("NaIII" == species):
         ionE = 71.6200

    if ("NaIV" == species):
         ionE = 98.936

    if ("NaV" == species):
         ionE = 138.400

    if ("NaVI" == species):
         ionE = 172.228

    if ("MgI" == species):
         ionE = 7.6462350

    if ("MgII" == species):
         ionE = 15.0352670

    if ("MgIII" == species):
         ionE = 80.14360

    if ("MgIV" == species):
         ionE = 109.2654

    if ("MgV" == species):
         ionE = 141.335

    if ("MgVI" == species):
         ionE = 186.760

    if ("AlI" == species):
         ionE = 5.9857684

    if ("AlII" == species):
         ionE = 18.828550

    if ("AlIII" == species):
         ionE = 28.447640

    if ("AlIV" == species):
         ionE = 119.9924

    if ("AlV" == species):
         ionE = 153.8252

    if ("AlVI" == species):
         ionE = 190.490

    if ("SiI" == species):
         ionE = 8.151683

    if ("SiII" == species):
         ionE = 16.345845

    if ("SiIII" == species):
         ionE = 33.493000

    if ("SiIV" == species):
         ionE = 45.141790

    if ("SiV" == species):
         ionE = 166.7670

    if ("SiVI" == species):
         ionE = 205.267

    if ("PI" == species):
         ionE = 10.486686

    if ("PII" == species):
         ionE = 19.769490

    if ("PIII" == species):
         ionE = 30.202640

    if ("PIV" == species):
         ionE = 51.44387

    if ("PV" == species):
         ionE = 65.02511

    if ("PVI" == species):
         ionE = 220.4304

    if ("SI" == species):
         ionE = 10.36001

    if ("SII" == species):
         ionE = 23.33788

    if ("SIII" == species):
         ionE = 34.856

    if ("SIV" == species):
         ionE = 47.222

    if ("SV" == species):
         ionE = 72.59449

    if ("SVI" == species):
         ionE = 88.05292

    if ("ClI" == species):
         ionE = 12.967632

    if ("ClII" == species):
         ionE = 23.81364

    if ("ClIII" == species):
         ionE = 39.80

    if ("ClIV" == species):
         ionE = 53.24

    if ("ClV" == species):
         ionE = 67.68

    if ("ClVI" == species):
         ionE = 96.940

    if ("ArI" == species):
         ionE = 15.75961120

    if ("ArII" == species):
         ionE = 27.62967

    if ("ArIII" == species):
         ionE = 40.735

    if ("ArIV" == species):
         ionE = 59.58

    if ("ArV" == species):
         ionE = 74.84

    if ("ArVI" == species):
         ionE = 91.290

    if ("KI" == species):
         ionE = 4.340663540

    if ("KII" == species):
         ionE = 31.62500

    if ("KIII" == species):
         ionE = 45.8031

    if ("KIV" == species):
         ionE = 60.917

    if ("KV" == species):
         ionE = 82.66 

    if ("KVI" == species):
         ionE = 99.40

    if ("CaI" == species):
         ionE = 6.11315520

    if ("CaII" == species):
         ionE = 11.8717180

    if ("CaIII" == species):
       ionE = 50.91315

    if ("CaIV" == species):
       ionE = 67.273

    if ("CaV" == species):
       ionE = 84.338

    if ("CaVI" == species):
       ionE = 108.78

    if ("ScI" == species):
         ionE = 6.561490

    if ("ScII" == species):
         ionE = 12.79977

    if ("ScIII" == species):
         ionE = 24.756838

    if ("ScIV" == species):
         ionE = 73.48940

    if ("ScV" == species):
         ionE = 91.949

    if ("ScVI" == species):
         ionE = 110.680

    if ("TiI" == species):
         ionE = 6.828120

    if ("TiII" == species):
         ionE = 13.5755

    if ("TiIII" == species):
         ionE = 27.49171

    if ("TiIV" == species):
         ionE = 43.26717

    if ("TiV" == species):
         ionE = 99.300

    if ("TiVI" == species):
         ionE = 119.530

    if ("VI" == species):
         ionE = 6.746187

    if ("VII" == species):
         ionE = 14.6200

    if ("VIII" == species):
         ionE = 29.3110

    if ("VIV" == species):
         ionE = 46.7090

    if ("VV" == species):
         ionE = 65.28165

    if ("VVI" == species):
         ionE = 128.130

    if ("CrI" == species):
         ionE = 6.766510

    if ("CrII" == species):
         ionE = 16.486305

    if ("CrIII" == species):
         ionE = 30.960

    if ("CrIV" == species):
         ionE = 49.160

    if ("CrV" == species):
         ionE = 69.460

    if ("CrVI" == species):
         ionE = 90.63500

    if ("MnI" == species):
         ionE = 7.4340377

    if ("MnII" == species):
         ionE = 15.639990

    if ("MnIII" == species):
         ionE = 33.668

    if ("MnIV" == species):
         ionE = 51.20

    if ("MnV" == species):
         ionE = 72.40

    if ("MnVI" == species):
         ionE = 95.600

    if ("FeI" == species):
         ionE = 7.9024678

    if ("FeII" == species):
         ionE = 16.199200

    if ("FeIII" == species):
         ionE = 30.651

    if ("FeIV" == species):
         ionE = 54.910

    if ("FeV" == species):
         ionE = 75.00

    if ("FeVI" == species):
         ionE = 98.985

    if ("CoI" == species):
         ionE = 7.88101

    if ("CoII)" == species):
         ionE = 17.0844

    if ("CoIII" == species):
         ionE = 33.500

    if ("CoIV" == species):
         ionE = 51.27

    if ("CoV" == species):
         ionE = 79.50

    if ("CoVI" == species):
         ionE = 102.00

    if ("NiI" == species):
         ionE = 7.639877

    if ("NiII" == species):
         ionE = 18.168837

    if ("NiIII" == species):
         ionE = 35.190

    if ("NiIV" == species):
         ionE = 54.90

    if ("NiV" == species):
         ionE = 76.060

    if ("NiVI" == species):
         ionE = 108.0

    if ("CuI" == species):
         ionE = 7.7263800

    if ("CuII" == species):
         ionE = 20.292390

    if ("CuIII" == species):
         ionE = 36.841

    if ("CuIV" == species):
         ionE = 57.380

    if ("CuV" == species):
         ionE = 79.80

    if ("CuVI" == species):
         ionE = 103.0

    if ("ZnI" == species):
         ionE = 9.3941970

    if ("ZnII" == species):
        ionE = 17.96439

    if ("ZnIII" == species):
         ionE = 39.72300

    if ("ZnIV" == species):
         ionE = 59.573

    if ("ZnV" == species):
         ionE = 82.60

    if ("ZnVI" == species):
         ionE = 108.0

    if ("GaI" == species):
         ionE = 5.9993018

    if ("GaII" == species):
         ionE = 20.51514

    if ("GaIII" == species):
         ionE = 30.72600

    if ("GaIV" == species):
         ionE = 63.2410

    if ("GaV" == species):
         ionE = 86.01

    if ("GaVI" == species):
         ionE = 112.7

    if ("GeI" == species):
         ionE = 7.899435

    if ("GeII" == species):
         ionE = 15.934610

    if ("GeIII" == species):
         ionE = 34.0576

    if ("GeIV" == species):
         ionE = 45.7150

    if ("GeV" == species):
         ionE = 90.500

    if ("GeVI" == species):
         ionE = 115.90

    if ("KrI" == species):
         ionE = 13.9996049

    if ("KrII" == species):
         ionE = 24.35984

    if ("KrIII" == species):
         ionE = 35.838

    if ("KrIV" == species):
         ionE = 50.85

    if ("KrV" == species):
         ionE = 64.69

    if ("KrVI" == species):
         ionE = 78.49

    if ("RbI" == species):
         ionE = 4.1771280

    if ("RbII" == species):
         ionE = 27.289540

    if ("RbIII" == species):
         ionE = 39.2470

    if ("RbIV" == species):
         ionE = 52.20

    if ("RbV" == species):
         ionE = 68.40

    if ("RbVI" == species):
         ionE = 82.9

    if ("SrI" == species):
         ionE = 5.69486720

    if ("SrII" == species):
         ionE = 11.0302760

    if ("SrIII" == species):
         ionE = 42.88353

    if ("SrIV" == species):
         ionE = 56.2800

    if ("SrV" == species):
         ionE = 71.00

    if ("SrVI" == species):
         ionE = 88.0

    if ("YI" == species):
         ionE = 6.21726

    if ("YII" == species):
         ionE = 12.22400

    if ("YIII" == species):
         ionE = 20.52441

    if ("YIV" == species):
         ionE = 60.6070

    if ("YV" == species):
         ionE = 74.97

    if ("YVI" == species):
         ionE = 91.390

    if ("ZrI" == species):
         ionE = 6.633900

    if ("ZrII" == species):
         ionE = 13.13

    if ("ZrIII" == species):
         ionE = 23.1700

    if ("ZrIV" == species):
         ionE = 34.418360

    if ("ZrV" == species):
         ionE = 80.3480

    if ("ZrVI" == species):
         ionE = 96.383

    if ("NbI" == species):
         ionE = 6.758850

    if ("NbII" == species):
         ionE = 14.32

    if ("NbIII" == species):
         ionE = 25.0

    if ("NbIV" == species):
         ionE = 37.611

    if ("NbV" == species):
         ionE = 50.5728

    if ("NbVI" == species):
         ionE = 102.0690

    if ("CsI" == species):
         ionE = 3.893905548

    if ("CsII" == species):
         ionE = 23.157450

    if ("CsIII" == species):
         ionE = 33.1950

    if ("CsIV" == species):
         ionE = 43.0

    if ("CsV" == species):
         ionE = 56.0

    if ("CsVI" == species):
         ionE = 69.1

    if ("BaI" == species):
         ionE = 5.2116640

    if ("BaII" == species):
         ionE = 10.003826

    if ("BaIII" == species):
         ionE = 35.8400

    if ("BaIV" == species):
         ionE = 47.03

    if ("BaV" == species):
         ionE = 58.0

    if ("BaVI" == species):
         ionE = 71.0

    if ("LaI" == species):
         ionE = 5.57690

    if ("LaII" == species):
         ionE = 11.184920

    if ("LaIII" == species):
         ionE = 19.17730

    if ("LaIV" == species):
         ionE = 49.950

    if ("LaV" == species):
         ionE = 61.60

    if ("LaVI" == species):
         ionE = 74.0

#//
    return ionE;

#  }  //end of method getIonE    


def getDissE(species):

    """ // Molecular dissociation energies in eV
//From NIST Allen's Astrophysical Quantities, 4th Ed. """

    dissE = 8.0 #//default initialization

    if (species == "H2"):
         dissE = 4.4781

    if (species == "H2+"):
         dissE = 2.6507

    if (species == "C2"):
         dissE = 6.296

    if (species == "CH"):
         dissE = 3.465

    if (species == "CO"):
         dissE = 11.092

    if (species == "CN"):
         dissE = 7.76

    if (species == "N2"):
         dissE = 9.759

    if (species == "NH"):
         dissE = 3.47

    if (species == "NO"):
         dissE = 6.497

    if (species == "O2"):
         dissE = 5.116

    if (species == "OH"):
         dissE = 4.392

    if (species == "MgH"):
         dissE = 1.34

    if (species == "SiO"):
         dissE = 8.26

    if (species == "CaH"):
         dissE = 1.70

    if (species == "CaO"):
         dissE = 4.8

    if (species == "TiO"):
         dissE = 6.87

    if (species == "VO"):
         dissE = 6.4

    if (species == "FeO"):
         dissE = 4.20

#//
    return dissE

#  };  //end of method getDissE    
