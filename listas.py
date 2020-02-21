
def average_temps(temps):
    sum_of_temps = 0
   #suma_total = 0

    for temp in temps:
        sum_of_temps += temp
       #suma_total = temp+suma_total
       #print('Suma forma tipica {}' .format(suma_total))
        print('Suma forma python {} '.format(sum_of_temps))
    return sum_of_temps / len(temps)

'''
amigos = list()

amigos.append('Jorge')
amigos.append('Nicolas')
'''


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temps(temps)
    print('La temperatura promedio es: {}'.format(average))

    '''
    for element in amigos:
        print(element)
    print(amigos)
    '''
