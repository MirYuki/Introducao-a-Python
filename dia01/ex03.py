#%%
raio = input("Insira o tabamho do raio: ")
raio = int(raio)

Area = (3.14*raio**2)
print("Area = 3.14 * (", raio, ")^2", sep="")
print("Area = ", Area, sep="")

P = (2*3.14*raio)
print("Perimetro = 2 * 3.14 *", raio,)
print("Perimetro =", P)

#%%
r = float(input("Insira o tamanho do raio em cm: "))
area = 3.14 * r**2
perimetro = 2*3.14*r
print("Para um raio de", r, "cm")
print("Área =", round(area, 2) )
print("Perimetro =", round(perimetro, 2))

#%%
r = float(input("Insira o tamanho do raio em cm: "))
area = 3.14 * r**2
perimetro = 2*3.14*r
print("Para um raio de", r, "cm")
print(f"Área = {area:.2f}")
print(f"Perimetro = {perimetro:.2f}")
