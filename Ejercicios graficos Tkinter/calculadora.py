from tkinter import *

#OPERACIONES APLICADAS
def calculadora(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operacion == "+":
            result = num1 + num2
        elif operacion == "-":
            result = num1 - num2
        elif operacion == "*":
            result = num1 * num2
        elif operacion == "/":
           if num2 != 0: 
                result = num1 / num2
           else:
                result_var.set("Error")
                return
        elif operacion == "%":
            result = num1 % num2
        result_var.set(str(result))
    except ValueError:
        result_var.set("Error")

#FUNCION PARA EL BOTON CLEAR
def limpiar():
    entry_num1.delete(0, END)
    entry_num2.delete(0, END)
    result_var.set("")

#DEFINIMOS LAS DIMENSIONES DE LA CALCULADORA
root = Tk()
root.title("Calculadora")
root.geometry("210x180")
root.resizable(0, 0)

# LABELS
label_num1 = Label(root, text="Primer número:")
label_num2 = Label(root, text="Segundo número:")
label_result = Label(root, text="Resultado:")

# ENTRADAS Y RESULTADO
entry_num1 = Entry(root, width=10, bd=5,insertwidth=1,justify="center")
entry_num2 = Entry(root, width=10, bd=5,insertwidth=1,justify="center")
result_var = StringVar()
entry_result = Entry(root, textvariable=result_var, state="readonly", width=10, bd=5,insertwidth=1,justify="center")

# BOTONES
button_add = Button(root, text="+",width=10, command=lambda: calculadora("+"))
button_subtract = Button(root, text="-",width=10, command=lambda: calculadora("-"))
button_multiply = Button(root, text="*",width=10, command=lambda: calculadora("*"))
button_divide = Button(root, text="/",width=10, command=lambda: calculadora("/"))
button_modulo = Button(root, text="%",width=10, command=lambda: calculadora("%"))
button_clear = Button(root, text="CLEAR",width=10, command=limpiar)

# UBICACION DE LOS COMPONENTES UTILIZANDO GRID
label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
label_result.grid(row=2, column=0)
entry_result.grid(row=2, column=1)
button_add.grid(row=3, column=0)
button_subtract.grid(row=3, column=1)
button_multiply.grid(row=4, column=0)
button_divide.grid(row=4, column=1)
button_modulo.grid(row=5, column=0)
button_clear.grid(row=5, column=1)

root.mainloop()

