#Tabuado de um número até 0 100
#%%
numero = int(input("Digite um número para gerar a tabuada: "))
multiplicador = 0

while multiplicador <= 100:
    print(f"{numero} * {multiplicador} = {numero * multiplicador}")
    multiplicador += 1

print("Fim da tabuada")
# %%
denominador = 4
i = 0

while i <= 100:
    resto = i % denominador
    if resto == 0:
        print(f"{i} é divisível por {denominador}")
    
    i += 1