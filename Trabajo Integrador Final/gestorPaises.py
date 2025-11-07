from pais import Pais
#--------------------------------------------
def cargarDatosCsv(rutaArchivo):
    listaPaises = []
    
    try:
        with open(rutaArchivo, mode='r', encoding='utf-8') as archivo:
            lineas = archivo.readlines() # Leemos TODAS las líneas
            for linea in lineas[1:]: # Salta la primera línea (cabecera)
                lineaLimpia = linea.strip() # Quitamos espacios y saltos de línea
                if not lineaLimpia:# Si la línea está vacía, la saltamos
                    continue
                partes = lineaLimpia.split(',')# Separamos por comas
                if len(partes) == 4: #Validamos que sean 4 partes (nombre, poblacion, superficie, continente)
                  
                    pais_nuevo = Pais( #Objeto Pais
                        nombre=partes[0].strip(), #eliminamos espacios por si las dudas
                        poblacion=partes[1].strip(),
                        superficie=partes[2].strip(),
                        continente=partes[3].strip()
                    )
                    listaPaises.append(pais_nuevo) #Agregamos a la lista
                else:
                    print(f"Línea con formato incorrecto, omitida: {lineaLimpia}") #Muestra la linea con error

    except FileNotFoundError: #Tipo de error
        print(f"No se encontro el archivo en {rutaArchivo}") #Muestra error si no encuentra el archivo
        return []
    except Exception as e: #tipo de error generalizado
        print(f"Error inesperado al leer el CSV: {e}") #Muestra error inesperado
        return [] #los corchetes indican que aunque no se pueda leer el archivo, la funcion devuelve una lista vacia, la "promesa"

    print(f"Se cargaron {len(listaPaises)} paises.") #Muestra cantidad de paises cargados
    return listaPaises
#-------------------------------------------------------------------
def mostrarPaises(listaPaises):
    """
    Recibe una lista de objetos Pais y la imprime en un formato de tabla.
    """
    if not listaPaises: #si la lista esta vacia,muestra mensaje y sale
        print("No se encontraron paises para mostrar.")
        return

    # Imprimimos una cabecera de tabla
    print("-" * 70)
    print(f"{'Nombre':<25} | {'Continente':<15} | {'Poblacion':>15} | {'Superficie (km²)' :>15}")
    print("-" * 70)
  
    for pais in listaPaises: # Recorremos la lista e imprimimos cada país usando los atributos
        print(f"{pais.nombre:<25} | {pais.continente:<15} | {pais.poblacion:>15,} | {pais.superficie:>15,}")
    print("-" * 70)
    
#-----------------------------------------------------------    
def buscarPaisPorNombre(listaPaises, nombreBuscado):
    paises_encontrados = []  #creamos una lista vacia para guardar los resultados
    for pais in listaPaises: #recorremos la lista de paises 
        if nombreBuscado.lower() in pais.nombre.lower(): #buscamos ignorando mayusculas/minusculas (clave el in en la linea busca el contenido de la cadena en otra cadena)
            paises_encontrados.append(pais)#si coincide lo agregamos a nuestra lista de resultados
            
    return paises_encontrados #Devolvemos la lista de resultados
#-------------------------------------------------------------
def filtrarPorContinente(listaPaises, continenteBuscado):
    paisesFiltrados = []#creamos una lista vacia para guardar los resultados
    for pais in listaPaises:   #recorremos la lista de paises
        if pais.continente.lower() == continenteBuscado.lower():# Comparamos en minúscula para evitar errores
            paisesFiltrados.append(pais) #si coincide, lo agregamos a nuestra lista de resultados
            
    return paisesFiltrados # Devolvemos la lista de resultados

#-----------------------------------------------------------

def filtrarPorRangoPoblacion(listaPaises, minPob, maxPob):
    paisesFiltrados = [] #creamos una lista vacia para guardar los resultados
    for pais in listaPaises: #recorremos la lista de paises
        if minPob <= pais.poblacion <= maxPob: #verificamos si la poblacion esta dentro del rango (minimo es menor o igual al pais y el maximo es mayor o igual al pais)
            paisesFiltrados.append(pais) #si coincide, lo agregamos a nuestra lista de resultados
    return paisesFiltrados # Devolvemos la lista de resultados

#-------------------------------------------------------------------
def filtrarPorRangoSuperficie(listaPaises, minSup, maxSup):  
    paisesFiltrados = [] #creamos una lista vacia para guardar los resultados
    for pais in listaPaises: #recorremos la lista de paises
        if minSup <= pais.superficie <= maxSup: #verificamos si la poblacion esta dentro del rango (minimo es menor o igual al pais y el maximo es mayor o igual al pais)
            paisesFiltrados.append(pais) #si coincide, lo agregamos a nuestra lista de resultados
    return paisesFiltrados # Devolvemos la lista de resultados
#--------------------------------------------------------------------
def ordenarPaises(listaPaises, criterio, descendente=False):
    if not listaPaises: # si la lista esta vacia devuelve lista vacia
        return []

    listaOrdenada = list(listaPaises) #copiamos la lista para no modificar la original
    n = len(listaOrdenada) #tamaño de la lista, la usamos para los bucles
    
    for i in range(n): #recorremos la lista
        for j in range(0, n - i - 1): #bucle interno para comparar elementos 
            """
            Metodo getattr: nos permite acceder a un atributo de un objeto
            lo usamos porque el criterio es una cadena, no podemos hacer listaOrdenada[j].criterio
            getattr(objeto, "nombre_atributo") es equivalente a objeto.nombre_atributo 
            """
            valor1 = getattr(listaOrdenada[j], criterio)
            valor2 = getattr(listaOrdenada[j+1], criterio)
            
            #condicion de intercambio
            intercambiar = False
            if descendente: #descendente = True
                
                if valor1 < valor2: #si el primero es MENOR que el segundo
                    intercambiar = True
            else: #ascendente = False

                if valor1 > valor2: #si el primero es MAYOR que el segundo
                    intercambiar = True
                    
            #intercambio
            if intercambiar:
                listaOrdenada[j], listaOrdenada[j+1] = listaOrdenada[j+1], listaOrdenada[j] #intercambiamos los elementos

    return listaOrdenada #devolvemos la lista ordenada

#---------------------------------------------------------------------
def calcularEstadisticas(listaPaises):
    if not listaPaises:
        return {} # Devuelve un diccionario vacío si no hay datos
    
    paisMayorPoblacion = listaPaises[0] #no podesmos usar 0 porque sino 0 seria la poblacion mas baja
    paisMenorPoblacion = listaPaises[0] #usamos el primer pais como referencia temporal
    
    totalPoblacion = 0 #acumuladores
    totalSuperficie = 0
    conteoPorContinente = {} # Un diccionario vacío para el conteo

    for pais in listaPaises: #recorremos la lista de paises
        
        # sumamos la poblacion y superficie 
        totalPoblacion += pais.poblacion
        totalSuperficie += pais.superficie

        # Comparamos para encontrar el pais con mayor y menor poblacion (mayor)
        if pais.poblacion > paisMayorPoblacion.poblacion:
            paisMayorPoblacion = pais
        # Comparamos para encontrar el pais con mayor y menor poblacion (menor)   
        if pais.poblacion < paisMenorPoblacion.poblacion:
            paisMenorPoblacion = pais

      
        continente = pais.continente # Obtenemos el continente del país
        #nos movemos en base al continente, es decir que en vez de pasar de argentina, canada , 
        # mexico... vamos a pasar por america, america y america. como estamos usando un diccionario (no podemos repetir claves)
        #usamos el continente como clave y la cantidad de paises como valor
        if continente in conteoPorContinente:  
            # Si el continente ya está en el dicc, le sumamos 1 (paises encontrados)
            conteoPorContinente[continente] += 1
        else:
            # pero si es la primera vez que vemos este continente, lo definimos al principio con 1
            conteoPorContinente[continente] = 1
        # 
            
   #promedios con validacion de division por cero
    try:
        cantidadPaises = len(listaPaises) #cantidad de paises en la lista
        promedioPoblacion = totalPoblacion / cantidadPaises #tiene la suma de todas las poblaciones y dividimos x cant paises
        promedioSuperficie = totalSuperficie / cantidadPaises ##tiene la suma de todas las superficies y dividimos x cant paises
    except ZeroDivisionError: #tipo de error de division por cero
        #cualquiera sea el error, dejamos los promedios en 0
        promedioPoblacion = 0
        promedioSuperficie = 0

    # Creamos otro diccionario para devolver todas las estadisticas
    estadisticas = {
        "paisMayorPoblacion": paisMayorPoblacion,
        "paisMenorPoblacion": paisMenorPoblacion,
        "promedioPoblacion": promedioPoblacion,
        "promedioSuperficie": promedioSuperficie,
        "conteoPorContinente": conteoPorContinente
    }
    return estadisticas #retornamos el diccionario con las estadisticas

#__------------------------------------------------------------------
def mostrarEstadisticas(estadisticas):

    if not estadisticas: #si el diccionario esta vacio
        print("No se pudieron calcular las estadísticas (no hay datos).")
        return
    
    try: #control de errores
        print("\n--- Estadísticas ---")
        
        mayor = estadisticas["paisMayorPoblacion"] #guardamos en variables los datos del diccionario
        menor = estadisticas["paisMenorPoblacion"] #guardamos en variables los datos del diccionario
    
        print(f"Pais con MAYOR Poblacion: {mayor.nombre} ({mayor.poblacion:,})") #mostramos el nombre y la poblacion del pais con mayor poblacion
        print(f"Pais con MENOR Poblacion: {menor.nombre} ({menor.poblacion:,}\n)") #mostramos el nombre y la poblacion del pais con menor poblacion
        
        promedioPob = estadisticas["promedioPoblacion"] #guardamos en variables los datos del diccionario
        promedioSup = estadisticas["promedioSuperficie"] #guardamos en variables los datos del diccionario

        print(f"Promedio de Poblacion:   {promedioPob:,.0f}") #mostramos el promedio de poblacion
        print(f"Promedio de Superficie: {promedioSup:,.0f} km²") #mostramos el promedio de superficie
        
        print("\n--- Conteo por Continente ---")
        
        conteo = estadisticas["conteoPorContinente"]
        
        if not conteo:
            print("\nNo hay datos de continentes.")
            return
            
        for continente, cantidad in conteo.items():
            print(f"  - {continente}: {cantidad} paises")
    
    except Exception as e: #cualquier error
        print(f"\nerror: {e}")