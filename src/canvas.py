from pixel import _Pixel
import os

class Canvas:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__canvas = [[' ' for x in range(width)] for y in range(height)]
        self.clear()

    def width(self):
        return self.__width
    def height(self):
        return self.__height

    def clear(self):
        for y in range(self.height()):
            for x in range(self.width()):
                self.__canvas[y][x] = ' '

    def draw(self, pixel):
        self.__canvas[pixel.y()][pixel.x()] = pixel.representation()

    def show(self):
        os.system('clear')
        for y in range(self.height()):
            for x in range(self.width()):
                print(self.__canvas[y][x], end='')
            print('')
        print('')