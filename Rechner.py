from tkinter import *


class Rechner:
    import re
    def __init__(self):

        self.meister = Tk()
        self.meister.geometry("400x400")
        self.meister.title("Taschenrechner")
        self.meister.resizable(width=False, height=False)
        self.alterWert = ""
        self.gewaehltesFeld = 21
        self.geklickt = False
        self.Tafel = Label(self.meister, text="", font=("Arial", 14), bg="white", fg="black", width=35,height=5, borderwidth=3, relief="solid")
        self.buttonNull = Button(self.meister, text="0",width=3, height=3, command=self.tasteNull)
        self.buttonEins = Button(self.meister, text="1",width=3, height=3, command=self.tasteEins)
        self.buttonZwei = Button(self.meister, text="2",width=3, height=3, command=self.tasteZwei)
        self.buttonDrei = Button(self.meister, text="3",width=3, height=3, command=self.tasteDrei)
        self.buttonVier = Button(self.meister, text="4",width=3, height=3, command=self.tasteVier)
        self.buttonFunf = Button(self.meister, text="5",width=3, height=3, command=self.tasteFunf)
        self.buttonSechs = Button(self.meister, text="6",width=3, height=3, command=self.tasteSechs)
        self.buttonSieben = Button(self.meister, text="7",width=3, height=3, command=self.tasteSieben)
        self.buttonAcht = Button(self.meister, text="8",width=3, height=3, command=self.tasteAcht)
        self.buttonNeun = Button(self.meister, text="9",width=3, height=3, command=self.tasteNeun)
        self.buttonKomma = Button(self.meister, text=",", width=3, height=3, command=self.tasteKomma)
        self.buttonZweiNull = Button(self.meister, text="00", width=3, height=3, command=self.tasteZweiNull)
        self.buttonPlus = Button(self.meister, text="+", width=3, height=3, command=self.tastePlus)
        self.buttonMinus = Button(self.meister, text="-",width=3,height=3,command=self.tasteMinus)
        self.buttonMulti = Button(self.meister, text="x", width=3, height=3, command=self.tasteMulti)
        self.buttonDiv = Button(self.meister, text=":", width=3,height=3, command=self.tasteDiv)
        self.buttonErgebnis = Button(self.meister, text="=", width=3,height=3,command=self.tasteErgebnis)
        self.buttonPotenz = Button(self.meister, text="^", width=3, height=3, command=self.tastePotenz)
        self.buttonWurzel = Button(self.meister, text="root", width=3, height=3, command=self.tasteWurzel)
        self.buttonPi = Button(self.meister, text="pi", width=3, height=3, command=self.tastePi)
        self.buttonCE = Button(self.meister, text="CE", width=3, height=3, command=self.tasteCE)
        #self.Tafel.bind("<Button-1>", self.gewaehltesFeld)
        self.Tafel.grid()
        self.buttonNull.place(x=100, y=300)
        self.buttonKomma.place(x=130, y=300)
        self.buttonZweiNull.place(x=160, y=300)
        self.buttonEins.place(x=100, y=245)
        self.buttonZwei.place(x=130, y=245)
        self.buttonDrei.place(x=160, y=245)
        self.buttonVier.place(x=100, y=200)
        self.buttonFunf.place(x=130, y=200)
        self.buttonSechs.place(x=160, y=200)
        self.buttonSieben.place(x=100, y=150)
        self.buttonAcht.place(x=130, y=150)
        self.buttonNeun.place(x=160, y=150)
        self.buttonPlus.place(x=190, y=150)
        self.buttonMinus.place(x=190, y=200)
        self.buttonMulti.place(x=190, y=245)
        self.buttonErgebnis.place(x=190, y=300)
        self.buttonDiv.place(x=220, y=150)
        self.buttonCE.place(x=250, y=150)
        self.buttonPotenz.place(x=220, y=200)
        self.buttonWurzel.place(x=220, y=245)
        self.buttonPi.place(x=220, y=300)
        self.meister.mainloop()   
    def wertEinlesen(self):
        exesStr = "self.alterWert = str(self.Tafel" + " .cget('text'))"
        exec(exesStr)
    def wertSchreiben(self):
        execStr = "self.Tafel" + ".config(text=self.neuerWert)"
        exec(execStr)
    def tasteNull(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "0"
        self.wertSchreiben()
    def tasteEins(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "1"
        self.wertSchreiben()
    def tasteZwei(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "2"
        self.wertSchreiben()
    def tasteDrei(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "3"
        self.wertSchreiben()
    def tasteVier(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "4"
        self.wertSchreiben()
    def tasteFunf(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "5"
        self.wertSchreiben()
    def tasteSechs(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "6"
        self.wertSchreiben()
    def tasteSieben(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "7"
        self.wertSchreiben()
    def tasteAcht(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "8"
        self.wertSchreiben()
    def tasteNeun(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "9"
        self.wertSchreiben()
    def tasteKomma(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + ","
        self.wertSchreiben()
    def tasteZweiNull(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "00"
        self.wertSchreiben()
    def tastePlus(self):
        self.wertEinlesen()
        self.geklickt = True
        self.neuerWert = str(self.alterWert) + "+"
        self.wertSchreiben()
    def tasteMinus(self):
        self.wertEinlesen()
        self.geklickt = True
        self.neuerWert = str(self.alterWert) + "-"
        self.wertSchreiben()
    def tasteMulti(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "x"
        self.wertSchreiben()
    def tasteDiv(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + ":"
        self.wertSchreiben()
    def tastePotenz(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "^"
        self.wertSchreiben()
    def tasteWurzel(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "root"
        self.wertSchreiben()
    def tastePi(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "pi"
        self.wertSchreiben()
    def tasteCE(self):
        self.wertEinlesen()
        self.neuerWert=""
        self.wertSchreiben()
    def tasteErgebnis(self):
        self.wertEinlesen()
        if self.alterWert == "":
            self.neuerWert = ""
        self.plusFinder = "+"
        self.minusFinder ="-"
        self.multiFinder = "x"
        self.divFinder = ":"
        self.start = 0
        self.geklickt = True
        if self.geklickt:
            self.neueErfahrung = ""
            for self.start in range(len(self.neuerWert)):
                if self.neuerWert[self.start] == self.plusFinder:
                   self.neueErfahrung = self.neuerWert.split('+')
                elif self.neuerWert[self.start] == self.minusFinder:
                    self.neueErfahrung = self.neuerWert.split('-')
                elif self.neuerWert[self.start] == self.multiFinder:
                    self.neueErfahrung = self.re.split(r'[-+x]+', self.neuerWert)
                elif self.neuerWert[self.start] == self.divFinder:
                    self.neueErfahrung = self.neuerWert.split(":")
                else:
                    pass
            self.plusBerechnung = 0
            self.minusBerechnung = 0
            self.multiBerechnung = 0
            self.diviBerechnung = 0
            self.plusZahlen = self.neueErfahrung
            self.minusZahlen = self.neueErfahrung
            self.multiZahlen = self.neueErfahrung
            self.diviZahlen = self.neueErfahrung
            self.Ergebnis = 0
            self.zweiteRunde = 0
            for self.zweiteRunde in range(len(self.neuerWert)):
                try:
                    if self.neuerWert[self.zweiteRunde] == self.minusFinder:
                        self.minusZahlen = self.neuerWert.split('-')
                        for self.minusBerechnung in range(len(self.minusZahlen)):
                            if self.Ergebnis == self.minusBerechnung:
                                self.Ergebnis += int(self.minusZahlen[0])
                                if self.Ergebnis == 1:
                                    self.Ergebnis -= int(self.minusZahlen[self.minusBerechnung])
                            else:
                                try:
                                    self.Ergebnis -= int(self.minusZahlen[self.minusBerechnung])
                                except:
                                        andererplusWert = 0
                                        for andererplusWert in range(len(self.minusZahlen[self.minusBerechnung])):
                                            if self.minusZahlen[self.minusBerechnung][andererplusWert] == "+":
                                                self.positiveBerechnung = self.minusZahlen[self.minusBerechnung].split('+')
                                                for neuesPositiv in range(len(self.positiveBerechnung)):
                                                    if self.Ergebnis == int(self.minusZahlen[0]):
                                                        self.Ergebnis -= int(self.positiveBerechnung[neuesPositiv])
                                                    else:
                                                        self.Ergebnis += int(self.positiveBerechnung[neuesPositiv])
                                            else:
                                                pass

                        break
                    elif self.neuerWert[self.zweiteRunde] == self.plusFinder:
                        self.plusZahlen = self.neuerWert.split('+')
                        for self.plusBerechnung in range(len(self.plusZahlen)):
                            try:
                                self.Ergebnis += int(self.plusZahlen[self.plusBerechnung])
                            except:
                                    andererminusWert = 0
                                    for andererminusWert in range(len(self.plusZahlen[self.plusBerechnung])):
                                        if self.plusZahlen[self.plusBerechnung][andererminusWert] == "-":
                                            self.mieseBerechnung = self.plusZahlen[self.plusBerechnung].split('-')
                                            for neueMiese in range(len(self.mieseBerechnung)):
                                                if self.Ergebnis == int(self.plusZahlen[0]):
                                                    self.Ergebnis += int(self.mieseBerechnung[neueMiese])
                                                else:
                                                    self.Ergebnis -= int(self.mieseBerechnung[neueMiese])


                        break
                    elif self.neuerWert[self.zweiteRunde] == self.multiFinder:
                        for self.multiBerechnung in range (len(self.multiZahlen)):
                            if self.Ergebnis == self.multiBerechnung:
                                self.Ergebnis += int(self.multiZahlen[self.multiBerechnung])
                                if self.Ergebnis == 1:
                                    self.Ergebnis *= int(self.multiZahlen[self.multiBerechnung])
                            else:
                                self.Ergebnis *= int(self.multiZahlen[self.multiBerechnung])
                        break
                    elif self.neuerWert[self.zweiteRunde] == self.divFinder:
                        for self.diviBerechnung in range (len(self.diviZahlen)):
                            if self.Ergebnis == self.diviBerechnung:
                                self.Ergebnis += int(self.diviZahlen[self.diviBerechnung])
                                if self.Ergebnis == 1:
                                    self.Ergebnis /= int(self.diviZahlen[self.diviBerechnung])
                            else:
                                self.Ergebnis /= int(self.diviZahlen[self.diviBerechnung])
                        break
                    else:
                        pass
                except:
                    self.neuerWert = "0"
            self.neuerWert = str(self.Ergebnis)
        else:
            pass
        self.wertSchreiben()


Rechner()