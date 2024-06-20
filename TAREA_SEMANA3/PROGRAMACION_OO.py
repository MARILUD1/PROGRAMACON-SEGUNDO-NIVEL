class EntidadTiempo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}:"


class Ciudad(EntidadTiempo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.registros = []

    def agregar_registro(self, tipo, temperatura):
        self.registros.append((tipo, temperatura))

    def promedio_temperaturas(self):
        if not self.registros:
            return 0
        suma_temperaturas = sum(temperatura for _, temperatura in self.registros)
        return suma_temperaturas / len(self.registros)


class Semana(EntidadTiempo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ciudades = []

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)


# Función para ingresar datos por consola
def ingresar_datos():
    dimension_temperaturas = []

    # Ingresar datos de temperaturas
    for semana_num in range(1, 4):  # Tres semanas
        semana = Semana(f"Semana {semana_num}")
        for _ in range(7):  # Siete ciudades por semana
            nombre_ciudad = input(f"Ingrese el nombre de la ciudad {semana_num}: ")
            temperatura = float(input(f"Ingrese la temperatura para {nombre_ciudad}: "))
            tipo = "temperatura"  # Se mantiene el tipo como 'temperatura'
            ciudad = Ciudad(nombre_ciudad)
            ciudad.agregar_registro(tipo, temperatura)
            semana.agregar_ciudad(ciudad)
        dimension_temperaturas.append(semana)

    return dimension_temperaturas


# Función para calcular promedio de temperaturas semanales para una provincia específica
def calcular_temperatura_promedio_semanal(provincia, datos):
    num_semanas = len(datos)
    suma_temperatura = 0
    num_registros = 0

    # Recorrer cada semana y sumar las temperaturas de la provincia especificada
    for semana in datos:
        for semana_ciudad in semana.ciudades:
            if semana_ciudad.nombre.lower() == provincia.lower():
                suma_temperatura += semana_ciudad.promedio_temperaturas()
                num_registros += 1

    if num_registros == 0:
        raise ValueError(f"No se encontraron registros para la provincia '{provincia}' en los datos proporcionados.")

    promedio_semanal = suma_temperatura / num_semanas
    return promedio_semanal


# Ingresar datos por consola
datos = ingresar_datos()

# Solicitar provincia al usuario
provincia = input("Ingrese el nombre de la provincia para calcular el promedio de temperaturas: ")

try:
    promedio_semanal = calcular_temperatura_promedio_semanal(provincia, datos)
    print(f"El promedio de temperatura semanal para la provincia de {provincia} es: {promedio_semanal:.2f}")
except ValueError as e:
    print(f"Error: {e}")
