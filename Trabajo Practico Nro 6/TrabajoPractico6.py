#Trabajo Practico Nro 6
#Tema: Funciones
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#Ejercicio Nro 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}¡")

nombre=input("Ingresa tu nombre: ")
saludar_usuario(nombre)

#Ejercicio Nro 3

def informacion_personal(nombre, apellido, edad, residencia):

    print(f"Soy {nombre}{apellido}, tengo {edad} años y vivo en {residencia}")

print("Ingresa tus datos")
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
edad=int(input("Ingresa tu edad: "))
residencia=input("Ingresa tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercico Nro 4
import math

def calcular_area_circulo(radio):
       
       return math.pi*(radio)**2



def calcular_perimetro_circulo(radio):
       
       return 2*math.pi*radio

radio=float(input("Ingrese el radio del circulo: "))

print(f"El area es: {calcular_area_circulo(radio)}")
print(f"El perimetro es: {calcular_perimetro_circulo(radio)}")

#Ejercicio Nro 5

def segundos_a_horas(segundos):

    return segundos/60/60

segundos=int(input("Ingrese los segundos: "))
print(f"Son {segundos_a_horas(segundos)} horas ")

#Ejercicio Nro 6

def tabla_multiplicar(numero):

    for i in range(1,10):
        print(f"{numero}x{i}={i*numero}")

numero=int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#Ejercicio Nro 7

def operaciones_basicas(a, b):
   suma=a+b
   resta=a-b
   division=a/b
   multiplicacion=a*b
   
   return suma,resta,division, multiplicacion

print("Ingrese 2 numeros")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: ")) 

print(operaciones_basicas(numero1,numero2))

#Ejercicio Nro 8

def calcular_imc(peso, altura):
    
    return peso/(altura*altura)

print("Calculadora de iMC")
peso=float(input("Ingresa tu peso: "))
altura=float(input("Ingresa tu estatura: "))

print(f"Tu IMC es: {calcular_imc(peso,altura)}")

#Ejercicio Nro 9

def celsius_a_fahrenheit(celsius):
    F = (celsius * 9/5) + 32

    return F

temperatura=int(input("Ingrese los grados celsius: "))
print(f"Son {celsius_a_fahrenheit(temperatura)} grados Fahrenheit")

#Ejercicio Nro 10

def calcular_promedio(a, b, c):

    return (a+b+c)/3

print("Ingrese 3 numeros para calcular el promedio")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

print(f"El promedio es: {calcular_promedio(numero1,numero2,numero3)}")