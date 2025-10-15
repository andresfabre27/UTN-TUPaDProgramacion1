#Ejercicio Nro 5

def es_palindromo(palabra):

    
    largo=len(palabra)
    if len(palabra)==1:
        return True
    
    if palabra[0]==palabra[-1]:

        return es_palindromo(palabra[1:largo-1])
    
    else:
        return False
    

palabra=input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")



