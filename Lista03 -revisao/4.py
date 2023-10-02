# Solicita ao usuário para fornecer a capacidade do tanque, quantidade de litros abastecidos e quilometragem percorrida
capacidade_tanque = float(input("Capacidade do tanque (em litros): "))
litros_abastecidos = float(input("Quantidade de litros abastecidos: "))
quilometragem_percorrida = float(input("Quilometragem percorrida desde o último abastecimento: "))

# Calcula o consumo de combustível (quilômetros por litro)
consumo = quilometragem_percorrida / litros_abastecidos

# Calcula a autonomia (quilômetros que o veículo pode percorrer com o tanque cheio)
autonomia = capacidade_tanque * consumo

# Exibe o consumo e a autonomia
print("O consumo foi de: ", consumo)
print("A autonomia do carro foi de", autonomia)
