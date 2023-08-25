from tkinter import *

#DEFINIMOS LA CLASE 
class Contador():
    def __init__(self):
        #DIMENSIONES DE LA VENTANA A UTILIZAR 
        self.root = Tk()
        self.root.title("Contador")
        self.root.geometry("500x40")
        self.root.resizable(0, 0)
        self.miFrame = Frame(self.root)
        self.miFrame.pack()

        self.count = IntVar(value=0)

        #DEFINICION DE LABELS, ENTRADAS (INEDITABLES) Y BOTONES
        self.label = Label(self.miFrame, text="Contador:")
        self.txt1 = Entry(self.miFrame, textvariable=self.count, state="readonly", width=10, bd=5,insertwidth=1,justify="center")
        self.botonMas = Button(self.miFrame, text="Count Up", command=self.count_up)
        self.botonMenos = Button(self.miFrame, text="Count Down", command=self.count_down)
        self.reset_button = Button(self.miFrame, text="Reset", command=self.reset)

        #DISTRIBUCION DE LOS WIDGETS
        self.label.grid(row=0, column=0)
        self.txt1.grid(row=0, column=1)
        self.botonMas.grid(row=0, column=2)
        self.botonMenos.grid(row=0, column=3)
        self.reset_button.grid(row=0, column=4)

        self.root.mainloop()
 
    #FUNCION PARA HACER LA CUENTA CRECIENTE
    def count_up(self):
        self.count.set(self.count.get() + 1)

    #FUNCION PARA HACER LA CUENTA DECRECIENTE
    def count_down(self):
        self.count.set(self.count.get() - 1)
    
    #FUNCION PARA EL BOTON DE RESETEO
    def reset(self):
        self.count.set(0)

def main():
    f = Contador()
    return 0

if __name__ == "__main__":
    main()
