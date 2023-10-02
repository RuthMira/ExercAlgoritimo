# Solicita informações sobre os três países
pontuacoes = []

# País 1
nome1 = input("Digite o nome do primeiro país: ")
ouro1 = int(input("Digite a quantidade de medalhas de ouro: "))
prata1 = int(input("Digite a quantidade de medalhas de prata: "))
bronze1 = int(input("Digite a quantidade de medalhas de bronze: "))
pontuacao1 = (ouro1 * 3) + (prata1 * 2) + bronze1
pontuacoes.append((nome1, pontuacao1))

# País 2
nome2 = input("Digite o nome do segundo país: ")
ouro2 = int(input("Digite a quantidade de medalhas de ouro: "))
prata2 = int(input("Digite a quantidade de medalhas de prata: "))
bronze2 = int(input("Digite a quantidade de medalhas de bronze: "))
pontuacao2 = (ouro2 * 3) + (prata2 * 2) + bronze2
pontuacoes.append((nome2, pontuacao2))

# País 3
nome3 = input("Digite o nome do terceiro país: ")
ouro3 = int(input("Digite a quantidade de medalhas de ouro: "))
prata3 = int(input("Digite a quantidade de medalhas de prata: "))
bronze3 = int(input("Digite a quantidade de medalhas de bronze: "))
pontuacao3 = (ouro3 * 3) + (prata3 * 2) + bronze3
pontuacoes.append((nome3, pontuacao3))

# Determina a classificação olímpica usando instruções if
classificacao = []
for nome, pontuacao in pontuacoes:
    if pontuacao >= 10:
        classificacao.append((nome, "Ouro"))
    elif pontuacao >= 7:
        classificacao.append((nome, "Prata"))
    elif pontuacao >= 4:
        classificacao.append((nome, "Bronze"))
    else:
        classificacao.append((nome, "Sem medalhas"))

# Exibe a classificação olímpica
print("Classificação Olímpica:")
for nome, medalha in classificacao:
    print(f"{nome}: {medalha}")
