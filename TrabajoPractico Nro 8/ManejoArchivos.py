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

    print("Imprimimos la lista")
    
    
   
        
        
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
    
    elif opcion==2:
        agregar_producto()
    
    elif opcion==3:
        buscar_producto()

    elif opcion==4:
        menu=True
    else:
        print("Opcion incorrecta, intente nuevamente")