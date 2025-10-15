#Trabajo Practico Nro 9
#Tema: Aplicaciones de la recursividad
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

def factorial(numero):
    if numero==0:
        return 1
    else:
        return numero*factorial(numero-1)
    

numero=int(input("Ingrese un numero: "))

for i in range(1,numero+1):
    print(f"EL factorial de {i} es: {factorial(i)}")

#Ejercicio Nro 2

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
numero=int(input("Ingrese la posicion para la serie de Fibonacci: "))

for i in range(numero+1):
    print(f"{fibonacci(i)},",end="")

#Ejercicio Nro 3


#EJercicio Nro 4

def convertir_binario(numero):
    lista=[]

    while(numero>0):
        
        resto=numero%2
        lista.append(resto)
        numero=numero//2
    
    invertido=lista[::-1]
    cadena_de_numeros = "".join(str(x) for x in invertido)
    return cadena_de_numeros


numero=int(input("Ingrese un numero para convertirlo en binario: "))
print(convertir_binario(numero))

#Ejercicio Nro 6