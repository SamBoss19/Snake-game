from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Cambria",20,"normal")
class Score (Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as doc:
            self.highscore = int(doc.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,315)
        self.hideturtle()
        # self.shape("none")
        self.write(f"Score: {self.score} High Score: {self.highscore}", move = False, align = ALLIGNMENT, font = FONT )
    def increase(self):
        self.clear()
        self.score += 1  
        # print(self.score)
        self.write(f"Score: {self.score}  High Score: {self.highscore}", move = False, align = ALLIGNMENT, font = FONT)
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"Gameover.", move = False, align = ALLIGNMENT, font = ("Cambria",20,"normal"))

    def reset(self):
        if self.score >self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as doc:
                doc.write(f"{self.highscore}")
        
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", move = False, align = ALLIGNMENT, font = FONT)

    # def reset(self):
    #     self.clear()
        # highscore()

