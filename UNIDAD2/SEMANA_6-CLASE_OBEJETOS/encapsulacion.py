class Persona: #plantilla para crear el objeto
    #clase Padre
    def __init__(self, nombre, apellido, edad): #atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Doctor(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, nacionalidad):
        super().__init__(nombre, apellido, edad)
        self.nacionalidad = nacionalidad #atributo propio
        self.correo = correo
        self.__contraseña = contraseña # Encapsulación de la contraseña

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, nacionalidad: {self.nacionalidad}"

    @property
    def contraseña (self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "Ecuatoriano")

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())
print("Contraseña del doctor:", profesion_doctor.contraseña)

# Cambiar la contraseña
profesion_doctor.contraseña = "nuevaContraseñaDoc"
print("Nueva contraseña del doctor:", profesion_doctor.contraseña)

class Chef(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, nacionalidad):
        super().__init__(nombre, apellido, edad)
        self.nacionalidad = nacionalidad #atributo propio
        self.correo = correo
        self.__contraseña = contraseña # Encapsulación de la contraseña

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, nacionalidad: {self.nacionalidad}"

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

# Crear el objeto de Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "Italiana")

# Mostrar la información del chef
print(profesion_chef.mostrar_informacion())
print("Contraseña del chef:", profesion_chef.contraseña)

# Cambiar la contraseña
profesion_chef.contraseña = "nuevaContraseñaChef"
print("Nueva contraseña del chef:", profesion_chef.contraseña)
