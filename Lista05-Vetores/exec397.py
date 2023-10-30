nome = [''] * 10
tel = [''] * 10
preco = [0.0] * 8
pedido = [0.0] * 10
flag = 0
flagl = 0

while True:
    print("\n\n\n")
    print("\n Atelier Maravilha \n")
    print("\n1 - Cadastrar as freguesas")
    print("\n2 - Cadastrar preços das costuras")
    print("\n3 - Calcular e imprimir o total que será pago por cada freguesa")
    print("\n4 - Lista dados de uma cliente")
    print("\n5 - Sair do programa")
    print("\nOPÇÃO:", end="")
    op = int(input())

    if op == 1:
        flag = 1
        for L in range(10):
            print("\nNome ", L + 1, ": ", end="")
            nome[L] = input()
            print("\nTelefone ", L + 1, ": ", end="")
            tel[L] = input()
    elif op == 2:
        print("\n1 Vestido curto\n2 Vestido longo\n3 Conjunto\n4 Blazer\n5 Saia\n6 Calça\n7 Blusa\n")
        for L in range(8):
            print("\nPreço do ", L + 1, ": ", end="")
            preco[L] = float(input())
        flagl = 1
    elif op == 3:
        if flagl == 0:
            print("\nNão tem preços cadastrados")
        else:
            soma = 0.0
            print("\n1 Vestido curto\n2 Vestido longo\n3 Conjunto\n4 Blazer\n5 Saia\n6 Calça\n7 Blusa\n0 Para acabar")
            ped = int(input())
            while ped != 0:
                while ped < 1 or ped > 7:
                    print("\n1 Vestido curto\n2 Vestido longo\n3 Conjunto\n4 Blazer\n5 Saia\n6 Calça\n7 Blusa\n")
                    ped = int(input())
                soma += preco[ped - 1]
                print("\n1 Vestido curto\n2 Vestido longo\n3 Conjunto\n4 Blazer\n5 Saia\n6 Calça\n7 Blusa\n0 Para acabar")
                ped = int(input())
            print("\nTotal: ", soma)
            resp = input("\nCliente cadastrada(S/N)? ")
            if resp == "S" or resp == "s":
                for L in range(10):
                    print("\n", L + 1, ": ", nome[L])
                n = int(input("\nNúmero da cliente: "))
                while n < 1 or n > 10:
                    print("\nNúmero de 1 - 10: ")
                    n = int(input())
                pedido[n - 1] = soma
    elif op == 4:
        for L in range(10):
            print("\n", L + 1, ": ", nome[L])
        n = int(input("\nNúmero da cliente: "))
        while n < 1 or n > 10:
            print("\nNúmero de 1 - 10: ")
            n = int(input())
        print("\nSaldo R$: ", pedido[n - 1])
        resp = input("\nFazer pagamento(S/N)? ")
        if resp == "S" or resp == "s":
            print("\nValor do pagamento: ", end="")
            valor = float(input())
            pedido[n - 1] -= valor
    elif op == 5:
        print("\nSaindo do algoritmo")
        break
    else:
        print("\nOpção não disponível")

print("\n")
