from tkinter import *

#DEFINIMOS DIMENSIONES DEL CONTADOR COMENZANDOLO POR EL NUMERO 88
ventana = Tk ()
ventana.title ("ContDecreciente")
ventana.resizable (0,0)
contador = IntVar(value=88)
#ENTRADA INEDITABLE DE LOS NUMEROS
salida = Entry (ventana, textvariable=contador, state="readonly", width=10, bd=5,insertwidth=1,justify="center")

#LABELS
cartel = Label (ventana, text= "CONTADOR")

#DISTRIBUCION DE LOS WIDGETS UTILIZANDO GRID 
cartel.grid (row=0, column= 0, sticky="w", padx=5, pady=5)
salida.grid (row=0, column= 1, padx=5, pady= 5)
salida.config (justify= "center")

#FUNCION DE DECRECIMIENTO
def restar ():
    contador.set (int(contador.get())-1)

#BOTON PARA EJECUTAR DICHO DECRECIMIENTO
boton = Button(ventana, text= "-", command=restar)
boton.grid (row=0, column=2, padx=5, pady=5)

ventana.mainloop()