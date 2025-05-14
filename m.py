
print ("ingrese un numero")
numero1=int (input("ingrese un numero"))
#print "ingrese otro numero"
numero2=int (input("ingrese otro numero"))
suma=(numero1 + numero2)
print("la suma de estos numeros da", suma)
menor = numero1 < numero2
mayor = numero1 > numero2
igual = numero1 == numero2
# igual ==
# print("tales mayor que tal", suma)
if numero1 > numero2:
     print("numero1 > numero2")

if numero1 < numero2:
     print("numero1 < numero2")
     
if numero1 == numero2:
     print("numero1 == numero2")


lista = [0,1,2,3,4,5,6,7]    
for elemento in lista [:]: 
     lista[elemento]=elemento*2
     print(lista[elemento], end=",") 
    
print("")                      

for x in range(1,7,2):
    print(lista[x])
    