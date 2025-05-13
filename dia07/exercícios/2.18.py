#Escreva um programa que solicite ao usuário frases.
#Para parar de solicitar frases, ele pode apenas apertar o “enter”.
#Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.


lista_frases = {}

while True:
    frase = input("Entre com uma frase: ")
    if frase == "":
        break

    if frase not in lista_frases:
        lista_frases[frase] = 1
    else:
        lista_frases[frase] += 1

print(lista_frases)
    
for i, j in lista_frases.items():
    if j > 1:
        print(f"A frase '{i}' foi dita {j} vezes")
    else:
        print(f"A frase '{i}' foi dita {j} vez")

#%%

dados = {
    "oi": 1,
    "ola": 10,
    "oi tudo bem": 3,
    "test": 2,
    "teste": 5
}

items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    if j > 1:
        print(f"A frase '{i}' foi dita {j} vezes")
    else:
        print(f"A frase '{i}' foi dita {j} vez")
# %%
