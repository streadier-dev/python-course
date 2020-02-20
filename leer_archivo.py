
def run(palabra):
    counter = 0
    with open('texto.txt', encoding="utf8") as f:
        for line in f:
            counter += line.count(palabra)
    if counter == 0:
        print('La letra no se encuentra en el texto')
    else:
        print('La palabra {} se encuentra {} en el texto'.format(palabra,counter))


if __name__ == '__main__':

    palabra = str(input('Ingresa la palabra para buscarla: '))
    run(palabra)
