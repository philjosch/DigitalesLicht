## Adds Support for python 2.7
try:
    from tkinter import *
except:
    from Tkinter import *

import time
import threading

class Weiche(Frame):
    DELAY = 0.05
    def __init__(self, master, text, port1, port2, module):
        Frame.__init__(self, master, bg="black");
        self._port1 = port1
        self._port2 = port2
        Label(self, text=text).place(x=1, y=1, width=73, height=24)
        self.__buttonOben  = Button(self, text="O", command=self.__Oben)
        self.__buttonOben.place(x=1, y=25, width=73, height=25)
        self.__buttonUnten = Button(self, text="O", command=self.__Unten)
        self.__buttonUnten.place(x=1, y=50, width=73, height=24)
        self._module = module
    def __Oben(self):
        self._module.switchOn(self._port2)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port2)
        self.__buttonOben.config(text="X")
        self.__buttonUnten.config(text="O")
    def __Unten(self):
        self._module.switchOn(self._port1)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port1)
        self.__buttonOben.config(text="O")
        self.__buttonUnten.config(text="X")
    def place(self, x, y):
        Frame.place(self, x=x, y=y, width=75, height=75)

class Weiche2(Frame):
    DELAY = 0.05
    def __init__(self, master, text, port11, port12, port21, port22, module1, module2):
        Frame.__init__(self, master, bg="black");
        self._port11 = port11
        self._port12 = port12
        self._port21 = port21
        self._port22 = port22
        self._module1 = module1
        self._module2 = module2
        Label(self, text=text).place(x=1, y=1, width=73, height=24)
        self.__buttonOben  = Button(self, text="O", command=self.__Oben)
        self.__buttonOben.place(x=1, y=25, width=73, height=25)
        self.__buttonUnten = Button(self, text="O", command=self.__Unten)
        self.__buttonUnten.place(x=1, y=50, width=73, height=24)
    def __Oben(self):
        self._module1.switchOn(self._port12)
        self._module2.switchOn(self._port22)
        time.sleep(self.DELAY)
        self._module1.switchOff(self._port12)
        self._module2.switchOff(self._port22)
        self.__buttonOben.config(text="X")
        self.__buttonUnten.config(text="O")
    def __Unten(self):
        self._module1.switchOn(self._port11)
        self._module2.switchOn(self._port21)
        time.sleep(self.DELAY)
        self._module1.switchOff(self._port11)
        self._module2.switchOff(self._port21)
        self.__buttonOben.config(text="O")
        self.__buttonUnten.config(text="X")
    def place(self, x, y):
        Frame.place(self, x=x, y=y, width=75, height=75)


class Taster(Frame):
    DELAY = 0.25
    def __init__(self, master, text, port1, module):
        Frame.__init__(self, master, bg="black");
        self._port1 = port1
        Label(self, text=text).place(x=1, y=1, width=73, height=24)
        self.__buttonOben  = Button(self, text="O", command=self.__Oben)
        self.__buttonOben.place(x=1, y=25, width=73, height=25)
        Label(self, bg="white").place(x=1,y=50, height=24, width=73)
        self._module = module
    def __Oben(self):
        self._module.switchOn(self._port1)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port1)
    def place(self, x, y):
        Frame.place(self, x=x, y=y, width=75, height=75)



class DreiWegeWeiche(Frame):
    DELAY = 0.05
    def __init__(self, master, text, portL1, portL2, portR1, portR2, module):
        Frame.__init__(self, master, bg="black");
        self._port1 = portL1
        self._port2 = portL2
        self._port3 = portR1
        self._port4 = portR2
        Label(self, text=text).place(x=1, y=1, width=73, height=24)
        self.__buttonLinks = Button(self, text="O", command=self.__Links)
        self.__buttonLinks.place(x=1, y=25, width=24, height=25)
        self.__buttonMitte = Button(self, text="O", command=self.__Mitte)
        self.__buttonMitte.place(x=25, y=25, width=25, height=25)
        self.__buttonRechts = Button(self, text="O", command=self.__Rechts)
        self.__buttonRechts.place(x=50, y=25, width=24, height=25)
        self.__labelRichtung = Label(self, text="?")
        self.__labelRichtung.place(x=1,y=50, width=73, height=24)
        self._module = module
    def __Links(self):
        self._module.switchOn(self._port3)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port3)
        self._module.switchOn(self._port2)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port2)
        self.__labelRichtung.config(text="\\ \\       ")
    def __Rechts(self):
        self._module.switchOn(self._port1)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port1)
        self._module.switchOn(self._port4)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port4)
        self.__labelRichtung.config(text="       / /")
    def __Mitte(self):
        self._module.switchOn(self._port1)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port1)
        self._module.switchOn(self._port3)
        time.sleep(self.DELAY)
        self._module.switchOff(self._port3)
        self.__labelRichtung.config(text="| |")


    def place(self, x, y):
        Frame.place(self, x=x, y=y, width=75, height=75)

# Klasse fuer einfache Objekte, Licht an- und ausschalten (Schalter)
class LichtObjekt(Frame, threading.Thread):
    COLOR_DISABLED = "#fcc"
    COLOR_WAITING = "#ffaf4b"
    COLOR_ENABLED = "#cfc"
    def __init__(self, master, text, port, module):
        Frame.__init__(self, master, bg="black")
        threading.Thread.__init__(self)
        self._Button = Button(self, text=text, command=self.__pressed)
        self._Button.place(x=2, y=2, width=172, height=21)
        self._Label = Label(self, text="Aus", bg=self.COLOR_DISABLED)
        self._Label.place(x=174, y=2, width=24, height=21)
        self._port = port
        self._on = False
        self._module = module
        self._threaded = False

    def __pressed(self):
        if (not self._threaded):
            if self._on:
                self.switchOff()
            else:
                self.switchOn()

    def switchOn(self):
        if (not self._on):
            self._module.switchOn(self._port)
            self._Label.config(bg=self.COLOR_ENABLED, text="An")
            self._on = True

    def switchOff(self):
        if (self._on):
            self._module.switchOff(self._port)
            self._Label.config(bg=self.COLOR_DISABLED, text="Aus")
            self._on = False

    def disable(self):
        self._Button.config(state=DISABLED)

    def enable(self):
        self._Button.config(state=NORMAL)

    def place(self, x, y):
        Frame.place(self, x=x, y=y, width=200, height=25)



class StralatLichtObjekt(LichtObjekt):
    # Klasse fuer z.B. Strassenlaternen
    def __init__(self, master, text, port1, port2, module):
        LichtObjekt.__init__(self, master, text, port1, module)
        self._port2 = port2
        self._Button.config(command=self.__pressed)

    def __pressed(self):
        if self._on:
            self.switchOff()
        else:
            self.switchOn()

    def switchOn(self):
        if (not self._on):
            ## Spezieller Ablauf, um die Strassenlaternen mit Flackern anzuschalten
            ## Koennte man in Zukunft noch mit einem Thread realisieren, sodass es komplett autonom und randomisiert passiert
            self._module.switchOn(self._port)
            time.sleep(0.08)
            self._module.switchOff(self._port)
            time.sleep(0.12)
            self._module.switchOn(self._port2)
            time.sleep(0.08)
            self._module.switchOn(self._port)
            self._module.switchOff(self._port2)
            time.sleep(0.1)
            self._module.switchOff(self._port)
            time.sleep(0.05)
            self._module.switchOn(self._port)
            time.sleep(0.05)
            self._module.switchOn(self._port2)
            time.sleep(0.05)
            self._module.switchOff(self._port)
            time.sleep(0.05)
            self._module.switchOn(self._port)
            self._module.switchOff(self._port2)
            time.sleep(0.05)
            self._module.switchOn(self._port2)
            time.sleep(0.1)
            self._module.switchOff(self._port2)
            time.sleep(0.05)
            self._module.switchOn(self._port2)
            
            self._Label.config(bg=self.COLOR_ENABLED, text="An")
            self._on = True

    def switchOff(self):
        if (self._on):
            self._module.switchOff(self._port2)
            self._module.switchOff(self._port)
            self._Label.config(bg=self.COLOR_DISABLED, text="Aus")
            self._on = False


class DelayedShutdown(threading.Thread):
    def __init__(self, lichtObjekt, laufzeit):
        threading.Thread.__init__(self)
        self.__object = lichtObjekt
        self.__laufzeit = laufzeit

    def run(self):
        self.__object.disable()
        self.__object.switchOn()
        time.sleep(self.__laufzeit)
        self.__object.switchOff()
        self.__object.enable()
        
