from tkinter import *
import random

#DEFINIMOS LA CLASE 
class GeneradorDeNumero:
    def __init__(self, root):
        #DIMENSIONES DE LA VENTANA A UTILIZAR 
        self.root = root
        self.root.title("Generador de Números")
        self.root.geometry("250x100")
        self.root.resizable(0, 0)
        
        #DEFINIMOS LABELS, SPINBOXS, ENTRADA Y BOTON
        self.label1 = Label(root, text="Número 1:")
        self.spinbox1 = Spinbox(root, from_=1, to=100)
        self.label2 = Label(root, text="Número 2:")
        self.spinbox2 = Spinbox(root, from_=1, to=100)
        self.label3 = Label(root, text="Número Generado:")
        self.num = StringVar()
        self.resultado = Entry(root, textvariable=self.num, state="readonly")
        self.botonGen = Button(root, text="Generar", command=self.generar_numero)

        #DISTRIBUCION DE LOS WIDGETS 
        self.label1.grid (row=0, column=0)
        self.label2.grid (row=1,column=0)
        self.label3.grid (row=2, column= 0)
        self.spinbox1.grid (row=0, column=2)
        self.spinbox2.grid (row=1, column=2)
        self.resultado.grid(row=2, column=2)
        self.botonGen.grid (row=3, column=2)
    
    #FUNCION PARA GENERAR EL NUMERO ALEATORIO
    def generar_numero(self):
        num1 = int(self.spinbox1.get())
        num2 = int(self.spinbox2.get())
        generated_num = random.randint(min(num1, num2), max(num1, num2))
        self.num.set(str(generated_num))

if __name__ == "__main__":
    root = Tk()
    app = GeneradorDeNumero(root)
    root.mainloop()
