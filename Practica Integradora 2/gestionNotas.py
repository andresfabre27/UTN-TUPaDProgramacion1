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
