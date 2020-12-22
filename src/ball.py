from pixel import _Pixel
from direction import _Direction
import random

class Ball(_Pixel):
    def __init__(self, x, y, direction = None):
        super().__init__(x, y, '*')
        if(isinstance(direction, _Direction) and int(direction)>3):
            self.__direction = direction
        else:
            self.__direction = _Direction(random.randint(4,7))
    
    def direction(self):
        return self.__direction
    def random_direction(self):
        original_direction = self.direction
        new_direction = original_direction
        while(new_direction == original_direction):
            new_direction = _Direction(random.randint(4,7))
        self.__direction = new_direction
    
    def update(self):
        if(self.direction() == _Direction.LEFTUP):
            return Ball(self.left_up().x(), self.left_up().y(), self.direction())
        elif(self.direction() == _Direction.LEFTDOWN):
            return Ball(self.left_down().x(), self.left_down().y(), self.direction())
        elif(self.direction() == _Direction.RIGHTUP):
            return Ball(self.right_up().x(), self.right_up().y(), self.direction())
        elif(self.direction() == _Direction.RIGHTDOWN):
            return Ball(self.right_down().x(), self.right_down().y(), self.direction())