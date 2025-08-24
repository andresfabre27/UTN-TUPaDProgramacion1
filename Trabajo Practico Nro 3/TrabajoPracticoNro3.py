#Trabajo Practico Nro 3
#Tema: Condicionales
#Nomnbre: Andrés Fabre, Cristian Zuñiga

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

#Ejercicio Nro 9

magnitud=float(input("Ingrese la magnitud del terremonto: "))
print("Clasificacion: ")

if magnitud<3 :
    print("Muy leve")
elif magnitud>=3 and magnitud<4 :
    print("Ligeramente perceptible")
elif magnitud>=4 and magnitud<5 :
    print("Moderado")
elif magnitud>=5 and magnitud<6 :
    print("Fuerte")
elif magnitud>=6 and magnitud<7 :
    print("Muy Fuerte")
else :
    print("Exremo")