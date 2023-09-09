import math as m

angulo = int(input('\nDigite um ângulo em graus: '))
rang = (angulo* 3.14) / 180
print(f'\nSeno: {m.sin(rang)}')
print(f'\nCo-seno: {m.cos(rang)}')
print(f'\nTangente: {m.tan(rang)}')
print(f'\nCo-secante: {1 / m.sin(rang)}')
print(f'\nSecante: {1 / m.cos(rang)}')
print(f'\nCotangente: {1 / m.tan(rang)}')
print('\n')