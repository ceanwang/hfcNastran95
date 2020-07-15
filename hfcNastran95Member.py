# hfcNastran95
#
# (c) Cean Wang (ceanwang@gmail.com) 2020                          
#                                                                         
# This program is free software but WITHOUT ANY WARRANTY.               
# Not for commercial use.                                                             

class hfc:
    def __init__(self, obj):
        '''"two properties" '''
        obj.addProperty("App::PropertyString","isEdge","hfc","Draw edges")
        obj.addProperty("App::PropertyString","isBackfaceCulling","hfc","BackfaceCulling")
        obj.addProperty("App::PropertyString","DatPath","hfc","Dat file path")
        obj.addProperty("App::PropertyString","DatFile","hfc","Dat file name")

        obj.Proxy = self


class Node:
    def __init__(self, id, x, y, z):
        self.id = str(id)
        self.x = x
        self.y = y
        self.z = z

class Member:
	# elmnt n1     n2    Ax     Asy     Asz     Jx     Iy     Iz     E     G     roll  density
    def __init__(self, id, n1, n2):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2

class MemberCELAS1:
    def __init__(self, id, n1, n2, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.mtype=mtype

class MemberCROD:
    def __init__(self, id, n1, n2, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.mtype=mtype
		
class MemberCBAR:
    def __init__(self, id, n1, n2, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.mtype=mtype
		
class MemberCBEAM:
    def __init__(self, id, n1, n2, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.mtype=mtype
		
class MemberCELBOW:
	#N95		
    def __init__(self, id, n1, n2, dx, dy, dz, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.mtype=mtype
		
class MemberCTRMEM:
	#N95
	#CTRMEMdef
    def __init__(self, id, n1, n2, n3, TH, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.TH = TH
        self.mtype = mtype
		
class MemberCTRIA1:
    def __init__(self, id, n1, n2, n3, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.mtype = mtype

class MemberCTRIA2:
    def __init__(self, id, n1, n2, n3, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.mtype = mtype

        
class MemberCTRIA3:
    def __init__(self, id, n1, n2, n3, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.mtype = mtype

class MemberCQDMEM:
	#N95
	#CQDMEMDef        
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype=mtype
		
class MemberCQUAD1:
	#N95
	#CQUAD1Def        
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype=mtype
		

class MemberCQUAD2:
	#N95
	#CQUAD2def        
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype=mtype
		
class MemberCQUAD4:
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype=mtype
		
class MemberCQUAD8:
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype=mtype

class MemberCTETRA:
    def __init__(self, id, n1, n2, n3, n4, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.mtype = mtype
		
class MemberCWEDGE:
    def __init__(self, id, n1, n2, n3, n4, n5, n6, mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.mtype = mtype
        
		

class MemberCHEXA:
    def __init__(self, sid, n1, n2, n3, n4, n5, n6, n7, n8, mtype):
        self.sid = str(sid)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.mtype = mtype
		
class MemberCHEXA1:
    def __init__(self, id , n1,n2,n3,n4,n5,n6,n7,n8,mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.mtype = mtype
        
class MemberCHEXA2:
    def __init__(self, id , n1,n2,n3,n4,n5,n6,n7,n8,mtype):
        self.id = str(id)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.mtype = mtype
        
		
