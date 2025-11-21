import gestorPaises #importamos modulo (caja de herramientas)
import pathlib #importamos modulo para manejar rutas de archivos

# Esqueleto del programa
def mostrarMenu():
    print("--- Gestion de datos de Paises ---")
    print("1. buscar país por nombre")
    print("2. Filtrar paises por...")
    print("3. Ordenar paises por...")
    print("4. Mostrar estadísticas")
    print("5. mostrar todos los paises (para probar)")
    print("6. Salir")
    
#---------------------------------------------   

def validarEnteroPositivo(mensaje):
    while True: #Bucle infinito hasta que el usuario ingrese un valor correcto
        try:
            valorCad = input(mensaje)
            valorNum = int(valorCad)
            if valorNum >= 0:
                return valorNum 
            else:
                print(": El numero no puede ser negativo.")
        except ValueError:
            print("Por favor, ingrese solo un numero entero.")
                        
#usamos esta funcion para validar que el min y max de poblacion y
# superficie sean numeros enteros positivos
              
#___------------------------------------------------------------------

def validarSiNo(mensaje):
    while True: #bucle infinito hasta que el usuario ingrese un valor correcto
        respuesta = input(mensaje).lower().strip()
        if respuesta == 's' or respuesta == 'si':
            return True # Devuelve True para 'si'
        elif respuesta == 'n' or respuesta == 'no':
            return False # Devuelve False para 'no'
        else:
            print("Responda solo 's' (si) o 'n' (no).")  
            
#usamos esta funcion para validar si el usuario quiere orden descendente o no y que responda s o n
       
#----------_-----------------------------------------------------
#carga de datos

def main():
    rutaArchivo = pathlib.Path(__file__).parent #Es para que encuentre el archivo csv en la misma carpeta 
    rutaCsv = rutaArchivo / "paises.csv" #une la ruta de la carpeta con el nombre del archivo csv
    print(f"Cargando dato desde: {rutaCsv}")
    listaPaises = gestorPaises.cargarDatosCsv(rutaCsv) #llamamos a la funcion cargarDatosCsv
    
   
    if not listaPaises: #si la lista esta vacia muestra mensaje y termina el programa
        print("No se pudieron cargar los datos. El programa terminara.")
        return  # sale de la funcion main y termina el programa


#Bucle del menu , Esqueleto
    while True: #bucle infinito hasta que el usuario elija salir (opcion 6)
        mostrarMenu()
        opcion = input("Seleccione una opcion (1-6): ") #pedimos al usuario que ingrese una opcion
        
        try: #validamos que la opcion sea un numero
            opcion = int(opcion) #convertimos la opcion a entero
        except ValueError:
            print("Opcion no valida. Debe ingresar un NUMERO.")
            continue  # Vuelve al inicio del bucle while
            
  
        if opcion == 1:
            
            print("\n--- Busqueda de Pais por Nombre ---")
            nombre = input("Ingrese el nombre (o parte del nombre) del pais: ")
            
            resultados = gestorPaises.buscarPaisPorNombre(listaPaises, nombre) #llamamos a la funcion
            
            if resultados: #si hay resultados los mostramos
                print(f"Se encontraron {len(resultados)} coincidencias:")
                gestorPaises.mostrarPaises(resultados) #mostramos paises encontrados con el formato ordenado
            else: #si no hay resultados mostramos mensaje
                print(f"No se encontraron paises con el nombre '{nombre}'.")
            
        elif opcion == 2:
            print("\n--- Filtrar Paises ---")
            print("a. Por Continente") 
            print("b. Por Rango de Poblacion") 
            print("c. Por Rango de Superficie") 
            # pedimos al usuario que ingrese una subopcion y la convertimos a minusculas y quitamos espacios
            subOpcion = input("Seleccione un tipo de filtro (a, b, c) o cualquier letra para salir: ").lower().strip() 
            
            resultados = [] # Preparamos una lista para los resultados
            
            if subOpcion == 'a': #subociones de filto
                continente = input("Ingrese el nombre del continente: ")
                resultados = gestorPaises.filtrarPorContinente(listaPaises, continente) #llamamos a la funcion
                
            elif subOpcion == 'b':
                print("--- Filtro por Poblacion ---")
                print("\n ADVERTECIA: Ingrese numeros enteros positivos.\n")
                minPob = validarEnteroPositivo("Ingrese la poblacion MINIMA: ") #usamos la funcion para validar
                maxPob = validarEnteroPositivo(f"Ingrese la poblacion MAXIMA (min. {minPob:,}): ") #usamos la funcion para validar
                
                if maxPob < minPob: #validamos que el maximo ingresado no sea menor al minimo
                    print("La poblacion maxima no puede ser menor a la minima.")
                else:
                    resultados = gestorPaises.filtrarPorRangoPoblacion(listaPaises, minPob, maxPob) #llamamos a la funcion

            elif subOpcion == 'c':
                print("--- Filtro por Superficie ---")
                print("\n ADVERTECIA: Ingrese numeros enteros positivos.\n")
                minSup = validarEnteroPositivo("Ingrese la superficie MINIMA (km²): ")#usamos la funcion para validar
                maxSup = validarEnteroPositivo(f"Ingrese la superficie MAXIMA (min. {minSup:,}): ")#usamos la funcion para validar

                if maxSup < minSup: #validamos que el maximo ingresado no sea menor al minimo
                    print("La superficie maxima no puede ser menor a la minima.")
                else:
                    resultados = gestorPaises.filtrarPorRangoSuperficie(listaPaises, minSup, maxSup)
            
            else:
                print("Opcion de filtro no valida.") #si la opcion no es valida vuelve al menu principal para no generar bucle infinito en la subopcion

            # Mostramos los resultados (si los hay)
            if resultados:
                print(f"\nSe encotraron {len(resultados)} paises con ese filtro:") #mostramos la cantidad de paises encontrados
                gestorPaises.mostrarPaises(resultados) #mostramos paises encontrados con el formato ordenado
            elif subOpcion in ['a', 'b', 'c']: # Solo muestra si la opción era valida
                print("No se encontraron paises que cumplan con el filtro.") 
            
        elif opcion == 3:
            print("\n--- Ordenar Paises ---")
            print("a. Por Nombre")
            print("b. Por Poblacion")
            print("c. Por Superficie")
            subOpcion = input("Seleccione un criterio de orden (a, b, c): ").lower().strip()
            
            criterio = None # Variable para guardar el atributo a ordenar
            """
            usamos la variable criterio para pedir al usuario que ingrese la forma de orden, luego esa variable se la pasamos a la funcion 
            y en la funcion usamos getattr para obtener el atributo dinamicamente segun lo que el usuario haya elegido
            
            """
            
            if subOpcion == 'a':
                criterio = "nombre"
            elif subOpcion == 'b':
                criterio = "poblacion"
            elif subOpcion == 'c':
                criterio = "superficie"
            else:
                print("Opcion de orden no valida.")
                continue # Vuelve al menu principal para no generar bucle infinito en la subopcion

           
            esDecendente = validarSiNo("¿Desea ordenar de forma DECENDENTE? (s/n): ") #usamos la funcion para validar si o no y guardar en variable
            
            listaOrdenada = gestorPaises.ordenarPaises(list(listaPaises), criterio, esDecendente)
            
            # Mostramos los resultados
            orden = "Decendente" if esDecendente else "Ascendente"
            print(f"\n--- Paises ordenados por '{criterio}' ({orden}) ---")
            gestorPaises.mostrarPaises(listaOrdenada)
            
        elif opcion == 4:
            estadisticas = gestorPaises.calcularEstadisticas(listaPaises)
            
            gestorPaises.mostrarEstadisticas(estadisticas)

        elif opcion == 5:
            print("\n--- Lista Complta de Paises ---")
            gestorPaises.mostrarPaises(listaPaises)

        elif opcion == 6:
            print("¡Hasta luego!")
            break  #break rompe el bucle while y termina el programa
            
        else:
            print("Opcion no valida.Elija entre 1 y 6.")

if __name__ == "__main__": 
    main()