#Ejercicio Nro 5

def segundos_a_horas(segundos):

    return segundos/60/60

segundos=int(input("Ingrese los segundos: "))
print(f"Son {segundos_a_horas(segundos)} horas ")

