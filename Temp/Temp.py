
<<<<<<< Updated upstream

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



=======
def fibonaci(n):

    if n==0 or n==1:
        return n
    
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    
numero=int(input("Ingrese hasta que posicion se calculara la serie de Fibonacci: "))

for i in range(numero+1):
    print(f"{fibonaci(i)}",end=" ")
>>>>>>> Stashed changes
