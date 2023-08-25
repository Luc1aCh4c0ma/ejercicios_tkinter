from tkinter import *

#DEFINIMOS DIMENSIONES DEL CONTADOR
ventana = Tk ()
ventana.title ("ContCreciente")
ventana.resizable (0,0)
contador = IntVar()

#ENTRADA INEDITABLE DE LOS NUMEROS
salida = Entry (ventana, textvariable=contador, state="readonly", width=10, bd=5,insertwidth=1,justify="center")

#LABEL
cartel = Label (ventana, text= "CONTADOR")

#DISTRIBUCION DE LOS WIDGETS UTILIZANDO GRID
cartel.grid (row=0, column= 0, sticky="w", padx=5, pady=5)
salida.grid (row=0, column= 1, padx=5, pady= 5)
salida.config (justify= "center")

#FUNCION DE INCREMENTO
def sumar ():
    contador.set (int(contador.get())+1)

#BOTON PARA EJECUTAR DICHO INCREMENTO
boton = Button(ventana, text= "+", command=sumar)
boton.grid (row=0, column=2, padx=5, pady=5)

ventana.mainloop()