import random

def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Intenta un numero: '))
        if number == random_number:
            print('Felicidades encontraste el numero')
            number_found = True
        elif number > random_number:
            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')


if __name__ == '__main__':
    run()


'''
    i = 0

    while i < 10:
        print(i)
        i += 1
'''
