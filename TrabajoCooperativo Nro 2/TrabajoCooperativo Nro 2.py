#Trabajo Cooperativo numero 2
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 2

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(lista)
mayor=lista[0]
menor=lista[0]

for i in range(1,5):
    if lista[i]>mayor:
        mayor=lista[i]
    if lista[i]<menor:
        menor=lista[i]

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}") 

#Ejercicio Nr 4

print("Ingrese 5 numeros")
pares=0
impares=0

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))
    if lista[i]%2==0:
        pares+=1
    elif lista[i]%3==0:
        impares+=1

print(f"Hay {pares} numeros pares")
print(f"Hay {impares} numeros inpares")

#Ejercicio Nro 6

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

lista_sin_duplicados=[]

for i in lista:

    if i not in lista_sin_duplicados:
        lista_sin_duplicados.append(i)

print(f"Lista sin duplicados: {lista_sin_duplicados}")

#Ejercicio nro 6 con funcion set

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

lista_sin_duplicados=[]

lista_sin_duplicados=list(set(lista))

print(lista_sin_duplicados)

#Ejercicio Nro 8
import random

lista=[random.randint(0, 10) for _ in range(10)]

vistos = set()
repetidos = set()

for elemento in lista:
    if elemento in vistos:
        repetidos.add(elemento)
    else:
        vistos.add(elemento)

print("Lista original:", lista)
print("Elementos repetidos:", list(repetidos))

#Ejercicio Nro 10

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

indice=int(input("Ingrese el indice del elemento a elimiar (0 a 5): "))

lista.pop(indice)

print(lista)

#Ejercicio Nro 12

lista1=list(range(0,10,2))
lista2=list(range(0,20,4))
lista_suma=[]

for i in range(5):
    lista_suma.append(lista1[i]+lista2[i])
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista SUMA: {lista_suma}")





