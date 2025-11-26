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


