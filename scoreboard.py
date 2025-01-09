from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            self.high_s = file.read()
        self.highscore = self.high_s

    def score_display(self, tot_score):
        self.clear()
        self.goto(0, 200)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.high_score(tot_score)
        self.write(f"Score: {tot_score}  High score: {self.highscore}", align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.write(f"GAME OVER", align="center", move=False, font=('Arial', 24, 'normal'))

    def high_score(self, tot_score):
        if tot_score > int(self.highscore):
            self.highscore = tot_score
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.highscore}")

    def reset(self):
        self.clear()
        self.score_display(tot_score=0)
