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
        self.createsnake()
        
    def createsnake(self):
        for i  in START:
            self.add_body(i)
            
    def add_body(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        snake.speed("fastest")
        self.snakes.append(snake)
    def extend(self):
        self.add_body(self.snakes[-1].position())
            
    def move(self):
       
        for object in range(len(self.snakes)-1, 0, -1):
            newx = self.snakes[0].xcor()
            newy = self.snakes[0].ycor()
            self.snakes[object].goto(newx,newy)
            
            self.snakes[0].forward(10)
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

    def reset(self):
        
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.createsnake()
        self.snakes[0].forward(10)
        
            




        screen.exitonclick


