# Pesos a Dolares
pesos = input("Cuantos pesos tienes?: ")
pesos = float(pesos)
valor_dolar = 19.91
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
print("Tienes $" + str(dolares) + " dolares")

# Dolares a Pesos
dolares = input("Cuantos dolares tienes?: ")
dolares = float(dolares)
pesos = dolares * valor_dolar
pesos = round(pesos, 2)
print("Tienes $" + str(pesos) + " pesos")