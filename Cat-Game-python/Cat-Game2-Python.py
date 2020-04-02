from tkinter import*
ventana=Tk()
ventana.config(bg="coral")
ventana.geometry("450x200")
fila1=["x","x","x"]
fila2=["x","x","x"]
fila3=["x","x","x"]


    
def ROJO1():    
    etiqueta=Label(ventana,text="O").place(x=10,y=50)
    R1["fg"]="red"
    R1["bg"]="white"
    R1["state"]="disable"
    A1["fg"]="red"
    A1["bg"]="white"
    A1["state"]="disable"
    fila1[0]="R"
    if fila1[0]=="R" and fila1[1]=="R" and fila1[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="R" and fila2[0]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="R" and fila2[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def AZUL1():
    etiqueta=Label(ventana,text="X").place(x=10,y=50)
    R1["fg"]="red"
    R1["bg"]="white"
    R1["state"]="disable"
    A1["fg"]="red"
    A1["bg"]="white"
    A1["state"]="disable"
    fila1[0]="A"
    if fila1[0]=="A" and fila1[1]=="A" and fila1[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[0]=="A" and fila3[0]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def ROJO2():
    etiqueta=Label(ventana,text="O").place(x=30,y=50)
    R2["fg"]="red"
    R2["bg"]="white"
    R2["state"]="disable"
    A2["fg"]="red"
    A2["bg"]="white"
    A2["state"]="disable"
    fila1[1]="R"
    if fila1[0]=="R" and fila1[1]=="R" and fila1[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[1]=="R" and fila2[1]=="R" and fila3[1]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def AZUL2():
    etiqueta=Label(ventana,text="X").place(x=30,y=50)
    R2["fg"]="red"
    R2["bg"]="white"
    R2["state"]="disable"
    A2["fg"]="red"
    A2["bg"]="white"
    A2["state"]="disable"
    fila1[1]="A"
    if fila1[0]=="A" and fila1[1]=="A" and fila1[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[1]=="A" and fila2[1]=="A" and fila3[1]=="A":
        Etiqueta= Label(ventana, text="Ganador AZUL")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def ROJO3():
    etiqueta=Label(ventana,text="O").place(x=50,y=50)
    R3["fg"]="red"
    R3["bg"]="white"
    R3["state"]="disable"
    A3["fg"]="red"
    A3["bg"]="white"
    A3["state"]="disable"
    fila1[2]="R"
    if fila1[0]=="R" and fila1[1]=="R" and fila1[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="R" and fila2[1]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="R" and fila2[2]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

        
def AZUL3():
    etiqueta=Label(ventana,text="X").place(x=50,y=50)
    R3["fg"]="red"
    R3["bg"]="white"
    R3["state"]="disable"
    A3["fg"]="red"
    A3["bg"]="white"
    A3["state"]="disable"
    fila1[2]="A"
    if fila1[0]=="A" and fila1[1]=="A" and fila1[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[1]=="A" and fila3[0]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[2]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

        
def ROJO4():
    etiqueta=Label(ventana,text="O").place(x=10,y=80)
    R4["fg"]="red"
    R4["bg"]="white"
    R4["state"]="disable"
    A4["fg"]="red"
    A4["bg"]="white"
    A4["state"]="disable"
    fila2[0]="R"
    if fila2[0]=="R" and fila2[1]=="R" and fila2[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)
        
        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="R" and fila2[0]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)
        
        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

        
def AZUL4():
    etiqueta=Label(ventana,text="X").place(x=10,y=80)
    R4["fg"]="red"
    R4["bg"]="white"
    R4["state"]="disable"
    A4["fg"]="red"
    A4["bg"]="white"
    A4["state"]="disable"
    fila2[0]="A"
    if fila2[0]=="A" and fila2[1]=="A" and fila2[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[0]=="A" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def ROJO5():
    etiqueta=Label(ventana,text="O").place(x=30,y=80)
    R5["fg"]="red"
    R5["bg"]="white"
    R5["state"]="disable"
    A5["fg"]="red"
    A5["bg"]="white"
    A5["state"]="disable"
    fila2[1]="R"
    if fila2[0]=="R" and fila2[1]=="R" and fila2[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[1]=="R" and fila2[1]=="R" and fila3[1]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="R" and fila2[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="R" and fila2[1]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
    
def AZUL5():
    etiqueta=Label(ventana,text="X").place(x=30,y=80)
    R5["fg"]="red"
    R5["bg"]="white"
    R5["state"]="disable"
    A5["fg"]="red"
    A5["bg"]="white"
    A5["state"]="disable"
    fila2[1]="A"
    if fila2[0]=="A" and fila2[1]=="A" and fila2[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[1]=="A" and fila2[1]=="A" and fila3[1]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[1]=="A" and fila3[0]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
        
def ROJO6():
    etiqueta=Label(ventana,text="O").place(x=50,y=80)
    R6["fg"]="red"
    R6["bg"]="white"
    R6["state"]="disable"
    A6["fg"]="red"
    A6["bg"]="white"
    A6["state"]="disable"
    fila2[2]="R"
    if fila2[0]=="R" and fila2[1]=="R" and fila2[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="R" and fila2[2]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def AZUL6():
    etiqueta=Label(ventana,text="X").place(x=50,y=80)
    R6["fg"]="red"
    R6["bg"]="white"
    R6["state"]="disable"
    A6["fg"]="red"
    A6["bg"]="white"
    A6["state"]="disable"
    fila2[2]="A"
    if fila2[0]=="A" and fila2[1]=="A" and fila2[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[2]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

        
def ROJO7():
    etiqueta=Label(ventana,text="O").place(x=10,y=110)
    R7["fg"]="red"
    R7["bg"]="white"
    R7["state"]="disable"
    A7["fg"]="red"
    A7["bg"]="white"
    A7["state"]="disable"
    fila3[0]="R"
    if fila3[0]=="R" and fila3[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="R" and fila2[0]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="R" and fila2[1]=="R" and fila3[0]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        


def AZUL7():
    etiqueta=Label(ventana,text="X").place(x=10,y=110)
    R7["fg"]="red"
    R7["bg"]="white"
    R7["state"]="disable"
    A7["fg"]="red"
    A7["bg"]="white"
    A7["state"]="disable"
    fila3[0]="A"
    if fila3[0]=="A" and fila3[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[0]=="A" and fila3[0]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[1]=="A" and fila3[0]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

        
def ROJO8():
    etiqueta=Label(ventana,text="O").place(x=30,y=110)
    R8["fg"]="red"
    R8["bg"]="white"
    R8["state"]="disable"
    A8["fg"]="red"
    A8["bg"]="white"
    A8["state"]="disable"
    fila3[1]="R"
    if fila3[0]=="R" and fila3[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[1]=="R" and fila2[1]=="R" and fila3[1]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        

    
def AZUL8():
    etiqueta=Label(ventana,text="X").place(x=30,y=110)
    R8["fg"]="red"
    R8["bg"]="white"
    R8["state"]="disable"
    A8["fg"]="red"
    A8["bg"]="white"
    A8["state"]="disable"
    fila3[1]="A"
    if fila3[0]=="A" and fila3[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
        
    if fila1[1]=="A" and fila2[1]=="A" and fila3[1]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
def ROJO9():
    etiqueta=Label(ventana,text="O").place(x=50,y=110)
    R9["fg"]="red"
    R9["bg"]="white"
    R9["state"]="disable"
    A9["fg"]="red"
    A9["bg"]="white"
    A9["state"]="disable"
    fila3[2]="R"
    if fila3[0]=="R" and fila3[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
        
        
    if fila1[2]=="R" and fila2[2]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        

        
    if fila1[0]=="R" and fila2[1]=="R" and fila3[2]=="R":
        Etiqueta= Label(ventana, text="Ganador Rojo")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        

    
def AZUL9():
    etiqueta=Label(ventana,text="X").place(x=50,y=110)
    R9["fg"]="red"
    R9["bg"]="white"
    R9["state"]="disable"
    A9["fg"]="red"
    A9["bg"]="white"
    A9["state"]="disable"
    fila3[2]="A"
    if fila3[0]=="A" and fila3[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[2]=="A" and fila2[2]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"
        
    if fila1[0]=="A" and fila2[1]=="A" and fila3[2]=="A":
        Etiqueta= Label(ventana, text="Ganador Azul")
        Etiqueta.place(x=10,y=140)

        R1["state"]="disable"
        R2["state"]="disable"
        R3["state"]="disable"
        R4["state"]="disable"
        R5["state"]="disable"
        R6["state"]="disable"
        R7["state"]="disable"
        R8["state"]="disable"
        R9["state"]="disable"
        A1["state"]="disable"
        A2["state"]="disable"
        A3["state"]="disable"
        A4["state"]="disable"
        A5["state"]="disable"
        A6["state"]="disable"
        A7["state"]="disable"
        A8["state"]="disable"
        A9["state"]="disable"

    

vocales=Label(ventana, text="GATO", bg="coral", fg="blue")
vocales.place(x=10,y=10)

#fila 1
#consonante=Label(ventana, text= "CASILLA 1 ", bg="coral", fg="blue")
#consonante.place(x=100,y=10)

R1=Button(ventana,text="ROJO",width=5,bg="red",command=ROJO1)
R1.place(x=100, y=50)
A1=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL1)
A1.place(x=150, y=50)

#consonante=Label(ventana, text= "CASILLA 2 ", bg="coral", fg="blue")
#consonante.place(x=200,y=10)

R2=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO2)
R2.place(x=230, y=50)
A2=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL2)
A2.place(x=280, y=50)

#consonante=Label(ventana, text= "CASILLA 3 ", bg="coral", fg="blue")
#consonante.place(x=300,y=10)

R3=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO3)
R3.place(x=350, y=50)
A3=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL3)
A3.place(x=400, y=50)
#fila 2
#consonante=Label(ventana, text= "CASILLA 4 ", bg="coral", fg="blue")
#consonante.place(x=50,y=250)

R4=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO4)
R4.place(x=100, y=100)
A4=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL4)
A4.place(x=150, y=100)

#consonante=Label(ventana, text= "CASILLA 5 ", bg="coral", fg="blue")
#consonante.place(x=180,y=250)

R5=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO5)
R5.place(x=230, y=100)
A5=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL5)
A5.place(x=280, y=100)

#consonante=Label(ventana, text= "CASILLA 6 ", bg="coral", fg="blue")
#consonante.place(x=300,y=250)


R6=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO6)
R6.place(x=350, y=100)
A6=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL6)
A6.place(x=400, y=100)

#fila 3
#consonante=Label(ventana, text= "CASILLA 7 ", bg="coral", fg="blue")
#consonante.place(x=50,y=320)

R7=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO7)
R7.place(x=100, y=150)
A7=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL7)
A7.place(x=150, y=150)

#consonante=Label(ventana, text= "CASILLA 8 ", bg="coral", fg="blue")
#consonante.place(x=180,y=320)

R8=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO8)
R8.place(x=230, y=150)
A8=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL8)
A8.place(x=280, y=150)

#consonante=Label(ventana, text= "CASILLA 9 ", bg="coral", fg="blue")
#consonante.place(x=300,y=320)


R9=Button(ventana,text="ROJO",width=5,bg="red", command=ROJO9)
R9.place(x=350, y=150)
A9=Button(ventana,text="AZUL",width=5,bg="blue", command=AZUL9)
A9.place(x=400, y=150)
