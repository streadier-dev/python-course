
mi_lista = []

mi_lista.append(1)

mi_lista_2 = [2, 3, 4]

mi_lista_3 = mi_lista + mi_lista_2

mi_lista_4 = ['a']

mi_lista_5 = mi_lista_4 * 10

casa = 'casa'

casa2 ='casa2'

lista_casa = list(casa)

union = ''.join(lista_casa)

result = "la %s es mas grande que la %s" % (union, casa2)

if __name__ == '__main__':
#   del mi_lista_2[1]
    print(mi_lista_3)
    print(mi_lista_2)
    print(lista_casa)
    print(result)
    print("la {} es mas grande que la {}".format(union, casa2))
    print(union + casa2)
    print('{} {}'.format(union,casa2))
