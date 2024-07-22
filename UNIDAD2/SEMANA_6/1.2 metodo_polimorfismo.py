class Persona:
    # Clase Padre
    def __init__(self, nombre, apellido, edad, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.__contraseña = contraseña

    # Método para verificar la contraseña
    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña

    # Método para cambiar la contraseña
    def cambiar_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña


class Doctor(Persona):
    # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, bisturi):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.bisturi = bisturi  # Atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, bisturi: {self.bisturi}"

    def preparar(self):
        return "Paciente atendido con éxito por el doctor Esteban"


class Chef(Persona):
    # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, sarten):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.sarten = sarten  # Atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, sarten: {self.sarten}"

    def preparar(self):
        return "Plato típico exquisito preparado por la chef Lucia"


# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "El Doctor cirujano")

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())

# Intentar acceder a la contraseña privada directamente (esto generará un error)
try:
    print(profesion_doctor.__contraseña)
except AttributeError as e:
    print(e)

# Verificar la contraseña del doctor
#print("Verificación de la contraseña del doctor:", profesion_doctor.verificar_contraseña("esDoc36"))

# Cambiar la contraseña del doctor (esto generará un error por el tipo de dato incorrecto)
try:
    profesion_doctor.cambiar_contraseña("esDoc36")
except Exception as e:
    print(e)

# Realizar la preparación del doctor
print(profesion_doctor.preparar())

# Crear el objeto Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "preparacion de comida")

# Mostrar la información del chef
print(profesion_chef.mostrar_informacion())

# Intentar acceder a la contraseña privada directamente (esto generará un error)
try:
    print(profesion_chef.__contraseña)
except AttributeError as e:
    print(e)

# Verificar la contraseña del chef
#print("Verificación de la contraseña del chef:", profesion_chef.verificar_contraseña("chef1234"))

# Cambiar la contraseña del chef (esto generará un error por el tipo de dato incorrecto)
try:
    profesion_chef.cambiar_contraseña("chef1234")
except Exception as e:
    print(e)

# Realizar la preparación del chef
print(profesion_chef.preparar())


# Función para que el objeto realice una acción
def realizar_preparacion(persona):
    print(persona.preparar())

# LLAMADA CON METODOS DE POLIMORFISMO
realizar_preparacion(profesion_doctor)  # Funcion del doctor
realizar_preparacion(profesion_chef)  # Funcion de la chef