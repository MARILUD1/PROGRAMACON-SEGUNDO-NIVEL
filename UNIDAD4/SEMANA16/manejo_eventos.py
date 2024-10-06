import tkinter as tk
from tkinter import messagebox


class TareaApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Registro de Tareas')


        # Configurar el tamaño de la ventana y color de fondo
        self.root.geometry('700x600')
        self.root.configure(bg='green')


        # Lista para almacenar las tareas
        self.tareas = []

        # Crear el campo de entrada para añadir nuevas tareas
        self.entrada_tarea = tk.Entry(self.root, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.focus()  # Coloca el cursor en el campo de entrada

        # Crear un Frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)


        # Botón para añadir tareas
        btn_añadir = tk.Button(frame_botones, text='Añadir Tarea', command=self.añadir_tarea)
        btn_añadir.grid(row=0, column=0, padx=10)


        # Botón para marcar como completada
        btn_completar = tk.Button(frame_botones, text='Marcar como Completada', command=self.marcar_completada)
        btn_completar.grid(row=0, column=1, padx=10)

        # Botón para eliminar tarea
        btn_eliminar = tk.Button(frame_botones, text='Eliminar Tarea', command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=10)

        # Crear la lista para mostrar las tareas
        self.lista_tareas = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.lista_tareas.pack(pady=20)

        # Asociar eventos de teclado
        self.root.bind('<Return>', lambda event: self.añadir_tarea())  # Enter para añadir tarea
        self.root.bind('<Delete>', lambda event: self.eliminar_tarea())  # Delete para eliminar tarea
        self.root.bind('<c>', lambda event: self.marcar_completada())  # "c" para completar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Escape para cerrar aplicación

    def añadir_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:  # Si el campo no está vacío
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)  # Añadir tarea a la lista gráfica
            self.entrada_tarea.delete(0, tk.END)  # Limpiar campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def marcar_completada(self):
        try:
            index = self.lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
            tarea_completada = self.tareas[index] + " ✔"  # Marcar la tarea con un símbolo de completado
            self.lista_tareas.delete(index)
            self.lista_tareas.insert(index, tarea_completada)  # Reemplazar tarea en la lista
            self.tareas[index] = tarea_completada
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            index = self.lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
            del self.tareas[index]  # Eliminar de la lista interna
            self.lista_tareas.delete(index)  # Eliminar de la lista gráfica
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")


# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TareaApp(root)
    root.mainloop()














