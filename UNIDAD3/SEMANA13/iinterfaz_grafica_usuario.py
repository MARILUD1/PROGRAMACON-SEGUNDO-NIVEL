#Interfaz grafica de usuario (GUI)

import tkinter as tk
from tkinter import messagebox

# Función para agregar un elemento a la lista
def agregar_dato():
    id_usuario = entrada_id.get()
    dato = entrada_texto.get()
    edad = entrada_edad.get()

    # Validación de los campos
    if id_usuario and dato and edad:
        if edad.isdigit():  # Verificar que la edad sea un número
            lista_datos.insert(tk.END, f"ID: {id_usuario} - Dato: {dato} - Edad: {edad}")
            entrada_id.delete(0, tk.END)
            entrada_texto.delete(0, tk.END)
            entrada_edad.delete(0, tk.END)
        else:
            messagebox.showerror("Intento fallido", "Colocar solo numeros.")
    else:
        messagebox.showwarning("Aviso", "Para agregar llenar todos los campos.")

# Función para limpiar la lista
def borrar_lista():
    lista_datos.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de usuarios")

# Etiqueta para el ID
etiqueta_id = tk.Label(ventana, text="Ingresar el número de cédula de usuarios:")
etiqueta_id.pack(pady=5)

# Campo de texto para el ID
entrada_id = tk.Entry(ventana, width=40)
entrada_id.pack(pady=5)

# Etiqueta para el dato
etiqueta_dato = tk.Label(ventana, text="Ingresar nombres y apellidos de cada usuario:")
etiqueta_dato.pack(pady=5)

# Campo de texto para el dato
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Etiqueta para la edad
etiqueta_edad = tk.Label(ventana, text="Ingresar la edad de cada usuario:")
etiqueta_edad.pack(pady=5)

# Campo de texto para la edad
entrada_edad = tk.Entry(ventana, width=40)
entrada_edad.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para borrar la lista
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_lista)
boton_borrar.pack(pady=5)



# Empezar a registrar
ventana.mainloop()
