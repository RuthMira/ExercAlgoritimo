idade = int(input("\nEntre com a idade:"))
nome = str(input("\nEntre com o nome: "))

if (idade <= 10 ):
    print(f"\n,{nome},pagara R$ 30,00")
elif (idade <= 29 ):
    print(f"\n{nome},pagara R$ 60,00")
elif (idade <= 45 ):
    print(f"\n{nome},pagara R$ 120,00")
elif  (idade <= 59 ):
    print(f"\n{nome},pagara R$ 150,00")
elif (idade <= 65 ):
    print(f"\n{nome},pagara R$ 250,00")
else: print(f"\n{nome},pagara R$ 400,00")
print("\n")