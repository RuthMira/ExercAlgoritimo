import math as m

base = float(input('\nDigite a base: '))
altura = float(input('\nDigite a altura: '))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)
print(f'\nPerimetro: {perimetro} ')
print(f'\nÁrea: {area} ')
print(f'\nDiagonal: {diagonal:.2f} ')
print('\n')