
   ChromaStarPy README:  Getting Started quickly:


   Running and setting inputs:
   

   1) Running at the command line prompt or in an interactive development environment (IDE) line spyder (recommended):

      - 'run' the main python source file: ChromaStarPy.py
      - All input parameters are read from a specifically formatted file called ChromaStarPy.input.txt
      - Sample template *.txt files are in the Inputs/ directory
 

   2) Running in a Jupyter notebook:

      - in Jupyter, open ChromaStarPy.ipynb (the other modules are imported).
      - All parameters are set in the notebook - ie. no input file for parameters


   Outputs:

   All output goes to a directory called Outputs/  - this directory must already exist
 
    

   Line list:

   ChromaStar expects to find the byte-date line list in a subdirectory called InputData/*.dat



   Visualization: 

   Sample blocks for plotting up various quantities with the pylab.plot function are in the main code


 
   Special notes:

   This is a unified atmospheric modelling and spectrum synthesis code (for now).  The atmospheric structure is
re-computed each time, and all atmospheric spectrum synthesis parameters are needed each time.

   

   
       