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

golosinasPedidas=[[]]

apagar= False

while apagar != True: 

    menu=input("A-Pedir Golosinas  B-Mostrar Golosinas  C-Rellenar Golosinas  D-Apagar Maquina \n ")
    
    if menu=="A":
        verificar_legajo=int(input("Ingrese su numero de legajo: "))
        if verificar_legajo in empleados:       #Verificamos si es un empleado
            verificar_golosina=int(input("Ingrese el codigo de la golosina: "))
            if any(verificar_golosina in sublista for sublista in golosinas): #Verificamos si esta la golosina ingresada en la lista
                if golosinas[verificar_golosina-1][2]>0: #Verificamos si queda la golosina X
                    golosinas[verificar_golosina-1][2]-=1
                    if any(golosinas[verificar_golosina-1][1] in sublista for sublista in golosinasPedidas): #Verificamos si golosina esta en golosinasPedidas
                         golosinasPedidas[golosinas[verificar_golosina-1].index][1]+=1
                    else:
                         golosinasPedidas.extend(golosinas[verificar_golosina-1],golosinas[verificar_golosina-1][1])
                         golosinasPedidas[golosinas[verificar_golosina-1].index][2]+=1

                else :
                                 print(f"Lo sentimos la golosina {golosinas[verificar_golosina-1][1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
            else:
                print("No se encuentra la golosina")  
        else:
            print("No se encuentra la golosina")        

    elif menu=="B":

        print(golosinas)
     
    elif menu=="C":
     
        pass

    elif menu=="D":
     
        apagar=True
        print(golosinasPedidas)

    else:

        print("Opcion Incorrecta")



    