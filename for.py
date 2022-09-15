def forString():
    nombre = input('escribe tu nombre: ')
    for letra in nombre:
        print(letra)
    frase = input('escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

def run():
    # range(1, 1001) rango del 1 al 1000
    for contador in range(1, 1001):
        print(contador)
    forString()

if __name__ == '__main__':
    run()