repetir = "s"
numero = int(input("digite o numero:" ))

while repetir =="S":
 if numero <0:
   if numero%2 ==0:
      print (f" numero e par e positivo ")
else:
       print (f" numero e impar e negativo")
if numero%2 ==0:
    print (f" numero par e positivo. ")
else:
    print (f" numero e impar e positivo. ")

repetir = input("deseja verificar novo numero?")


