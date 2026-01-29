#Ejercicio 3

import os

direccion=os.path.join(os.path.dirname(__file__), 'productos.txt')

productos=[]

def cargar_productos_lista(productos):
    productos.clear()
    with open(direccion,"r") as archivo:
        for linea in archivo:
            temp=linea.split(",")
            diccionario={} 
            diccionario["Producto"]=temp[0]
            diccionario["Precio"]=temp[1]
            diccionario["Cantidad"]=temp[2].strip()
            productos.append(diccionario)

def actualizar_productos(productos):

    with open(direccion,"w") as archivo:
        for diccionario in productos:
            archivo.write(f"{diccionario['Producto']},{diccionario['Precio']},{diccionario['Cantidad']}\n")

        
menu=True



while menu==True:
    
    cargar_productos_lista(productos)

    print("A- Leer productos")
    print("B- Agregar Producto")
    print("C- Buscar producto")
    print("D- Salir")
    print("F- Mostrar Lista")
    opcion=input().upper()


    if opcion=="A":

        with open(direccion,"r") as archivo:

            for linea in archivo:
                temp=linea.split(",")
                print(f"Producto: {temp[0].strip()} | Precio: {temp[1].strip()} | Cantidad: {temp[2].strip()}")
                
        actualizar_productos(productos)

    elif opcion=="B":

        with open(direccion,"a") as archivo:  
            print("Agregar producto")
            producto=input("Ingrese el nombre del producto: ")     
            precio=input("Ingrese el precio del producto: ") 
            cantidad=input("Ingrese la cantidad: ")
            archivo.write(f"{producto},{precio},{cantidad}\n")
            print("Producto agregado!!")
        
        cargar_productos_lista(productos)
        actualizar_productos(productos)

    elif opcion=="C":
        nombre=input("Ingrese el nombre del producto: ")
        encontrado=None
        for diccionario in productos:
            if diccionario["Producto"]==nombre:
                encontrado=True
                print(diccionario)
        if encontrado==None:
            print("Producto no encontrado!!")
        
        actualizar_productos(productos)

    elif opcion=="D":
        menu=False
    
    elif opcion=="F":
        print(productos)

    else:
        print("Error de Menu!!")





    