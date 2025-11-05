import os
from datetime import date
from DetalleOrdenCompra import DetalleOrdenCompra
from Producto import Producto 
from OrdenCompra import OrdenCompra 

class GenerarOrdenComprasMain:

    def ver_orden_compra(self):

        with open(direccion,"r") as archivo:
            
            for fila in archivo:
                temp=fila.split(";")
                #print(f" {fechaHoy = date.today()}{temp[0]} {temp[4]} ")




    def leer_archivo(self):

        with open(direccion,"r") as archivo:
           
            print(archivo.read())



    def main(self):

        

        while True:

            self.leer_archivo()
            menu=input("""a- Ver Orden de Compras Cargadas
b- Cargar 1 o más Órdenes de Compra
c- Generar Archivo Orden de Compra por numero
d- Salir""")
            
            if menu=='a':
                pass

            if menu=='b':
                pass

            if menu=='c':
                pass

            if menu=='d':
                break


direccion=os.path.join(os.path.dirname(__file__), 'productos_compra.txt')
instanciaMain=GenerarOrdenComprasMain()
instanciaMain.main()   
                                                    