from turtle import Turtle, Screen
import time
START = [(0,0), (-20,0), (-40,0)]
screen = Screen()
class Snake:
    def __init__(self):
        self.snakes = []
        self.makesnake()

    def makesnake(self):
        from turtle import Turtle, Screen
        import time
        
        screen.setup(width = 700, height= 700)
        screen.bgcolor("black")
        screen.tracer(0)
        screen.title("Snake Xenzia")
        
        for i  in START:
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(i)
            snake.speed(3)
            self.snakes.append(snake)
        
    def move(self):
       
        for object in range(len(self.snakes)-1, 0, -1):
            newx = self.snakes[object - 1].xcor()
            newy = self.snakes[object - 1].ycor()
            self.snakes[object].goto(newx,newy)
            
            self.snakes[0].forward(20)
            # self.snakes[0].right(20)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)
        # self.snakes[0].degrees(90)
        # self.snakes[0].forward(20)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)
        # self.snakes[0].forward(20)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(360)
        # self.snakes[0].forward(20)

    def left(self):
        if self.snakes[0].heading() != 360:
            self.snakes[0].setheading(180)
        
            




        screen.exitonclick


