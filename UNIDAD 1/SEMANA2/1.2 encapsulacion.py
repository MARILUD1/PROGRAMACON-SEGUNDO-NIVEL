class CuentaBancaria:
    def __init__(self, balance_inicial): #__ metodo de seguridad, es decir es privado
        #Encapsulacion
        self.__balance = balance_inicial

    def depositar(self, monto):# paso para depositar
        if monto > 0: # logicamente desde 1 dolar en adelante
            self.__balance += monto
            print(f"Se han depositado $(monto). Nuevo balance: $(self.__balance).")
        else:
            print("El monto a depositar debe ser > a 0.")

    def retirar(self, monto): # retiro de dinero
        if 0 < monto <= self.__balance:# condicion para verificar el retiro valido del monto
            self.__balance -= monto
            print(f"Se han retirado $(monto). Nuevo balance: $(self.__balance).")
        elif monto > self.__balance:
            print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser mayor a 0.")#mostrar en la pantalla este mensaje

    def consultar_balance(self):
        print(f"El balance actual es: $(self.__balance).")

# Crear una cuenta con un balance inicial de 500 dólares
cuenta = CuentaBancaria(500)

# Consultar el balance inicial
cuenta.consultar_balance()

# Depositar 200 dólares
cuenta.depositar(200)

# Retirar 100 dólares
cuenta.retirar(100)

# Consultar el balance final
cuenta.consultar_balance()






