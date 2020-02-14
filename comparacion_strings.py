# -*- coding: utf-8 -*-
'''
nombre1 = 'gabo'
nombre2 = 'gabo'


if nombre1 == nombre2:
    print('Los nombres son iguales')
else:
    print('Los nombres no son iguales')
'''
def func():

    nombre1 = str(input('Escribe el primer nombre: '))
    nombre2 = str(input('Escribe el segundo nombre: '))

    if nombre1 == nombre2:
        return True
    else:
        return False
'''
def rps():
    return True
'''
if __name__ == '__main__':
    resultado = func()
    print(resultado)
