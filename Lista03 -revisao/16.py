# Função para calcular a exponenciação
def calcular_exponenciacao(base, expoente):
    resultado = 1
    
    # Caso especial quando o expoente é 0, o resultado é 1
    if expoente == 0:
        return resultado
    
    # Calcula a exponenciação usando um loop
    for _ in range(abs(expoente)):
        resultado *= base
    
    # Se o expoente for negativo, calcula o inverso
    if expoente < 0:
        resultado = 1 / resultado
    
    return resultado

# Solicita a base e o expoente ao usuário
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente (inteiro): "))

# Calcula e imprime o resultado da exponenciação
resultado = calcular_exponenciacao(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado}")
