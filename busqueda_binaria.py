
def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


def binary_search2(numbers2, number_to_find, low, high):

    if low > high:
        return False

    mid = (low + high) // 2

    if numbers2[mid] == number_to_find:
        return True
    elif numbers2[mid] > number_to_find:
        return binary_search(numbers2, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers2, number_to_find, mid + 1, high)

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numbers2 = [2, 1, 11, 10, 15, 14, 13, 13]
    numbers2.sort()
    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    result2 = binary_search2(numbers2, number_to_find, 0, len(numbers2) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista.')
    if result2 is True:
            print('El número sí está en la lista2.')
    else:
        print('El número NO está en la lista2.')
