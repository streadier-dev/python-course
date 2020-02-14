
if __name__ == "__main__":

    for i in range(30):
        if i % 3 != 0:
            continue
        else:
            print(i**2)

    print("#" * 50)

    for i in range(30):
        if i % 3 == 0:
            print(i)
        if i == 22:
            break

    print("#" * 50)

    texto = "Hola Chupeta"
    for letter in texto:
        print(list(letter.upper()))
