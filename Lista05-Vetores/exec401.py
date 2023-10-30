op = 0
c = 0
dados1 = [''] * 50
dados2 = [''] * 50
dados3 = [''] * 50
milha = [0.0] * 50

while op != 6:
    print("\n********************")
    print("* MENU *")
    print("********************")
    print("\n1 - Cadastrar dados do cliente")
    print("2 - Cadastrar milhagem do cliente")
    print("3 - Listar milhagem do cliente")
    print("4 - Imprimir os nomes que têm maior e menor milhagem")
    print("5 - Imprimir os nomes e as milhagens")
    print("6 - SAIR")
    op = int(input("\nOPÇÃO: "))

    if op == 1:
        if c <= 49:
            print("\n", c + 1, "- nome: ", end="")
            dados1[c] = input()
            print("endereco: ", end="")
            dados2[c] = input()
            print("telefone: ", end="")
            dados3[c] = input()
            c += 1
        else:
            print("\nArquivo cheio")

    elif op == 2:
        print("\nNome para procura: ", end="")
        nome = input()
        d = 0
        while d < c and nome != dados1[d]:
            d += 1
        if d < c and nome == dados1[d]:
            print("\nDigite milhagem de ", dados1[d], ": ", end="")
            milhas = float(input())
            milha[d] -= milhas
        else:
            print("\nNome não encontrado")

    elif op == 3:
        print("\nNome para procura: ", end="")
        nome = input()
        d = 0
        while d < c and nome != dados1[d]:
            d += 1
        if d < c and nome == dados1[d]:
            print("\nMilhagem de ", dados1[d], ": ", milha[d])
        else:
            print("\nNão encontrado")

    elif op == 4:
        d = 1
        posmenor = 0
        posmaior = 0
        while d < c:
            if milha[d] > milha[posmaior]:
                posmaior = d
            elif milha[d] < milha[posmenor]:
                posmenor = d
            d += 1
        print("\nDados da pessoa de maior milhagem")
        print("Nome: ", dados1[posmaior])
        print("Endereco: ", dados2[posmaior])
        print("Telefone: ", dados3[posmaior])
        print("Milhagem: ", milha[posmaior])
        print("\nDados da pessoa de menor milhagem")
        print("Nome: ", dados1[posmenor])
        print("Endereco: ", dados2[posmenor])
        print("Telefone: ", dados3[posmenor])
        print("Milhagem: ", milha[posmenor])

    elif op == 5:
        print("\nListagem")
        for d in range(c):
            print(d + 1, "-", dados1[d], ":", milha[d])

    elif op == 6:
        print("\nBOA VIAGEM")

    else:
        print("\nOpção inexistente")

print("\n")
