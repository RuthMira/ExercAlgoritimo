# Solicita ao usuário o valor da prestação em atraso
valor_prestacao_atraso = float(input("Digite o valor da prestação em atraso: "))

# Calcula o acréscimo de 10%
acrescimo = valor_prestacao_atraso * 0.1

# Calcula o valor após o acréscimo
valor_com_acrescimo = valor_prestacao_atraso + acrescimo

# Calcula o desconto de 10%
desconto = valor_com_acrescimo * 0.1

# Calcula o valor final a pagar
valor_final = valor_com_acrescimo - desconto

# Calcula o prejuízo do comerciante
prejuizo = valor_prestacao_atraso - valor_final

# Exibe o valor final a pagar e o prejuízo do comerciante
print("Valor final a pagar: R$ ", valor_final)
print("Prejuízo do comerciante: R$: ", prejuizo)
