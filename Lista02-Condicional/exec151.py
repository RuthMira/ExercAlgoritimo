peso = float(input("\nDigite o peso: "))
altura = float(input("\nDigite a altura: "))
imc = peso / (altura ** 2)

if (imc < 20.0):
    print("\nAbaixo do peso")
elif (imc <= 25.0):
    print("\nNormal")
elif (imc <= 30.0):
    print("\nExcesso de peso")
elif (imc <= 35.0):
    print("\nObesidade")
else:
    print("\nObesidade mórbida")

print("\n")
