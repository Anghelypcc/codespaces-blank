
class Madre:
    apellido = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}")

class Hija(Madre):
    def __init__(self, nombre, lenguajeDeProgramacion):
        super().__init__(nombre)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido} - Lenguaje: {self.lenguajeDeProgramacion}")

madre = Madre("María")
madre.apellido = "Gómez"

hija = Hija("Lucía", "Python")
hija.apellido = madre.apellido  

madre.mostrar_info()
hija.mostrar_info()