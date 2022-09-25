from turtle import Screen
from ball_pads import Pads
from ball import Ball
from random import randint
from score import Score
import time


screen = Screen()
screen.listen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

screen.tracer(0)
ball = Ball(0, randint(-250, 250), "red", "circle")
human_pad = Pads("white", "square", 5, 370, -150)
machine_pad = Pads("white", "square", 5, -370, 50)
score = Score()
screen.tracer(1)

time.sleep(1)


def ball_hit_human_pad():
    if ball.distance(human_pad) < 50:
        if ball.xcor() > 330:
            return True
    return False


def ball_hit_machine_pad():
    if ball.distance(machine_pad) < 50:
        if ball.xcor() < -330:
            return True
    return False


def play_game():
    while not ball.is_ball_out():
        ball.ball_move(4)
        if ball.ball_hit_wall() == 'up' or ball.ball_hit_wall() == 'down':
            ball.change_direction()

        if ball_hit_human_pad() or ball_hit_machine_pad():
            ball.change_direction()
            ball.move_speed += 0.05

        screen.onkey(human_pad.move_up, "Up")
        screen.onkey(human_pad.move_down, 'Down')

        screen.onkey(machine_pad.move_up, "w")
        screen.onkey(machine_pad.move_down, 's')
        time.sleep(0.05 / ball.move_speed)

    return ball.ball_hit_wall()


while True:
    increase_score = play_game()
    score.increase_score(increase_score)
    time.sleep(1)
    ball.restart_ball()
    time.sleep(1)
