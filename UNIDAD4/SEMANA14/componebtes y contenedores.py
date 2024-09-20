import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#Función para obtener la fecha automatica actual  dd/mm/aaaa
def obtener_fecha_actual():
    hoy = datetime.now()
    return hoy.strftime("%d/%m/%Y")

# Función para agregar un nuevo evento a la lista
def agregar_evento():
    empleado_id = entry_id.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if empleado_id and hora and descripcion:
        fecha_actual = obtener_fecha_actual()
        treeview.insert('', 'end', values=(fecha_actual, empleado_id, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar completos.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para salir de la aplicación
def salir():
    Appregistro.quit()

# Configuración de la ventana principal
Appregistro = tk.Tk()
Appregistro.title("Registro de Asistencia")
Appregistro.geometry("800x700")

# Frame para la lista de eventos (TreeView)
frame_lista = tk.Frame(Appregistro)
frame_lista.pack(pady=10)

# Configuración del TreeView para mostrar los eventos
treeview = ttk.Treeview(frame_lista, columns=("Fecha","ID Empleado", "Hora", "Entrada o salida"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("ID Empleado", text="ID Empleado")
treeview.heading("Hora", text="Hora")
treeview.heading("Entrada o salida", text="Entrada o Salida")
treeview.pack()
# Frame para los campos de entrada y etiquetas
frame_entrada = tk.Frame(Appregistro)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="ID Empleado:").grid(row=0, column=0, padx=4, pady=4)
entry_id = tk.Entry(frame_entrada)
entry_id.grid(row=0, column=1, padx=4, pady=4)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=4, pady=4)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=4, pady=4)

tk.Label(frame_entrada, text="Entrada o salida:").grid(row=2, column=0, padx=4, pady=4)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=4, pady=4)

# Frame para los botones de acción
frame_botones = tk.Frame(Appregistro)
frame_botones.pack(pady=10)

# Botones para agregar, limpiar y salir
btn_agregar = tk.Button(frame_botones, text="Agregar Datos", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Borrar Datos", command=limpiar_campos)
btn_limpiar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# Iniciar el loop principal de la aplicación
Appregistro.mainloop()
