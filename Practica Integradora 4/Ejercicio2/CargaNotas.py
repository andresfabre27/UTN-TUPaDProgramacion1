from Nota import Nota 
from Alumno import Alumno


class CargaNotas:
    def __init__(self):
        self.alumnos = []
    
    def cargar_alumnos(self, datos):
        
        self.alumnos.append(datos)

    def Main(self):


        while True:
            
            print("Ingrese datos del alumno")
            while True:
                nombreCompleto=input("Ingrese el Nombre del alumno: ")
                if not nombreCompleto:
                    print("Error, valor vacio")
                else:
                    break
            while True:    
                legajo=input("Ingrese el legajo: ")
                if not legajo:
                    print("Error, valor  vacio")     
                else:
                    legajo=int(legajo)
                    break
            instaciaAlumno=Alumno(nombreCompleto,legajo)
            self.cargar_alumnos(instaciaAlumno)

            while True:

                print("Ahora ingrese las notas del alumno")
                while True:
                    catedra=input("Ingrese el nombre de la catedra: ")
                    if not catedra:
                        print("Error, valor vacio")
                    else:
                        break
                while True:
                    notaExamen=input("Ingrese la nota del examen: ")
                    if not notaExamen:
                        print("Error, valor vacio")
                    else:
                        notaExamen=float(notaExamen)
                        break
                instanciaNota=Nota(catedra,notaExamen)
                instaciaAlumno.agregar_elemento(instanciaNota)
                salirNota=input("¿Desea cargar otra nota? SI/NO ")
                
                if salirNota=="NO":
                    break
                elif salirNota=="SI":
                    pass
                else:
                    print("Error de menu")
                    break
                
                

            salirAlumno=input("¿Desea cargar otro alumno? SI/NO ")
            if salirAlumno=="NO":
                break
            elif salirAlumno=="SI":
                pass
            else:
                print("Error de menu")
                break


        for p in self.alumnos:
            print(f"Nombre: {p.nombreCompleto} legajo: {p.legajo}")

            for o in p.notas:
                print(f"Catedra: {o.catedra} Nota: {o.notaExamen}")
            print(f"El promedio es: {p.promedio()}")


instanciaMain=CargaNotas()
instanciaMain.Main()
          
 
