# Lista com os nomes dos meses
nomes_meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita ao usuário para fornecer o número do mês
numero_mes = int(input("Digite o número do mês (1 a 12): "))

# Verifica se o número do mês é válido
if 1 <= numero_mes <= 12:
    # Obtém o nome do mês correspondente ao índice da lista
    nome_mes = nomes_meses[numero_mes - 1]
    print("O mês correspondente ao número é:", nome_mes)
else:
    print("Número de mês inválido. Por favor, digite um número de 1 a 12.")
