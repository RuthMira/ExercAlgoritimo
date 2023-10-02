# Solicita ao usuário para fornecer a idade
idade = int(input("Digite a sua idade: "))

# Determina a classe eleitoral
if idade < 16:
    classe_eleitoral = "Não vota (menor de 16 anos)"
elif idade >= 18 and idade <= 65:
    classe_eleitoral = "Voto obrigatório (18 a 65 anos)"
elif (idade >= 16 and idade < 18) or idade >= 65:
    classe_eleitoral = "Voto opcional (16 a 18 anos ou maior de 65 anos)"
else:
    classe_eleitoral = "Idade inválida"

# Exibe a classe eleitoral
print(f"A sua classe eleitoral é: {classe_eleitoral}")
