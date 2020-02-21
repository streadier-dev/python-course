# -*- coding: utf-8 -*-


def foreign_exchange_calculator(ammount):
    cl_to_col_rate = 791.81

    return cl_to_col_rate * ammount

def run():
    print('Calculadora de divisas ')
    print('Convierte pesos chilenos a dolares. ')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos chilenos que quieres convertir '))

    result = int(foreign_exchange_calculator(ammount))

    print(' ${} esta cantidad de dolares son ${} pesos chilenos ' .format(ammount, result))
    print('')

if __name__ == '__main__':
    run()