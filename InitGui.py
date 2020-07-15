# hfcNastran95
#
# (c) Cean Wang (ceanwang@gmail.com) 2020                          
#                                                                         
# This program is free software but WITHOUT ANY WARRANTY.               
# Not for commercial use.                                                             

class hfcNastran95Workbench (Workbench):
    "hfcNastran95Workbench object"
    Icon = """
        /* XPM */
        static char * Nastran95_Workbench_Main_xpm[] = {
        "16 16 48 1",
        " 	c None",
        ".	c #171D96",
        "+	c #1A229B",
        "@	c #222CA1",
        "#	c #181D95",
        "$	c #232DA2",
        "%	c #3344B3",
        "&	c #2A36A9",
        "*	c #181C96",
        "=	c #181B94",
        "-	c #161C96",
        ";	c #4961C8",
        ">	c #5776D5",
        ",	c #192098",
        "'	c #171C96",
        ")	c #394DB9",
        "!	c #5C7DDB",
        "~	c #5B7BDA",
        "{	c #465FC5",
        "]	c #384AB5",
        "^	c #4D67CB",
        "/	c #4D67CC",
        "(	c #171D97",
        "_	c #3D51BC",
        ":	c #181E96",
        "<	c #181E97",
        "[	c #4961C7",
        "}	c #1B2099",
        "|	c #1F269E",
        "1	c #506DCF",
        "2	c #516ED0",
        "3	c #171F96",
        "4	c #4861C8",
        "5	c #5A7BDA",
        "6	c #2631A5",
        "7	c #191E97",
        "8	c #181F99",
        "9	c #1B229A",
        "0	c #445AC3",
        "a	c #597AD9",
        "b	c #1F279E",
        "c	c #2E3BAD",
        "d	c #181D97",
        "e	c #192097",
        "f	c #181D98",
        "g	c #181F97",
        "h	c #3C51BC",
        "i	c #10128F",
        "                ",
        "                ",
        "          ..    ",
        "          +@    ",
        "  #$%&*= -;>,   ",
        " ')!!!~{]^!!/(  ",
        " '!!!!!!!!!!!_: ",
        " <[!!!!!!!!!!!} ",
        "  |!!!!11!!!!23 ",
        "  :4!567890!ab  ",
        "   |!c    def   ",
        "   gh(          ",
        "    i           ",
        "                ",
        "                ",
        "                "};
        """
    MenuText = "hfcNastran95"
    ToolTip = "This is hfcNastran95 workbench"
	
    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
	
		
        import hfcNastran95InpInFem
        self.appendToolbar("Pre", ["hfcNastran95InpInFem"])
		
        #import hfcNastran95DatInFemWire
        #self.appendToolbar("Pre", ["hfcNastran95DatInFemWire"])
        
        import hfcNastran95OpenInp
        self.appendToolbar("Pre", ["hfcNastran95OpenInp"])

        #import hfcNastran95Run
        #self.appendToolbar("Solve", ["hfcNastran95Run"])
		
        #import hfcNastran95F06Draw
        #self.appendToolbar("Post", ["hfcNastran95F06Draw"])
		
        import hfcNastran95OpenF06
        self.appendToolbar("Post", ["hfcNastran95OpenF06"])

        Log("Loading hfcNastran95... done\n")

    def Activated(self):
        # do something here if needed...
        Msg("hfcNastran95.Activated()\n")

    def Deactivated(self):
        # do something here if needed...
        Msg("hfcNastran95.Deactivated()\n")

FreeCADGui.addWorkbench(hfcNastran95Workbench)