vet1 = [0] * 10
vet2 = [0] * 20
vetc = [-999999999] * 10
L = 0

# Entrada de dados do vetor 1 (10 elementos)
print("\nEntrada de dados do vetor 1 (10 elementos)")
for i in range(10):
    vet1[i] = int(input(f"Entre com {i + 1} elemento: "))

# Entrada de dados do vetor 2 (20 elementos)
print("\nEntrada de dados do vetor 2 (20 elementos)")
for i in range(20):
    vet2[i] = int(input(f"Entre com {i + 1} elemento: "))

for i in range(10):
    c = 0
    while vet1[i] != vet2[c] and c < 19:
        c += 1
    if vet1[i] == vet2[c]:
        d = 0
        while vet1[i] != vetc[d] and d < L:
            d += 1
        if d == L:
            vetc[d] = vet1[i]
            L += 1

if L != 0:
    print("\n\nElementos comuns\n")
    for i in range(L):
        print(vetc[i])
else:
    print("\n\nNão existem elementos comuns")

print("\n")
