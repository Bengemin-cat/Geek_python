from time import sleep
import turtle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        ben = turtle.Turtle()
        ben.hideturtle()
        ben.speed(20)
        ben.pu()
        ben.setposition(-100, 200)
        ben.pd()
        for i in range(4):
            if i % 2 == 0:
                ben.forward(200)
                ben.right(90)
            else:
                ben.forward(350)
                ben.right(90)

        ben.showturtle()
        ben.pu()
        ben.setposition(0, 100)
        ben.pd()
        ben.circle(40)

        ben.pu()
        ben.setposition(0, 0)
        ben.pd()
        ben.circle(40)

        ben.pu()
        ben.setposition(0,-100)
        ben.pd()
        ben.circle(40)

        turtle.done()


traffic = TrafficLight()

traffic.running()
