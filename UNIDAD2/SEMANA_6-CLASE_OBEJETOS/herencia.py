#herencia
class Persona: #plantilla parar crear el objeto
    #clase Padre
    def __init__(self, nombre, apellido, edad): #atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Doctor(Persona): #Classe hija
    def __init__(self, nombre, apellido, edad, nacionalidad):
        super().__init__(nombre, apellido, edad)
        self.nacionalidad = nacionalidad #atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre}, {self.apellido}, {self.edad} años, de nacionalidad {self.nacionalidad}"

# # Crear el objeto de Doctor  con atributos heredador y propio
profesion  = Doctor("Esteban", "Torres", 36, "Ecuatoriano")

# Mostrar la información del doctor
print(profesion.mostrar_informacion())
class Chef(Persona):
    def __init__(self, nombre, apellido, edad, nacionalidad):
        super().__init__(nombre, apellido, edad)
        self.nacionalidad = nacionalidad #atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre}, {self.apellido}, {self.edad} años, de nacionalidad {self.nacionalidad}"

# Crear el objeto de Chef con atrubutos heredador y propio
profesion  = Chef("Lucia", "Rodriguez", 28, "Italiana")

# Mostrar la información del doctor
print(profesion.mostrar_informacion())



