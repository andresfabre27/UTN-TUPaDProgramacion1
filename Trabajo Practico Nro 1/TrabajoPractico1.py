#Trabajo Práctico 1: Estructuras secuenciales
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

print("Hola Mundo!")

#Ejercicio Nro 2

nombre=input("Ingresa tu nombre ")
print(f"Hola {nombre}!")

#Ejercicio Nro 3

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu Apellido: ")
edad=int(input("Ingresa tu edad: "))
residencia=input("Ingresa tu residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")

#Ejercicio Nro 4
import math

radio=int(input("Ingresa el radio del circulo: "))

area=math.pi*radio**2
perimetro=2*math.pi*radio

print(f"El area es: {area}")
print(f"El perimetro es: {perimetro}")

#Ejercicio Nro 5

segundos=int(input("Ingrese la cantidad de segundos: "))
horas=segundos/3600

print(f"son {horas} horas ")

#Ejercicio Nro 6

numero=int(input("Ingrese un numero: "))

print(f"{numero}x1={numero*1}")
print(f"{numero}x2={numero*2}")
print(f"{numero}x3={numero*3}")
print(f"{numero}x4={numero*4}")
print(f"{numero}x5={numero*5}")
print(f"{numero}x6={numero*6}")
print(f"{numero}x7={numero*7}")
print(f"{numero}x8={numero*8}")
print(f"{numero}x9={numero*9}")

#Ejercicio Nro 7

print("Ingrese 2 numeros distintos de cero")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero:"))

suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicacion es {multiplicacion}")
print(f"La division es {division}")

#Ejercicio Nro 8

altura=float(input("Ingresa tu altura en metros: "))
peso=int(input("INgresa tu peso en kg: "))

IMC=peso/(altura**2)

print(f"Su indice de masa corporal es: {IMC}")

#Ejercicio Nro 9

temperaturacelsius=int(input("Ingrese su temperatura en grados celsius: "))

temperaturafahrenheit=(9/5)*temperaturacelsius+32

print(f"La temperatura en grados fahrenheit es: {temperaturafahrenheit}")

#Ejercicio Nro 10

print("Ingrese 3 numeros")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

promedio=(numero1+numero2+numero3)/3

print(f"El promedio es: {promedio}")