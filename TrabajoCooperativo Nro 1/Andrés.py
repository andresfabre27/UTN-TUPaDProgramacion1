#Trabajo Practico cooperativo Nro 1
#Nombre: Andrés Fabre

#Ejercicio Nro 2

"""""
En Python, asignar un valor fuera del rango definido de una variable causa un error específico del tipo de dato (por ejemplo, ValueError para caracteres o IndexError para listas), ya que no hay un límite nativo en la asignación de tipos numéricos. Para resolverlo, se debe validar la entrada del valor con condiciones if antes de la asignación, o manejar la posible excepción usando bloques try-except para capturar el error y actuar de manera controlada, evitando que el programa se detenga abruptamente. 
¿Qué ocurre?
No hay un error genérico de "rango" para todos los tipos de variables:
Python no impone un límite de rango para variables numéricas como enteros o flotantes; puedes asignar un número muy grande sin problema. 
Errores específicos:
Los errores ocurren cuando la asignación o el uso de ese valor viola las restricciones de un tipo de dato o estructura específica.
ValueError: Si intentas, por ejemplo, convertir un número a un carácter con chr() y este está fuera del rango de valores ASCII válidos, obtendrás este error. 
IndexError: Si intentas acceder o asignar a un índice de una lista o secuencia que no existe, te encontrarás con un IndexError. 
Otros errores: Dependiendo del contexto, otras funciones o operaciones pueden arrojar errores si un valor está fuera de sus rangos permitidos.
¿Cómo resolverlo? 
Validación de entrada (con if):
Comprobar límites: Usa operadores de comparación (>, >=, <, <=) para verificar si el valor está dentro del rango deseado antes de asignarlo o usarlo.
Ejemplo:
Python

        edad = -5
        if 0 <= edad <= 120:
            print(f"Edad válida: {edad}")
        else:
            print("La edad está fuera de rango.")
Manejo de excepciones (con try-except):
Capturar el error: Envuelve el código que podría generar el error en un bloque try y maneja el error específico en un bloque except. 
Ejemplo:
Python

        try:
            # Código que podría generar un error, por ejemplo, al asignar un índice fuera de rango
            mi_lista = [1, 2]
            print(mi_lista[3]) # Esto causará un IndexError
        except IndexError:
            print("Error: Índice de lista fuera de rango. Se manejará el error.")
            # Puedes asignar un valor por defecto, registrar el error, etc.
Uso de lógica condicional en el uso del valor:
Asegúrate de que la operación o función que recibe el valor pueda manejarlo, o realiza una conversión de tipo si es necesario. 
Ejemplo:
Python

        valor_potencial = "100000000000000000000" # Un número muy grande
        try:
            numero_entero = int(valor_potencial)
            print(f"Número asignado: {numero_entero}")
        except OverflowError:
            print("El valor es demasiado grande para un entero")
""" 

#Ejercicio Nro 4

#Ejercicio Nro 6

cadena="La lluvia en Mendoza es escasa"
palabras=cadena.split() #divide la cadena en una lista de palabras sin espacios
cadena_sin_espacios="".join(palabras) #unimos las palabras con "" para q no haya espacios entre ellas
tamaño=int(len(cadena_sin_espacios))
print(f"El tamaño es: {tamaño}")

#Ejercicio Nro 8

palabra=input("Ingrese una palabra: ")
nueva_palabra=palabra.replace("a","e")
print(f"La nueva palabra es: {nueva_palabra}")

#Ejercicio Nro 10

palabra=input("Ingrese una palabra: ")
menu=int(input("1-Mayusculas 2-Minusculas\n"))

if menu==1:
    nueva_palabra=palabra.upper()
elif menu==2:
    nueva_palabra=palabra.lower()
else:
    nueva_palabra="Error de Menu"

print(nueva_palabra)

#Ejercicio Nro 12

cadena="hipopotamo"
nueva_cadena=cadena[3:5]
print(nueva_cadena)

