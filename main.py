from turtle import Turtle, mainloop


class Etch:  # composition method
    def __init__(self):
        self.__t = Turtle()
        self.__screen = self.__t.screen
        self.__screen.title('Etch A Sketch')
        self.__t.color('blue')
        self.__t.pensize(2)
        self.__t.speed(0)
        self.__distance = 5
        self.__turn = 10

        # register out callbacks
        self.__screen.onkey(self.__fwd, 'Up')
        self.__screen.onkey(self.__bkwd, 'Down')
        self.__screen.onkey(self.__left, 'Left')
        self.__screen.onkey(self.__right, 'Right')
        self.__screen.onkey(self.__toggle_pen, 't')
        self.__screen.onkey(self.__clear, 'c')
        self.__screen.onkey(self.__color, 'space')
        self.__screen.onkey(self.__quit, 'q')
        self.__screen.onkey(self.__quit, 'Escape')
        self.__screen.listen()

    def __fwd(self):
        self.__t.forward(self.__distance)

    def __bkwd(self):
        self.__t.backward(self.__distance)

    def __left(self):
        self.__t.left(self.__turn)

    def __right(self):
        self.__t.right(self.__turn)

    def __toggle_pen(self):
        if self.__t.isdown():
            self.__t.penup()
        else:
            self.__t.pendown()
    def __clear(self):
        self.__t.clear()

    def __color(self):
        if self.__t.color()[0] == 'red':
            self.__t.color('green')
        elif self.__t.color()[0] == 'green':
            self.__t.color('blue')
        else:
            self.__t.color('red')

    def __quit(self):
        self.__screen.bye()


    def main(self):
        mainloop()





if __name__ == '__main__':
    draw = Etch()
    draw.main()