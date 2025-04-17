repetir= "s"
while repetir=="s":
    peso = float(input(" digite o peso. "))
    altura = float(input("digite a altura. "))
    imc = peso / (altura * altura)
    if imc < 18.5:
      print ("abaixo do peso")
    elif  imc >18.6 and imc <=24.9:
        print ("peso ideal. ")
    elif imc > 25.0 and imc <=29.0:
        print (" levemente acima do peso.")
    elif imc >30.0 and imc <34.9:
        print ("obesidade grau 1.")
    elif imc >35.0 and imc <39.9:
        print ("obesidade grau 2")
    elif imc >40.0:
        print ("obesidade grau 3.")
    repetir = input("deseja verificar novo numero?")