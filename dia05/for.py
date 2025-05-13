 #%%
nome = "Michael"

for i in nome:
    print(i)

# %%
numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(f"{numero} * {i} = {numero * i}")
    

# %%
numerador = 100
denominador = 4

for i in range(0, numerador + 1):
    if i % denominador == 0:
        print(f"{i} é divisível por {denominador}")

# %%
# Faça um programa que receba 4 alturas usando um laço de 
# repetição e realize a soma dessas alturas, usando o for

soma_altura = 0
qntd_entradas = 4

for i in range(qntd_entradas): # range(0, qntd_entradas)
    altura = input("Insira a altura do objeto: ")
    altura = float(altura)
    soma_altura += altura

print(f"A altura total é {soma_altura}")
# %%
