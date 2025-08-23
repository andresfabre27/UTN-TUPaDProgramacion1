#Ejercicio Nro 5

contraseña=input("Ingresa una contraseña entre 8 y 14 caracteres: ")

if len(contraseña)>=8 and len(contraseña)<=14 :
    print("Ha ingresado una contraseña correcta")

else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")