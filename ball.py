from turtle import Turtle, Screen
from random import choice, randint


class Ball(Turtle):
    """control the all the activities of ball"""
    def __init__(self, x_cor, y_cor, color, shape):
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.goto(x_cor, y_cor)
        self.color(color)
        self.shape(shape)
        self.position = (x_cor, y_cor)
        self.moving_direction = choice(["right_up", "left_up", "left_down", "right_down"])
        self.move_speed = 0.9

    def ball_move(self, distance):
        self.screen.tracer(0)
        direct_dict = {"right_up": (1, 1), "left_up": (-1, 1), "left_down": (-1, -1), "right_down": (1, -1)}
        direction = self.moving_direction
        x, y = self.position[0], self.position[1]
        x, y = x + (direct_dict[direction][0] * distance), (y + direct_dict[direction][1] * distance)
        self.position = (x, y)
        self.goto(self.position)
        self.screen.tracer(1)
        return None

    def is_ball_out(self):
        if self.position[0] < -410 or self.position[0] > 410:
            return True
        return False

    def ball_hit_wall(self):
        if self.position[1] >= 285:
            return "up"
        elif self.position[1] <= -280:
            return "down"
        elif self.position[0] >= 350:
            return "right"
        elif self.position[0] <= -350:
            return "left"
        else:
            return "No"

    def change_direction(self):
        hit_wall = self.ball_hit_wall()
        move_direction = self.moving_direction

        if hit_wall == "up" and move_direction == "left_up":
            self.moving_direction = "left_down"
        elif hit_wall == "up" and move_direction == "right_up":
            self.moving_direction = "right_down"
        elif hit_wall == "down" and move_direction == "right_down":
            self.moving_direction = "right_up"
        elif hit_wall == "down" and move_direction == "left_down":
            self.moving_direction = "left_up"
        elif hit_wall == "right" and move_direction == "right_up":
            self.moving_direction = "left_up"
        elif hit_wall == "right" and move_direction == "right_down":
            self.moving_direction = "left_down"
        elif hit_wall == "left" and move_direction == "left_up":
            self.moving_direction = "right_up"
        elif hit_wall == "left" and move_direction == "left_down":
            self.moving_direction = "right_down"
        return None

    def restart_ball(self):
        self.screen.tracer(0)
        x_cor, y_cor = 0, randint(-250, 250)
        self.goto(x_cor, y_cor)
        self.position = (x_cor, y_cor)
        self.moving_direction = choice(["right_up", "left_up", "left_down", "right_down"])
        self.move_speed = 0.9
        self.screen.tracer(1)
