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
# Inicializa as variáveis para armazenar o menor e o maior valor
menor_valor = float('inf')  # Inicializa com infinito para garantir que qualquer valor seja menor
maior_valor = float('-inf')  # Inicializa com menos infinito para garantir que qualquer valor seja maior

# Solicita valores ao usuário até que -1 seja digitado
print("Digite os valores inteiros e positivos. Digite -1 para finalizar.")
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break  # Sai do loop se -1 for digitado
    if valor < 0:
        print("Por favor, digite um valor inteiro e positivo.")
        continue  # Pula para a próxima iteração se um valor negativo for inserido
    # Atualiza o menor e o maior valor, se necessário
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor

# Verifica se foram inseridos valores válidos antes de imprimir os resultados
if menor_valor != float('inf') and maior_valor != float('-inf'):
    print(f"O menor valor do conjunto é: {menor_valor}")
    print(f"O maior valor do conjunto é: {maior_valor}")
else:
    print("Nenhum valor válido foi inserido.")
