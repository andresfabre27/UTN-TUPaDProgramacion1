from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

class CostoComputadora:
    @staticmethod
    def main():
        while True:
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo: ")

            computadora = Computadora(marca, modelo)

            while True:
                componente = input("Ingrese el nombre del componente (o 'FIN' para terminar): ")
                if componente.upper() == "FIN":
                    break
                marca_comp = input("Ingrese la marca del componente: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio unitario: "))

                comp = ComponenteCPU(componente, marca_comp, cantidad, precio)
                computadora.agregar_componente(comp)

            computadora.mostrar_informacion()

            continuar = input("¿Desea cotizar otra computadora? (SI/NO): ")
            if continuar.upper() != "SI":
                print("Programa finalizado.")
                break


if __name__ == "__main__":
    CostoComputadora.main()
