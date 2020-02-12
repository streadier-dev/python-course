# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_rectangle(dave)
    turtle.mainloop()


def make_rectangle(dave):
    lenght = int(input('tamaño de cuadrado : '))

    for i in range(4):
        make_line_and_turn(dave, lenght)

def make_line_and_turn(dave, lenght):
    dave.forward(lenght)
    dave.left(90)

if __name__ == '__main__':
    main()