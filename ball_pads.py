from turtle import Turtle, Screen
screen = Screen()


class Pads(Turtle):
    """controlling the pads of the game"""
    def __init__(self, color, shape, size, height, width):
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.screen.tracer(0)
        self.goto(height, width)
        self.color(color)
        self.shapesize(stretch_wid=size, stretch_len=1)
        self.shape(shape)
        self.screen.tracer(1)

    def move_up(self):
        screen.tracer(0)
        speed = 30
        y_axis = self.ycor()
        if y_axis < 250:
            y_axis += speed
            self.goto(self.xcor(), y_axis)
        screen.tracer(1)

    def move_down(self):
        screen.tracer(0)
        speed = 30
        y_axis = self.ycor()
        if y_axis > -240:
            y_axis += -speed
            self.goto(self.xcor(), y_axis)
        screen.tracer(1)
