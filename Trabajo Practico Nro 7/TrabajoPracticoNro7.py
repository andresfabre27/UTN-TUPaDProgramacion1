#Trabajo Practico Nro 7
#Estructuras de datos complejas
#Nombre: Daniel Andrés Fabre

#Ejercicio Nro 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

print(precios_frutas)

#Ejercicio Nro 2

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800

print(precios_frutas)

#Ejercicio Nro 3

lista=list(precios_frutas)

print(lista)

#Ejercicio Nro 4

print("Ingrese 5 contactos")
diccionario={}

for i in range(5):
    nombre=input(f"Ingresa el nombre del contacto Nro {i+1}: ")
    dato=input("Ingresa el numero telefonico: ")
    diccionario[nombre]=dato

mostrar_nombre=input("Ingrese el nombre para mostrar su numero: ")

if mostrar_nombre in diccionario:
    print(diccionario[mostrar_nombre])
else:
    print("No existe el registro")

#Ejercicio Nro 5

frase=input("Ingrese una frase: ")

conjunto=set(frase.split())
lista=frase.split()
print(conjunto)
diccionario={}

for palabra in lista:
    if palabra in diccionario:
        diccionario[palabra]+=1
    else:
        diccionario[palabra]=1

print(diccionario)

#Ejercicio Nro 6

diccionario={}
nota=[0,0,0]
promedio=[]

for i in range(3):
    nombre=input(f"Ingrese el nombre del alumno numero {i+1}: ")
    promedio.append(0)
    for j in range(3):

        nota[j]=float(input(f"Ingrese la nota numero {j+1}: "))
        promedio[i]=promedio[i]+nota[j]
    promedio[i]=promedio[i]/3
    diccionario[nombre]=(nota[0],nota[1],nota[2])

print(diccionario)
print(f"Los promedios son: {promedio}")


#Ejercicio Nro 7

parcial1={"Andres","Cristian","Luciano","Federico","Yanina","Elio","Rosa","Anibal"}
parcial2={"Andres","Luciano","Rosa","Teresa","Silvana"}



ambos_parciales=parcial1&parcial2
solo_uno_de_los_dos=parcial1^parcial2
al_menos_un_parcial=parcial1|parcial2

print(f"Aprobaron ambos parciales: {ambos_parciales}")
print(f"Aprobaron solo uno de los dos parciales: {solo_uno_de_los_dos}")
print(f"Aprobo al menos uno: {al_menos_un_parcial}")

#Ejercicio Nr 8

diccionario={}

salir=False

while(salir!=True):

   menu=int(input("1-Consultar stock 2-Agregar Stock 3-Agregar producto Nuevo 4-Salir\n "))

   if menu==1:
      stock=input("Ingrese el nombre del producto: ")
      if stock in diccionario:
         print(diccionario[stock])

      else:
         print("Producto no encontrado")

   elif menu==2:
      stock=input("Ingrese el nombre del producto: ")
      if stock in diccionario:
         cantidad=int(input("Ingrese la cantidad a agregar: "))    
         diccionario[stock]+=cantidad
         print("Hecho")

      else:
         print("Stock no encontrado")

   elif menu==3:
      stock=input("Ingrese el nombre del producto a agregar: ")
      if stock in diccionario:
         print("El producto ya existe")
      else:
         cantidad=int(input("Ingrese la cantidad a agregar: "))
         diccionario[stock]=cantidad
         print("Hecho")

   elif menu==4:
      salir=True

   else:
      print("Opcion incorrecta")

#Ejercicio Nro 9

agenda={("lunes","10:00"): "Reunion",
        ("martes","15:00"): "Clases de ingles",
        ("miercoles", "18:00"): "Gimnasio",
        ("Jueves", "8:00"): "Cursado Facultad"
        }

dia=input("Ingrese el dia: ")
hora=input("Ingrese la hora: ")
clave=(dia,hora)

if clave in agenda:
    print(agenda[clave])
else:
    print("Nada para esta fecha")

#Ejercicio Nro 10

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción"
}

# Construir nuevo diccionario: capitales -> países
capitales = {capital: pais for pais, capital in paises.items()}


print("Diccionario original (país -> capital):")
print(paises)

print("\nDiccionario invertido (capital -> país):")
print(capitales)