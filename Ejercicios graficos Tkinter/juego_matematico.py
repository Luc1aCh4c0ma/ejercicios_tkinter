"""ESTE ULTIMO EJERCICIO NO ESTÁ TERMINADO PERO LO INTENTÉ JAJAJ TIENE ALGUNOS ERRORES QUE NO LLEGUÉ A CORREGIR"""

import tkinter as tk
from tkinter import messagebox
import random

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Matemático")
        self.root.resizable (0,0)
        self.root.geometry ("480x250")

        self.juegos = 0
        self.buenos = 0
        self.malos = 0
        self.tiempo_restante = 180

        self.difficulty = tk.StringVar(value="easy")
        self.operation = tk.StringVar(value="")

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.juegos_label = tk.Label(self.root, text="Juegos: 0")
        self.buenos_label = tk.Label(self.root, text="Buenos: 0")
        self.malos_label = tk.Label(self.root, text="Malos: 0")
        self.operation_label = tk.Label(self.root, text="?")
        self.num1_entry = tk.Entry(self.root, state= "readonly", width=20,justify="center")
        self.num2_entry = tk.Entry(self.root, state= "readonly", width=20,justify="center")
        self.result_entry = tk.Entry(self.root,width=15, bd=5,insertwidth=1,justify="center")
        self.new_number_button = tk.Button(self.root, text="Nuevo Numero", command=self.new_game)
        self.result_button = tk.Button(self.root, text="Resultado", command=self.check_result)
        self.easy_radio = tk.Radiobutton(self.root, text="Fácil", variable=self.difficulty, value="easy")
        self.medium_radio = tk.Radiobutton(self.root, text="Medio", variable=self.difficulty, value="medium")
        self.hard_radio = tk.Radiobutton(self.root, text="Difícil", variable=self.difficulty, value="hard")
        self.add_radio = tk.Radiobutton(self.root, text="Sumar", variable=self.operation, value="+")
        self.subtract_radio = tk.Radiobutton(self.root, text="Restar", variable=self.operation, value="-")
        self.multiply_radio = tk.Radiobutton(self.root, text="Multiplicar", variable=self.operation, value="*")
        self.divide_radio = tk.Radiobutton(self.root, text="Dividir", variable=self.operation, value="/")
        self.timer_label = tk.Label(self.root, text="Tiempo restante: ")

        self.update_timer()

        #DISTRIBUCION DE WIDGET
        self.juegos_label.grid(row=6, column=3)
        self.buenos_label.grid(row=7, column=3)
        self.malos_label.grid(row=8, column=3)
        self.operation_label.grid(row=0, column=1)
        self.num1_entry.grid(row=0, column=0)
        self.num2_entry.grid(row=0, column=2)
        self.result_entry.grid(row=3, column=3)
        self.new_number_button.grid(row=1, column=3)
        self.result_button.grid(row=4, column=3)
        self.easy_radio.grid(row=8, column=0)
        self.medium_radio.grid(row=8, column=1)
        self.hard_radio.grid(row=8, column=2)
        self.add_radio.grid(row=2, column=0)
        self.subtract_radio.grid(row=3, column=0)
        self.multiply_radio.grid(row=4, column=0)
        self.divide_radio.grid(row=5, column=0)
        self.timer_label.grid(row=7, column=0)



    def new_game(self):
        self.num1_entry.config(state="normal")
        self.num2_entry.config(state="normal")

        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)

        if self.difficulty.get() == "easy":
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            self.tiempo_restante = 180
        elif self.difficulty.get() == "medium":
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            self.tiempo_restante = 120
        else:
            num1 = random.randint(0, 1000)
            num2 = random.randint(0, 1000)
            self.tiempo_restante = 60

        self.num1_entry.insert(0, str(num1))
        self.num2_entry.insert(0, str(num2))

        self.num1_entry.config(state="readonly")
        self.num2_entry.config(state="readonly")

        self.operation.set(random.choice(["+", "-", "*", "/"]))

        self.update_timer()

    def check_result(self):
     num1 = int(self.num1_entry.get())
     num2 = int(self.num2_entry.get())
     entered_operation = self.operation.get()
     expected_result = eval(f"{num1} {entered_operation} {num2}")
     entered_result = self.result_entry.get()

     if not entered_result.replace(".", "", 1).lstrip('-').isdigit():
        messagebox.showwarning("Error", "Ingresa un valor numérico válido en el campo de resultado.")
        return

     entered_result = float(entered_result)

     if entered_result == expected_result:
        self.juegos += 1
        self.buenos += 1
        self.juegos_label.config(text=f"Juegos: {self.juegos}")
        self.buenos_label.config(text=f"Buenos: {self.buenos}")
     else:
        self.juegos += 1
        self.malos += 1
        self.juegos_label.config(text=f"Juegos: {self.juegos}")
        self.malos_label.config(text=f"Malos: {self.malos}")

     self.new_game()

    def update_timer(self):
        self.timer_label.config(text=f"Tiempo restante: {self.tiempo_restante} segundos")
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo. ¡Perdiste!")
            self.new_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
