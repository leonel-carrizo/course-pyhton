import tkinter
from tkinter import *
from tkinter import ttk

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)

window = Tk()  # inicio del programa
window.title('Inicio')  # titulo de la ventana
window.resizable(1, 1)  # redimencionar
window.geometry('400x400')  # dimensiona la ventana principal
window.config(bg='blue')  # background de la ventana

c = Frame()  # se establece el contenedor o frame
c.grid()  # empaquetar el Frame para que pueda fuinsionar
c.config(bg='red', width=100, height=100, relief='solid', bd=2, cursor='hand2')

lb = tkinter.Label(c, text='Prueba de Titulo',
                   width=10, height=10, padx=10, pady=10)
lb.pack(padx=10, pady=10)

window.mainloop()
