# Solicita ao usuário para fornecer um número
numero = int(input("Digite um número de três dígitos: "))

# Converte o número em uma string, inverte a string e converte-a de volta para um número
numero_invertido = int(str(numero)[::-1])

# Exibe o número invertido
print("O número invertido é:", numero_invertido)
