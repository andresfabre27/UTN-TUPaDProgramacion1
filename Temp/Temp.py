#Ejercicio Nro 10

n=int(input("Ingrese el tamaño de la matriz nxn: "))
matriz = [[int(input(f"Ingrese un numero {i} {j} : ")) for j in range(n)] for i in range(n)]

transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(f"La matriz original es: {matriz}")
print(f"La matriz transpuesta es: {transpuesta}")

if transpuesta==matriz:
    print("La matriz es simétrica")
else:
    print("La matriz no es simetrica")