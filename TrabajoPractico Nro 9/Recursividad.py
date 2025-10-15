#Trabajo Practico Nro 9
#Tema: Aplicaciones de le recursividad
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
#Revisar

def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:
        
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es: {resultado}")


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

#Ejercicio Nro 5

def es_palindromo(palabra):

    
    largo=len(palabra)
    if len(palabra)==1:
        return True
    
    if palabra[0]==palabra[-1]:

        return es_palindromo(palabra[1:largo-1])
    
    else:
        return False
    

palabra=input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")


#Ejercicio Nro 6
def suma_digitos(n):
    
    
    digito=n%10
    
    if n==0:
        return 0
    else:
        return digito+suma_digitos(n//10)

numero=int(input("Ingrese el numero para sumar sus digitos: "))
print(suma_digitos(numero))

#Ejercicio Nro 7

def contar_bloques(n):

    if n==0:
        return 0
    
    else:
        return n+contar_bloques(n-1)
    
numero=int(input("Ingrese la cantidad de bloques: "))
print(contar_bloques(numero))

#Ejercicio Nro 8

def contar_digito(numero, numero2):

    digito=numero%10
    if numero==0:
        return 0
    else:
        if numero2==digito:
            
            return 1+contar_digito(numero//10,numero2)
        else:
            return contar_digito(numero//10,numero2) 


numero=int(input("Ingrese un numero: "))
digito=int(input("Ingrese un digito: "))

print(contar_digito(numero,digito))