from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.001
        self.goto(0, -220)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self, x, y):
        """Set the direction (x,y) to change"""
        self.x_move *= x
        self.y_move *= y

    def bounce_set(self, x, y):
        """Set the direction for the x and y coordinates manually"""
        self.x_move = abs(self.x_move) * x
        self.y_move = abs(self.y_move) * y

    def restart_ball(self):
        self.goto(0, -220)
        self.bounce_set(1, 1)