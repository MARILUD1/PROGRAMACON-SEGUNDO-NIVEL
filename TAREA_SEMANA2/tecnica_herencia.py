class Personaje:# clase madre

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): #atributos a heredar
        self.nombre = nombre
        self.fuerza = fuerza +2
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def descansar (self):
        self.fuerza += 3  # aumento de fuerza

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

class Guerrero(Personaje): # clase que heredera

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada # atributo propio





class Mago(Personaje):# clase heredada o clase hija

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) #especificacion
        self.libro = libro #atributo propio





personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()












