def buscar_pais():
    pass

def filtrar_pais():
    pass

def ordenar_pais():
    pass

def mostrar_estadisticas():
    pass


def main():

    menu=False

    while menu!=True:

        opcion=input(f"""------------------
A- Buscar país
B- Filtrar país
C- Ordenar país
D- Mostrar estadisticas
E- Salir
----------------------- \n""")
        
        if opcion=="A":
            buscar_pais()

        elif opcion=="B":
            filtrar_pais()

        elif opcion=="C":
            ordenar_pais()

        elif opcion=="D":
            mostrar_estadisticas()
        
        elif opcion=="E":
            menu=True
        
        else:
            print("Error de Menu")


main()