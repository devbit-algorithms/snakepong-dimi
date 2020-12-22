from sllist import SingleLinkedList
from pixel import _Pixel

class PongPaddle:
    def __init__(self, size, maxHeight):
        self.__maxHeight = maxHeight
        self.__size = size
        self.__pongPaddle = SingleLinkedList()
        for i in range(size):
            self.__pongPaddle.prepend(True)
        for i in range((maxHeight-size)//2):
            self.__pongPaddle.prepend(False)
        self.__just_moved = False
    
    def update(self, ball):
        self.__just_moved = not self.__just_moved
        if(self.__just_moved):
            copy = self.__pongPaddle.copy()
            middle_y = copy.size() - (self.__size//2)
            if(middle_y < ball.y() and copy.size() < self.__maxHeight):
                self.__pongPaddle.prepend(False)
            elif(middle_y > ball.y() and copy.size() > self.__size+1):
                self.__pongPaddle = self.__pongPaddle.tail()

    def has_ball_collision(self, ball):
        return (ball.x() == 2
        and self.__pongPaddle.size() > ball.y()
        and self.__pongPaddle.size()-self.__size < ball.y())
    
    def draw(self, canvas):
        pongPaddle = self.__pongPaddle.copy()
        y = 0
        while(pongPaddle.head() is not None):
            if(pongPaddle.head()):
                _Pixel(2, y, '|').draw(canvas)
            y = y+1
            pongPaddle = pongPaddle.tail()