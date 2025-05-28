if True:
    print("hola")
numero=0
boleano = True 
while boleano:
   print("ingrese un numero")
   numero=int(input(":"))
   numeroDoble=numero*2
   print(numeroDoble, end=",")
   numero+=1
   boleano= numero == 32