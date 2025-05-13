#%%
idade = int(input("Qual a sua idade? "))

if idade < 18:
    print("Sem bebida para você!")
    print("Vá beber leite!")

elif idade > 70: 
    print("Beba com moderação e não tome remédio!")

else :
    print("Bebida liberada!")