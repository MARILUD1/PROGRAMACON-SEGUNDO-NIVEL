class Persona:
    # Clase Padre
    def __init__(self, nombre, apellido, edad, correo, contraseña):
        # Atributos para clase hija
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.__contraseña = contraseña  # Atributo privado

    # Método para verificar la contraseña
    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña

    # Método para cambiar la contraseña (setter)
    def cambiar_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña


class Doctor(Persona):  # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, bisturi):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.bisturi = bisturi  # Atributo propio

    def mostrar_informacion(self):
        return f"Doctor {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, bisturi: {self.bisturi}"


class Chef(Persona):  # Clase hija
    def __init__(self, nombre, apellido, edad, correo, contraseña, sarten):
        super().__init__(nombre, apellido, edad, correo, contraseña)
        self.sarten = sarten  # Atributo propio

    def mostrar_informacion(self):
        return f"Chef {self.nombre} {self.apellido}, {self.edad} años, correo: {self.correo}, sarten: {self.sarten}"


# Crear el objeto de Doctor con atributos heredados y propio
profesion_doctor = Doctor("Esteban", "Torres", 36, "esteban36@gmail.com", "esDoc36", "opera pacientes")

# Intentar acceder a la contraseña privada directamente (esto generará un error)
try:
    print(profesion_doctor.__contraseña)
except AttributeError as e:
    print(e)

print(profesion_doctor.verificar_contraseña("esDoc36"))
print(profesion_doctor.cambiar_contraseña(123j))



# Se verifica la contraseña usando el método de la clase
#print("Verificación de la contraseña del doctor:", profesion_doctor.verificar_contraseña("esDoc36"))

# Mostrar la información del doctor
print(profesion_doctor.mostrar_informacion())

# Crear el objeto Chef con atributos heredados y propio
profesion_chef = Chef("Lucia", "Rodriguez", 28, "lucia28@gmail.com", "chef1234", "prepara alimentos")

# Mostrar la información del chef
print(profesion_chef.mostrar_informacion())
try:
    print(profesion_chef.__contraseña)
except AttributeError as e:
    print(e)
    print(profesion_chef.verificar_contraseña("chef1234"))
    print(profesion_doctor.cambiar_contraseña("123Chef"))



