try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    numero = int(input("Introduce un número: "))
except ValueError:
    print("Error: Debes introducir un número válido.")
finally:
    print("Gracias por usar el programa.")