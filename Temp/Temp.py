#Ejercicio Nro 10

import math

numero=int(input("Ingrese un numero: "))
numero_invertido=0

while numero>0:
    digito=numero%10
    numero_invertido=numero_invertido*10+digito
    numero=math.trunc(numero/10)

print(numero_invertido)



