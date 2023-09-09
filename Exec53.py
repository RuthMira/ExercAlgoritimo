import math as m

a = int(input('\nEntre com a base: '))
b = int(input('\nEntre com a altura: '))
c = int(input('\nEntre com a profundidade: '))
diagonal = m.sqrt(a**2 + b**2 + c**2)
print(f'\nDiagonal: {diagonal:.2f} ')
print('\n')