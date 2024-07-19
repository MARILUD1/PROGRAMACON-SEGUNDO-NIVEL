class Camioneta:
    def __init__(self, color, marca, modelo):
        self.color = color        # Color de la camioneta
        self.marca = marca        # Marca de la camioneta
        self.modelo = modelo      # Modelo de la camioneta
        self.velocidad = 0        # Velocidad inicial de la camioneta

    def acelerar(self, incremento):
        #AumentO de la velocidad de la camioneta.
        self.velocidad += incremento
        print("La camioneta ha acelerado. Nueva velocidad: {self.velocidad} km/h")

    def frenar(self, decremento):
        #Disminuye la velocidad de la camioneta.
        if self.velocidad - decremento >= 0:
            self.velocidad -= decremento
        else:
            self.velocidad = 0
        print(f"La camioneta ha frenado. Nueva velocidad: {self.velocidad} km/h")

    def mostrar_informacion(self):
        #Muestra la información de la camioneta.
        print(f"Camioneta - Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h")

# Comportamiento de los atributos
mi_camioneta = Camioneta("Rojo", "Toyota", "Hilux")
mi_camioneta.mostrar_informacion()  # Muestra la información inicial de la camioneta

mi_camioneta.acelerar(50)  # Acelera la camioneta en 50 km/h
mi_camioneta.frenar(20)    # Frena la camioneta en 20 km/h
mi_camioneta.mostrar_informacion()  # Muestra la información actualizada de la camioneta
