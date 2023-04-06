from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        randx = random.randint(-320,320)
        randy = random.randint(-320,320)
        self.goto(randx, randy)