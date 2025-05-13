lista = [2, 132, "mike", ["ds", "de", "da"]]

lista [2]

#%%
# pares de chave/valor
dados_mike = {"sobrenome": "Yuki",
              "nome": "Michael",
              "filhos": False,
              "formação": ["Economia", "Big Data e Data Science"],
              "cargos": [
                  {"nome": "ds jr.", "empresa": "GB Adm"},
                  {"nome": "ds pl.", "empresa": "Cooper"},
                  {"nome": "ds sr.", "empresa": "TBA"},
                  {"nome": "ds esp.", "empresa": "TBA 2"}
              ]
             }

print(f"{dados_mike["nome"]}")

# %%
print(dados_mike)
print(dados_mike["formação"][-1])
print(dados_mike["cargos"][-1]["empresa"])

# %%
dados_mike["estado civil"] = "Solteiro"     #atribui uma nova chave no dicionário

print(dados_mike)

# %%
print("Chaves: ", dados_mike.keys())

print("Valores:", dados_mike.values())

print("Items:", dados_mike.items())

# %%
for i in dados_mike:
    print(i, "→", dados_mike[i])

# %%
for chave, valor in dados_mike.items():
    print(chave, "→", valor)

# %%
dados_mike["estado civil"] = "Casado" # Alterando valor de um chave

print(dados_mike)
# %%
