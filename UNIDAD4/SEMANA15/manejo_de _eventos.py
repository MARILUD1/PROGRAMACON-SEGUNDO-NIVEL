# registro para trabajadores de una empresa
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


# Función para obtener la fecha automática actual (dd/mm/aaaa)
def obtener_fecha_actual():
    hoy = datetime.now()
    return hoy.strftime("%d/%m/%Y")

# Función para agregar un nuevo evento de asistencia a la lista
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

# Función para agregar una nueva tarea a la lista de tareas
def agregar_tarea(event=None):
    tarea = entry_tarea.get()
    if tarea:
        tareas_treeview.insert('', 'end', values=(tarea, "Ahora coloque su observación"))
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingresar las actividades realizadas.")

# Función para marcar una tarea como completada
def marcar_completada(event=None):
    seleccion = tareas_treeview.selection()
    if seleccion:
        for item in seleccion:
            tareas_treeview.item(item, values=(tareas_treeview.item(item, 'values')[0], "Registro de actividades realizadas"))

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    seleccion = tareas_treeview.selection()
    if seleccion:
        for item in seleccion:
            tareas_treeview.delete(item)
    else:
        messagebox.showwarning("Advertencia", "Seleccionar la actividad que desea eliminar.")

# Función para agregar observaciones a una tarea seleccionada
def agregar_observacion():
    seleccion = tareas_treeview.selection()
    observacion = entry_observacion.get()
    if seleccion and observacion:
        for item in seleccion:
            tarea, estado = tareas_treeview.item(item, 'values')
            tareas_treeview.item(item, values=(tarea, observacion))  # Agrega la observación a la tarea
        entry_observacion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debe seleccionar una actividad y agregar una observación.")

# Configuración de la ventana principal
Appregistro = tk.Tk()
Appregistro.title("Registro de Asistencia y Registro de actividad realizada")
Appregistro.geometry("800x750")
Appregistro.configure(bg="light blue")  # Fondo celeste para la ventana principal

# Frame superior para los campos de entrada y botones
frame_entrada_botones = tk.Frame(Appregistro, bg="light green")
frame_entrada_botones.pack(pady=10)

# Frame para los campos de entrada
frame_entrada = tk.Frame(frame_entrada_botones, bg="yellow")
frame_entrada.grid(row=0, column=0, padx=10, pady=10)

# Etiquetas y entradas de datos de asistencia
tk.Label(frame_entrada, text="ID Empleado:", bg="yellow").grid(row=0, column=0, padx=4, pady=4)
entry_id = tk.Entry(frame_entrada)
entry_id.grid(row=0, column=1, padx=4, pady=4)

tk.Label(frame_entrada, text="Hora:", bg="yellow").grid(row=1, column=0, padx=4, pady=4)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=4, pady=4)

tk.Label(frame_entrada, text="Entrada o salida:", bg="yellow").grid(row=2, column=0, padx=4, pady=4)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=4, pady=4)

# Frame para los botones de acción
frame_botones = tk.Frame(frame_entrada_botones, bg="light blue")
frame_botones.grid(row=0, column=1, padx=10, pady=10)

# Botones para agregar, limpiar y salir de la sección de eventos de asistencia
btn_agregar = tk.Button(frame_botones, text="Agregar Datos", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Borrar Datos", command=limpiar_campos)
btn_limpiar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# Frame para la lista de eventos (TreeView)
frame_lista = tk.Frame(Appregistro, bg="light blue")  # Fondo celeste para el contenedor frame
frame_lista.pack(pady=10)

# Configuración del TreeView para mostrar los eventos de asistencia
treeview = ttk.Treeview(frame_lista, columns=("Fecha", "ID Empleado", "Hora", "Entrada o salida"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("ID Empleado", text="ID Empleado")
treeview.heading("Hora", text="Hora")
treeview.heading("Entrada o salida", text="Entrada o Salida")
treeview.pack()

# Frame para la lista de tareas (TreeView)
frame_tareas = tk.Frame(Appregistro, bg="orange")
frame_tareas.pack(pady=20)

# Etiqueta y entrada de tareas
tk.Label(frame_tareas, text="Informe diario:").grid(row=0, column=0, padx=4, pady=4)
entry_tarea = tk.Entry(frame_tareas, width=50)
entry_tarea.grid(row=0, column=1, padx=4, pady=4)
entry_tarea.bind("<Return>", agregar_tarea)  # Añadir tarea con Enter

# Botones para agregar y eliminar tareas
btn_agregar_tarea = tk.Button(frame_tareas, text="Agregar actividad realizada", command=agregar_tarea)
btn_agregar_tarea.grid(row=0, column=2, padx=5)

btn_eliminar_tarea = tk.Button(frame_tareas, text="Eliminar actividad realizada", command=eliminar_tarea)
btn_eliminar_tarea.grid(row=0, column=3, padx=5)

# Configuración del TreeView para mostrar las tareas
tareas_treeview = ttk.Treeview(frame_tareas, columns=("Actividad realizada", "Observaciones"), show="headings")
tareas_treeview.heading("Actividad realizada", text="Actividad realizada")
tareas_treeview.heading("Observaciones", text="Observaciones")
tareas_treeview.grid(row=1, column=0, columnspan=4, padx=4, pady=10)

# Frame para agregar observaciones
frame_observacion = tk.Frame(Appregistro)
frame_observacion.pack(pady=10)

tk.Label(frame_observacion, text="Observación:").grid(row=0, column=0, padx=4, pady=4)
entry_observacion = tk.Entry(frame_observacion, width=50)
entry_observacion.grid(row=0, column=1, padx=4, pady=4)

# Botón para agregar observación a una actividad seleccionada
btn_agregar_observacion = tk.Button(frame_observacion, text="Agregar Observación", command=agregar_observacion)
btn_agregar_observacion.grid(row=0, column=2, padx=5)

# Asignar evento de doble clic para marcar tareas como completadas
tareas_treeview.bind("<Double-1>", marcar_completada)

# Iniciar el loop principal de la aplicación
Appregistro.mainloop()
