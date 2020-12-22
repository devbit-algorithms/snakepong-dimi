from pixel import _Pixel
from direction import _Direction, _Direction_check_result, _check_direction
from dllist import DoubleLinkedList
import random

class Snake:
    def __init__(self, x: int, y: int, startLength: int):
        self.__snake = DoubleLinkedList()
        pixel = _Pixel(x, y, 's')
        for i in range(startLength):
            self.__snake.addBack(pixel)
            pixel = pixel.right()
        self.__direction = _Direction(random.randint(0,2))
        self.__grow = False
    
    def direction(self):
        return self.__direction
    
    def head(self):
        return self.__snake.front()
    
    def draw(self, canvas):
        snake = self.__snake.copy()
        pixel = snake.removeFront()
        while(not pixel is None):
            pixel.draw(canvas)
            pixel = snake.removeFront()
    
    def grow(self):
        self.__grow = True

    def update(self):
        if(self.direction() == _Direction.LEFT):
            self.__snake.addFront(self.__snake.front().left())
        elif(self.direction() == _Direction.RIGHT):
            self.__snake.addFront(self.__snake.front().right())
        elif(self.direction() == _Direction.UP):
            self.__snake.addFront(self.__snake.front().up())
        elif(self.direction() == _Direction.DOWN):            
            self.__snake.addFront(self.__snake.front().down())
        if(not self.__grow):
            self.__snake.removeBack()
        self.__grow = False
    
    def cut_itself(self):
        copy = self.__snake.copy()
        front = copy.removeFront()
        body = copy.removeFront()
        while(body is not None):
            if(front.x() == body.x() and front.y() == body.y()):
                return True
            body = copy.removeFront()
        return False

    def try_set_direction_left(self):
        return self.__try_set_direction(_Direction.LEFT)
    def try_set_direction_right(self):
        return self.__try_set_direction(_Direction.RIGHT)
    def try_set_direction_up(self):
        return self.__try_set_direction(_Direction.UP)
    def try_set_direction_down(self):
        return self.__try_set_direction(_Direction.DOWN)

    def __try_set_direction(self, newDirection):
        if(_check_direction(self.direction(), newDirection) == _Direction_check_result.OK):
            self.__direction = newDirection
            return True
        return False

    def has_ball_collision(self, ball):
        snake = self.__snake.copy()
        snake_element = snake.removeFront()
        while(snake_element is not None):
            if(ball.x() == snake_element.x() and ball.y() == snake_element.y()):
                return True
            snake_element = snake.removeFront()
        return False