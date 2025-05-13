#%%
arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines() #le o arquivo como uma lista

print(lines)

for l in lines:
    print(l)

# %%

dados = dict()

chaves = lines[0].strip("\n").split(";")

print(chaves)

for c in chaves:
    dados[c] = []

print(dados)

# %%

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

print(dados)

# %%

print(dados["idade"])

idades = []

for i in dados["idade"]:
    idades.append(int(i))

avg_idades = sum(idades) / len(idades)

print(avg_idades)
    
# %%
