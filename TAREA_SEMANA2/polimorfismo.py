
#Las clases heredadas tienen su propio comportamiento en cada uno de los atributos heredados
class Guerrero:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        self.nombre = nombre
        self.fuerza = fuerza + 2
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.espada = espada

    def descansar(self):
        # Aumento de fuerza cada vez que descansa
        self.fuerza

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def atacar(self):
        # Implementación específica para Guerrero
        return f"{self.nombre} ataca con una espada con una fuerza de {self.fuerza + self.espada}"
 # comportamiento propio con su metodo adecuado

class Mago:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        self.nombre = nombre
        self.fuerza = fuerza + 2
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.libro = libro

    def descansar(self):#comportamiento
        # Aumento de fuerza
        self.fuerza

    def atributos(self): # caracteristicas
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def atacar(self):
        # comportamiento propio
        return f"{self.nombre} lanza un hechizo con una inteligencia de {self.inteligencia + self.libro}"
# comportamiento propio con su metodo adecuado

# Función que acepta cualquier objeto que tenga los métodos `atributos` y `atacar`
def mostrar_atributos_y_atacar(personaje):
    personaje.atributos()
    print(personaje.atacar())
    print()

# Crear la acciones y los efectos  de Guerrero y Mago
guerrero = Guerrero("Guts", 20, 10, 4, 100, 4)
mago = Mago("Vanessa", 5, 15, 4, 100, 3)

# Usar la función para mostrar atributos y atacar para cada personaje
mostrar_atributos_y_atacar(guerrero)
mostrar_atributos_y_atacar(mago)
