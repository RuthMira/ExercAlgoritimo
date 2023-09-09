na = int(input('\nHoras trabalhadas: '))
vha = float(input('\nValor da hora-aula: '))
pd = float(input('\nPercentual de desconto: '))
sb = na * vha
td = (pd / 100) * sb
sl = sb - td
print(f'\nSalário líquido: {sl}')
print('\n')