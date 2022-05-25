from turtle import Screen
from paddle import Paddle
from ball import Ball
from interface import Interface
from bricks import Bricks, NUM_X, NUM_Y
import time

# ------- Setup Screen ----------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Clone")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
interface = Interface()
bricks = Bricks()
screen.update()

#---------- Setup keypresses ------------

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")
screen.onkeypress(paddle.left, "a")
screen.onkeypress(paddle.right, "d")


# -------------- Game Loop ------------

def gamestate():
    global game_is_on
    global bricks
    interface.click_to_start()
    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()
        screen.update()

        # detect collisions
        # x
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.bounce(-1, 1)

        # y
        elif ball.ycor() > 290:
            ball.bounce(1, -1)

        # if miss
        elif ball.ycor() < -290:
            # TODO: lose a life
            pass

        # check for collision with brick
        for row in bricks.brick_array:
            # consider checking y cor here for efficiency
            # if ball.ycor() <= brick[0].ycor() + 5 or ball.ycor() >= brick[0].ycor() - 5:
            for brick in row:
                if ball.ycor() <= brick.ycor() + 10 and ball.ycor() >= brick.ycor() - 10:
                    if ball.xcor() <= brick.xcor() + 25 and ball.xcor() >= brick.xcor() - 25:
                        # make ball bounce (y)
                        # if ball.ycor() < brick.ycor() or :
                        ball.bounce(1, -1)
                        interface.update_score()

                        # TODO: make ball bounce (x)
                            # TODO: update score

                        # remove brick (or change coords to out of bounds)
                        brick.goto(1000,1000)
                        # check if all blocks are cleared
                        if interface.score % 96 == 0 and interface.score != 0:
                            # TODO: fix this, delete all objects in the array
                            bricks.reset_array()
                            paddle.reset_paddle((0, -250))
                            ball.restart_ball()
                            screen.update()
                            time.sleep(1)

        # check for collision with paddle
        # check if collision
        if ball.ycor() <= paddle.ycor() + 10 and ball.ycor() >= paddle.ycor() - 10:
            if ball.xcor() <= paddle.xcor() + 40 and ball.xcor() >= paddle.xcor() - 40:
                # check where collision
                # TODO: change angle depending on where it hits
                if ball.xcor() < paddle.xcor() - 15:
                    ball.bounce_set(-1, 1) # if ball hits left, bounce towards top left
                elif ball.xcor() > paddle.xcor() + 15:
                    ball.bounce_set(1, 1) # if ball hits right, bounce towards top right
                else:
                    ball.bounce(1, -1) # if ball hits center, just flip y direction



        # check if player misses
        if ball.ycor() < paddle.ycor() - 50:
            ball.restart_ball()
            interface.lose_a_life()
            if interface.num_lives <  1: # if player runs out of lives, game over
                interface.game_over()
                game_is_on = False
            paddle.reset_paddle((0, -250))
            screen.update()
            time.sleep(1)
            

# -------------- Start Game ---------

game_is_on = False

if not game_is_on:
    screen.onkeypress(gamestate, "space")

screen.exitonclick()
