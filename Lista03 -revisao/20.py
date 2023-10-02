# Inicializa o número de grãos no primeiro quadrado
graos_no_primeiro_quadrado = 1

# Inicializa o total de grãos recebidos pelo monge
total_de_graos = 0

# Inicializa o contador para o número de quadrados percorridos
quadrado_atual = 1

# Enquanto não percorrer todos os 64 quadrados
while quadrado_atual <= 64:
    total_de_graos += graos_no_primeiro_quadrado
    graos_no_primeiro_quadrado *= 2  # Dobra o número de grãos no próximo quadrado
    quadrado_atual += 1  # Move para o próximo quadrado

# Imprime o total de grãos recebidos pelo monge
print("O monge receberá um total de", total_de_graos, "grãos de trigo.")
