#%%
segundos = int(input("Indique quantos segundos: "))
horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

print(f"Isto dá {horas:02}:{minutos:02}:{segundos:02}")