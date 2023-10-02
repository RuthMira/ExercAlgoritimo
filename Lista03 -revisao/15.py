# Solicita aos usuários para fornecer os números
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

# Inicializa o quociente e o contador
quociente = 0
contador = 0

# Calcula o quociente usando subtrações sucessivas
while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1
    contador += 1

# Exibe o quociente inteiro
print(f"Quociente inteiro da divisão: {quociente}")
print(f"Número de subtrações realizadas: {contador}")
