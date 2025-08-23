#Trabajo Practico Nro 3
#Tema: Condicionales
#Nomnbre: Andrés Fabre, Cristian 

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