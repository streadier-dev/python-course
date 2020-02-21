
if __name__ == '__main__':
    #mi_diccionario = dict()
    mi_diccionario = {}
    mi_diccionario['primer_elemento'] = 'wea'
    versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    diccionario = {
             "clave1": 234,
             "clave2": True,
             "clave3": "Valor 1",
             "clave4": [1, 2, 3, 4]
        }
    valor1 = diccionario['clave2']
    valor2 =diccionario.get('clave1')
    print(valor1)
    print(valor2)
    print(mi_diccionario)
for key in diccionario:
    print(key)
for value in diccionario.values():
    print(value)
for key, value in versiones.items():
    print('llave: {} , valor : {}'.format(key,value))