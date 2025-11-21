class Pais:
    def __init__(self, nombre, poblacion, superficie, continente): #Constructor
        self.nombre = str(nombre)
        self.continente = str(continente)
        try: #Validamos numeros
            self.poblacion = int(poblacion)
        except ValueError: #Si no es un numero lo remplaza con 0
            self.poblacion = 0
            
        try:
            self.superficie = int(superficie)
        except ValueError:#Si no es un numero lo remplaza con 0
            self.superficie = 0
            
    
    def mostrarPaises(self): #muestra los datos del pais
        return print(f"{self.nombre} ({self.continente}) - Pob: {self.poblacion:,} - Sup: {self.superficie:,} km²")