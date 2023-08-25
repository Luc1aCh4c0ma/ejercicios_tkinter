from tkinter import *

def agregar_pelicula():
    pelicula = entry_pelicula.get()
    if pelicula:
        list_peliculas.insert(END, pelicula)
        entry_pelicula.delete(0, END)

# DIMENSIONES DE LA APP
root = Tk()
root.title("Películas")
root.geometry("300x180")
root.resizable(0, 0)

# LABELS
label_ingresar = Label(root, text="Escribe el título de una película:")
label_peliculas = Label(root, text="Películas")

# ENTRADA PARA INGRESAR LA PELICULA
entry_pelicula = Entry(root,width=20, bd=5,insertwidth=1,justify="center")

# LISTBOX PARA ALMACENAR LAS PELICULAS 
list_peliculas = Listbox(root, width=15, height=7, justify= "center")

# BOTON PARA GUARDAR LAS MISMAS 
btn_anadir = Button(root, text="Añadir", command=agregar_pelicula)

# DISTRIBUCION DE LOS WIDGETS UTILIZANDO GRID
label_ingresar.grid(row=0,column=0)
entry_pelicula.grid(row=1,column=0)
btn_anadir.grid(row=2,column=0)
label_peliculas.grid(row=0,column=2)
list_peliculas.grid(row=1,column=2)

root.mainloop()
