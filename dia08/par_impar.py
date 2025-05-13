#%%
def par_impar(numero: int):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

#%% 
numero = input("Entre com um numero: ")
numero = int(numero)
par_impar(numero = numero)

#%%
#%%
def par_impar2(numero: int):
    if numero % 2 == 0:
        return("par")
    else:
        return("impar")

numero = input("Entre com um numero: ")
numero = int(numero)

resultado = par_impar2(numero)

print(f"O numero {numero} é {resultado}")
# %%
