
numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))

# Usar comprensión de listas para separar pares e impares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))