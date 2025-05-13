
idade = input("Quantos anos você tem? ")
idade = int(idade)

if idade >= 70:
    print("Cuidado com a bebida!")
    print("Consulte o seu médico.")

elif idade >=18:
    print("Você pode beber cerva!")
    print("Beba com moderação.")

elif idade == 17:
    print("Você ainda não pode beber cerveja.")
    print("Fique no refri!")

else:
    print("Você não pode beber.")
    print("Volte para casa!")