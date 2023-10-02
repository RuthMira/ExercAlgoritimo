# Solicita ao usuário para fornecer a data, mês e ano atual separadamente
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

# Solicita ao usuário para fornecer a data, mês e ano do aniversário separadamente
dia_aniversario = int(input("Digite o dia do seu aniversário: "))
mes_aniversario = int(input("Digite o mês do seu aniversário: "))
ano_aniversario = int(input("Digite o ano do seu aniversário: "))

# Calcula a idade em anos
idade_anos = ano_atual - ano_aniversario

# Calcula a idade em meses
idade_meses = mes_aniversario - mes_atual

# Calcula a idade em dias
idade_dias = dia_aniversario - dia_atual

# Exibe a idade em anos, meses e dias
print(f"Idade: {idade_anos} anos, {idade_meses} meses e {idade_dias} dias.")
