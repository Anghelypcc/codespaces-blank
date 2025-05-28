import random
numero_secreto = random.randint(1, 100)
noAdivinado = True
def rangoCorrecto(num):
    minimo=1
    maximo=100
    return minimo<num or num>maximo
 
while noAdivinado:

  numeroIngresado = int(input("Adivina el numero (entre 1 y 100):"))
  if rangoCorrecto(numeroIngresado):
   print("Por favor, ingresa un numero entre 1 y 100.")
   continue
  if numeroIngresado > numero_secreto:
    print("el numero que ingresaste es mayor al que tienes que adivinar")
   
  if numeroIngresado < numero_secreto :
    print("el numero que ingresaste es menor al que tienes que adivinar")
    
  if numeroIngresado == numero_secreto:
   print("adivinaste el numero")
  