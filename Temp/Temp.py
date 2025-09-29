#Ejercicio Nro 7

parcial1={"Andres","Cristian","Luciano","Federico","Yanina","Elio","Rosa","Anibal"}
parcial2={"Andres","Luciano","Rosa","Teresa","Silvana"}



ambos_parciales=parcial1&parcial2
solo_uno_de_los_dos=parcial1^parcial2
al_menos_un_parcial=parcial1|parcial2

print(f"Aprobaron ambos parciales: {ambos_parciales}")
print(f"Aprobaron solo uno de los dos parciales: {solo_uno_de_los_dos}")
print(f"Aprobo al menos uno: {al_menos_un_parcial}")