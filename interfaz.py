from tkinter import *



interfaz = Tk()
interfaz.title("Afinador de guitarra")
interfaz.geometry("400x500")


def apretar():
    lblCuerda = Label(interfaz, text="6ta Cuerda").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="80Hz").pack()
    lblApretar = Label(interfaz, text="Es necesario apretar").pack()

def aflojar():
    lblCuerda = Label(interfaz, text="6ta Cuerda").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="80Hz").pack()
    lblAflojar = Label(interfaz, text="Es necesario aflojar").pack()

def correcto():
    lblCuerda = Label(interfaz, text="6ta Cuerda").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="80Hz").pack()
    lblCorreto = Label(interfaz, text="La frecuencia es correcta").pack()

def iniciar():
    apretar()
    aflojar()
    correcto()
    

boton = Button(interfaz, text="Iniciar", command=iniciar)
boton.pack()

interfaz.mainloop()
