#%%
def f(x):
    resultado = 1 + x
    return resultado

#%%
f(10)

# %%
def juros(aporte: int, i:float, t:int)->float:
    """juros servem para calcular o retorno financeiro a partir de um aporte.
    Deve se considerar o valor, a taxa de juros atual e o tempo (em anos)
    para cálculo do valor a ser retornado"""
    return round(aporte * (1 + i) ** t),2

# %%
aporte = int(input("entre com seu aporte: "))
i = 0.13
t = 4
juros(aporte=aporte, t=t, i=i)
# %%
