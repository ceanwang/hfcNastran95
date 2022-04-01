# hfcNastran95
#
# (c) Cean Wang (ceanwang@gmail.com) 2020                          
#                                                                         
# This program is free software but WITHOUT ANY WARRANTY.               
# Not for commercial use.                                                             

from hfcNastran95Member import *

import FreeCAD,FreeCADGui
import Fem
import os
import shutil
import math

import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *
		
class hfcNastran95InpInFem:
	"hfcNastran95InpInFem object"
	def GetResources(self):
		return {"MenuText": "Inp In",
				"Accel": "Ctrl+t",
				"ToolTip": "Input inp file",
				"Pixmap": os.path.dirname(__file__)+"./resources/folderIcon.svg"
		}

	def IsActive(self):

		if FreeCAD.ActiveDocument is None:
			return False
		else:
			return True

	def Activated(self):
		import ObjectsFem
		
		isNastran95=1
		
		ininame="Mod/hfcNastran95/hfcNastran95.ini"
        
		inifile = FreeCAD.getHomePath()+ininame
		if os.path.exists(inifile):	
			iniF = open(inifile,"r")
			path=iniF.readline()
			iniF.close()
		else:
			path=FreeCAD.getHomePath()
                
		try:
			fName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Read a Nastran95's inp file"),path, "*.inp") # PyQt4
		except Exception:
			fName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a Nastran95's inp file", path, "*.inp") #PySide
            
		print ("src: "+fName)
		DesName = FreeCAD.getHomePath()+"bin/hfcNastran95.Inp"	
		print ("Des: "+DesName)	
		shutil.copyfile(fName,DesName)	
        
		data=fName.split("/")
		n=len(data)
		path=""
		for i in range(n-1):
			path=path+data[i]+"/"

		inifileOut = FreeCAD.getHomePath()+ininame
		iniFout = open(inifileOut,"w")
		iniFout.writelines(path)
		iniFout.close()
		
		#print (path)
		iHfc =FreeCAD.ActiveDocument.getObject('hfc')
		if iHfc==None:
			isEdge = 0
			isBackfaceCulling=1
			iHfc = FreeCAD.ActiveDocument.addObject("Part::FeaturePython",'hfc')
			hfc(iHfc)
			#iHfc.ViewObject.Proxy=0
			#ViewProviderCFG(iHfc.ViewObject)
			iHfc.DatPath = path
			iHfc.DatFile = fName
			iHfc.isEdge = str(isEdge)
			iHfc.isBackfaceCulling = str(isBackfaceCulling)
		else:	
			isEdge = int(iHfc.isEdge)
			isBackfaceCulling = int(iHfc.isBackfaceCulling)
		
		numNode=0
		numMember=0
		
		nodes_x=[]
		nodes_y=[]
		nodes_z=[]

		NodeList = {}
		MemberList = {}                                  

		NodeEndList = {}
		MemberEndList = {}                                  

		ProjectDescription = ''
		
		nodes = {}
		results = []
		mode_results = {}
		mode_disp = {}
		iFilled=[]
        
		mode_disp_x=[]
		mode_disp_y=[]
		mode_disp_z=[]


		nDisp=0
		mDisp=0
		isDebug=1
		
		#factor = 25.42
		factor = 1
		
		factorZoom = 100

		#000000000000000000000000000000000000000000000000000000000000000000
		
		fpDat = open(fName)
		tline=[]
		for line in fpDat:
			aline=line.strip()	
			if len(aline)==0 or aline[0]=='$':
				continue
			else:		
				tline.append(line.strip())
		fpDat.close()
			
		for id in range(len(tline)):
        
			aline=tline[id].strip()	
			data = aline.split()
			data1 = aline.split(",")
			#print (data)
			
			# Node 22222222222222222222222222222222222222222222222222222222222222222222	
			if data[0]=='GRID':
				#gridin
				#           id          cp  x1
                #GRID       10101       0   0.000   0.000   0.000       0
				gid=aline[8:16].strip()
				#cid1=aline[16:24].strip()
				xstr=aline[24:32].strip()
				if xstr=='':
					x=0.0
				else:	
					x=float(xstr)
				
				ystr=aline[32:40].strip()
				if ystr=='':
					y=0.0
				else:	
					y=float(ystr)
				zstr=aline[40:48].strip()
				if zstr=='':
					z=0.0
				else:	
					z=float(zstr)
				NodeList[gid] = Node(gid, x, y, z)
				numNode=numNode+1                
                
			if data[0]=='GRID*':
				#GRID*In
				#GRID*    1                               0.00000E+00     0.00000E+00
				gid=aline[8:24].strip()
				#cid1=aline[24:40].strip()
				x=aline[40:56].strip()
				y=aline[56:72].strip()
				bline=tline[id+1].strip()	
				z=bline[8:24].strip()
				NodeList[gid] =  Node(gid, float(x), float(y), float(z))
				numNode=numNode+1                

           
			# Member 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333	
            #CBAR    201     2       11      21      0.0     0.0     1.0                
			if data[0]=='CBAR':
				#CBARIn
				MemberList[data[1].strip()] =  MemberCBAR(data[1].strip(), data[3], data[4], data[0].strip())  
				numMember+=1

            #CBEAM   9400    9401    9401    9402    0.      0.      1.
			if data[0]=='CBEAM':
				#CBEAMIn
				MemberList[data[1].strip()] =  MemberCBEAM(data[1].strip(), data[3], data[4], data[0].strip())  
				numMember+=1

            #CROD, 418,418,8,3
			if data[0]=='CROD':
				#CRODIn
				MemberList[data[1].strip()] =  MemberCROD(data[1].strip(), data[3] ,data[4], data[0].strip())  
				numMember+=1



            #CROD, 418,418,8,3
			if data1[0]=='CROD':
				#CROD,In
				MemberList[data1[1].strip()] =  MemberCROD(data1[1].strip(), data1[3] ,data1[4], data1[0].strip())  
				numMember+=1
	
            #CTRMEM  24      91      1033    1032    1023
			if data[0]=='CTRMEM':
				#CTRMEMin
				EID=aline[8:16].strip()
				PID=aline[16:24].strip()
				G1=aline[24:32].strip()
				G2=aline[32:40].strip()
				G3=aline[40:48].strip()
				THstr=aline[48:54].strip()
				if THstr=='':
					TH=0.0
				else:	
					TH=float(THstr)
				
				MemberList[EID] = MemberCTRMEM(EID, G1, G2, G3, TH, data[0].strip())  
				numMember+=1

            #CTRIA1  24      91      1033    1032    1023
			if data[0]=='CTRIA1':
				#CTRIA1in
				MemberList[data[1].strip()] =  MemberCTRIA1(data[1].strip(), data[3] ,data[4] , data[5] ,data[0].strip())  
				numMember+=1

            #CTRIA2  24      91      1033    1032    1023
			if data[0]=='CTRIA2':
				#CTRIA2in
				MemberList[data[1].strip()] =  MemberCTRIA2(data[1].strip(), data[3] ,data[4] , data[5] ,data[0].strip())  
				numMember+=1

	
            #CTRIA3  24      91      1033    1032    1023
			if data[0]=='CTRIA3':
				#CTRIA3
				MemberList[data[1].strip()] =  MemberCTRIA3(data[1].strip(), data[3] ,data[4] , data[5] ,data[0].strip())  
				numMember+=1

            #CQDMEM  31      1       31      32      42      41                              
			if data[0]=='CQDMEM':
				#CQDMEMin
				MemberList[data[1].strip()] =  MemberCQDMEM(data[1].strip(), data[3], data[4], data[5], data[6], data[0].strip())  
				numMember+=1
            
            #CQUAD1  31      1       31      32      42      41                              
			if data[0]=='CQUAD1':
				#CQUAD1in
				MemberList[data[1].strip()] =  MemberCQUAD1(data[1].strip(), data[3], data[4], data[5], data[6], data[0].strip())  
				numMember+=1
            
            #CQUAD2  31      1       31      32      42      41                              
			if data[0]=='CQUAD2':
				#CQUAD2in
				MemberList[data[1].strip()] =  MemberCQUAD2(data[1].strip(), data[3], data[4], data[5], data[6], data[0].strip())  
				numMember+=1
            
			#CQUAD4      1001       1    1001    1002    2002    2001
			if data[0]=='CQUAD4':
				#CQUAD4in
				MemberList[data[1].strip()] =  MemberCQUAD4(data[1].strip(), data[3], data[4], data[5], data[6], data[0].strip())  
				numMember+=1
            
			#CQUAD8     16004       1   16007   16009   18009   18007   16008   17009
            #18008   17007
			if data[0]=='CQUAD8':
				#CQUAD8in
				MemberList[data[1].strip()] =  MemberCQUAD8(data[1].strip(), data[3] ,data[4] , data[5] , data[6],data[0].strip())  
				numMember+=1

			#CTETRA   1       1       8       13      67      33
			if data[0]=='CTETRA':
				#CTETRAin
				MemberList[data[1].strip()] =  MemberCTETRA(data[1].strip(), data[3] ,data[4] , data[5], data[6], data[0].strip())  
				numMember+=1
				
			#
			#CHEXA      10101     100   10101   10103   10303   10301   30101   30103+E     1
			#+E     1   30303   30301
			if data[0]=='CHEXA':
				#CHEXAin
				bline=tline[id+1].strip()	
				if len(aline)==80:
					eid=aline[9:16].strip()
					pid=aline[17:24].strip()
					g1=aline[25:32].strip()
					g2=aline[33:40].strip()
					g3=aline[41:48].strip()
					g4=aline[49:56].strip()
					g5=aline[57:64].strip()
					g6=aline[65:72].strip()
				if aline[73:80]==bline[1:8]:
					g7=bline[9:16].strip()
					g8=bline[17:24].strip()
				
				#print (eid+" "+g1+" "+g2+" "+g3+" "+g4+" "+g5+" "+g6+" "+g7+" "+g8)
				MemberList[eid] =  MemberCHEXA(eid, g1, g2, g3, g4, g5, g6, g7, g8, data[0].strip())  
				numMember+=1

		#print (NodeList)
		#print (MemberList)
		
		print ('numNode = '+str(numNode))		
		print ('numMember = '+str(numMember))	
		
		#for id in NodeList:
		#	print (NodeList[id].id+" "+str(NodeList[id].x)+" "+str(NodeList[id].y)+" "+str(NodeList[id].z))
		
		femmesh = Fem.FemMesh()
		# nodes
		#print ("Add nodes")
		for id in NodeList: # node
			#femmesh.addNode(NodeList[id].x,NodeList[id].y,NodeList[id].z, int(id)+1 )
			femmesh.addNode(NodeList[id].x,NodeList[id].y,NodeList[id].z, int(id) )
				
		for id in MemberList:
        
			mtype = MemberList[id].mtype
				
			if mtype == 'CROD':
				#CRODDraw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				femmesh.addEdge([n1, n2])
				
			elif mtype == 'CBAR':
				#CBARDraw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				femmesh.addEdge([n1, n2])
				
			elif mtype == 'CBEAM':
				#CBEAMDraw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				femmesh.addEdge([n1, n2])
				
			elif mtype =='CTRMEM':
				#N95	
				#CTRMEMDraw
				n1=MemberList[id].n1
				n2=MemberList[id].n2
				n3=MemberList[id].n3
				
				TH=float(MemberList[id].TH)
				
				n1=str(n1)
				n2=str(n2)
				n3=str(n3)
				
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n1])
				else:
					femmesh.addFace([n1,n2,n3])
						
			elif mtype =='CTRIA1':
				#CTRIA1Draw
				n1=int(MemberList[id].n1)
				n2=int(MemberList[id].n2)
				n3=int(MemberList[id].n3)
				
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n1])
				else:
					femmesh.addFace([n1,n2,n3])
				
			elif mtype =='CTRIA2':
				#CTRIA2Draw
				n1=int(MemberList[id].n1)
				n2=int(MemberList[id].n2)
				n3=int(MemberList[id].n3)
				
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n1])
				else:
					femmesh.addFace([n1,n2,n3])
				
			
			elif mtype =='CTRIA3':
				#CTRIA3Draw
				n1=int(MemberList[id].n1)
				n2=int(MemberList[id].n2)
				n3=int(MemberList[id].n3)
				
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n1])
				else:
					femmesh.addFace([n1,n2,n3])
				
			elif mtype == 'CQDMEM':
				#N95	
				#CQDMEMDraw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				n3 = int(MemberList[id].n3)
				n4 = int(MemberList[id].n4)
				
				#print (str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4))
                
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])
				else:
					femmesh.addFace([n1,n2,n3,n4])
				
			elif mtype == 'CQUAD1':
				#N95	
				#CQUAD1Draw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				n3 = int(MemberList[id].n3)
				n4 = int(MemberList[id].n4)
				
				#print (str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4))
                
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])
				else:
					femmesh.addFace([n1,n2,n3,n4])
				
			elif mtype == 'CQUAD2':
				#N95	
				#CQUAD2Draw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				n3 = int(MemberList[id].n3)
				n4 = int(MemberList[id].n4)
				
				#print (str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4))
                
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])
				else:
					femmesh.addFace([n1,n2,n3,n4])
				
			elif mtype == 'CQUAD4':
				#CQUAD4Draw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				n3 = int(MemberList[id].n3)
				n4 = int(MemberList[id].n4)
				
				#print (str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4))
                
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])
				else:
					femmesh.addFace([n1,n2,n3,n4])
                
			elif mtype == 'CQUAD8':
				#CQUAD8Draw
				n1 = int(MemberList[id].n1)
				n2 = int(MemberList[id].n2)
				n3 = int(MemberList[id].n3)
				n4 = int(MemberList[id].n4)
                
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])
				else:
					femmesh.addFace([n1,n2,n3,n4])
				
			elif mtype =='CTETRA':
				#CTETRADraw
				n1=int(MemberList[id].n1)
				n2=int(MemberList[id].n2)
				n3=int(MemberList[id].n3)
				n4=int(MemberList[id].n4)

				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n1])
					femmesh.addEdge([n4, n1])
					femmesh.addEdge([n4, n2])
					femmesh.addEdge([n4, n3])
				else:
					femmesh.addVolume([n1,n2,n3,n4])

			elif mtype =='CHEXA':
				#CHEXADraw
				n1=int(MemberList[id].n1)
				n2=int(MemberList[id].n2)
				n3=int(MemberList[id].n3)
				n4=int(MemberList[id].n4)

				n5=int(MemberList[id].n5)
				n6=int(MemberList[id].n6)
				n7=int(MemberList[id].n7)
				n8=int(MemberList[id].n8)
				
				if isEdge==1:
					femmesh.addEdge([n1, n2])
					femmesh.addEdge([n2, n3])
					femmesh.addEdge([n3, n4])
					femmesh.addEdge([n4, n1])

					femmesh.addEdge([n5, n6])
					femmesh.addEdge([n6, n7])
					femmesh.addEdge([n7, n8])
					femmesh.addEdge([n8, n5])
					
					femmesh.addEdge([n1, n5])
					femmesh.addEdge([n2, n6])
					femmesh.addEdge([n3, n7])
					femmesh.addEdge([n4, n8])
				else:
					femmesh.addVolume([n1,n2,n3,n4,n5,n6,n7,n8])
				
			else:
				print (mtype+' Not supported yet')
					
					
		result_mesh_object = None
		result_mesh_object = ObjectsFem.makeMeshResult(
			FreeCAD.ActiveDocument,
			"hfcMesh"
		)
		result_mesh_object.FemMesh = femmesh
		if isBackfaceCulling==0:
			result_mesh_object.ViewObject.BackfaceCulling=False	

		FreeCAD.ActiveDocument.recompute()
		FreeCADGui.activeDocument().activeView().viewAxonometric()
		FreeCADGui.SendMsgToActiveView("ViewFit")
		
		print ('Input done.')
		print ('')
		

FreeCADGui.addCommand('hfcNastran95InpInFem',hfcNastran95InpInFem())