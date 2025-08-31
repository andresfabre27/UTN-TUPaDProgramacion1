#1- CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la 
#conversión. Muestre por pantalla el resultado de las conversiones.  

valorDecimal = float(input("Ingrese un número decimal: "))
#entero
valorEntero = int(valorDecimal)
#string
valorTexto = str(valorDecimal)
#booleano
valorBooleano = bool(valorDecimal)  # False si es 0.0, True si es distinto de 0
#lista
valorLista = list(valorTexto)
#resultados
print("Valor original (float):", valorDecimal)
print("Convertido a entero (int):", valorEntero)
print("Convertido a texto (str):", valorTexto)
print("Convertido a booleano (bool):", valorBooleano)
print("Convertido a lista (list):", valorLista)


#3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
#y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
#efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
#14. Plantee el algoritmo planteando métodos para su resolución.