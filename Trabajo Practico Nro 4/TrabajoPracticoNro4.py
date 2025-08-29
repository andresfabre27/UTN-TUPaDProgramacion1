#Trabajo Practico Nro 4
#Tema: Estructuras repetitivas
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

for i in range(101) :
    print (i)

#Ejercicio Nro 2

import math

numero=int(input("Ingrese un numero entero: "))
digitos=0

while numero>0 : 
    digitos += 1
    numero=math.trunc(numero/10)

print(f"La cantidad de digitos que tiene el numero es: {digitos}")

#Ejercicio nro 3

suma=0
print("Ingrese 2 numeros enteros")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

for i in range(numero1+1,numero2) :
     suma=suma+i
     
print(f"La suma entre los 2 valores es: {suma}")

#Ejercicio Nro 4

print("Ingrese numeros para sumarlos en secuencia")
suma=0
fin_suma=False

while fin_suma!=True :
    numero=int(input("Ingrese un numero distinto de cero: "))
    suma=suma+numero
    if numero==0 :
        fin_suma=True

print(f"La suma acumulada es: {suma}")

# Ejercicio Nro 5

import random

print("Adivine un numero del 0 al 9")
numero_aleatorio=random.randint(0,9)
adivinado=False
intentos=0

while adivinado!=True :

  numero=int(input("Ingrese un numero: "))
  intentos+=1

  if numero==numero_aleatorio :
    adivinado=True

print(f"Usted realizo {intentos} intentos para adivinar el numero") 

#Ejercicio Nr6 

for i in range(100,-1,-1):
    if i%2==0:
        print(i)

#Ejercicio Nro 7

numero=int(input("Ingrese un numero: "))
suma=0

for i in range(0,numero+1):
    suma=suma+i

print(f"La suma es: {suma}")

#Ejercicio nro 8

contador=0
numeros_pares=0
numeros_impares=0
numeros_positivos=0
numeros_negativos=0

while contador <100:
  numero=int(input("Ingrese un numero: "))
  if numero%2==0:
    numeros_pares=numeros_pares+1
  elif numero%3==0:
    numeros_impares=numeros_impares+1

  if numero>0:
    numeros_positivos=numeros_positivos+1
  elif numero<0:
    numeros_negativos=numeros_negativos+1

  contador+=1

print(f"Hay {numeros_pares} numeros PARES")
print(f"Hay {numeros_impares} numeros IMPARES")
print(f"Hay {numeros_positivos} numeros POSITIVOS")
print(f"Hay {numeros_negativos} numeros NEGATIVOS ")

#Ejercicio Nro 9

promedio=0
suma=0

for i in range(100):
   numero=int(input("Ingrese un numero: "))
   suma=suma+numero

promedio=suma/100
print(f"El promedio es: {promedio}")

#Ejercicio Nro 10

import math

numero=int(input("Ingrese un numero: "))
numero_invertido=0

while numero>0:
    digito=numero%10
    numero_invertido=numero_invertido*10+digito
    numero=math.trunc(numero/10)

print(numero_invertido)
