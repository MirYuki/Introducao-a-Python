
#%%
texto = """
Escolha a sua água para comprar:
(1) Água mineral natural | R$ 1,50
(2) Água mineral com gás | R$ 2,00
(3) Água mineral aromatizada | R$ 2,50
"""

opção = input("Escolha entre as opções: 1, 2 ou 3: ")

opção = int(opção)

if opção == 1:
    print("A água custará R$ 1,50.")

elif opção == 2:
    print("A água custará R$ 2,00.")

elif opção == 3:
    print("A água custará R$ 2,50")

else:
    print("Opção inválida, selecione entre 1, 2 ou 3")

#%%
texto = """
Escolha a sua água para comprar:
(1) Água mineral natural | R$ 1,50
(2) Água mineral com gás | R$ 2,00
(3) Água mineral aromatizada | R$ 2,50
"""

print(texto)

opção = input("Escolha entre as opções: 1, 2 ou 3: ")

opção = int(opção)

conta = "A água custará R$"

valor = 0

if opção == 1:
    valor = "1,50"
elif opção == 2:
    valor = "2,00"
elif opção == 3:
    valor = "2,50"

if valor == 0:
    print("Opção inválida, selecione entre 1, 2 ou 3")
elif valor == 1:
    print(f"{conta} {valor}.")
elif valor == 2:
    print(f"{conta} {valor}.")
else:
    print(f"{conta} {valor}.")