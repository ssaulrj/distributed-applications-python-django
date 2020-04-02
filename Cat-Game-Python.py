from random import randint, uniform,random
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

def bloq():
 for i in range(0,9):
    lisb[i].config(state="disable")

def inij():
 print("Inicio")
 for i in range(0,9):
    lisb[i].config(state="normal")
    lisb[i].config(bg="lightgreen")
    lisb[i].config(text="")
    tab[i] = "N"
 global nomj1,nomj2,numjx #indica a que variables queremos acceder
 nomj1 = "Computadora"
 nomj2 = tkinter.simpledialog.askstring("Jugador","Nombre de jugador 1: ")
 numjx = 0
 #turj.set("Turno: "+nomj1)

def cam(num):
 global turno,nomj1,nomj2, numjx, numx
 if tab[num] == "N" and turno == 0:
  lisb[num].config(text="X")
  lisb[num].config(bg="black")
  tab[num]="X"
  turno=1
  lisb[num].config(state="disable")
  numjx=numjx+1
  #turj.set("Turno: "+nomj2+" "+str(numjx))
  #turj.set("Turno: "+nomj2)
  if numjx != 9:
      while True:
        numx = int(random()*8+1)
        print(numx)
        if tab[numx] == "N" and turno == 1:
            if tab[numx] != "O" and tab[numx] != "X":
              lisb[numx].config(text="O")
              lisb[numx].config(bg="white")
              tab[numx]="O"
              turno=0
              #turj.set("Turno: "+nomj1+" "+str(numjx))
              #turj.set("Turno: "+nomj1)
              lisb[numx].config(state="disable")
              numjx=numjx+1
              verif()
              break   
 #elif tab[num]=="N" and turno==1:
  #lisb[num].config(text="O")
  #lisb[num].config(bg="white")
  #tab[num]="O"
  #turno=0
  #turj.set("Turno: "+nomj1+" "+str(numjx))
  #turj.set("Turno: "+nomj1)
 if (numjx == 9):
      print("Fin")
 verif()
 
def verif():
 if (tab[0]=="X" and tab[1]=="X" and tab[2]=="X") or (tab[3]=="X" and tab[4]=="X" and tab[5]=="X") or (tab[6]=="X" and tab[7]=="X" and tab[8]=="X"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (tab[0]=="X" and tab[3]=="X" and tab[6]=="X") or (tab[1]=="X" and tab[4]=="X" and tab[7]=="X") or (tab[2]=="X" and tab[5]=="X" and tab[8]=="X"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (tab[0]=="X" and tab[4]=="X" and tab[8]=="X") or (tab[2]=="X" and tab[4]=="X" and tab[6]=="X"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (tab[0]=="O" and tab[1]=="O" and tab[2]=="O") or (tab[3]=="O" and tab[4]=="O" and tab[5]=="O") or (tab[6]=="O" and tab[7]=="O" and tab[8]=="O"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (tab[0]=="O" and tab[3]=="O" and tab[6]=="O") or (tab[1]=="O" and tab[4]=="O" and tab[7]=="O") or (tab[2]=="O" and tab[5]=="O" and tab[8]=="O"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (tab[0]=="O" and tab[4]=="O" and tab[8]=="O") or (tab[2]=="O" and tab[4]=="O" and tab[6]=="O"):
  bloq()
  tkinter.messagebox.showinfo("Yey","Jugador: "+nomj2+ " gana!")
 elif (numjx == 9):
  bloq()
  print("Fin")
  tkinter.messagebox.showinfo("Buhh!","Nadie ha ganado!")
  inij()
 
ven=Tk()
ven.geometry("370x460")
ven.title("3 en raya")
turno = 0

nomj1 = ""
nomj2 = ""
numjx = 0
numx  = 0

lisb=[]
tab=[]
turj=StringVar()

for i in range(0,9):
 tab.append("N")
 
b0=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(0))
lisb.append(b0)
b0.place(x=50,y=50)
b1=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(1))
lisb.append(b1)
b1.place(x=150,y=50)
b2=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(2))
lisb.append(b2)
b2.place(x=250,y=50)
b3=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(3))
lisb.append(b3)
b3.place(x=50,y=150)
b4=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(4))
lisb.append(b4)
b4.place(x=150,y=150)
b5=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(5))
lisb.append(b5)
b5.place(x=250,y=150)
b6=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(6))
lisb.append(b6)
b6.place(x=50,y=250)
b7=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(7))
lisb.append(b7)
b7.place(x=150,y=250)
b8=Button(ven,width=9,height=3,relief=SOLID,cursor="pencil",command=lambda: cam(8))
lisb.append(b8)
b8.place(x=250,y=250)
tue=Label(ven, textvariable=turj).place(x=140,y=330)
bini=Button(ven,bg='black',fg='white',text='A jugar!',cursor="sizing",width=15,height=3,command=inij).place(x=130,y=360)
bloq()

linea = Canvas(ven,width=310, height=10)
linea.place(x=30,y=120)
linea.create_line(310,0,0,0, width=10, fill='white')
l2 = Canvas(ven,width=310, height=10)
l2.place(x=30,y=220)
l2.create_line(310,0,0,0, width=10, fill='white')
l3 = Canvas(ven,width=10, height=310)
l3.place(x=130,y=25)
l3.create_line(0,310,0,0, width=10, fill='white')
l4 = Canvas(ven,width=10, height=310)
l4.place(x=230,y=25)
l4.create_line(0,310,0,0, width=10, fill='white')

ven.mainloop()
