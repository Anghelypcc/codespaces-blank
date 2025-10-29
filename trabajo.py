class Madre:
    apellido=''
    def __init__(self, nombre):
        self.nombre=nombre
        

class Hija(Madre):
    def __init__(self, nombre, lenguajeDeProgramacion):
         super().__init__(nombre)
         self.lenguajeDeProgramacion=lenguajeDeProgramacion

madre = Madre('nombre del madre')
madre.apellido='apellido del madre'
hija = Hija('nombre de la hija','python')
print(hija.nombre,hija.apellido)
