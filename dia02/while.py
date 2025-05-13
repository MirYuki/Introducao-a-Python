#%%
while True:
    print("Esse não para nunca")

#%%
i = 1
while True:
    print(i)
    i = i + 1
    if i > 100:
        print("Pediu pra parar, parou!")
        break

#%%
i = int(input("Entre com o valor mínimo da iteração "))
j = int(input("Entre com o valor máximo da iteração "))

while i <= j:
    print(i, end=" ")
    i += 1