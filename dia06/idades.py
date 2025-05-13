#%%
idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade =="":
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qntd = len(idades)

print(f"Média: {media}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Quantidade: {qntd}")

# %%
