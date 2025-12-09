

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

numero=int(input("Ingrese del 1 al 9: "))


"""for i in range(len(matriz)):
    if numero==matriz[i][0]:
        posicion=i"""

contador=0
for linea in matriz:
    if numero in linea:
        posicion=contador
    contador+=1

print(f"El numero esta en la posicion {posicion}") 



