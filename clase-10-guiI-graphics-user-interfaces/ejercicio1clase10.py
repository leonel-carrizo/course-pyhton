# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio. Al principio no tiene que haber una opción seleccionada.
import tkinter
from tkinter import *

# Root
window = tkinter.Tk()
window.title('Ejercicio 1 Tema 10')
window.geometry('300x400')
window.resizable(0, 0)
window.config(background='blue')

# Functions


def reset():
    selected.set(0)


def salir():
    quit()


# Tagget
lb = tkinter.Label(window,
                   text='Please select an option:',
                   font='helvetica 15 bold', relief=GROOVE,
                   bd=2, bg='blue', fg='white', width=30, pady=10)
lb.pack(padx=10, pady=45)

# RadiosButtom
selected = IntVar()
r1 = tkinter.Radiobutton(window, text='Opcion 1', bg='blue',
                         font='helvetica 12 bold', value=1, variable=selected)
r1.pack(pady=2)
r2 = tkinter.Radiobutton(window, text='Opcion 2', bg='blue',
                         font='helvetica 12 bold', value=2, variable=selected)
r2.pack(pady=2)
r3 = tkinter.Radiobutton(window, text='Opcion 3', bg='blue',
                         font='helvetica 12 bold', value=3, variable=selected)
r3.pack(pady=2)
r4 = tkinter.Radiobutton(window, text='Opcion 4', bg='blue',
                         font='helvetica 12 bold', value=4, variable=selected)
r4.pack(pady=2)

# Buttons
btn = tkinter.Button(text='Reset', font='helvetica 15',
                     command=reset, bg='green', padx=1)
btn.pack(side='left', padx=20)
btn2 = tkinter.Button(text='Exit', font='helvetica 15',
                      command=salir, bg='red', padx=10)
btn2.pack(side='right', padx=20)


window.mainloop()
