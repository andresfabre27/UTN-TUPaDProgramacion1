#Ejercicio Nro 5

def es_palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:                        
        return True
    else:
        if palabra[0]==palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False
        
palabra=input("Ingrese una palabra: ")
print(f"¿Es palindromo? {es_palindromo(palabra)}")