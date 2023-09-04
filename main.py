from turtle import *
import colorsys
import config


# Choose a picture:
# star
# lotus
# some flower
# propeller
# web
# hurt-flower
# clover

def main():
    speed(0)
    pensize(2)
    bgcolor('black')
    extent, cycles = config.CONSTANTS.get('clover')()  # U can change the config to see different flowers
    h = 0.0
    for i in range(cycles):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        pencolor(c)
        h += 0.005
        circle(5-i, extent)
        lt(80)
        circle(5-i, extent)
        rt(100)
    done()


if __name__ == '__main__':
    main()
