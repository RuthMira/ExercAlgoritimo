import math

ang = float(input("\nDigite o ângulo em graus: "))
rang = ang * math.pi / 180

if (rang > math.pi / 2 and rang <= math.pi) or (rang > 3 * math.pi / 2 and rang <= 2 * math.pi):
    print("\nseno:", math.sin(rang))
else:
    print("\nco - seno:", math.cos(rang))

print("\n")
