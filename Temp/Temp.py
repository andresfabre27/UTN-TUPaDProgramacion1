
original={"Argentina":"Buenos Aires",
          "Chile":"Santiago",
          "Peru":"Lima"
          
          }

print(original)

invertido={}

for clave,valor in original.items():
    invertido[valor]=clave

print(invertido)



