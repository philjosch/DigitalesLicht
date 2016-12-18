try:
    from tkinter import *
except:
    from Tkinter import *

from Steuerung import *
from smbus import *
from Objekte import *
import random

class GUISteuerung(Tk):
    def __init__(self, port):
        Tk.__init__(self)
        self.title("Lichtsteuerung fuer die Eisenbahn")
        
        self.geometry("600x710")
        
        self.__port = port
        self.__bus = SMBus(self.__port)
        
        ## Folgendes muss noch angepasst werden
        self.__module1 = Steuerung(self.__bus, 0x20) ## Weichen
        self.__module2 = Steuerung(self.__bus, 0x21) ## Weichen
        self.__module3 = Steuerung(self.__bus, 0x22) ## Weichen
        self.__module4 = Steuerung(self.__bus, 0x23) ## Licht
        self.__module5 = Steuerung(self.__bus, 0x24) ## Licht
        self.__module6 = Steuerung(self.__bus, 0x25) ## Licht
        self.__module7 = Steuerung(self.__bus, 0x26) ## Licht
##        self.__module8 = Steuerung(self.__bus, 0x3f) ## Licht
        
        ## Die Weichen
        self.__WeichenMain = Frame(self)
        self.__WeichenMain.place(x=0, y=0, width=600, height=150)
        Label(self.__WeichenMain, text="Weichen").place(x=0, y=0, width=200, height=25)
        
        self.__FrameWeichen = Frame(self.__WeichenMain)
        self.__FrameWeichen.place(x=0, y=0, width=600, height=150)

        ## Linksweiche
        self.__LW = Weiche(self.__FrameWeichen, "Links W.", 0, 1, self.__module1)
        self.__LW.place(0, 0)
        ## Linksweiche
        self.__BH = Weiche(self.__FrameWeichen, "Bahnhof", 2, 3, self.__module1)
        self.__BH.place(75, 0)
        ## Linksweiche
        self.__BUE = Weiche(self.__FrameWeichen, "Uebergang", 4, 5, self.__module1)
        self.__BUE.place(150, 0)
        ## Linksweiche
        self.__AG = Weiche(self.__FrameWeichen, "Abstell", 6, 7, self.__module1)
        self.__AG.place(400, 75)
        ## Linksweiche
        self.__W1 = Weiche(self.__FrameWeichen, "W1", 0, 1, self.__module2)
        self.__W1.place(325, 75)
        ## Linksweiche
        self.__W2 = Weiche(self.__FrameWeichen, "W2", 2, 3, self.__module2)
        self.__W2.place(250, 75)
        ## Dreiwegeweiche
        self.__LW = DreiWegeWeiche(self.__FrameWeichen, "Dreiwegw", 4, 5, 6, 7, self.__module2)
        self.__LW.place(325, 0)
        ## Taster BH unten
        self.__TasterBHUnten = Taster(self.__FrameWeichen, "Bh Unten", 0, self.__module3)
        self.__TasterBHUnten.place(0, 75)
        ## Taster BH Oben
        self.__TasterBHOben = Taster(self.__FrameWeichen, "Bh Oben", 1, self.__module3)
        self.__TasterBHOben.place(75, 75)
        
        # Die Einzelnen Buttons zur Steuerung des Lichtes
        self.__LichtMain = Frame(self)
        self.__LichtMain.place(x=0, y=150, width=600, height=560)
        Label(self.__LichtMain, text="Licht").place(x=0, y=0, width=200, height=25)
        ## Alles an
        self.__alleAnButton = Button(self.__LichtMain, text="Alle Anschalten", command=self.alleAn)
        self.__alleAnButton.place(x=0, y=25, width=200, height=25)
        ## Alles Aus
        self.__alleAusButton = Button(self.__LichtMain, text="Alle Ausschalten", command=self.alleAus)
        self.__alleAusButton.place(x=200, y=25, width=200, height=25)
        ## Alle Zufaellig
        self.__randomButton = Button(self.__LichtMain, text="Zufaelliges Schalten", command=self.random)
        self.__randomButton.place(x=400, y=25, width=200, height=25)

        self.__FrameLicht = Frame(self.__LichtMain)
        self.__FrameLicht.place(x=0, y=60, width=600, height=500)
        ## Hauptbahnhof
        self.__HBF = LichtObjekt(self.__FrameLicht, "Hauptbahnhof", 0, self.__module7)
        self.__HBF.place(0, 0)
        ## Sued-Bahnhof
        self.__BhS = LichtObjekt(self.__FrameLicht, "Sued-Bahnhof", 1, self.__module7)
        self.__BhS.place(200, 0)
        ## Strassenlaterne
        self.__stralat = StralatLichtObjekt(self.__FrameLicht, "Strassenlaternen", 1, 2, self.__module4)
        self.__stralat.place(400, 0)
        ## Kirche
        self.__kirche = LichtObjekt(self.__FrameLicht, "Kirche", 3, self.__module4)
        self.__kirche.place(0, 50)
        ## Flutlicht
        self.__flutlicht = LichtObjekt(self.__FrameLicht, "Flutlicht", 4, self.__module4)
        self.__flutlicht.place(200, 50)
        ## Gottesdienst
        self.__gottesdienstButton = Button(self.__FrameLicht, text="Gottesdienst", command=self.gottesdienst)
        self.__gottesdienstButton.place(x=400, y=62, width=200, height=25)
        ## Baeckerei
        self.__baeckerei = LichtObjekt(self.__FrameLicht, "Baeckerei", 3, self.__module5)
        self.__baeckerei.place(0, 100)
        ## Wirtschaft
        self.__wirtschaft = LichtObjekt(self.__FrameLicht, "Wirtschaft", 4, self.__module5)
        self.__wirtschaft.place(200, 100)
        ## Haus 1
        self.__haus1 = LichtObjekt(self.__FrameLicht, "Haus 1", 5, self.__module5)
        self.__haus1.place(400, 100)
        ## Haus 2
        self.__haus2 = LichtObjekt(self.__FrameLicht, "Haus 2", 6, self.__module5)
        self.__haus2.place(0, 150)
        ## Haus 3
        self.__haus3 = LichtObjekt(self.__FrameLicht, "Haus 3", 7, self.__module5)
        self.__haus3.place(200, 150)
        ## Haus 4
        self.__haus4 = LichtObjekt(self.__FrameLicht, "Haus 4", 0, self.__module6)
        self.__haus4.place(400, 150)
        ## Haus 5
        self.__haus5 = LichtObjekt(self.__FrameLicht, "Haus 5", 1, self.__module6)
        self.__haus5.place(0, 200)
        ## Haus 6
        self.__haus6 = LichtObjekt(self.__FrameLicht, "Haus 6", 2, self.__module6)
        self.__haus6.place(200, 200)
        ## Haus 7
        self.__haus7 = LichtObjekt(self.__FrameLicht, "Haus 7", 3, self.__module6)
        self.__haus7.place(400, 200)
        ## Haus 8
        self.__haus8 = LichtObjekt(self.__FrameLicht, "Haus 8", 4, self.__module6)
        self.__haus8.place(0, 250)
        ## Haus 9
        self.__haus9 = LichtObjekt(self.__FrameLicht, "Haus 9", 5, self.__module6)
        self.__haus9.place(200, 250)
        ## Metzgerei
        self.__metzgerei = LichtObjekt(self.__FrameLicht, "Metzgerei", 6, self.__module6)
        self.__metzgerei.place(400, 250)
        ## Haus 10
        self.__haus10 = LichtObjekt(self.__FrameLicht, "Haus 10", 7, self.__module6)
        self.__haus10.place(0, 300)
        ## Cafe
        self.__cafe = LichtObjekt(self.__FrameLicht, "Cafe", 0, self.__module4)
        self.__cafe.place(200, 300)
        ## Hammerschmiede
        self.__hammerschmiede = LichtObjekt(self.__FrameLicht, "Hammerschmiede", 5, self.__module4)
        self.__hammerschmiede.place(0, 350)
        ## Stellwerk
        self.__stellwerk = LichtObjekt(self.__FrameLicht, "Stellwerk", 1, self.__module5)
        self.__stellwerk.place(200, 350)
        ## Lokschuppen
        self.__lokschuppen = LichtObjekt(self.__FrameLicht, "Lokschuppen", 2, self.__module5)
        self.__lokschuppen.place(400, 350)
        ## 2 Fam haus
        self.__2famhaus = LichtObjekt(self.__FrameLicht, "2-Familienhaus", 6, self.__module4)
        self.__2famhaus.place(0, 400)
        ## Neubau 1
        self.__neubau1 = LichtObjekt(self.__FrameLicht, "Neubau 1", 7, self.__module4)
        self.__neubau1.place(200, 400)
        ## Bauernhof
        self.__bauernhof = LichtObjekt(self.__FrameLicht, "Bauernhof", 0, self.__module4)
        self.__bauernhof.place(400, 400)
        
        self.__objects = [self.__cafe, self.__stralat, self.__kirche, self.__flutlicht, self.__hammerschmiede, self.__2famhaus, self.__neubau1,
                          self.__bauernhof, self.__stellwerk, self.__lokschuppen, self.__baeckerei, self.__wirtschaft, self.__haus1, self.__haus2, self.__haus3,
                          self.__haus4, self.__haus5, self.__haus6, self.__haus7, self.__haus8, self.__haus9, self.__metzgerei, self.__haus10,
                          self.__HBF, self.__BhS]
    
        self.__noRandom = [self.__stralat, self.__HBF, self.__BhS]

    def alleAn(self):
        for i in self.__objects:
            i.switchOn()
    
    def alleAus(self):
        for i in self.__objects:
            i.switchOff()
        pass
    
    def gottesdienst(self):
        # Spezielle Programme zum Ablauf der Lichtsteuerung
        self.__kirchenThread = DelayedShutdown(self.__kirche, 10)
        self.__kirchenThread.start()
    
    def random(self):
        for i in self.__objects:
            if (i not in self.__noRandom):
                if (random.random() < 0.5):
                    i.switchOn()
                else:
                    i.switchOff()


