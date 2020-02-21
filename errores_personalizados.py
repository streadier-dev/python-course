
countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 32
}

while True:
    country = str(input('Escribe el nombre del pais ')).lower()
    try:
        print('La poblacion de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(country))