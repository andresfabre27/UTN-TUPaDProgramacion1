#Trabajo Practico Nro 5
#Tema: Listas
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

lista=list(range(4,101,4))
print(f"{lista}")

#Ejercicio Nro 2

lista=list(range(5))
print(lista)
print(lista[-2])

#Ejercicio Nro 3

lista=[]
lista.append("Palabra1")
lista.append("Palabra2")
lista.append("Palabra3")
print(lista)

#Ejercicio Nro 4

animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1]="loro"
animales[-1]="oso"
print(animales)

#Ejercicio Nro 5

#El ejercicio nro 5 lo que hace es eliminar de una lista de numeros el mayor valor, que en este caso es 22
# y finalmente imprime la lista resultante sin el valor 22.

#Ejercicio Nro 6

lista=list(range(10,31,5))
print(f"{lista[0]} {lista[1]}")

#Ejercicio Nro 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1]="peugeot 208"
autos[2]="fiat"

print(autos)

#Ejercicio Nro 8

doble=[]
doble.append(5*2)
doble.append(10*2)
doble.append(15*2)
print(doble)

#Ejercicio Nro 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(compras)

#Ejercicio Nro 10

lista_anidada=[15,True,[25.5,57.9,30.6],False]

print(lista_anidada)