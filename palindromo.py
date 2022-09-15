# Dos espacion entre cada funcion 👍
def es_palindromo(texto):
    palabra = texto.replace(' ', '')
    palabra = palabra.lower()
    # [::-1] para obtener una lista o cadena al reves
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    palindromo = es_palindromo(palabra)
    if palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()