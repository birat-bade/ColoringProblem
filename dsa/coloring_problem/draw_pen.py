import turtle


class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.shape('square')
        self.pen.color('white')
        self.pen.penup()
        self.pen.speed(0)


    def get_pen(self):
        return self.pen
