from turtle import Turtle, Screen


class Score(Turtle):
    """controlling the all the functions of score board"""
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.human_score = 0
        self.machine_score = 0
        self.goto(-100, 230)
        self.write(self.human_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.machine_score, align="center", font=("Courier", 50, "normal"))
        self.screen.tracer(1)

    def increase_score(self, who):
        self.screen.tracer(0)
        self.clear()
        if who == "left":
            self.machine_score += 1
        elif who == "right":
            self.human_score += 1
        else:
            pass
        self.goto(-100, 230)
        self.write(self.human_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.machine_score, align="center", font=("Courier", 50, "normal"))
        self.screen.tracer(1)
        self.screen.tracer(1)
