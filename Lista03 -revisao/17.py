# Solicita os dois primeiros termos ao usuário
primeiro_termo = int(input("Digite o primeiro termo: "))
segundo_termo = int(input("Digite o segundo termo: "))

# Inicializa a lista com os dois primeiros termos
serie = [primeiro_termo, segundo_termo]

# Gera os próximos 18 termos da série
for _ in range(18):
    proximo_termo = primeiro_termo + segundo_termo
    serie.append(proximo_termo)
    
    # Atualiza os valores de primeiro_termo e segundo_termo para os próximos cálculos
    primeiro_termo, segundo_termo = segundo_termo, proximo_termo

# Imprime a série gerada
print("Os 20 primeiros termos da série são:")
print(serie)
