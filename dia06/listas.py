#%%
# Uma maneira de definir listas
idades = [28, 46, 24, 87 ,34 ,68]

print (idades)

# %%
mike = ["Michael", "Mike", 25, False, "Solteiro", 2843,24]

type(mike)

#%%

# Nome
mike[0]
# Apelido
mike[1]
# Status civil
mike[5-1]

# %%

idades = [28, 46, 24, 87 ,34 ,68]

sum(idades)

print(f"Soma das idades: ", sum(idades))

print(f"Quantidade de idades: ", len(idades)) # mostra a quantidade de elementos

print(f"Média das idades:", sum(idades) / len(idades))

print("Menor idade: ", min(idades))

print("Maior idade: ", max(idades))

# %%

mike = ["Mike", 
        25, 
        False, 
        "Solteiro", 
        ["estagiario", "ds jr.", "ds pl.", "ds sr.", "head"], 
        [1500, 4000, 4600, 6500, 10000], 
        ["Ana", "Maira", "Bruna"]]

mike[4][0]

exs = mike[4]
primeira = exs[0]
print(primeira)

tamanho = len(mike)
pos = tamanho - 1
exs = mike[pos]
print(exs)

mike[pos][len(exs) - 1]

mike[-1][-1] # retorna o ultimo item da lista
# %%

mike[0:4]

mike[-3][3:5]
#%%

mike[-3][-2:] #vai até o final da lista

#%%

mike[:3] #começa no inicio da lista

#%%

mike[-3][:3]

# %%

salarios = mike[5]
salarios[::-1] #[start : stop : step] retorna a lista de trás para frente
salarios[::2] # retorna a lista a cada 2 posições

# %%
