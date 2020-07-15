# hfcNastran95
#
# (c) Cean Wang (ceanwang@gmail.com) 2020                          
#                                                                         
# This program is free software but WITHOUT ANY WARRANTY.               
# Not for commercial use.                                                             

import FreeCAD,FreeCADGui
import Fem
import os
import subprocess

import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *

class hfcNastran95OpenInp:
	"hfcNastran95OpenInp"
	def GetResources(self):
		return {"MenuText": "Inp",
				"Accel": "Ctrl+t",
				"ToolTip": "Open an Inp file",
				"Pixmap": os.path.dirname(__file__)+"./resources/Inp.svg"
		}

	def IsActive(self):

		#if FreeCAD.ActiveDocument == None:
		#	return False
		#else:
		#	return True
        
		return True

	def Activated(self):
		import FreeCADGui

		myDocument = FreeCAD.ActiveDocument
		if myDocument==None:
			pass
		else:
		
			iHfc =FreeCAD.ActiveDocument.getObject('hfc')
			if iHfc==None:
				ininame="Mod/hfcNastran95/hfcNastran95.ini"
				
				inifile = FreeCAD.getHomePath()+ininame
				if os.path.exists(inifile):	
					iniF = open(inifile,"r")
					path=iniF.readline()
					iniF.close()
				else:
					path=FreeCAD.getHomePath()
						
				try:
					filename = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Read a Mystarn's Inp file"),path, "*.Inp") # PyQt4
				except Exception:
					filename, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a Nastran95's Inp file", path, "*.Inp") #PySide
					
				data=filename.split("/")
				n=len(data)
				path=""
				for i in range(n-1):
					path=path+data[i]+"/"

				inifileOut = FreeCAD.getHomePath()+ininame
				iniFout = open(inifileOut,"w")
				iniFout.writelines(path)
				iniFout.close()

			else:	
				path=iHfc.DatPath
				filenameDat=iHfc.DatFile
				#filename=filenameDat[:len(filenameDat)-3]+'dat'
				filename=filenameDat
		
			if os.path.exists(filename):	
				process=subprocess.Popen(["notepad",filename])

		
		

FreeCADGui.addCommand('hfcNastran95OpenInp',hfcNastran95OpenInp())