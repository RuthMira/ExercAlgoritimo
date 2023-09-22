conta = int(input('\nDigite a conta de três dígitos: '))
d1 = int(conta / 100)
d2 = int(conta % 100 / 10)
d3 = int(conta % 100 % 10)
inv = int(d3 * 100 + d2 * 10 + d1)
soma = int(conta + inv)
d1 = int(soma / 100) * 1
d2 = int(soma % 100 / 10) * 2
d3 = int(soma % 100 % 10) * 3
digito = int(d1 + d2 + d3) % 10
print(f'\nDigito verificador: {digito}')
print('\n')