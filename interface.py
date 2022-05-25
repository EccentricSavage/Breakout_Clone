from turtle import Turtle

FONT = "Small Fonts"
class Interface():

    def __init__(self):
        self.interface = Turtle()
        self.interface.color("white")
        self.interface.penup()
        self.interface.hideturtle()
        self.interface.write("Press Spacebar to start the game", align="center", font=(FONT, 40, "normal"))

        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()

        self.lives = Turtle()
        self.lives.color("white")
        self.lives.penup()
        self.lives.hideturtle()

        self.score = -1     # start at -1 since function adds 1
        self.update_score()

        self.num_lives = 6    # start at 6 since function subtracts 1
        self.lose_a_life()


    def click_to_start(self):
        self.interface.clear()

    def lose_a_life(self):
        self.lives.clear()
        self.num_lives -= 1
        self.lives.clear()
        self.lives.goto(200, 230)
        self.lives.write(f"{self.num_lives}", font=(FONT, 40, "normal"))

    def update_score(self):
        self.scoreboard.clear()
        self.score += 1
        self.scoreboard.goto(-200, 230)
        self.scoreboard.write(f"{self.score}", font=(FONT, 40, "normal"))

    def game_over(self):
        self.interface = Turtle()
        self.interface.color("white")
        self.interface.penup()
        self.interface.hideturtle()
        self.interface.write("Game Over", align="center", font=(FONT, 40, "normal"))




