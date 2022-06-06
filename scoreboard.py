from turtle import Turtle
FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hi_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoredboard()

    def update_scoredboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.hi_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
        self.score = 0
        self.update_scoredboard()


    # def game_over(self):
    #     self.goto(-20, 0)
    #     self.write("GAME OVER")

    def increase_score(self):
        self.score += 1
        self.update_scoredboard()


