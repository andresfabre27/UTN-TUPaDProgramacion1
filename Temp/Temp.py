#Ejercicio Nro 9

magnitud=float(input("Ingrese la magnitud del terremonto: "))
print("Clasificacion: ")

if magnitud<3 :
    print("Muy leve")
elif magnitud>=3 and magnitud<4 :
    print("Ligeramente perceptible")
elif magnitud>=4 and magnitud<5 :
    print("Moderado")
elif magnitud>=5 and magnitud<6 :
    print("Fuerte")
elif magnitud>=6 and magnitud<7 :
    print("Muy Fuerte")
else :
    print("Exremo")

