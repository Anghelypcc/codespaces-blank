class Clase:

def __init__(self, atributo):
            self.atributo = atributo

def imprimir(self):
            print("imprimiendo: " + self.atributo)

def metodo(self):
            return "el atributo es" + self.atributo

instancia = Clase("valor")
print (instancia.metodo() )
instancia.imprimir()