#from tkinter import *
import tkinter
from mastermind import *

     #####INTERFACE######
        ##OKNO GLOWNE##
glowneOkno = Tk()
glowneOkno.title("mastermind")
glowneOkno.geometry("400x390")

    ##WPROWADZANIE ODP##
img=PhotoImage(file='mm.png')
master = Label(glowneOkno,image=img)
master.place(x=270,y=10)

tekst = Label(glowneOkno, text="Wprowadz kod: ")
tekst.place(x=20,y=5)
poleTekstowe = Entry(glowneOkno)
poleTekstowe.place(x=110, y=5)

for x in range(1,13):
    probaLabel = Label(glowneOkno,text=str(x))
    probaLabel.place(x=2,y=30+x*25)

    
odp1Label = Label(glowneOkno, text='Odpowiedz')
odp1Label.place(x=25,y=35)
odp1Label = Label(glowneOkno, text='Poprawne')
odp1Label.place(x=105,y=35)
odp1Label = Label(glowneOkno, text='Bledne')
odp1Label.place(x=187,y=35)

    ##LISTA ODPOWIEDZI##
odp1 = Entry(glowneOkno,state='readonly',width = 12)
p1 = Entry(glowneOkno,state='readonly',width = 12)
b1 = Entry(glowneOkno,state='readonly',width = 12)

odp2 = Entry(glowneOkno,state='readonly',width = 12)
p2 = Entry(glowneOkno,state='readonly',width = 12)
b2 = Entry(glowneOkno,state='readonly',width = 12)

odp3 = Entry(glowneOkno,state='readonly',width = 12)
p3 = Entry(glowneOkno,state='readonly',width = 12)
b3 = Entry(glowneOkno,state='readonly',width = 12)

odp4 = Entry(glowneOkno,state='readonly',width = 12)
p4 = Entry(glowneOkno,state='readonly',width = 12)
b4 = Entry(glowneOkno,state='readonly',width = 12)


odp5 = Entry(glowneOkno,state='readonly',width = 12)
p5 = Entry(glowneOkno,state='readonly',width = 12)
b5 = Entry(glowneOkno,state='readonly',width = 12)

odp6 = Entry(glowneOkno,state='readonly',width = 12)
p6 = Entry(glowneOkno,state='readonly',width = 12)
b6 = Entry(glowneOkno,state='readonly',width = 12)

odp7 = Entry(glowneOkno,state='readonly',width = 12)
p7 = Entry(glowneOkno,state='readonly',width = 12)
b7 = Entry(glowneOkno,state='readonly',width = 12)

odp8 = Entry(glowneOkno,state='readonly',width = 12)
p8 = Entry(glowneOkno,state='readonly',width = 12)
b8 = Entry(glowneOkno,state='readonly',width = 12)

odp9 = Entry(glowneOkno,state='readonly',width = 12)
p9 = Entry(glowneOkno,state='readonly',width = 12)
b9 = Entry(glowneOkno,state='readonly',width = 12)

odp10 = Entry(glowneOkno,state='readonly',width = 12)
p10= Entry(glowneOkno,state='readonly',width = 12)
b10 = Entry(glowneOkno,state='readonly',width = 12)

odp11 = Entry(glowneOkno,state='readonly',width = 12)
p11 = Entry(glowneOkno,state='readonly',width = 12)
b11 = Entry(glowneOkno,state='readonly',width = 12)

odp12 = Entry(glowneOkno,state='readonly',width = 12)
p12 = Entry(glowneOkno,state='readonly',width = 12)
b12 = Entry(glowneOkno,state='readonly',width = 12)

listaOdpowiedzi = [odp1,odp2,odp3,odp4,odp5,odp6,odp7,odp8,odp9,odp10,odp11,odp12]
p = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
b = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]

for x in range(12):
    listaOdpowiedzi[x].place(x=20, y=55+x*25)

for x in range(12):
    p[x].place(x=97,y=55+x*25)

for x in range(12):
    b[x].place(x=174,y=55+x*25)

    ##PRZYCISKI##
sprawdz=Button(glowneOkno, text = "Sprawdz",width = 8, command =lambda: newGame.sprawdz())
sprawdz.place(x=25, y=355)
oszust = Button (text = "Oszust",width = 8, command =lambda: newGame.oszust())
oszust.place(x=103,y=355)
reset = Button (text = "Reset",width = 8, command =lambda: newGame.reset())
reset.place(x=181,y=355)

glowneOkno.mainloop()
