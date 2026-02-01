#Programacion 1
#Practica Integradora 2
#Nombre: Daniel Andrés Fabre

alumnos={60902:"Rodolfo Fernandez",
         61654:"Luis Gomez",
         61852:"Andrea Pereira",
         61754:"Juan Cruz Gonzales" 
         }

materias=[["Ciencias",0,0,0],
          ["Historia",0,0,0],
          ["Geografia",0,0,0],
          ["Matematicas",0,0,0],
          ["Fisica",0,0,0]
          ]

notasFinales=[["Rodolfo Fernandez",0],
              ["Luis Gomez",0],
              ["Andrea Pereira",0],
              ["Juan Cruz Gonzales",0]
              ]

def iterar_alumnos(diccionario,materias,notasfinales):
    for alumno in diccionario.values():
        print(f"Para el alumno: {alumno}")
        contador=0
        for materia in materias:
            print(f"Para la materia {materias[contador][0]}")
            materias[contador][1]=validar_nota(int(input("Ingrese la primer nota: ")))
            materias[contador][2]=validar_nota(int(input("Ingrese la segunda nota: ")))
            materias[contador][3]=(materias[contador][1]+materias[contador][2])/2
            contador+=1
        impresora(materias)
        print(f"La materia con calificacion mas alta es: {calificacion_mas_alta(materias)}")
        print(f"El promedio general del alumno es: {promedio(alumno,materias,notasfinales)}")
        print("\n")
    nota,nombre =mejor_promedio(notasFinales)
    print("----------------------------------------------")
    print(f"El mejor promedio es de: {nombre} con {nota}")    
       
def validar_nota(nota):
    while nota<0 or nota >10:
        print("Error, la nota debe estar entre 0 y 10")
        nota=int(input("Ingrese la nota nuevamente: "))
    return nota

def impresora(materias):
    for materia,nota1,nota2,promedio in materias:
        print(f"Materia: {materia} nota 1= {nota1} nota 2= {nota2} promedio= {promedio}")


def calificacion_mas_alta(materias):
    mayor=""
    partida=0
    contador=0
    for materia in materias:
        if materias[contador][3]>=partida:
            partida=materias[contador][3]
            mayor=materias[contador][0]
        contador+=1
    return mayor

def promedio(alumno,materias,notasfinales):
    suma=0
    contador=0
    for materia in materias:
        suma+=materias[contador][3]
        contador+=1
    promedio=suma/5
    posicion=buscar_posicion(notasfinales,alumno)
    notasfinales[posicion][1]=promedio
    
    return promedio

def buscar_posicion(notas, nombre):
    for i in range(len(notas)):
        if notas[i][0] == nombre:
            return i
    return -1

def mejor_promedio(mejorpromedio):
    contador=0
    promedio=0
    nombre=""
    for i in mejorpromedio:
        if mejorpromedio[contador][1]>=promedio:
            promedio=mejorpromedio[contador][1]
            nombre=mejorpromedio[contador][0]
        contador+=1
    return promedio,nombre





iterar_alumnos(alumnos,materias,notasFinales)






#Practica integradora 2 Correciones y codigo completo (sin validaciones)

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



        
