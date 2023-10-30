num = [''] * 20
valor = [''] * 20
destino = [''] * 20
data = [''] * 20

print("\nNúmero de cheques do talonário: ")
nc = int(input())

for k in range(nc):
    print("\nNúmero do cheque: ")
    num[k] = input()
    print("\nValor do cheque: ")
    valor[k] = input()
    print("\nData do cheque (ddmmaa): ")
    data[k] = input()
    print("\nDestino do cheque: ")
    destino[k] = input()

print("\nRELACAO dos CHEQUES\n")

for k in range(nc):
    print("\nNúmero do cheque: ", num[k])
    print("Valor do cheque: ", valor[k])
    print("Data do cheque: ", data[k])
    print("Destino do cheque: ", destino[k])
    resp = input("\nPressione enter para ver outro cheque: ")

print("\n")
