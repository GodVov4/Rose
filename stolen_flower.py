import colorsys
from turtle import *


def main():  # I made lil changes, now it looks better
    speed(0)
    tracer(10)
    width(2)
    bgcolor('black')
    hideturtle()
    for j in range(50):
        for i in range(15):
            color(colorsys.hsv_to_rgb(i / 15, j / 50, 1))
            right(90)
            circle(200 - j * 4, 90)
            left(90)
            circle(200 - j * 4, 90)
            right(180)
            circle(50, 24)
    done()


if __name__ == '__main__':
    main()
