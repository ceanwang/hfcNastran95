## hfcNastran95
Pre/Post processor for Nastran95 within FreeCAD

## Background
[Nastran95](http://github.com/nasa/NASTRAN-95) NASTRAN-95 is the NASA Structural Analysis System, a finite element analysis program (FEA) completed in the early 1970's.

[FreeCAD](https://freecadweb.org) is an open source CAD/CAM solution.

## Features 
Currently this workbench contains the following tools:

###  Reading Inp files 
The ability to read in an Inp case file and draw mesh. 

### Run Nastran95
Not implimented yet.
Execture the `Nastran` binary which reads in the Inp file and writes the result into a F06 file.

### Show Results
Not implimented yet.
Read in F06 result file and draw the mesh and displacement.

## Prerequisites

* Nastran95
* FreeCAD v0.19.x

## Installation
This workbench is developed on Windows 10.  

Note: Nastran excutable file must be in Windows's PATH. Under Window 10, it must be named as `Nastran95.exe`. If you use a python script to run that exe file, your Python and that python script also need to be in window 10's
PATH.

Download as hfcNastran95.zip and unzip it under FreeCad's `Mod/` folder. The result is a new 'Mod/hfcNastran95' folder with all the codes.

## License
GPL v3.0 (see [LICENSE](LICENCE) file)
