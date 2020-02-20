
def numeros():

    pares = []

    for num in range(1, 31):
        print(num, end=', ')
        if num % 2 == 0:
            pares.append(num)
    print('')
    print(pares)

    cuadrados = {}

    for num2 in range(1, 11):
        cuadrados[num2] = num2 ** 2
    print(cuadrados)


def numeros2():
    even = [num for num in range(1, 31) if num % 2 == 0]
    print(even)

    squares = {num2: num2 ** 2 for num2 in range(1, 11)}
    print(squares)

if __name__ == '__main__':
    numeros()
    numeros2()
