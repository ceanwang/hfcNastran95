## hfcNastran95
Pre/Post processor for Nastran95 within FreeCAD.

[Nastran95](http://github.com/nasa/NASTRAN-95) is the 1995 version of the NASA Structural Analysis program.

[FreeCAD](https://freecadweb.org) is an open source CAD/CAM solution.

## Features 
Currently this workbench contains the following tools:

Import an Inp case file and draw mesh. 

Import F06 result file, draw mesh and displacement.

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
