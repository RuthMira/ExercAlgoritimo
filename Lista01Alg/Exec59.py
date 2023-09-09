import math as m

b = float(input('\nEntrar com 1° cateto: '))
c = float(input('\nEntrar com 2° cateto: '))
a = m.sqrt(b**2 + c**2)
print(f'\nA hipotenusa é {a:.2f}')
print('\n')