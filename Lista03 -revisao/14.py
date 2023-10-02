# Função para calcular o MDC usando o Algoritmo de Euclides
def calcular_mdc(a, b):
    contador = 1
    while b != 0:
        a, b = b, a % b
        contador += 1
    return a, contador

# Solicita aos usuários para fornecer os números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula o MDC e o número de iterações usando o Algoritmo de Euclides
mdc, iteracoes = calcular_mdc(num1, num2)

# Exibe o MDC e o número de iterações
print(f"O MDC de {num1} e {num2} é {mdc}.")
print(f"Foram necessárias {iteracoes} iterações para encontrar o MDC.")
