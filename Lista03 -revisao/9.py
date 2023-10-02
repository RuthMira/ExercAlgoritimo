# Solicita ao usuário para fornecer dia e mês
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento (1 a 12): "))

# Determina o signo do zodíaco
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Áries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Touro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Gêmeos"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Câncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leão"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpião"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitário"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricórnio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Aquário"
else:
    signo = "Peixes"

# Exibe o signo do zodíaco
print(f"O seu signo do zodíaco é {signo}.")
