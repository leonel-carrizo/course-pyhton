# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Ejercicio 2 Clase 10')
window.geometry('400x300')
window.config(background='yellow')
window.resizable(0, 0)

# Finction exit


def salir():
    quit()


# Top Taget
l = tkinter.Label(window, text='SELECTOR DE COMIDA', justify='center',
                  font='helvetica 12 bold', fg='black', bg='yellow', bd=2, border=1, relief='solid', width=30, padx=10, pady=8)
l.pack(pady=20)


# Container
contenedor = tkinter.LabelFrame(
    text='Elija su Comida Favorita', font='helvetica 12 bold', labelanchor='n', bg='yellow', border=3, relief='solid', bd=1)
contenedor.pack(pady=20, ipadx=80, ipady=40)

# Selectable
selected = IntVar()
lb = tkinter.Label(contenedor, text='Arroz con Pollo',
                   font='helvetica 10 bold', bg='yellow')
lb.place(x=12, y=4)

lb1 = tkinter.Label(contenedor, text='Pasta con Carne',
                    font='helvetica 10 bold', bg='yellow')
lb1.place(x=6, y=30)

lb2 = tkinter.Label(contenedor, text='Con Bebida',
                    font='helvetica 10 bold', bg='yellow')
lb2.place(x=35, y=60)

r = tkinter.Radiobutton(contenedor, bg='yellow', value=1,
                        variable=selected, cursor='hand2')
r.pack(pady=2)

r1 = tkinter.Radiobutton(contenedor, bg='yellow', value=2,
                         variable=selected, cursor='hand2')
r1.pack(pady=2)

c = tkinter.Checkbutton(contenedor, bg='yellow', cursor='hand1')
c.pack()


# Button Exit
btn = tkinter.Button(contenedor, text='Salir', font='helvetica 10 bold', bd=2,
                     relief='groove', border=3, bg='aquamarine', command=salir, cursor='hand2')
btn.place(x=155, y=120)


window.mainloop()
