# Practica integradora 1 

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