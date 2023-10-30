nomes = [''] * 20
sal = [0.0] * 20

# Entrada de 20 nomes
for L in range(20):
    print(f"\nDigite {L + 1} nome: ", end="")
    nomes[L] = input()
    while len(nomes[L]) > 30:
        print("\nNomes com até 30 caracteres")
        print(f"\nDigite {L + 1} nome: ", end="")
        nomes[L] = input()
    t = 30 - len(nomes[L])
    for c in range(t):
        nomes[L] += ' '

    print("\nDigite salário: ", end="")
    sal[L] = float(input())
    sal[L] *= 1.08

# Saída dos nomes
print("\nNOMES\t\t\t\t\t\n")
for L in range(20):
    print(f"\n{L + 1}\t\t{nomes[L]}\t{sal[L]}")
print("\n")
