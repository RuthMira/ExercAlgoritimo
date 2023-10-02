# Função para converter Fahrenheit para Celsius
def converter_para_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Imprimir cabeçalho da tabela
print("Fahrenheit | Celsius")
print("-----------|---------")

# Calcular e imprimir os valores da tabela de 50 a 150 Fahrenheit
for fahrenheit in range(50, 151):
    celsius = converter_para_celsius(fahrenheit)
    print(f"{fahrenheit:^10} | {celsius:^7.2f}")
