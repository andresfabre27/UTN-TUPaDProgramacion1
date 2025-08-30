#Ejercicio Nro 20

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


class OperacionesFraccion:
    @staticmethod
    def main():
        n1 = int(input("Numerador 1: "))
        d1 = int(input("Denominador 1: "))
        n2 = int(input("Numerador 2: "))
        d2 = int(input("Denominador 2: "))

        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)

        print("Suma:", Fraccion.sumarFracciones(f1, f2))
        print("Resta:", Fraccion.restarFracciones(f1, f2))
        print("Multiplicación:", Fraccion.multiplicarFracciones(f1, f2))
        print("División:", Fraccion.dividirFracciones(f1, f2))


if __name__ == "__main__":
    OperacionesFraccion.main()
    


          
          

