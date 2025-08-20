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

class SumaNumeros:
    def __init__(self):
        self.numero1 = float(input("Por favor, ingrese el primer número: "))
        self.numero2 = float(input("Ahora ingrese el segundo número: "))

    def sumar(self):
        return self.numero1 + self.numero2

    def mostrar_suma(self):
        print ("La suma de ambos números da:", self.sumar())

instancia_suma = SumaNumeros()
instancia_suma.mostrar_suma()