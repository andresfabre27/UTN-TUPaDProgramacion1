#Trabajo Practico POO
#Nombre: Andrés Fabre, Cristian Zuñiga

#Ejercicio Nro 1

class celda:

    def __init__(self, valor, fila, columna):
        
        self.valor=valor
        self.fila=fila
        self.columna=columna                
        

class matriz:

    def __init__(self):

        self.celdasMatriz = []
    
    def agregar_elemento(self,elemento):

        self.celdasMatriz.append(elemento)

def devolver_fila_columna(fila1,columna1,instancia):

    encontrado=False
    for celda in instancia:
        if celda.fila==fila1 and celda.columna==columna1:
            print(celda.valor)
            encontrado=True
    if encontrado==False:
        print("La fila y columna indicada no ha sido asignada en ninguna celda")    

    
instancia2=matriz()

while(True):
    
    temp=input("Ingrese el valor de la celda: ")
    if str(temp)=="FIN":
        break
    valor=float(temp)
    
    fila=int(input("Ingrese la fila de la celda: "))
    columna=int(input("Ingrese la columna de la celda: "))

    instancia1=celda(valor,fila,columna)
    
    instancia2.agregar_elemento(instancia1)

for p in instancia2.celdasMatriz:
    print(f"{p.valor} {p.fila} {p.columna}")

fila1=int(input("Ingrese la fila a buscar: "))
columna1=int(input("Ingrese la columna a buscar: "))

devolver_fila_columna(fila1,columna1,instancia2.celdasMatriz)