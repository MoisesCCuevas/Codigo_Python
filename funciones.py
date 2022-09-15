# def imprimir_mensaje():
#     print('mensaje 1')
#     print('mensaje 2')
# 
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def imprimir_mensaje2(mensaje):
    print('saludos')
    print(mensaje)
    print('adios')

opcion = int(input('Elige una opcion (1, 2, 3):'))

if opcion == 1:
    imprimir_mensaje2('mensaje 1')
elif opcion == 2:
    imprimir_mensaje2('mensaje 2')
elif opcion == 3:
    imprimir_mensaje2('mensaje 3')
else:
    pass