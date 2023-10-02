# Solicita ao usuário para fornecer dia, mês e ano
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Lista de meses com 31 dias
meses_31_dias = [1, 3, 5, 7, 8, 10, 12]

# Valida o dia, mês e ano
if mes >= 1 and mes <= 12:
    if mes in meses_31_dias and dia >= 1 and dia <= 31:
        print("Data válida.")
    elif mes == 2:
        if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)) and dia >= 1 and dia <= 29:
            print("Data válida.")
        elif dia >= 1 and dia <= 28:
            print("Data válida.")
        else:
            print("Data inválida.")
    elif dia >= 1 and dia <= 30:
        print("Data válida.")
    else:
        print("Data inválida.")
else:
    print("Data inválida.")
