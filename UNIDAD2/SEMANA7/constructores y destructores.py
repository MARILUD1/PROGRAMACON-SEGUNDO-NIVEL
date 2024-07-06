class Carpeta:
    def __init__(self, nombre, apellidos, correo, ciudad):  # Constructor
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.ciudad = ciudad
        print(f"Constructor Carpeta: Carpeta creada con {self.nombre}, {self.apellidos}, {self.correo}, {self.ciudad}. Datos.")

    def __del__(self):#Destructor
        print(f"Destructor Carpeta: {self.nombre} {self.apellidos}, {self.correo}, {self.ciudad} ha sido eliminado.")

    def mostrar_informacion(self):
        return f"Carpeta {self.nombre}, {self.apellidos}, {self.correo}, {self.ciudad}" #Devolver estos atributos

# Crear el objeto Carpeta
print("Creando el objeto Carpeta...")
archivos = Carpeta("Carlos", "Enriquez", "juan.perez@example.com", "Madrid")

# Mostrar informacion del objeto Carpeta
print(archivos.mostrar_informacion())

# Eliminar el objeto explícitamente para demostrar el uso del destructor
print("Eliminando la Carpeta...")
del archivos # Se eliminara la carpeta
