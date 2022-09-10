from turtle import Screen
from paddle import Paddle
from ball import Ball
from layout import Outline
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
score = ScoreBoard()
outline = Outline()

paddle_left = Paddle('left')
paddle_right = Paddle('right')
screen.listen()
screen.onkeypress(fun=paddle_left.up, key="w")
screen.onkeypress(fun=paddle_left.down, key="s")
screen.onkeypress(fun=paddle_right.up, key="Up")
screen.onkeypress(fun=paddle_right.down, key="Down")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.03)

    ball.move()

    # detect collision with paddle
    if ball.xcor() <= -375:
        for seg in paddle_left.segments:
            if seg.distance(ball) <= 18:
                if 0 <= ball.heading() <= 180:
                    ball.setheading(180 - ball.heading())
                else:
                    ball.setheading(-180 - ball.heading())
                break

    if ball.xcor() >= 365:
        for seg in paddle_right.segments:
            if seg.distance(ball) <= 18:
                if 0 <= ball.heading() <= 180:
                    ball.setheading(180 - ball.heading())
                else:
                    ball.setheading(-180 - ball.heading())
                break

    # detect collision with miss ball
    if ball.xcor() > 400:
        score.increase_score("left")
        ball.refresh()
        time.sleep(0.5)
    if ball.xcor() < -410:
        score.increase_score("right")
        ball.refresh()
        time.sleep(0.5)

    # game_over
    winner = None
    if score.left_score == 3:
        winner = "Player 1"
    if score.right_score == 3:
        winner = "Player 2"
    if winner:
        score.game_over(winner)
        is_game_on = False

screen.exitonclick()
