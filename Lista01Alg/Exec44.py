import math as m

num = int(input('\nEntre com o logaritmando: '))
base = int(input('\nEntre com a base: '))
logaritmo = m.log(num) / m.log(base)
print(f'\nO Logaritmo de {num} na base {base} é {logaritmo:}')
print('\n')