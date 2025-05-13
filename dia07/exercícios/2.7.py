fruta = input("Entre com o nome da fruta: ")

lista_frutas = {
                "Maçã": "R$ 1,50",
                "Banana": "R$ 2,75",
                "Uva": "R$ 1,90",
                "Pera": "R$ 1,25",
                "Laranja": "R$ 0,65",
                "Limão": "R$ 1,25",
                "Pera": "R$ 1,25",
                "Laranja": "R$ 0,65",
                "Limão": "R$ 1,25"
}

if fruta in lista_frutas:
    print(f"O valor da {fruta} é {lista_frutas[fruta]}")

else:
    print("Entre com uma fruta válida")