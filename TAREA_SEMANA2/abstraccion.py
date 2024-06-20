from abc import ABC, abstractmethod

class Personaje(ABC):


    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):

       #Muestra los atributos del personaje.
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    @abstractmethod
    def daño(self, enemigo): #metodo abstracto
        #Método abstracto para calcular el daño contra un enemigo.
        pass

    def atacar(self, enemigo):
        #Realiza un ataque al enemigo y muestra los resultados.
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha ganado", daño, "puntos por atacar a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def esta_vivo(self):
        #Verifica si el personaje está vivo.
        return self.vida > 0

    def morir(self):
        #Marca al personaje como muerto.
        self.vida = 0
        print(self.nombre, "ha caido")


class Guerrero(Personaje):
   #Clase para representar un Guerrero, subclase de Personaje.

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada #espada atributo propio para usar en su metodo

    def atributos(self):
        #Muestra los atributos del Guerrero incluyendo la espada.
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        #Calcula el daño que el Guerrero puede hacer.
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro #espada atributo propio para usar en su metodo

    def atributos(self):
        #Muestra los atributos del Mago incluyendo el libro de hechizos.
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        #Calcula el daño que el Mago puede hacer.
        return self.inteligencia * self.libro - enemigo.defensa


# Ejemplo de uso en PyCharm:

if __name__ == "__main__":
    # Crear instancias de Guerrero y Mago
    personaje_1 = Guerrero("Guts", 20, 5, 10, 100, 8)  # Nombre, fuerza, inteligencia, defensa, vida, espada
    personaje_2 = Mago("Merlin", 5, 20, 8, 80, 10)     # Nombre, fuerza, inteligencia, defensa, vida, libro

    # Mostrar atributos iniciales
    print("Atributos iniciales de los personajes:")
    personaje_1.atributos()
    personaje_2.atributos()

    # Simular combate entre los personajes
    print("empezó el combate:")
    personaje_1.atacar(personaje_2)
    if personaje_2.esta_vivo():
        personaje_2.atacar(personaje_1)
