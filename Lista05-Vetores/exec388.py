a = [0] * 10

for L in range(10):
    a[L] = 0

for L in range(10):
    print("Elemento do vetor A[", L, "]: ", end="")
    n = int(input())
    c = 0
    while n >= a[c] and c < L:
        c += 1
    if L > 0:
        for d in range(L, c, -1):
            a[d] = a[d - 1]
    a[c] = n

print("\n\nVetor Ordenado\n")
for L in range(10):
    print("a[", L + 1, "]-", a[L])

print("\n")
