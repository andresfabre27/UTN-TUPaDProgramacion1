from Ingrediente import Ingrediente
from Plato import Plato

class MenuRestaurant:

    def __init__(self):

        self.platos=[]

    def agregar_platos(self,dato):

        self.platos.append(dato)

    def Main(self):

        while True:

            nombrecompleto=input("Ingrese el nombre del plato: ")
            precio=float(input("Ingrese el precio: "))
            while True:
                bebida=input("¿Es bebida? SI/NO ")
                if bebida=="SI":
                    esbebida=True
                    break
                elif bebida=="NO":
                    esbebida=False
                    break
                else:
                    print("Error, solo es posible SI y NO")
                    

            
            instanciaplato=Plato(nombrecompleto,precio,esbebida)
            self.agregar_platos(instanciaplato)

            if esbebida==False:
                while True:

                    nombre=input("Ingrese el nombre del Ingrediente: ")
                    cantidad=float(input("Ingrese la cantidad: "))
                    unidadmedida=input("Ingrese la unidad de medida: ")
                    intanciaingrediente=Ingrediente(nombre,cantidad,unidadmedida)
                    instanciaplato.agregar_ingredientes(intanciaingrediente)

                    opcion1=input("¿Desea cargar otro ingrediente? SI/NO ")
                    if opcion1=="SI":
                        pass
                    elif opcion1=="NO":
                        break
                    else:
                        print("Error, solo es posible SI/NO")
                        break
            
            opcion2=input("¿Desea cargar otro plato? SI/NO ")
            if opcion2=="SI":
                    pass
            elif opcion2=="NO":
                    break
            else:
                    print("Error, solo es posible SI/NO")
                    break

        print("-------MENU-------")   
        for o in self.platos:
              
             print(f"""{o.nombreCompleto}
precio: $ {o.precio}    """)
             if o.esBebida==False:
                  print("Ingredientes:")
                  print("Nombre  Cantidad  Unidad de Medida")
                  for p in o.lista_de_ingredientes:
                      print(f" {p.nombre}    {p.cantidad}       {p.unidadDeMedida} ")
             print("------------------")
             
    
instanciaMain=MenuRestaurant()
instanciaMain.Main()