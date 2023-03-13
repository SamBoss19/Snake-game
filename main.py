from turtle import Turtle, Screen
import time
screen = Screen()
# screen.setup(width = 700, height= 700)
# screen.bgcolor("black")
# screen.tracer(0)
# screen.title("Snake Xenzia")


# snakes = []
# start = [(0,0), (-20,0), (-40,0)]
# for i  in start:
#     snake = Turtle()
#     snake.penup()
#     snake.shape("square")
#     snake.color("white")
#     snake.goto(i)
#     snakes.append(snake)

# game_on = True
# while game_on:
#     screen.update()
#     time.sleep(0.1)
#     for object in range(len(snakes)-1, 0, -1):
#         newx = snakes[object - 1].xcor()
#         newy = snakes[object - 1].ycor()
#         snakes[object].goto(newx,newy)
#     snakes[0].forward(20)
#     snakes[0].right(20)

  
from snake import Snake        
        
snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.6)
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")










# screen.exitonclick()