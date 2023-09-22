saldomedio = float(input("\nDigite o saldo médio: "))

if (saldomedio < 501.0) :
    credito = 0.0
elif (saldomedio < 1001.0) :
    credito = saldomedio * 0.3
elif (saldomedio < 3001.0) :
    credito = saldomedio * 0.4
else:
    credito = saldomedio * 0.5

if credito != 0.0:
    print("\nComo seu saldo era de:", saldomedio, "seu crédito será de:", credito)
else:
    print("\nComo seu saldo era de:", saldomedio, "você não terá nenhum crédito")

print("\n")
