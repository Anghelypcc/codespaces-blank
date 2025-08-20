class Padre:
    apellido=''
    def __init__(self, nombre):
        self.nombre=nombre
        

class Hijo(Padre):
    def __init__(self, nombre, lenguajeDeProgramacion):
         super().__init__(nombre)
         self.lenguajeDeProgramacion=lenguajeDeProgramacion

padre = Padre('nombre del padre')
padre.apellido='apellido del padre'
hijo = Hijo('nombre del hijo','python')
print(hijo.nombre,hijo.apellido)
