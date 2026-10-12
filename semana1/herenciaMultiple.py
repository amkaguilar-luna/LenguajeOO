from random import *

# ==========================
# Clase Padre
# ==========================

class Tarjeta:

    def __init__(self, titular):
        # Crear atributos
        pass

    def getId(self):
        pass

    def getTitular(self):
        pass


# ==========================
# Clase Hija
# ==========================

class TarjetaCredito(Tarjeta):

    def __init__(self, titular):
        # Llamar al constructor padre
        # Crear limite de credito
        pass

    def setAumentarCredito(self, opcionTC):
        # Utilizar match
        # Validar opcion s o n
        pass

    def getLimiteCredito(self):
        pass


# ==========================
# Herencia Multinivel
# ==========================

class TarjetaDescuento(TarjetaCredito):

    def __init__(self, titular):
        # Llamar al constructor padre
        # Seleccionar aleatoriamente un descuento
        pass

    def mostrarDescuento(self):
        # Mostrar descripcion del descuento
        pass

    def calcularDescuento(self):
        # Calcular porcentaje de descuento
        pass

    def __str__(self):
        # Mostrar informacion de la tarjeta
        pass


# ==========================
# Otra Clase Hija
# ==========================

class TarjetaDebito(Tarjeta):

    def __init__(self, titular):
        # Crear saldo inicial
        pass

    def getSaldo(self):
        pass

    def setDepositar(self, cantidad):
        # Validar deposito
        pass

    def __str__(self):
        # Mostrar saldo
        pass


# ==========================
# Programa Principal
# ==========================
opcion = 0

while opcion != 3:

    print("\nMENU")
    print("1. Tarjeta Crédito con Descuento")
    print("2. Tarjeta Débito")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                try:

                    # Solicitar titular

                    # Crear objeto TarjetaDescuento

                    # Mostrar información

                    # Solicitar autorización
                    # para aumentar crédito

                    # Llamar al método correspondiente

                    # Mostrar nuevo límite

                    pass

                except ValueError as error:
                    print(error)

            case 2:
                try:
                    # Solicitar titular

                    # Solicitar cantidad a depositar

                    # Crear objeto TarjetaDebito

                    # Realizar depósito

                    # Mostrar saldo final

                    pass

                except ValueError as error:
                    print(error)
            case 3:
                print("...")

            case _:
                print("...")

    except ValueError:
        print("...")
