class Persona: #plantilla para crear el objeto
    #clase Padre
    def __init__(self, nombre, apellido, edad,correo,contraseña): #atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.contraseña=contraseña


class Doctor(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, bisturi):
        super().__init__(nombre, apellido, edad,correo,contraseña)

        self.__contraseña = contraseña # Encapsulación de la contraseña
        self.bisturi= bisturi # atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, bisturi: {self.bisturi}"

    @property
    def contraseña (self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "El Doc. Esteban opera un paciente")

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())
print("Contraseña del doctor:", profesion_doctor.contraseña)

# Cambiar la contraseña

print("Nueva contraseña del doctor:", profesion_doctor.contraseña)

class Chef(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, sarten):
        super().__init__(nombre, apellido, edad,correo,contraseña)

     # Encapsulación de la contraseña
        self.__contraseña = contraseña
        self.sarten = sarten   # atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, sarten: {self.sarten}"

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

# Crear el objeto de Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "La chef Lucia prepara un plato tipico")

# Mostrar la información del chef
print(profesion_chef.mostrar_informacion())

# Cambiar la contraseña
profesion_chef.contraseña = "nuevaContraseñaChef"
print("Nueva contraseña del chef:", profesion_chef.contraseña)
