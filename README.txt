
   ChromaStarPy README:  Getting Started quickly:

   Updated July 2019
   December 2017

   Ian Short 
   Saint Mary's University
   Halifax, NS, Canada



   ** History and references

This is the python V. 3 port of the Java atmospheric modeling and spectrum synthesis 
code ChromaStarServer, formerly known as GrayStarServer,
supplemented with the two-level-atom facility of ChromaStar (formerly GrayStar).

July 2019 - Equation sof state (EOS) and chemical/ionization equilibrium now computed
with Phil Bennett's "GAS" package.  Includes 51 molecules, including 16 polyatomic
molecules

The version numbering is date-based using the ISO 8601 scheme YYYY-MM-DD

References:
Bennett, P.D., "A fast, robust algorithm for the solution of the equation of state for
	late-type stellar atmospheres", 1983, M.Sc. Thesis, University of British Columbia" ("GAS")
Short, C. Ian, 2017, ChromaStarDB: SQL Database-driven Spectrum Synthesis and More, 
PASP, 129, 094504, 11 pp., arXiv:1707.07725 
Short, C. Ian, 2016, GrayStarServer: Server-side Spectrum Synthesis with a Browser-based 
Client-side User Interface, PASP, 128, 104503, 11 pp., arXiv:1605.09368



   ** License

 * The MIT License (MIT)
 * Copyright (c) 2016 C. Ian Short 
 *
 * Permission is hereby granted, free of charge, to any person 
 obtaining a copy of this software and associated documentation 
 files (the "Software"), to deal in the Software without 
 restriction, including without limitation the rights to use, 
 copy, modify, merge, publish, distribute, sublicense, and/or 
 sell copies of the Software, and to permit persons to whom the 
 Software is furnished to do so, subject to the following 
 conditions:
 *
 * The above copyright notice and this permission notice shall 
 be included in all copies or substantial portions of the 
 Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY 
 KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
 WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
 AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
 OTHER DEALINGS IN THE SOFTWARE.


   ** Fundamental assumptions

     Atmospheric structure: Un-blanketed, LTE, static, 1D, plane-parallel geometry
     Chemical equilibrium: See Phil Bennett's GAS package
     Spectrum synthesis: Power law approximation for the Voigt line profile, opacity due to lines whose line-center 
wavelengths fall in the synthesis region only (eg. if you synthesize from 390 to 395 nm for the Sun, you will get 
the Ca II K line opacity, but NOT the effect of the Ca II H blue line wing - synthesize from 390 - 400 nm to get both
everywhere in the range.)	 

   
   **
   ** Installation and initial set-up:
   **

   Unzip the source tarball: gunzip ChromaStarPy.tar.gz

   To extract the ChromaStarPy directory structure, and all needed source files and inputs data files:

   tar xvf ChromaStarPy.tar

   This will create a subdirectory in the current directory called ChromaStarPy/ with subdirectories called
    InputData/, Inputs/, Outputs/, linpack/ and blas/

	- All source files (*.py) are in ChromaStarPy/, linpack/, and blas/
	- The ascii and byte-data versions of the atomic line list are in InputData/ in files with a .dat file 
          extension.  The byte-data version contains the string "Bytes" at the end of its main filename
	- Sample input files for setting up an atmosphere and spectrum modeling run are in the Input/ directory.  
   
	- By default the code writes all results to files in the Outputs/ directory

    Setting the environment:
    ChromaStarPy must import the matlplotlib [1] and numpy [2] python modules.  It is recommended that the user
obtain a comprehensive python installation that will likely ship with these, such as the python distribution
available through the Anaconda package manager (anaconda.org/anaconda/python).     
    ChromaStar will automatically detect the OS, and will automatically determine the current directory (the 
'run directory') for the cases where the OS is Windows or Unix/Linux, and will set the value of its absPath
variable.  ChromaStaryPy will most likely work as is if the run directory is the installation directory. 

    Atomic line list:
    ChromaStar expects to read the byte-data version of the line list in a subdirectory of the installation/run
directory called InputData/*.dat.  A default line list ships with the tarball.
    
[1] Hunter, J. D., Matplotlib: A 2D graphics environment, 2007, Computing In Science & Engineering, 9, 90    
[2] van der Walt, S., Colbert, S.C. & and Varoquaux, G., The NumPy Array: A Structure for Efficient Numerical 
    Computation, 2011, Computing in Science & Engineering, 13, 22 

   ** 
   ** Running
   **

    ChromaStarPy is known to run in Python V. 3.6 in the spYder V. 3.2.3 IDE under Windows 10, and is python 
V. 2.7 under linux (see the note about required python modules in "Installation and initial set-up").  The main 
program resides in source file ChromaStarGasPy.py and all other source files are 'import'ed here - the user must 
"run" this file in the IDE to run the code.  

    To run at the command line prompt outside an IDE:
    python ./ChromaStarGasPy.py

    To run in an IDE:
    Open ChromaStarGasPy.py
    Click 'Run'

    Textual run-time indicators at the console prompt, in order of appearance:
    
    Echoes the OS it has detected and echoes the absolute path of the run directory it has detected (value of 
its absPath variable) in which it expects to find the InputData/ and Outputs/ directories (see "Installation 
and initial set-up").
    Echoes which plot the user has selected (see "Setting up a modeling run" and "Outputs").
    Confirms that it has parsed the input file by echoing back the names and values of all input parameters.
    Indicates whether it is running the routines suitable for "Hot stars" or "Cool stars" (the "mode"), 
and the estimated spectral type based on the stellar data in Appendix G of An Introduction to Modern
Astrophysics, 2nd Ed. by Bradley W. Carroll and Dale A. Ostlie. 
    Indicates when it is beginning to read the atomic line list (meaning the atmospheric structure has 
been calculated), and when it has finished doing so.
    Indicates when it has begun the spectrum synthesis stage of the calculation, and then when it has 
finished doing so.  
    Echoes the value of Teff that it has recovered from an extended rectangle-rule numerical 
integration of the modeled monochromatic flux spectrum between 260 and 2600 nm, and the computed 
values of seven Johnson UBVRIJHK color indices for the model.     

 
   **
   ** Setting up a modeling run
   **


        ChromaStarPy is most likely to work if the run directory is the same as the main installation directory
(ChromaStarPy/), in keeping with the default behavior of IDEs. 
It will try to automatically detect the absolute path of this directory and will report its determination (see
"Installation and initial set-up").

	Input parameters:

	Currently ChromaStarPy is necessarily a unified atmosphere and spectrum modeling code in that it 
re-computes a new atmospheric model each time, even if only the spectrum synthesis or two-level-atom parameters 
are changed.  However, if specSynMode = True in the Input.py file, it will adopt the structure in Restart.py
and limit itself to just one iteration of the structure equations.

        All parameters for all aspects of the modeling AND post-processing are imported from a module (a python 
source file) in the run directory called Input.py.  The sample *.py files in the Input/ directory that ships with 
the installation can be simply copied to Input.py in the main installation/run directory.     

        Structure of Input.py:

  	See sample of Input.py content at end of this file.

        Because Input.py is imported as a python source file, the input parameters are set by python variable
assignment statements.  As a result, the input procedure will work regardless of the order of the parameters, 
number and location of blank lines, and discretionary comment statements.  The default format of the sample input 
files is simply for purposes of readability.  The default format is divided into six sections that are denoted 
with a descriptive header that begins with a hash (#) symbol.  

#Custom filename, #Default plot, #Spectrum synthesis mode

        Includes two string variables, project, and runVers, that the user can use to create distinct file 
names to distinguish model runs that woudl otherwise have indistinct names (see "Outputs" section).  
Includes a string variable, makePlot, that determines which of six build-in plotting routines will be
executed for the default graphical display.  If specSynMode = True, ChromaStarPy will adopt the atmospheric
structure in input module Restart.py and only perform one structure iteration before computing the synthetic
spectrum.
  
#Model atmosphere

   	Includes three basic input parameters needed to specify a spherical gravitating blackbody.  Two of these
are needed to specify an un-blanketed plane-parallel static 1D atmosphere.
Additional parameters as needed to specify the overall abundance distribution, to vary key groups of 
elements from the scaled-solar distribution, to tune the level of the background continuum opacity, etc.

#Spectrum synthesis

	Includes parameters for the synthesis range, the minimum oscillator strength, line broadening enhancement, 
and macroscopic broadening parameters.  (Note that voigtThresh is currently not used - all lines are treated
with Voigt profiles.)

#Performance vs realism

	Parameters for managing the balance between modeling realism and execution speed.  Includes the number
of outer and inner iterations of the atmospheric structure calculation, and whether TiO JOLA bands are included.

#Gaussian filter for limb darkening curve, Fourier transform

	This is for post-processed "data products" associated with observing the model through a Gaussian
narrow band filter.  The wavelength and band-width of the filter may be adjusted here. 

#Two-level atom and spectral line

	Parameters for a user-defined atomic species with two bound energy levels and the one bound-bound 
transition thereof.  All atomic data that specify the energy level structure, the ionization stage, 
and the line transition parameters.

Spectrum synthesis mode:

If the parameter specSynMode = False ChromaStar.py will perform the number of outer and inner iterations of
the atmospheric structure equtions specified by input parameters nOuterIter and nInnerIter before 
synthesizing the spectrum.
If  specSynMode = True the code will adopt the structure specified with python assignments statements in
the source file (python module) Restart.py, and will only perform one outer and inner structure iteration
before proceeding to spectrum synthesis.  This allows for rapid spectrum synthesis experiments in the case
where a converged structure has already been computed.  
** Note: ChromaStarPy automatically writes the current structure to the *_restart.py file in the Outputs 
directory (see "outputs" section) each time, and the user must manually copy the desired *_restart.py file to 
Restart.py in the run directory (see "Inputs" directory). 

	Restart.py

	This source file must always be present and contains an atmospheric model structure as python assignment 
statements.  When running with 'specSynMode = True' (see above), the user must manually ensure that the desired
atmospheric structure is contained in Restart.py.  This can be done by copying the *_restart.py file (see "Outputs"
section) from the relevant structure run.    



   **
   ** Output files
   **

   
   All output files are created in the Outputs/ directory in the installation/run directory (see the absPath 
environment variable in "Installation and initial set-up").

   ChromaStarPy automatically creates six output files for each run.  Each of these has several lines of 
header that specify the modeling parameters, describe the units, and label the columns.  The filenames for a 
given run are distinguished from each other by the filename stem, as described below, and are generally 
distinguished from those of other runs by a string that contains the main atmospheric modeling parameters 
(Teff, logg, [A/H]) and spectrum synthesis parameters (starting and ending wavelengths), and by the user-defined 
value of the project and runVers string variables (see "Input parameters" under "Setting up a modeling run").
All output files have the *.txt extension so as to be recognizable by simple editors under Windows.
 
   File: *.struc.txt:  The tabulated atmospheric structure ("Report 1")
         *.sed.txt:  The absolute overall spectral energy distribution (SED) ("Report 2")
         *.spec.txt:  The continuum rectified synthetic spectrum for the user-specified wavelength range,
                     AND the line center wavelengths and line identification strings for the lines that 
                     were included in the synthesis ("Report 3")
         *.ldc.txt:  The disk-centred limb-darkening curve of the model as observed with the user-defined 
                     Gaussian filter, and the discrete Fourier cosine transform of the full diameter limb
                     darkening profile, and the spectrum of monochromatic continuum linear limb darkening 
                     coefficients (LDCs)  ("Report 4")
         *.tla.txt:  The continuum rectified spectral line, and the atomic energy-level populations of the 
                     user-defined two-level atom (TLA) ("Report 5")
         *_retart.py The stellar parameters and converged structure are written as python assignment statements.
		     This file is automatically input as a module, and whether the structure it contains is
		     used depends on the value of the input parameter specSynMode (see "Input parameters:" 
 		     under ("Setting up a modeling run").  
	*.ppress.txt	Partial pressures of all atmoic, ionic, and molecular species that are treated in
			Phil Bennett's integrated EOS/Checmical Equilibrium package "GAS"

   **
   ** Integrated post-processing, reporting, and visualization
   **

   
   The application automatically imports matplotlib.pyplot() as plt() and automatically plots one of six
different outputs depending on the choice of the input parameters makePlot (see "Input parameters:" under
"Setting up a modeling run").
 
   All variables declared in the main ChromaStarPy.py file are available for printing or plotting at the
console prompt, and the most useful ones have been given descriptive names using camelCase (note that
python names are case-sensitive).  The user can identify the names of variables that hold the crucial 
distributions by inspection of the output blocks of code that write the standard output files (see "Output 
files"). These output blocks can be found by searching for the string "Report n", where "n" currently 
ranges from 1 to 5.   


   Four output blocks are located after the main atmospheric and spectrum modeling code: 
   Report 1 block: Atmospheric structure distributions (writes to *.struc.txt file).  
   Report 2 block: Spectral energy distribution (SED) (writes to *.sed.txt file).
   Report 3 block: Synthetic spectrum and line identifications (writes to *.spec.txt file)
   Report 4 block: Tuneable narrow-band limb darkening curve and its Fourier transform (writes to
     *.ldc.txt file), and spectrum of monochromatic linear limb darkening coefficients (LDCs)

   One output block is found after the user-defined two-level atom section of the code:
   Report 5 block: Spectral line profile and atomic energy level populations of user-defined two-level
     atom (writes to *.tla.txt file) 
   Report 6 block: Found after Report 4 block: Log10 partial pressures for 105 species, including 51 molecules
     computed by Phil Bennett's multi-D linearization package "GAS" - now integrated with ChromaStarPy


   **
   **
   ** Atomic line list
   **
   **
 
     ChromaStarPy ships with ascii and byte-data versions of a default line list with ~26000 lines spanning 260 to 
2600 nm drawn from the on-line NIST Atomic Spectra Database (Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD 
Team, 2015, NIST Atomic Spectra Database (ver. 5.3), [Online]. Available: http://physics.nist.gov/asd 
[2015, November 26]. National Institute of Standards and Technology, Gaithersburg, MD. 

     The utility program LineListPy.py ships with the source tarball.  It may be used to produce a byte-data
line list suitable for reading by ChromaStarPy from an input ascii line list as output by the on-line NIST Atomic 
Spectra Database.
CAUTION: The output options of the NIST database interface must be selected so as to produce output with select
fields and units that match the ascii sample.  Additionally, special characters that appear in some output
fields of the raw NIST ascii output (eg. '[', ']', '(', ')', '+', etc.) must be manually removed. 


Sample Input.py file for the Sun (see "Setting up a modeling run" section) 

#
#
#Custom filename tags to distinguish from other runs
project = "Project"
runVers = "Run"

#Default plot
#Select ONE only:

#makePlot = "structure"
#makePlot = "sed"
makePlot = "spectrum"
#makePlot = "ldc"
#makePlot = "ft"
#makePlot = "tlaLine" 
###The following two plot variables refer to the partial pressure outpue ("Report 6")
#makePlot = "ppress"
#plotSpec = "H"

#Spectrum synthesis mode
# - uses model in Restart.py with minimal structure calculation
specSynMode = False

#Model atmosphere
teff = 5777.0  #,    K
logg = 4.44 #,      cgs
log10ZScale = 0.0     # [A/H]
massStar = 1.0 #,      solar masses
xiT = 1.0  #,       km/s
logHeFe = 0.0  #,   [He/Fe]
logCO = 0.0  #,   [C/O]
logAlphaFe = 0.0   #,   [alpha-elements/Fe]


#Spectrum synthesis
lambdaStart = 390.0  #,       nm    
lambdaStop = 400.0  #,     nm

fileStem = project + "-"\
 + str(round(teff, 7)) + "-" + str(round(logg, 3)) + "-" + str(round(log10ZScale, 3))\
 + "-" + str(round(lambdaStart, 5)) + "-" + str(round(lambdaStop, 5))\
 + "-" + runVers  

lineThresh = -3.0  #,    min log(KapLine/kapCnt) for inclusion at all - areally, being used as "lineVoigt" for now
voigtThresh = -3.0  #,     min log(KapLine/kapCnt) for treatment as Voigt - currently not used - all lines get Voigt
logGammaCol = 0.5
logKapFudge = 0.0
macroV = 1.0  #,     km/s
rotV = 2.0  #,   km/s
rotI = 90.0 #,    degrees
RV = 0.0 #,   km/s
vacAir = "vacuum"    
sampling = "fine"

#Performance vs realism
nOuterIter = 12   #,     no of outer Pgas(HSE) - EOS - kappa iterations
nInnerIter = 12   #,    no of inner (ion fraction) - Pe iterations
ifTiO = 1   #,     where to include TiO JOLA bands in synthesis 

#Gaussian filter for limb darkening curve, fourier transform
diskLambda = 500.0  #,      nm
diskSigma = 0.01  #,     nm

#Two-level atom and spectral line
userLam0 = 589.592  #,   nm 
userA12 = 6.24  #,    A_12 logarithmic abundance = log_10(N/H_H) = 12
userLogF = -0.495   #,  log(f) oscillaotr strength // saturated line
userStage = 0  #,   ionization stage of user species (0 (I) - 3 (IV)
userChiI1 = 5.139   #,  ground state chi_I, eV
userChiI2 = 47.29   #,  1st ionized state chi_I, eV
userChiI3 = 71.62   #,  2nd ionized state chi_I, eV
userChiI4 = 98.94   #,  3rd ionized state chi_I, eV
userChiL = 0.0  #,   lower atomic E-level, eV
userGw1 = 2   #,  ground state state. weight or partition fn (stage I) - unitless
userGw2 = 1   #,  ground state state. weight or partition fn (stage II) - unitless
userGw3 = 1   #,   ground state state. weight or partition fn (stage III) - unitless
userGw4 = 1  #,  ground state state. weight or partition fn (stage IV) - unitless
userGwL = 2  #,   lower E-level state. weight - unitless
userMass = 22.9   #,  amu
userLogGammaCol = 1.0   #,  log_10 Lorentzian broadening enhancement factor

