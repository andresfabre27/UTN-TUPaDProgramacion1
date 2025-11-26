#Trabajo Practico Nro 8
#Tema: Manejo de Archivos
#Nombre: Daniel Andrés Fabre

#Ejercicio 2

direccion=r"C:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\TrabajoPractico Nro 8\productos.txt"
with open(direccion, "r") as archivo:
    
    for linea in archivo:
        partes=linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")

#Ejercicio Nro 3  

direccion=r"C:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\TrabajoPractico Nro 8\productos.txt"
with open(direccion, "r") as archivo:
    
    for linea in archivo:
        partes=linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}") 

print("Ingrese un nuevo producto")
nombre=input("Ingrese el nombre: ")
precio=float(input("Ingrese el precio: ")) 
cantidad=int(input("Ingrese la cantidad: "))

with open(direccion, "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

#Ejercicio Nro 4  

direccion=r"C:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\TrabajoPractico Nro 8\productos.txt"
with open(direccion, "r") as archivo:
    
    for linea in archivo:
        partes=linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}") 

print("Ingrese un nuevo producto")
nombre=input("Ingrese el nombre: ")
precio=float(input("Ingrese el precio: ")) 
cantidad=int(input("Ingrese la cantidad: "))

with open(direccion, "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    
with open(direccion, "r") as archivo:
    productos=[]
    for linea in archivo:
        almacen=linea.split(",")
        productos.append({"nombre":almacen[0].strip(),"precio":almacen[1].strip(),"cantidad":almacen[2].strip()})

print(productos)

#Ejercicio Nro 5

direccion=r"C:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\TrabajoPractico Nro 8\productos.txt"
with open(direccion, "r") as archivo:
    
    buscar=input("Ingrese un producto para buscarlo: ")
    producto_encontrado=False

    for linea in archivo:
        if buscar in linea:
            partes=linea.split(",")
            print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")
            producto_encontrado=True 

    if producto_encontrado==False:
        print("Error, producto no encontrado")

#Ejercicio Nro 6

def crear_lista(): #Creamos una lista
    
    productos=[]
    with open(direccion, "r") as archivo: 
        for linea in archivo:
            almacen=linea.split(",")
            productos.append({"nombre":almacen[0].strip(),"precio":almacen[1].strip(),"cantidad":almacen[2].strip()})

    return productos
    
def actualizar_productos(productos):

    with open(direccion, "w") as archivo:
        for filas in productos:
            temporal=list(filas.values())
            contador=0   
            for palabra in temporal:
                archivo.write(palabra)
                if contador<2:
                    archivo.write(",")
                contador+=1
            archivo.write("\n")


        
def mostrar_archivo(): #Mostramos el archivo

    with open(direccion, "r") as archivo: 
    
        for linea in archivo:
            partes=linea.split(",")
            print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}") 


def agregar_producto(): #Agregamos productos al archivo

    print("Ingrese un nuevo producto")
    nombre=input("Ingrese el nombre: ")
    precio=float(input("Ingrese el precio: ")) 
    cantidad=int(input("Ingrese la cantidad: "))

    with open(direccion, "a") as archivo: 
        archivo.write(f"{nombre},{precio},{cantidad}\n")

def buscar_producto():

    with open(direccion, "r") as archivo: #Buscamos un producto
    
        buscar=input("Ingrese un producto para buscarlo: ")
        producto_encontrado=False

        for linea in archivo:
            if buscar in linea:
                partes=linea.split(",")
                print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")
                producto_encontrado=True 

        if producto_encontrado==False:
            print("Error, producto no encontrado")

direccion=r"C:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\TrabajoPractico Nro 8\productos.txt"
crear_lista()

menu=False

while menu==False:
    opcion=int(input("1- Mostrar Archivo 2-Argregar Producto 3-Buscar Producto 4-Salir \n")) 
    if opcion==1:
        mostrar_archivo()
        actualizar_productos(crear_lista())
    
    elif opcion==2:
        agregar_producto()
        actualizar_productos(crear_lista())

    
    elif opcion==3:
        buscar_producto()
        actualizar_productos(crear_lista())

    elif opcion==4:
        menu=True
    else:
        print("Opcion incorrecta, intente nuevamente")

#Ejercicio Nro 6 mejorado

import os

direccion=os.path.join(os.path.dirname(__file__), 'productos.txt')

def cargar_en_diccionario():

    lista=[]

    with open(direccion,"r") as archivo:
        for linea in archivo:
            temp=linea.split(",")
            diccionario={
            "nombre":temp[0],
            "precio":temp[1],
            "cantidad":temp[2]
            }
            lista.append(diccionario)
            
    guardar_productos_actualizados(lista)
    
def guardar_productos_actualizados(lista):

    with open(direccion,"w") as archivo:
        
        for linea in lista:
            
            archivo.write(f"{linea["nombre"].strip()},{linea["precio"].strip()},{linea["cantidad"].strip()}\n")
            



def agregar_producto(nombre,precio,cantidad):
    with open(direccion,"a") as archivo:

        archivo.write(f"{nombre},{precio},{cantidad}\n")

def buscar_producto():

    with open(direccion,"r") as archivo:
        
        encontrado=False
        producto=input("Ingrese el nombre del producto: ")
        for linea in archivo:
            temp=linea.split(",")
            if producto in temp:
                print(f"Producto: {temp[0].strip()} | Precio: ${temp[1].strip()} | Cantidad: {temp[2].strip()}")
                encontrado=True
            
        if encontrado==True:
            pass
        else:
            print("Producto no encontrado")




def mostrar_productos():
    with open(direccion,"r") as archivo:

        for linea in archivo:

            temp=linea.split(",")
            print(f"Producto: {temp[0].strip()} | Precio: ${temp[1].strip()} | Cantidad: {temp[2].strip()}")


menu=False

while menu==False:

    opcion=input("A-Leer Productos B-Agregar Producto C-Buscar Producto D-Salir\n")

    if opcion=="A":
        mostrar_productos()
        cargar_en_diccionario()

    elif opcion=="B":
        nombre=input("Ingrese el nombre del producto: ")
        precio=int(input("Ingrese el precio del producto: "))
        cantidad=int(input("Ingrese la cantidad de productos: "))

        agregar_producto(nombre,precio,cantidad)
        cargar_en_diccionario()

    elif opcion=="C":
        buscar_producto()
        cargar_en_diccionario()

    elif opcion=="D":
        menu=True

    else:
        print("Error de menu")









    
