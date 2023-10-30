num = [0] * 15

# Entrada de 15 elementos
for L in range(15):
    print("11")
    num[L] = int(input(f"Digite {L + 1} numero: "))

# Saída
print("\nRELACAO DOS NUMEROS")
for L in range(15):
    print(f"\n{L + 1} - {num[L]}", end="")
    if num[L] % 2 == 0:
        print(" e' PAR", end="")
    else:
        print(" e' IMPAR", end="")
print("\n")
