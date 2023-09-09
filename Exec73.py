num = float(input('\nEntre com um número com parte fracionária: '))
numi = float(int(num - 0.5))
numfrac = num - numi
numa = float(int(num + 0.00001))
print(f'\nParte inteira: {numi}')
print(f'\nParte fracionária: {(numfrac + 0.00001):.3f}')
print(f'\nParte arredondado: {numa}')
print('\n')