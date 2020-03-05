def sumar():
    suma = 0
    while True:
        numero = int(input("Ingrese intervalo principal "))
        numero2 = int(input("Ingrese intervalo limite"))
        if numero <= numero2:
            suma = suma + (numero2 +numero +1)
            print("El resultado de una suma recursiva es: {} ".format(suma))
            return True
        else:
            print("El intervalo no es valido por favor intentar nuevamnete")


if __name__ == '__main__':
    sumar()

