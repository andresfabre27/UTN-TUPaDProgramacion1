
#Ecepciones basicas

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


"""
Excepciones comunes
TypeError: Ocurre cuando una operación se aplica a un tipo de dato incorrecto, como sumar un número y una cadena.
ZeroDivisionError: Se genera al intentar dividir un número por cero.
IndexError: Se produce cuando intentas acceder a un elemento de una lista o tupla con un índice que está fuera de rango.
KeyError: Sucede al intentar acceder a un diccionario con una clave que no existe.
ValueError: Ocurre cuando una función recibe un argumento del tipo correcto, pero con un valor inadecuado (por ejemplo, intentar convertir la cadena "hola" a un entero).
FileNotFoundError: Se activa cuando se intenta abrir un archivo que no existe en la ruta especificada. 

"""



#Recorrer e imprimir un diccionario

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

for item in likes.items():
    print(item)


for key, value in likes.items():
    print(key, "->", value)

#Recoorrer e imprimir solo las claves de un diccionario

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

for key in likes.keys():
    print(key)

#Para imprimir los valores hacemos lo mismo con .values() en vez de .Keys()


#2 formas de buscar en una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

numero=int(input("Ingrese del 1 al 9: "))


"""for i in range(len(matriz)):
    if numero==matriz[i][0]:
        posicion=i"""

contador=0
for linea in matriz:
    if numero in linea:
        posicion=contador
    contador+=1

print(f"El numero esta en la posicion {posicion}") 