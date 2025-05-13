#%%
try:
    numero = int(input("Escolha um número da sorte entre 1 e 15: "))    

    sorte = 7   

    if numero < sorte:
        print("Errrou! Escolha um número maior")    

    elif numero > sorte:
        print("Errrou! Escolha um número menor")    

    else :
        print("Acertou mizeravi")
    except ValueError as err 