#EJercicio Nro 4

def convertir_binario(numero):
    lista=[]

    while(numero>0):
        
        resto=numero%2
        lista.append(resto)
        numero=numero//2
    
    invertido=lista[::-1]
    cadena_de_numeros = "".join(str(x) for x in invertido)
    return cadena_de_numeros


numero=int(input("Ingrese un numero para convertirlo en binario: "))
print(convertir_binario(numero))

