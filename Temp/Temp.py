def convertir_binario(numero):
   
    if numero==1:
        return "1"
    
    elif numero==0:
        return "0"

    else:
       
        resto=numero%2
        total=str(resto)
        return convertir_binario(numero//2)+total
    

numero=int(input("Ingrese un numero: "))
      
print(convertir_binario(numero))