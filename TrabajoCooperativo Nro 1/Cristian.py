#1- CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la 
#conversión. Muestre por pantalla el resultado de las conversiones.  
"""
valorDecimal = float(input("Ingrese un número decimal: "))
#entero
valorEntero = int(valorDecimal)
#string
valorTexto = str(valorDecimal)
#booleano
valorBooleano = bool(valorDecimal)  # False si es 0.0, True si es distinto de 0
#lista
valorLista = list(valorTexto)
#resultados
print("Valor original (float):", valorDecimal)
print("Convertido a entero (int):", valorEntero)
print("Convertido a texto (str):", valorTexto)
print("Convertido a booleano (bool):", valorBooleano)
print("Convertido a lista (list):", valorLista)


#3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
#y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
#efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
#14. Plantee el algoritmo planteando métodos para su resolución.

numero=int(input("ingrese un numero de 3 digitos "))
suma=0
if numero >99 and numero < 1000:
    while numero > 0:
        digito=numero%10
        suma=suma+digito
        numero=int(numero//10)
else:   
    print("El número debe ser entre 100 y 999")
    
print(f"La suma del valor ingresado es {suma}")

#5- Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre 
#la cadena resultante.

frase=input("Ingrese una frase ")
frase_sin_espacios =frase.replace(" ","") #metodo para remplazar
print(f"Su frase sin espacios es: {frase_sin_espacios}")

#7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas 
#vocales tiene en total. 

frase = input("Ingrese una frase ").lower()

print(f"El tamaño de su cadena es de {len(frase)}")

total_vocales=0

for v in "aeiou": #recorre la frase tomando cada vocal en v.
    total_vocales+=frase.count(v)

print(f"El total de las vocales en la frasa es de: {total_vocales}")

#9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
#Muéstralos en línea recta, separados por un espacio entre cada carácter.
 
cadena = "La lluvia en Mendoza es escasa"

for caracter in cadena:
    print(ord(caracter), end=" ")  
    # ord transforma un caracter en un ASCII, devuelve un numero entero
    #end=" " evita el salto de línea y pone un espacio

print()  # para dejar una línea vacía al final

#11- Pedir dos palabras por teclado, indicar si son iguales. 
"""
palabra1 =input("Ingrese la primer palabra")
palabra2 =input("Ingrese la segunda palabra")

if palabra1 == palabra2:
    print("las frases son identicas")
else:
    print("las Frases son diferentes") 
    
#13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera.  

cad1 = input("Ingrese la primera cadena: ")
cad2 = input("Ingrese la segunda cadena: ")

if cad1.count(cad2) > 0:
    print("La segunda cadena SE ENCUENTRA dentro de la primera.")
else:
    print("La segunda cadena NO se encuentra dentro de la primera.")

#15- Indique que sucede si realizo la siguiente declaración de variable:  
#x = None print(x)  
#Explique y ejemplifique el uso de None 
# None es un objeto especial que representa la ausensia de un valor o un valor nulo

resultado = None #se inicializa pero no se asigna valor
resultado = 25



