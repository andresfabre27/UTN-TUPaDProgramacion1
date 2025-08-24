#Ejercicio Nro 7

palabra=input("Ingrese una palabra: ")
vocal="aeiouAEIOU"
ultima_letra=palabra[-1] #utilizamos tecnica de rebanada para obtener ultimo caracter
letra_agregar="¡"

if ultima_letra in vocal :
    palabra_final=palabra+letra_agregar
    print(palabra_final)
else :
    print(palabra) 