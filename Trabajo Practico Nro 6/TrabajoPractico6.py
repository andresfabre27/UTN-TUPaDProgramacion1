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