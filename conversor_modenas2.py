menu = """
  Conversor de Monedas 💰

  1 - Pesos
  2 - Dolares

  Elige una opcion:
"""

opcion = input(menu)

valor_dolar = 19.91

def conversor_modena(moneda):
    ingresa =  input("Cuantos " + moneda + " tienes?: ")
    total = float(ingresa)
    if moneda == 'dolares':
        total = total * valor_dolar
    elif moneda == 'pesos':
        total = total / valor_dolar
    else:
        pass
    return round(total, 2)

if opcion == '1':
    # Dolares a Pesos
    print("Tienes $" + str(conversor_modena('dolares')) + " pesos")
elif opcion == '2':
    # Pesos a Dolares
    print("Tienes $" + str(conversor_modena('pesos')) + " dolares")
else:
    print('Opcion no valida')