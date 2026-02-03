import os

def leer_alumnos(direccion):

    with open(direccion, "r") as archivo: 
    
        for linea in archivo:        
            partes=linea.split(";")    
            print(f"Nombre: {partes[0].strip()} | Apellido: {partes[1].strip()} | Legajo: {partes[2].strip()} | promedio: {partes[3].strip()}")
            print("")

def generar_diccionario():
    with open(direccion, "r") as archivo:
        diccionario={}
        for linea in archivo:
            partes=linea.split(";")
            diccionario[partes[2]]=partes[0]+partes[1]
        
        return diccionario
    
def agregar_alumno(diccionario):

    while True:
        nombre=input("Ingrese el nombre: ")
        if nombre.isalpha():
            break        
        else:
            print("Debe Ingresar unicamente caracteres")
    while True:
        apellido=input("Ingrese el Apellido: ")
        if apellido.isalpha():
            break
        else:
            print("Debe Ingresar unicamente caracteres")
    while True:
        legajo=int(input("Ingrese el legajo: "))
        if len(str(legajo))==5:
            if str(legajo) in diccionario:
                print(f"El legajo {legajo} ya existe en el archivo, no se permite su escritura\n")
                return False
            else:
                break
        else: 
            print("El numero de legajo solo debe tener 5 numeros")
    while True:
        nota_promedio=int(input("Ingrese el promedio del alumno: "))
        if 1<=nota_promedio<=10:
            break
        else:
            print("La nota debe estar comprendida entre 1 y 10")
    
    with open(direccion, "a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota_promedio}\n")
        print("Hecho¡¡")

def guardar_aprobados():
    with open(direccion, "r") as archivo_lectura, open(direccion2, "w") as archivo_escritura:

        for linea in archivo_lectura:
            temporal=linea.split(";")
            if int(temporal[3])>=6:
                archivo_escritura.write(f"{temporal[0]} {temporal[1]}\n" )

    with open(direccion2, "r") as archivo_escritura:
        print("")
        print("------------------------")
        print("Alumnos aprobados")
        print("------------------------")
        for linea in archivo_escritura:
            print(linea)


direccion=os.path.join(os.path.dirname(__file__), 'alumnos.txt')
direccion2=os.path.join(os.path.dirname(__file__), 'aprobados.txt')
#direccion=r"c:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\Practica Integradora 3\alumnos.txt"
#direccion2=r"c:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\Practica Integradora 3\aprobados.txt"

menu=False
generar_diccionario()

while menu==False:
    print("    -----------------------------------")
    opcion=input("""    1-Ver alumnos  
    2-Agregar alumno 
    3-Generar y mostrar archivo de aprobados
    4-Salir
    -----------------------------------\n""")
    
    if opcion=='1':

        leer_alumnos(direccion)

    elif opcion=='2':
        
        agregar_alumno(generar_diccionario())


    elif opcion=='3':

        guardar_aprobados()

    elif opcion=='4':
        menu=True

    elif not opcion:
        print("El menu no puede ser un valor vacio")
        
    
    else:
        print("Error de menu, intente nuevamente")

#------------------------------------------------------
# Practica integradora 3 mejor version
#------------------------------------------------------

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