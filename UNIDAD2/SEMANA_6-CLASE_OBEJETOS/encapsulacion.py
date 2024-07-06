class Persona:
    # Clase Padre
    def __init__(self, nombre, apellido, edad, correo, contraseña):
        # Atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.__contraseña = contraseña

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña


class Doctor(Persona): # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, bisturi):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.bisturi = bisturi # Atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, bisturi: {self.bisturi}"


class Chef(Persona): # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, sarten):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.sarten = sarten # Atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, sarten: {self.sarten}"


# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "opera pacientes")

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())

# Solicitar la contraseña  del doctor por consola
ingresa_contraseña = input("Ingrese la contraseña actual del doctor: ")
if ingresa_contraseña == profesion_doctor.contraseña:

    nueva_contraseña = input("Ingrese la nueva contraseña del doctor: ")

    print("La contraseña correcta.")
else:
    print("Contraseña incorrecta.")

# Crear el objeto Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "prepara alimentos")

# Mostrar la información del chef
print(profesion_chef.mostrar_informacion())

# Solicitar la contraseña  del chef por consola
ingresar_contraseña = input("Ingrese la contraseña actual del chef: ")
if ingresar_contraseña == profesion_chef.contraseña:


    print("La contraseña correcta.")
else:
    print("Contraseña incorrecta.")


