

def protected(func):

    def wrapper(password):

        while True:
            if password == 'platzi':
                return func()

            else:
                print('La contraseña es incorrecta')
                password = str(input('Escribe una contraseña: '))

    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta: ')

if __name__ == '__main__':
    password = str(input('Escribe una contraseña: '))

    '''
    wrapper = protected(protected_fun)
    wrapper(password)
    '''
    protected_func(password)
