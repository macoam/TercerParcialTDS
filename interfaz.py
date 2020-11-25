from tkinter import *



interfaz = Tk()
interfaz.title("Afinador de guitarra")
interfaz.geometry("400x500")


def apretar():
    lblCuerda = Label(interfaz, text="5ta (La) - 110Hz)").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="107.6Hz").pack()
    lblApretar = Label(interfaz, text="Es necesario apretar la cuerda").pack()

def aflojar():
    lblCuerda = Label(interfaz, text="5ta (La) - 110Hz)").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="114.6Hz").pack()
    lblAflojar = Label(interfaz, text="Es necesario aflojar la cuerda").pack()

def correcto():
    lblCuerda = Label(interfaz, text="5ta (La) - 110Hz)").pack()
    lblFrecuencia = Label(interfaz, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(interfaz, text="110.4Hz").pack()
    lblCorreto = Label(interfaz, text="La afinación es correcta").pack()

def iniciar():
    apretar()
    aflojar()
    correcto()
    

boton = Button(interfaz, text="Afinar", command=iniciar)
boton.pack()

interfaz.mainloop()
