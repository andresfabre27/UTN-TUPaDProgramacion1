"""
| Función                 | Descripción                                       | Ejemplo                            |
| ----------------------- | ------------------------------------------------- | ---------------------------------- |
| `len(lista)`            | Devuelve la cantidad de elementos                 | `len([1,2,3]) → 3`                 |
| `sum(lista)`            | Devuelve la suma de los elementos (numéricos)     | `sum([1,2,3]) → 6`                 |
| `max(lista)`            | Devuelve el mayor valor                           | `max([1,4,2]) → 4`                 |
| `min(lista)`            | Devuelve el menor valor                           | `min([1,4,2]) → 1`                 |
| `sorted(lista)`         | Devuelve una **nueva lista** ordenada             | `sorted([3,1,2]) → [1,2,3]`        |
| `list(objeto_iterable)` | Convierte un iterable en lista                    | `list("hola") → ['h','o','l','a']` |
| `any(lista)`            | Devuelve True si **algún elemento es True**       | `any([0,0,1]) → True`              |
| `all(lista)`            | Devuelve True si **todos los elementos son True** | `all([1,2,3]) → True`              |


| Método             | Descripción                                                | Ejemplo                           |
| ------------------ | ---------------------------------------------------------- | --------------------------------- |
| `append(x)`        | Agrega un elemento al final                                | `[1,2].append(3) → [1,2,3]`       |
| `extend(iterable)` | Agrega varios elementos                                    | `[1,2].extend([3,4]) → [1,2,3,4]` |
| `insert(i, x)`     | Inserta un elemento en el índice `i`                       | `[1,2].insert(1,99) → [1,99,2]`   |
| `remove(x)`        | Elimina la **primera aparición** de `x`                    | `[1,2,2,3].remove(2) → [1,2,3]`   |
| `pop(i=-1)`        | Elimina y devuelve el elemento en `i` (último por defecto) | `[1,2,3].pop() → 3`               |
| `index(x)`         | Devuelve la posición de la primera aparición de `x`        | `[1,2,3].index(2) → 1`            |
| `count(x)`         | Devuelve cuántas veces aparece `x`                         | `[1,2,2].count(2) → 2`            |
| `sort()`           | Ordena la lista **modificándola**                          | `lista.sort()`                    |
| `reverse()`        | Invierte la lista **modificándola**                        | `[1,2,3].reverse() → [3,2,1]`     |
| `copy()`           | Devuelve una copia superficial de la lista                 | `nueva = lista.copy()`            |
| `clear()`          | Elimina todos los elementos de la lista                    | `lista.clear()`                   |
  
    """

#Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
#suma de todos los elementos en la lista.

entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [float(x) for x in entrada.split()] #split, separa la cadena en partes dividido por espacios y los ingresa en una lista

promedio = sum(numeros)

print("La suma de los elementos es:", promedio)

#Escribe un programa que permita al usuario ingresar una lista y la invierta.

entrada = input("Ingrese los elementos de la lista separados por espacios: ")

lista = entrada.split()

lista.reverse()

print("La lista invertida es:", lista)

#Escribe un programa que multiplique cada elemento de una lista de números por un 
#valor ingresado por el usuario. 

entrada = input("Ingrese una lista de números separados por espacios: ")

lista = [float(x) for x in entrada.split()]

multiplicador = float(input("Ingrese el valor por el cual quiere multiplicar: "))

resultado = [num * multiplicador for num in lista]

print("La lista resultante es:", resultado)

#Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
#promedio de los elementos. 

entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [float(x) for x in entrada.split()] #split, separa la cadena en partes dividido por espacios y los ingresa en una lista
cant_numeros= len(numeros)

promedio = sum(numeros)/cant_numeros

print("La suma de los elementos es:", promedio)

