import turtle


FONT = ("Title Block", 8, 'normal')


class Entry(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_place(self, state, x, y):
        self.goto(x, y)
        self.write(state, font=FONT, align="left")
