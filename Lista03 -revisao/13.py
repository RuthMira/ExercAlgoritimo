# Função para calcular o MDC usando o Algoritmo de Euclides
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o MMC usando a fórmula MMC(a, b) = (a * b) / MDC(a, b)
def calcular_mmc(a, b):
    mdc = calcular_mdc(a, b)
    mmc = (a * b) // mdc
    return mmc

# Solicita aos usuários para fornecer os números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula e exibe o MMC dos números fornecidos
mmc = calcular_mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é {mmc}.")
