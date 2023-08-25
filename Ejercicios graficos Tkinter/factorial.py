from tkinter import *

#DEFINIMOS LA CLASE 
class Factorial ():
    def __init__(self):
        #DIMENSIONES DE LA VENTANA A UTILIZAR 
        self.root = Tk ()
        self.root.title ("Factorial")
        self.root.geometry("500x50")
        self.root.resizable(0,0)
        self.miFrame = Frame(self.root)
        self.miFrame.pack ()

        self.n1= IntVar(value=0)
        self.n2 = StringVar()

        #DEFINICION DE LABELS, ENTRADAS (INEDITABLES) Y BOTON
        self.lb1 = Label (self.miFrame, text="n")
        self.txt1 = Entry(self.miFrame, textvariable=self.n1, state="readonly", width=15, bd=5,insertwidth=1,justify="center")
        self.lb2 = Label (self.miFrame, text="Factorial(n)")
        self.txt2 = Entry (self.miFrame, textvariable=self.n2, state="readonly", width=15, bd=5,insertwidth=1,justify="center")
        self.btn = Button (self.miFrame,text="Siguiente", width=10, command=self.num_factorial)

        #DISTRIBUCION DE LOS WIDGETS 
        self.lb1.grid (row= 0, column=0)
        self.txt1.grid (row=0, column= 1)
        self.lb2.grid (row=0, column=2)
        self.txt2.grid (row=0, column=3)
        self.btn.grid (row=0, column=4)

        self.root.mainloop()    
    
    #FUNCION PARA CALCULAR EL FACTORIAL
    def num_factorial (self):
        self.n1.set (self.n1.get()+1) 
        
        #"FOR" PARA PASAR AL SIGUIENTE NUMERO 
        fact = 1
        for i in range (1,(self.n1.get())+1):
            fact = fact * i
            self.n2.set(fact)

def main ():
    f = Factorial()
    return 0
if __name__ == "__main__":
    main()

        