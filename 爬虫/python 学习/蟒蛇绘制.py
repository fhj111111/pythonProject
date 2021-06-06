import turtle


def drawSnke(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)

    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(13500, 8100, 10, 90)
    prthonsize = 30
    turtle.pensize(prthonsize)
    turtle.pencolor('blue')
    turtle.seth(-40)
    drawSnke(40, 80, 5, prthonsize / 2)


main()
