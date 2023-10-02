# Solicita ao usuário para fornecer cinco números
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))

# Define os pesos
peso1, peso2, peso3, peso4, peso5 = 1, 2, 3, 4, 5

# Calcula a média ponderada
soma_numeros = (num1 * peso1) + (num2 * peso2) + (num3 * peso3) + (num4 * peso4) + (num5 * peso5)
soma_pesos = peso1 + peso2 + peso3 + peso4 + peso5

media_ponderada = soma_numeros / soma_pesos

# Exibe o resultado
print("A média ponderada dos números fornecidos é:", media_ponderada)
