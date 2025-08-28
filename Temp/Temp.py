#Ejercicio Nro 4

print("Ingrese numeros para sumarlos en secuencia")
suma=0
fin_suma=False

while fin_suma!=True :
    numero=int(input("Ingrese un numero distinto de cero: "))
    suma=suma+numero
    if numero==0 :
        fin_suma=True

print(f"La suma acumulada es: {suma}")