#Ejercicio Nro 10

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción"
}

# Construir nuevo diccionario: capitales -> países
capitales = {capital: pais for pais, capital in paises.items()}

# Mostrar resultado
print("Diccionario original (país -> capital):")
print(paises)

print("\nDiccionario invertido (capital -> país):")
print(capitales)