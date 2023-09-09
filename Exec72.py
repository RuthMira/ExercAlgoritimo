deposito = float(input('\nEntre com deposito: '))
taxa = float(input('\nEntre com a taxa de juros: '))
valor = deposito * taxa / 100
total = deposito + valor
print(f'\nRendimento: {valor} \nTotal: {total}')
print('\n')
