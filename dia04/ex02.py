texto = """
\n
Escolha a sua água para comprar:
(1) Água mineral natural | R$ 1,50
(2) Água mineral com gás | R$ 2,00
(3) Água mineral aromatizada | R$ 2,50
"""
print(texto)

opção = input("Escolha entre as opções: 1, 2 ou 3: ")

valor = 0

if opção == "1":
    valor = 1.50
elif opção == "2":
    valor = 2.00
elif opção == "3":
    valor = 2.50

if valor == 0:
    print("Opção inválida, selecione entre 1, 2 ou 3")

else:
    qntd = input("Quantas unidades você deseja? ")
    qntd = int(qntd)
    total = valor * qntd
    print(f"O valor total é R$ {total:.2f}")