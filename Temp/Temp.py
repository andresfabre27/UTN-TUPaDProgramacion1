#Practica integradora 2

alumnos={60902 : "Rodolfo Fernandez",
         61654 : "Luis Gomez",
         61852 : "Andrea Pereira",
         61754 : "Juan Cruz Gonzales"
        }

materias=[["Ciencias",None,None,None],
          ["Historia",None,None,None],
          ["Geografia",None,None,None],
          ["Matematicas",None,None,None],
          ["Fisica",None,None,None]
          ]

notasFinales=[]

def cargar_notas_Main(alumnos,materias,notasFinales):

    print("Carga de Notas para los alumnos") 
    for diccionario in alumnos.values():
        print(f"Alumno: {diccionario}")
        contador=0
        for linea in materias:
            print(f"Materia: {linea[0]}")
            nota1=float(input("Ingrese la primer nota: "))
            materias[contador][1]=nota1
            nota2=float(input("Ingrese la segunda nota: "))
            materias[contador][2]=nota2
            promedio=(nota1+nota2)/2
            materias[contador][3]=promedio
            contador+=1
        mostrar_materias(materias)
        print(f"La materia con mejor nota es: {materia_mejor_calificacion(materias)}")
        print(f"El promedio general del alumno es: {promedio_general(materias,diccionario,notasFinales)}")
    print(f"El alumno con mejor promedio es: {mejor_promedio(notasFinales)}")

def mostrar_materias(materias):

    for linea in materias:
        print(f"Materia: {linea[0]} Nota 1: {linea[1]} Nota 2: {linea[2]}")

def materia_mejor_calificacion(materias):

    mejor=0
    mejorMateria=[]

    for linea in materias:
        if linea[3]>=mejor:
            mejor=linea[3]

    for linea in materias:
            if linea[3]==mejor:
                mejorMateria.append(linea[0])

    return mejorMateria 

def promedio_general(materias,diccionario,notasFinales):
    
    promedio=0
    for linea in materias:
        promedio+=linea[3]

    promedio/=5
    lista=[diccionario,promedio]
    notasFinales.append(lista)

    return promedio

def mejor_promedio(notasFinales):
    
    notaMayor=0
    mejorAlumno=[]
    for linea in notasFinales:
        if linea[1]>notaMayor:
            notaMayor=linea[1]

    for linea in notasFinales:
        if linea[1]==notaMayor:
            mejorAlumno.append(linea[0])
    return mejorAlumno
        
        

cargar_notas_Main(alumnos,materias,notasFinales)



        



