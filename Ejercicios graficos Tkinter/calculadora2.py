from tkinter import *

#FUNCIONES DE LAS OPERACIONES
def calcular():
   try:
        num1 = float(valor1_var.get())
        num2 = float(valor2_var.get())
        operacion = operacion_var.get()
        if operacion == "Sumar":
            result = num1 + num2
        elif operacion == "Restar":
            result = num1 - num2
        elif operacion == "Multiplicar":
            result = num1 * num2
        elif operacion == "Dividir":
           if num2 != 0: 
                result = num1 / num2
           else:
                resultado_var.set("Error")
                return
        resultado_var.set(str(result))
   except ValueError:
        resultado_var.set("Error")

#DIMENSIONES DE LA CALCULADORA
root = Tk()
root.title("Calculadora 2")
root.resizable (0,0)
root.geometry ("250x200")

#DEFINIMOS LAS VARIABLES PARA ALMACENAR LOS VALORES 
valor1_var = StringVar()
valor2_var = StringVar()
resultado_var = StringVar()
operacion_var = StringVar()
operacion_var.set("Sumar")

#LABELS, ENTRADAS, RADIOBUTTONS, BOTON 
label_valor1 = Label(root, text="Valor 1:")
label_valor2 = Label(root, text="Valor 2:")
label_operacion = Label(root, text="Operaciones:")
label_resultado = Label(root, text="Resultado:")
entry_valor1 = Entry(root, textvariable=valor1_var, width=10, bd=5,insertwidth=1,justify="center")
entry_valor2 = Entry(root, textvariable=valor2_var, width=10, bd=5,insertwidth=1,justify="center")
entry_resultado = Entry(root, textvariable=resultado_var, state="readonly", width=10, insertwidth=1,justify="center")
radio_sumar = Radiobutton(root, text="Sumar", variable=operacion_var, value="Sumar")
radio_restar = Radiobutton(root, text="Restar", variable=operacion_var, value="Restar")
radio_multiplicar = Radiobutton(root, text="Multiplicar", variable=operacion_var, value="Multiplicar")
radio_dividir = Radiobutton(root, text="Dividir", variable=operacion_var, value="Dividir")
boton_calcular = Button(root, text="Calcular", command=calcular)

#DISTRIBUCION DE LOS WIDGETS
label_valor1.grid(row=1, column=0)
label_valor2.grid(row=3, column=0)
label_operacion.grid(row=0, column=2)
label_resultado.grid(row=5, column=0)
entry_valor1.grid(row=1, column=1)
entry_valor2.grid(row=3, column=1)
entry_resultado.grid(row=5, column=1)
radio_sumar.grid(row=2, column=2)
radio_restar.grid(row=3, column=2)
radio_multiplicar.grid(row=4, column=2)
radio_dividir.grid(row=5, column=2)
boton_calcular.grid(row=7, column=1)

root.mainloop()
