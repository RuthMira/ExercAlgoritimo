import math as m

xnum1 = float(input('\nEntrar com 1° valor: '))
xnum2 = float(input('\nEntrar com 2° valor: '))
xnum3 = float(input('\nEntrar com 3° valor: '))
x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 - xnum2) + m.log(64.) / m.log(2.)
print(f'\nX: {x:.2f}')
print('\n')