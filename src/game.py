from ball import Ball
from wall import Wall
from snake import Snake
from canvas import Canvas
from pongpaddle import PongPaddle
import random

class Game:
    def __init__(self, height = 0, width = 0):
        if(height<10):
            height = 10
        if(width<20):
            width = 20
        height = height+2   #borders
        width = width+2     #borders
        self.__height = height
        self.__width = width
        self.__snake = Snake((width-2)//2, height//2, 5)
        self.__pongPaddle = PongPaddle(4, height)
        self.__ball = Ball(random.randint(3,width-2), random.randint(1, height-2))
        self.__create_walls()
        self.__canvas = Canvas(height, width)
        self.__is_over = False
        self.__score = 0
        self.__render()

    def width(self):
        return self.__width
    def height(self):
        return self.__height
    
    def is_over(self):
        return self.__is_over

    def score(self):
        return self.__score

    def __render(self):
        self.__canvas.clear()
        for wall in self.__walls:
            wall.draw(self.__canvas)
        self.__snake.draw(self.__canvas)
        self.__pongPaddle.draw(self.__canvas)
        self.__ball.draw(self.__canvas)
        self.__canvas.show()
    
    def __update(self):
        if(not self.is_over()):
            self.__update_snake()
            self.__update_ball()
            if(self.__scored()):
                self.__snake.grow()
            if(self.__ball.x()>2):
                self.__update_pongPaddle()

    def __update_snake(self):
        self.__snake.update()
        if(self.__snake.cut_itself() or self.__snake_goes_outside()):
            self.__is_over = True
    def __update_ball(self):
        while(self.__ball_vs_snake_collision()
        or self.__ball_vs_pongPaddle_collision()
        or self.__ball_goes_outside()
        ):
            self.__ball.random_direction()
        self.__ball = self.__ball.update()
    def __update_pongPaddle(self):
        self.__pongPaddle.update(self.__ball)

    def __ball_vs_snake_collision(self):
        return (self.__snake.has_ball_collision(self.__ball.update()))
    def __ball_vs_pongPaddle_collision(self):
        return (self.__pongPaddle.has_ball_collision(self.__ball.update()))
    def __ball_goes_outside(self):
        ball = self.__ball.update()
        return (ball.x()<1 or ball.x()>self.width()-2 or ball.y()<1 or ball.y()>self.height()-2)
    def __snake_goes_outside(self):
        head = self.__snake.head()
        return (head.x()<3 or head.x()>self.width()-2 or head.y()<1 or head.y()>self.height()-2)
    def __scored(self):
        if(self.__ball.x() < 2):
            self.__score = self.__score+1
            return True
        return False

    def __create_walls(self):
        self.__walls = []
        for x in range(self.width()):
            self.__walls.append(Wall(x, 0))
            self.__walls.append(Wall(x, self.height()-1))
        for y in range(1, self.height()):
            self.__walls.append(Wall(0, y))
            self.__walls.append(Wall(self.width()-1, y))

    def move_left(self):
        self.__snake.try_set_direction_left()
        self.__update()
        self.__render()
    def move_right(self):
        self.__snake.try_set_direction_right()
        self.__update()
        self.__render()
    def move_up(self):
        self.__snake.try_set_direction_up()
        self.__update()
        self.__render()
    def move_down(self):
        self.__snake.try_set_direction_down()
        self.__update()
        self.__render()


