#Trabajo Practico Nro 3
#Tema: Condicionales
#Nomnbre: Andrés Fabre, Cristian 
"""
#Ejercicio Nro 1
edad=int(input("Ingresa tu edad: "))

if edad>=18 :
    print("Sos mayor de edad")




#Ejercicio Nro 2

nota=int(input("Ingresa tu nota: "))

if nota>=6 :
    print("Aprobado")

else :
    print("Desaprobado")

#Ejercicio Nro 3

numero=float(input("Ingrese un numero PAR: "))

if numero%2==0 :
    print("Ha ingresado un número PAR")

else :
    print("Por favor, ingrese un numero PAR")

#Ejercicio Nro 4

edad=int(input("Ingresa tu edad: "))

if edad<12 :
    print("Eres un niño")

elif edad>=12 and edad <18 :
    print("Eres un Adolecente")

elif edad>=18 and edad <30 :
    print("Eres un Adulto/a joven")

else :
    print("Eres un Adulto/a")


#Ejercicio Nro 5

contraseña=input("Ingresa una contraseña entre 8 y 14 caracteres: ")

if len(contraseña)>=8 and len(contraseña)<=14 :
    print("Ha ingresado una contraseña correcta")

else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio Nro 6
import random
from statistics import mode, median, mean

numeros_aleatorios=[random.randint(1,100) for i in range(50)]
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

if media>mediana and mediana>moda :

    print("Hay Sesgo positivo o a la derecha")

elif media<mediana and mediana<moda :

    print("Hay Sesgo negativo o a la izquierda")

elif media==mediana==moda :

    print("Sin sesgo")


#Ejercicio Nro 7

palabra=input("Ingrese una palabra: ")
vocal="aeiouAEIOU"
ultima_letra=palabra[-1] #utilizamos tecnica de rebanada para obtener ultimo caracter
letra_agregar="¡"

if ultima_letra in vocal :
    palabra_final=palabra+letra_agregar
    print(palabra_final)
else :
    print(palabra) 
   """
#Ejercicio Nro 8

#Pedimos los datos y la opcion que desea realizar
nombre=input("Ingrese Su nombre.")
opcion=int(input("Ingrese la opcion deseada:\nOpcion 1 si quiere su nombre en mayuscula\nOpcion 2 si lo quiere en minuscula\nOpcion 3 si solo quiere la primer letra en mayuscula. "))

# Usamos condicionales para transformar el nombre según la opción
if opcion == 1:
    print(f"tu nombre en mayuscula es {nombre.upper()}")   
elif opcion == 2:
    print(f"tu nombre en mayuscula es {nombre.lower()}")   
elif opcion == 3:
    print(f"tu nombre en mayuscula es {nombre.title()}")
else:
    print("la opcion ingresada no es correcta")
    
#Ejercicio Nro 9

#Pedimos los Datos
magnitud = float(input("ingrese la magnitud del sismo. "))
#Definimos la magnitud e imprimimos
if magnitud < 3 :
    print ("La MAgnitud del sismo fue Muy  leve ")
elif magnitud >=3 and magnitud < 4:
    print ("La MAgnitud del sismo fue Leve ")
elif magnitud >=4 and magnitud < 5:
    print ("La MAgnitud del sismo fue Moderado ")
elif magnitud >=5 and magnitud < 6:
    print ("La MAgnitud del sismo fue Fuerte")
elif magnitud >=6 and magnitud < 7:
    print ("La MAgnitud del sismo fue Muy Fuerte")
else:
    print ("La MAgnitud del sismo fue Extremo")

#entiendo que el ejercicio pide Mayor o igual que 3  y menor que 4, etc pero el rango de diferencia es minima pero se podria ahorra codigo de la siguiente forma
    """
    if magnitud < 3:
    print("La magnitud del sismo fue muy leve")
elif magnitud < 4:
    print("La magnitud del sismo fue leve")
elif magnitud < 5:
    print("La magnitud del sismo fue moderado")
elif magnitud < 6:
    print("La magnitud del sismo fue fuerte")
elif magnitud < 7:
    print("La magnitud del sismo fue muy fuerte")
else:
    print("La magnitud del sismo fue extremo")
    """

