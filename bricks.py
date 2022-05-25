from turtle import Turtle
import numpy as np
import random

START_POS_X = -380
START_POS_Y = 200
NUM_X = 6
NUM_Y = 16

class Bricks:

    def __init__(self):
        self.brick_array = np.empty((NUM_X, NUM_Y), Turtle)
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

        self.level = 1 # consider different levels

        self.create_bricks()

    def reset_array(self):
        self.brick_array = np.empty((NUM_X, NUM_Y), Turtle)
        self.create_bricks()

    def create_bricks(self):
        for i in range(6):
            for j in range(16):
                new_brick = Turtle("square")
                # new_brick.color(random.choice((self.colors)))  ## random colors
                new_brick.color(self.colors[i])
                new_brick.shapesize(1,2.5)
                new_brick.penup()
                new_brick.goto(START_POS_X + j*50, START_POS_Y-i*20)
                self.brick_array[i][j] = new_brick

            # ------------ test bricks ---------

            # new_brick = Turtle("square")
            # new_brick.color("blue")
            # new_brick.shapesize(1,2.5)
            # new_brick.penup()
            # new_brick.goto(START_POS_X, START_POS_Y)
            #
            # new_brick2 = Turtle("square")
            # new_brick2.color("blue")
            # new_brick2.shapesize(1, 2.5)
            # new_brick2.penup()
            # new_brick2.goto(START_POS_X + 50*15, START_POS_Y - 20)

