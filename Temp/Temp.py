#Ejercicio Nro 8

nombre=input("Ingrese su nombre: ")
print(""" 1- Si quiere su nombre en mayúsculas.
 2- Si quiere su nombre en minúsculas.
 3- Si quiere su nombre con la primera letra mayúscula.""")
menu=int(input("Ingrese el numero: "))

if menu==1 :
    print(nombre.upper())
elif menu==2 :
    print(nombre.lower())
elif menu==3 :
    print(nombre.title())
else :
    print("No elijio una opción valida")