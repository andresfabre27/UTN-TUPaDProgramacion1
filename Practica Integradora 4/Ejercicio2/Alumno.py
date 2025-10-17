class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto=nombreCompleto
        self.legajo=legajo
        self.notas=[]

    def agregar_elemento(self,elemento):

        self.notas.append(elemento)