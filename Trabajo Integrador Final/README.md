# TPI Programación 1: Gestión de Datos de Países 

Repositorio para el Trabajo Práctico Integrador de la materia Programación 1 (Tecnicatura en Programación, UTN).

## 1. Descripción del Programa

Esta es una aplicación de consola desarrollada en Python que gestiona un conjunto de datos de países. El programa lee la información desde un archivo `paises.csv` y ofrece un menú de usuario para interactuar con los datos.

### Funcionalidades Principales
* **Carga de Datos:** Lectura manual del archivo `paises.csv`, procesando cada línea y creando una lista de objetos `Pais`.
* **Búsqueda:** Búsqueda de países por nombre (parcial e insensible a mayúsculas).
* **Filtrado:** Sub-menú para filtrar la lista de países por continente, rango de población o rango de superficie.
* **Ordenamiento:** Ordenamiento de la lista por nombre, población o superficie (ascendente o descendente), utilizando una implementación manual del algoritmo Bubble Sort.
* **Estadísticas:** Cálculo de datos clave, incluyendo el país con mayor/menor población, promedios, y un conteo de países por continente. 

### Arquitectura
El proyecto está modularizado en tres archivos principales:
* `pais.py`: Define la clase `Pais`, que sirve como molde para cada registro.
* `gestorPaises.py`: Módulo que contiene toda la lógica de negocio (carga, búsqueda, filtros, ordenamiento y estadísticas).
* `main.py`: Punto de entrada de la aplicación. Contiene el menú principal, la interacción con el usuario y las validaciones de entrada.

---

## 2. Instrucciones de Uso

### Requisitos
* Python 3.x

### Ejecución
1.  Asegúrese de que todos los archivos (`main.py`, `gestorPaises.py`, `pais.py`, `paises.csv`) se encuentren en el mismo directorio.
2.  Abra una terminal en la ubicación del proyecto.
3.  Ejecute el script `main.py` con el siguiente comando:

# En Windows
python main.py

# En macOS / Linux
python3 main.py

##Ejemplos de Entradas y Salidas
###Menú Principal

```
--- 🌎 Gestión de Datos de Países 🌎 ---
1. Buscar país por nombre
2. Filtrar países por...
3. Ordenar países por...
4. Mostrar estadísticas
5. Mostrar todos los países
6. Salir
Seleccione una opción (1-6):
```

###Ejemplo de Filtro por Población (Opción 2b)
```
Seleccione una opción (1-6): 2

--- 🔎 Filtrar Países ---
a. Por Continente
b. Por Rango de Población
c. Por Rango de Superficie
Seleccione un tipo de filtro (a, b, c): b
--- Filtro por Población ---
Ingrese la población MÍNIMA: 100000000
Ingrese la población MÁXIMA (mín. 100,000,000): 300000000

Se encontraron 3 países con ese filtro:
----------------------------------------------------------------------
Nombre                    | Continente      |       Población |   Superficie (km²)
----------------------------------------------------------------------
Japon                     | Asia            |     125,800,000 |          377,975
Brasil                    | America         |     213,993,437 |        8,515,767
Nigeria                   | Africa          |     206,139,589 |          923,768
----------------------------------------------------------------------
```
###Ejemplo de Estadísticas (Opción 4)

```
Seleccione una opción (1-6): 4

--- 📈 Estadísticas Globales 📈 ---
País con MAYOR Población: India (1,380,004,385)
País con MENOR Población: Australia (25,687,041)
Promedio de Población:   213,999,800
Promedio de Superficie: 3,425,768 km²

--- Conteo por Continente ---
  - America: 3 países
  - Asia: 2 países
  - Europa: 2 países
  - Africa: 2 países
  - Oceania: 1 países
---------------------------------
```

###### *Readme creado con [Meditor.mb](http://https://pandao.github.io/editor.md/en.html "Meditor.mb") Open source online Markdown editor.*