# Practica integradora 3 Repaso

import os

direccion=os.path.join(os.path.dirname(__file__), 'alumnos.txt')
direccion2=os.path.join(os.path.dirname(__file__), 'aprobados.txt')

diccionario={}

def crear_archivo_alumnos():

    try:
        with open(direccion, 'x') as f:
            print("Archivo alumnos creado!!")
    except FileExistsError:
        print("El archivo alumnos ya existe.")


def crear_diccionario(diccionario):
    
    with open(direccion,"r") as archivo:
        for linea in archivo:
            temp=linea.split(";")
            diccionario[int(temp[2])]=temp[0]+" "+temp[1]

def ver_alumnos():
    with open(direccion,"r") as archivo:
        print("Alumnos--------------")
        for linea in archivo:
            temp=linea.split(";")
            print(f"Nombre: {temp[0]} {temp[1]} legajo: {temp[2]} promedio: {temp[3].strip()}")

def agregar_alumnos(diccionario):
    
    while True:
        legajo=input("Ingrese el legajo del alumno: ")
        if len(legajo)==5:
            break
        else:
            print("El legajo debe tener 5 numeros!!")

    legajo=int(legajo)

    for key in diccionario.keys():
        if legajo==key:
            print(f"El legajo {legajo} ya existe en el archivo.txt")
            return

    while True:    
        nombre=input("Ingrese el nombre del alumno: ")
        if not nombre:
            print("Debe ingresar algun valor!!")
        elif not nombre.isalpha():
            print("El nombre no pueden ser numeros!!")
        else:
            break
    while True:    
        apellido=input("ingrese el apellido del alumno: ")
        if not apellido:
            print("Debe ingresar algun valor!!")
        elif not apellido.isalpha():
            print("El apellido no pueden ser numeros!!")
        else:
            break
    
    while True:
        promedio=int(input("Ingrese el promedio: "))
        if 0<promedio<=10:
            break
        else:
            print("El promedio debe ser mayor a cero y menor a 11!!")
    with open(direccion,"a") as archivo:
       
            archivo.write(f"{nombre};{apellido};{legajo};{promedio}\n")
            print("Alumno cargado!!")

def generar_aprobados():
    with open(direccion,"r") as archivo1, open(direccion2,"w") as archivo2:
        for linea in archivo1:
            temp=linea.split(";")
            if int(temp[3].strip())>=6:
                archivo2.write(f"{temp[0]};{temp[1]};{temp[2]};{temp[3].strip()}\n")
        print("Archivo generado!!")
    
    print("------------Alumnos Aprobados-------------")
    with open(direccion2,"r") as archivo:
        for linea in archivo:
            temp=linea.split(";")
            print(f"Nombre: {temp[0]} {temp[1]} legajo: {temp[2]} promedio: {temp[3].strip()}")


menu=False
crear_archivo_alumnos()
crear_diccionario(diccionario)
while menu==False:
    print("a- Ver alumnos")
    print("b- Agregar alumno")
    print("c- Generar y mostrar archivo de aprobados")
    print("d- Salir")
    opcion=input().lower()

    if opcion=="a":
        ver_alumnos()

    elif opcion=="b":
        agregar_alumnos(diccionario)
        crear_diccionario(diccionario)

    elif opcion=="c":
        generar_aprobados()

    elif opcion=="d":
        menu=True

    else:
        print("Error de menu!!")