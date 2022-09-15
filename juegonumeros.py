import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegino = int(input('Elige un numero del 1 al 100: '))
    while numero_elegino != numero_aleatorio:
        if numero_elegino < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_elegino = int(input('Elige otro numero: '))
    print('Win!')

if __name__ == '__main__':
    run()