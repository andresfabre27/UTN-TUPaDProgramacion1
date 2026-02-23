#Repasando practica integradora 2

alumnos={60902 : "Rodolfo Fernandez",
         61654 : "Luis Gomez",
         61852 : "Andrea Pereira",
         61754 : "Juan Cruz Gonzales"
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

contador2=0
for clave,valor in alumnos.items():
    print(f"Alumno {valor}")
    print("Ahora cargaremos los datos de las materias")
    contador=0
    promedio_final=0
    
    for lista in materias:
        
        print(f"Materia: {lista[0]}")
        while True:
            nota1=int(input("Ingrese la nota nro 1: "))
            if 0<nota1<=10:
                break
            else:
                print("La nota debe estar entre 1 y 10")
        while True:
            nota2=int(input("Ingrese la nota nro 2: "))
            if 0<nota2<=10:
                break
            else:
                print("La nota debe estar entre 1 y 10")
        materias[contador][1]=nota1
        materias[contador][2]=nota2
        promedio=(nota1+nota2)/2
        materias[contador][3]=promedio
        promedio_final+=materias[contador][3]
        contador+=1
        
    print(materias)
    
    
    calificacion_masalta=0
    for lista in materias:
        if lista[3]>calificacion_masalta:
            calificacion_masalta=lista[3]

    mejores_materias=[]

    for lista in materias:
        if lista[3]==calificacion_masalta:
            mejores_materias.append(lista[0])

    for lista in materias:
        print(f"Materia: {lista[0]} Nota 1: {lista[1]} Nota 2: {lista[2]} Promedio: {lista[3]} ")
    
    print(f"La mejor materias es: {mejores_materias} con nota {calificacion_masalta}")
    promedio_final=promedio_final/5
    notasFinales[contador2][1]=promedio_final
    contador2+=1

mejor_nota_final=0
for lista in notasFinales:
    if lista[1]>mejor_nota_final:
        mejor_nota_final=lista[1]

mejor_alumno=[]

for lista in notasFinales:
    if lista[1]==mejor_nota_final:
        mejor_alumno.append(lista[0])

print(f"El/los mejores alumnos son: {mejor_alumno} con promedio: {mejor_nota_final}")
