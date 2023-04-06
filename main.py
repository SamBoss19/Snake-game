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
from food import Food  
from scoreboard import Score   
        
snake = Snake()
food = Food()
score = Score()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #dectect food
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()
   
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
     #detect wall
    if snake.snakes[0].xcor() > 330 or snake.snakes[0].xcor() < -330 or snake.snakes[0].ycor() > 330 or snake.snakes[0].ycor() < -330:
        game_on = False
        score.gameover()
    #detect tail
    for tail in snake.snakes[1:]:
        # if tail == snake.snakes[0]:
        #     pass
        if snake.snakes[0].distance(tail) < 10:
            game_on= False
            score.gameover()










screen.exitonclick()