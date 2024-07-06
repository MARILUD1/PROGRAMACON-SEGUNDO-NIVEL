class Persona: #plantilla para crear el objeto
    #clase Padre
    def __init__(self, nombre, apellido, edad,correo,contraseña): #atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.__contraseña=contraseña


class Doctor(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, bisturi):
        super().__init__(nombre, apellido, edad,correo,contraseña)

        self.__contraseña = contraseña # Encapsulación de la contraseña
        self.bisturi= bisturi # atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, bisturi: {self.bisturi}"
    def preparar(self):

        return "Paciente atendido con exito por el doctor Esteban"

    @property
    def contraseña (self):
        return self.__contraseña

# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "El Doctor cirujano")

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())
ingresa_contraseña = input("Ingrese la contraseña actual del doctor: ")
if ingresa_contraseña == profesion_doctor.contraseña:

    nueva_contraseña = input("Ingrese la nueva contraseña del doctor: ")

    print("La contraseña correcta.")
else:
    print("Contraseña incorrecta.")

print(profesion_doctor.preparar())

class Chef(Persona): #Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, sarten):
        super().__init__(nombre, apellido, edad,correo,contraseña)

     # Encapsulación de la contraseña
        self.__contraseña = contraseña
        self.sarten = sarten   # atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, sarten: {self.sarten}"
    def preparar(self):

        return "Plato tipico exquisito preparado por la chef Lucia"
    @property
    def contraseña(self):
        return self.__contraseña

# Crear el objeto de Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "preparacion de comida")
print(profesion_chef.mostrar_informacion())

# Mostrar la información del chef

ingresa_contraseña = input("Ingrese la contraseña actual de la chef: ")
if ingresa_contraseña == profesion_chef.contraseña:

    print("La contraseña correcta.") #erdadero
else:
    print("Contraseña incorrecta.") # falso

    print(profesion_chef.preparar())

    # llamada a la funcion para que el objeto realice una accion
    def realizar_preparacion(persona):
        print(persona.preparar())


    # LLAMADA CON METODOS DE POLOÍMORFISMO
    realizar_preparacion(profesion_doctor) #Funcion del doctor
    realizar_preparacion(profesion_chef) # Funcion de la chef





