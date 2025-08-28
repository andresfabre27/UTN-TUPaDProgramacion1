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