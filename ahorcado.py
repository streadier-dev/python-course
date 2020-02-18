import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- ')

def random_world():
    indice = random.randint(0, len(WORDS) - 1)
    return WORDS[indice]

def run():
    word = random_world()
    hidden_word =['-'] * len(word)
    tries = 0
    current_letter_index = []
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
        letter_indexes = []
        if current_letter in current_letter_index:
            print('La letra que ingresaste ya se encuentra en el arreglo')
            continue
        else:
            current_letter_index.append(current_letter)
        if current_letter_index != []:
            current = ''.join(current_letter_index)
            print('Las letras que se usaron fueron: ')
            print(*current, sep=", ")
        for idx in range(len(word)):
            if word[idx] == current_letter: ## logica de comparacion de los indices del arreglo con la letra ingresada
                letter_indexes.append(idx)
        #print(current_letter_index)
        if current_letter == '':
            print('Los espacios en blancos no estan permitidos, por favor intenta nuevamente con una letra')
            continue
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perdiste! la palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades Ganaste. La palabra es {}'.format(word))
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S A A H O R C A D O S')
    run()
