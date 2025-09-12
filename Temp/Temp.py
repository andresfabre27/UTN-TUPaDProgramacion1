#Ejercicio Nro 10

def calcular_promedio(a, b, c):

    return (a+b+c)/3

print("Ingrese 3 numeros para calcular el promedio")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

print(f"El promedio es: {calcular_promedio(numero1,numero2,numero3)}")