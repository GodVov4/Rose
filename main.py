from turtle import *
import colorsys


def main():
    speed(0)
    pensize(2)
    bgcolor('black')
    h = 0.0
    for i in range(2000):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        pencolor(c)
        h += 0.005
        circle(5-i, 100)
        lt(80)
        circle(5-i, 100)
        rt(100)
    done()


if __name__ == '__main__':
    main()
