from Barrio import Barrio
from Vivienda import Vivienda
from Habitacion import Habitacion

class MainBarrio:
    @staticmethod
    def main():
        barrio_nombre = input("Ingrese el nombre del barrio: ")
        empresa = input("Ingrese el nombre de la empresa constructora: ")
        barrio = Barrio(barrio_nombre, empresa)

        while True:
            print("\n--- Nueva Vivienda ---")
            calle = input("Calle: ")
            numero = int(input("Número: "))
            manzana = input("Manzana: ")
            nroCasa = int(input("Número de casa: "))
            superficieTerreno = float(input("Superficie del terreno (m²): "))

            vivienda = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno)

            while True:
                print("\n--- Nueva Habitación ---")
                nombre_hab = input("Nombre de la habitación (o 'FIN' para terminar): ")
                if nombre_hab.upper() == "FIN":
                    break
                metros = float(input("Metros cuadrados: "))
                habitacion = Habitacion(nombre_hab, metros)
                vivienda.agregar_habitacion(habitacion)

            barrio.agregar_vivienda(vivienda)

            continuar = input("\n¿Desea agregar otra vivienda? (SI/NO): ")
            if continuar.upper() != "SI":
                break

        # Mostrar resultados
        print("\n----------- INFORME DEL BARRIO -----------")
        print(f"Barrio: {barrio.nombre}")
        print(f"Empresa Constructora: {barrio.empresaConstructora}")
        print("------------------------------------------")

        for v in barrio.viviendas:
            print(f"\nVivienda en {v.calle} {v.numero} (Manzana {v.manzana}, Casa {v.nroCasa})")
            print(f"Superficie del terreno: {v.superficieTerreno} m²")
            print("Habitaciones:")
            for h in v.habitaciones:
                print(f"  - {h.nombre}: {h.metrosCuadrados} m²")
            try:
                print(f"Superficie cubierta total: {v.getMetrosCuadradosCubiertos()} m²")
            except Exception as e:
                print(f"Error: {e}")

        print("\n==========================================")
        print(f"Superficie total de terrenos: {barrio.getSuperficieTotalTerreno()} m²")
        print(f"Superficie total cubierta: {barrio.getSuperficieTotalCubierta()} m²")

        manzana_consulta = input("\nIngrese una manzana para calcular su superficie total: ")
        print(f"Superficie total de la manzana {manzana_consulta}: {barrio.getSuperficieTotalTerrenoXManzana(manzana_consulta)} m²")
        print("==========================================")

if __name__ == "__main__":
    MainBarrio.main()
