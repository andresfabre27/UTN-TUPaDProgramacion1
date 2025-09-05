# Clase que representa una fracción
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # Método para mostrar la fracción de forma legible
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # Suma de fracciones
    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # Resta de fracciones
    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # Multiplicación de fracciones
    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # División de fracciones
    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)


# Clase para manejar la ejecución principal
class OperacionesFraccion:
    @staticmethod
    def main():
        print("Ingrese los valores de la primera fracción:")
        n1 = int(input("Numerador: "))
        d1 = int(input("Denominador: "))
        print("Ingrese los valores de la segunda fracción:")
        n2 = int(input("Numerador: "))
        d2 = int(input("Denominador: "))

        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)

        suma = Fraccion.sumarFracciones(f1, f2)
        resta = Fraccion.restarFracciones(f1, f2)
        multiplicacion = Fraccion.multiplicarFracciones(f1, f2)
        division = Fraccion.dividirFracciones(f1, f2)

        print("\nResultados:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")



OperacionesFraccion.main()