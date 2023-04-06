from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Cambria",20,"normal")
class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,315)
        self.hideturtle()
        # self.shape("none")
        self.write(f"Score: {self.score}", move = False, align = ALLIGNMENT, font = FONT )
    def increase(self):
        self.clear()
        self.score += 1  
        print(self.score)
        self.write(f"Score: {self.score}", move = False, align = ALLIGNMENT, font = FONT)
    def gameover(self):
        self.goto(0,0)
        self.write(f"Gameover.", move = False, align = ALLIGNMENT, font = ("Cambria",20,"normal"))
