import random
from tkinter import *
import interface
from exception import *

class RegulyGry:  
    def __init__(self):
        self.liczbaCyfr = 4
        self.liczbaProb = 12
        self.r = random.randint(0,2)

class BadAnswer (RegulyGry):
    @staticmethod
    def genOdp():
        i = random.randint(0,3)
        j = random.randint(0,4-i)
        interface.listaOdpowiedzi[newGame.lp].config(state='normal')
        interface.listaOdpowiedzi[newGame.lp].insert(END,newGame.kodU)
        interface.listaOdpowiedzi[newGame.lp].config(state='readonly')
        interface.p[newGame.lp].config(state='normal')
        interface.p[newGame.lp].insert(END,str(i))
        interface.p[newGame.lp].config(state='readonly')
        interface.b[newGame.lp].config(state='normal')
        interface.b[newGame.lp].insert(END,str(j))
        interface.b[newGame.lp].config(state='readonly')

class Logika(RegulyGry):
    def __init__(self):
        RegulyGry.__init__(self)
        self.kod = [ random.randint(1,6) for i in range(self.liczbaCyfr) ]
        self.kodU =""
        self.wygrana = 0
        self.lp = 0
  
    def genOdp(self):
        i=0
        j=0
        licznikLiczb = [0,0,0,0,0,0]
        if self.r==0:
            BadAnswer.genOdp()
        else:
            for x in range(self.liczbaCyfr):
                licznikLiczb[self.kod[x]-1] +=1
            for x in range(self.liczbaCyfr):
                if int(self.kodU[x]) == self.kod[x]:
                    i+=1
                    licznikLiczb[int(self.kodU[x])-1] -=1
                    if licznikLiczb[int(self.kodU[x])-1]<0:
                        j -=1
                        licznikLiczb[int(self.kodU[x])-1] +=1
                elif int(self.kodU[x]) in self.kod:
                    if licznikLiczb[int(self.kodU[x])-1] > 0:
                        j+=1
                        licznikLiczb[int(self.kodU[x])-1] -=1

            interface.listaOdpowiedzi[self.lp].config(state='normal')
            interface.listaOdpowiedzi[self.lp].insert(END,self.kodU)
            interface.listaOdpowiedzi[self.lp].config(state='readonly')
            interface.p[self.lp].config(state='normal')
            interface.p[self.lp].insert(END,str(i))
            interface.p[self.lp].config(state='readonly')
            interface.b[self.lp].config(state='normal')
            interface.b[self.lp].insert(END,str(j))
            interface.b[self.lp].config(state='readonly')
            if i == self.liczbaCyfr:
                self.wygrana = 1
                

    def sprawdz(self):
        from tkinter import messagebox
        self.kodU = interface.poleTekstowe.get()
        try:
            if self.kodU.isdigit() != True:
                raise BadChar()
            elif len(self.kodU) > 4:
                raise BadSize(0)
            elif len(self.kodU)<4:
                raise BadSize(1)         
            else:
                self.genOdp()
                self.lp+=1
        except BadChar:
            pass
        except BadSize:
            pass
        except BadSize:
            pass
        if self.wygrana == 1:
            messagebox.showinfo("Koniec gry", "WYGRANA")
            interface.poleTekstowe.config(state = 'disabled')
            interface.sprawdz.config(state = 'disabled')
            interface.oszust.config(state = 'disabled')
        elif self.lp == self.liczbaProb:
            messagebox.showinfo("Koniec gry","PRZEGRANA")
            interface.poleTekstowe.config(state = 'disabled')
            interface.sprawdz.config(state = 'disabled')
            interface.oszust.config(state = 'disabled')
        print("Proba: "+str(self.lp))
        interface.poleTekstowe.delete(0,END)

    def oszust(self):
        from tkinter import messagebox
        if self.r==0:
            interface.poleTekstowe.config(state = 'disabled')
            interface.sprawdz.config(state = 'disabled')
            interface.oszust.config(state = 'disabled')
            messagebox.showinfo("Oszust?","Złapałeś/łaś mnie!")
        else:
            messagebox.showinfo("Oszust?","Tere fere "+str(self.kod))
            
    def reset(self):
        for x in range(self.lp):
            interface.listaOdpowiedzi[x].config(state='normal')
            interface.listaOdpowiedzi[x].delete(0,END)
            interface.listaOdpowiedzi[x].config(state='readonly')
            interface.p[x].config(state='normal')
            interface.p[x].delete(0,END)
            interface.p[x].config(state='readonly')
            interface.b[x].config(state='normal')
            interface.b[x].delete(0,END)
            interface.b[x].config(state='readonly')
        interface.poleTekstowe.config(state = 'normal')
        interface.poleTekstowe.delete(0,END)
        interface.sprawdz.config(state = 'normal')
        interface.oszust.config(state = 'normal')
        Logika.__init__(self)
        print(self.r)
        print(self.kod)


newGame = Logika()
print(newGame.kod)
print(newGame.r)
