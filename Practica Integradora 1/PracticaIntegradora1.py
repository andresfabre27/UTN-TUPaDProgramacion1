golosinas=[[1,"KitKat",20],
           [2,"Chicles",50],
           [3,"Caramelos de Menta",50],
           [4,"Huevos Kinder",10],
           [5,"Chetoos",10],
           [6,"Twix",10],
           [7,"MYM'S",10],
           [8,"Papas Lays",2],
           [9,"Milkybar",10],
           [10,"Alfajor Tofi",15],
           [11,"Lata Coca",20],
           [12,"Chitos",10]]

empleados={
        1100: "José Alonso",
        1200: "Federico Pacheco",
        1300: "Nelson Pereira",
        1400: "Osvaldo Tejada",
        1500: "Gastón Garcia"

}

clavesTecnico=("admin","CCCDDD",2020)

golosinasPedidas=[]

apagar= False

while apagar != True: 

    menu=input("A-Pedir Golosinas  B-Mostrar Golosinas  C-Rellenar Golosinas  D-Apagar Maquina \n ")
    
    if menu=="A":
        verificar_legajo=int(input("Ingrese su numero de legajo: ")) 
        if verificar_legajo in empleados:       #Verificamos si es un empleado
            verificar_golosina=int(input("Ingrese el codigo de la golosina: "))
            if any(verificar_golosina in sublista for sublista in golosinas): #Verificamos si el codigo de la golosina esta en la lista
                if golosinas[verificar_golosina-1][2]>0: #Verificamos si queda la golosina X
                    golosinas[verificar_golosina-1][2]-=1
                    if any(golosinas[verificar_golosina-1][1] in sublista for sublista in golosinasPedidas): #Verificamos si golosina esta en golosinasPedidas
                         nombre_busqueda=golosinas[verificar_golosina-1][0]
                         for i in range(len(golosinasPedidas)):        #Buscamos el indice de la fila
                             if nombre_busqueda==golosinasPedidas[i][0]:
                                 indice_busqueda=i
                                                         
                         golosinasPedidas[indice_busqueda][2]+=1 #Aumentamos +1 la cantidad de la golosina
                    else:
                         sublista=[]
                         sublista.append(golosinas[verificar_golosina-1][0])
                         sublista.append(golosinas[verificar_golosina-1][1])
                         sublista.append(1)
                         golosinasPedidas.append(sublista)

                else :
                    print(f"Lo sentimos la golosina {golosinas[verificar_golosina-1][1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
            else:
                print("No se encuentra la golosina")  
        else:
            print("No se encuentra el legajo")        

    elif menu=="B":

        for codigo, nombre, stock in golosinas:
         print(f"Código: {codigo} | {nombre} | Stock: {stock}")
     
    elif menu=="C":
     
        print("Ingrese la contraseña en 3 pasos")
        contraseña1=input("Ingrese la primer contraseña: ")
        if contraseña1==clavesTecnico[0]:
            contraseña2=input("Ingrese la segunda contraseña: ")
            if(contraseña2==clavesTecnico[1]):
                contraseña3=int(input("Ingrese la tercer contraseña: "))
                if contraseña3==clavesTecnico[2]:
                    verificar_golosina=int(input("Ingrese el codigo de la golosina: "))
                    if any(verificar_golosina in sublista for sublista in golosinas): #Verificamos si el codigo de la golosina esta en la lista
                        cantidad_a_recargar=int(input("ingrese cuanto quiere recargar: "))
                        if cantidad_a_recargar>0:

                             golosinas[verificar_golosina-1][2]+=cantidad_a_recargar #cargamos las golosinas

                        else:
                            print("La cantidad debe ser mayor que cero")


                    else:
                        print("No se encuentra la golosina")    

                else:
                    print("No tiene permiso para ejecutar la función de recarga")    
            
            else:
                print("No tiene permiso para ejecutar la función de recarga")

        else:  
            print("No tiene permiso para ejecutar la función de recarga")  


    elif menu=="D":
     
        apagar=True
        for codigo, nombre, cantidad_pedida in golosinasPedidas:
            print(f"Código: {codigo} | {nombre} | Cantidad Pedida: {cantidad_pedida}")

    else:

        print("Opcion Incorrecta")

#---------------------------------------------------------------------------
# Practica integradora 1 Mejor ejercicio
#---------------------------------------------------------------------------


golosinas=[[1, "KitKat", 20],
           [2, "Chicles", 50],
           [3, "Caramelos de Menta", 50],
           [4, "Huevo Kinder", 10],
           [5, "Chetoos", 10],
           [6, "Twix" ,10],
           [7, "M&M'S", 10],
           [8, "Papas Lays", 2],
           [9, "Milkybar", 10],
           [10, "Alfajor Tofi", 15],
           [11, "Lata Coca", 20],
           [12, "Chitos", 10]
           ]

empleados={1100 : "José Alonso",
           1200 : "Federico Pacheco",
           1300 : "Nelson Pereira",
           1400 : "Osvaldo Tejada",
           1500 : "Gastón Garcia"
           }

clavesTecnico=("admin", "CCCDDD", 2020)

golosinasPedidas=[["Código golosina", "Denominación Golosina", "Cantidad total pedida"]]

def pedir_golosinas(empleados,golosinas,golosinasPedidas):

    legajo=int(input("Ingrese el legajo: "))
    encontrado=False
    
    #if legajo in empleados:  Otra forma de encontralo pero menos precisa
       # print("Empleado encontrado!!")
       # encontrado=True

    for key in empleados.keys():
        if legajo==key:
            print("Empleado encontrado!!")
            encontrado=True
    
    if encontrado==False:
        print("Empleado no encontrado!!")
        return
    else:
        while True:
            codigo=input("Ingrese el codigo de la golosina: ")
            if codigo=="Salir":
                break
                       
            contador=0 
            encontrado=False
            for linea in golosinas:
                if linea[0]==int(codigo):
                    print("Golosina encontrada!!")
                    encontrado=True
                    if golosinas[contador][2]>0: 
                        golosinas[contador][2]-=1
                        print("Golosina adquirida!!")

                        encontrado=False
                        contador=0
                        for linea in golosinasPedidas:

                            if golosinas[contador][1] in linea:
                                encontrado=True
                                golosinasPedidas[contador][2]+=1

                            contador+=1

                        if encontrado==False:
                            temp=[golosinas[contador][0],golosinas[contador][1],1]
                            golosinasPedidas.append(temp)


                        return

                    else:
                        print(f"Lo sentimos, la golosina {golosinas[contador][1]} no se encuentra disponible, intente nuevamente o escriba Salir")

                contador+=1

            if encontrado==False:
                print("Golosina no encontrada, intente nuevamente!!")
                  
def mostrar_golosina(golosinas):
    for linea in golosinas:
        print(f"Golosina: {linea[1]} | Cantidad: {linea[2]}")     


def rellenar_golosina(clavesTecnico,golosinas): 
    clave1=input("Ingrese la primer contraseña: ") 
    if clave1==clavesTecnico[0]:
        clave2=input("Ingrese la segunda contraseña: ")
        if clave2==clavesTecnico[1]:
            clave3=int(input("Ingrese la tercer contraseña: "))
            if clave3==clavesTecnico[2]:
                print("Acceso consedido")
                
                while True:
                    codigo=input("Ingrese el codigo de la golosina: ")
                    contador=0 
                    encontrado=False
                    for linea in golosinas:
                        if linea[0]==int(codigo):
                            print("Golosina encontrada!!")
                            encontrado=True
                            cantidad=int(input("Ingrese la cantidad: "))
                            golosinas[contador][2]+=cantidad
                            print("Golosinas agregadas!!")
                            return
                        
                        contador+=1

                    if encontrado==False:
                        print("Golosina no encontrada, intente nuevamente!!")


            else:
                print("Contraseña Incorrecta!!")

        else:
            print("Contraseña Incorrecta!!")

    else:
        print("Contraseña Incorrecta!!")      





menu=False

while menu==False:

    print("a- Pedir Golosina")
    print("b- Mostrar Golosinas")
    print("c- Rellenar golosina")
    print("d- Apagar maquina")
    opcion=input().lower()

    if opcion=="a":
        pedir_golosinas(empleados,golosinas,golosinasPedidas)

    elif opcion=="b":
        mostrar_golosina(golosinas)

    elif opcion=="c":
        rellenar_golosina(clavesTecnico,golosinas)

    elif opcion=="d":
        menu=True
        for linea in golosinasPedidas:
            print(linea)


    else:
        print("Error de menu, intente nuvamente")   