def run():
    mi_diccionario = {
        'llave 1': 1,
        'llave 2': 2,
        'llave 3': 3
    }
    # print(mi_diccionario['llave 1'])
    for llave in mi_diccionario.keys():
        print(llave)
    for valorllave in mi_diccionario.values():
        print(valorllave)
    for llave, valor in mi_diccionario.items():
        print(llave, valor)

if __name__ == '__main__':
    run()