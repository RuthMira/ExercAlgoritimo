import math

x = float(input("\nDigite o valor de x: "))

if (x > 4.0 or x < -4.0):
    fx = (5 * x + 3) / math.sqrt(x**2 - 16)
    print("\nf(x) =", fx)
else:
    print("\nNAO PODE SER FEITA")

print("\n")
