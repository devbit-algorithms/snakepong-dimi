from position import _Position

class _Pixel(_Position):
    def __init__(self, x, y, representation):
        super().__init__(x, y)
        self.__representation = representation 

    def representation(self):
        return self.__representation

    def up(self):
        return _Pixel(self.x(), self.y()-1, self.representation())
    def down(self):
        return _Pixel(self.x(), self.y()+1, self.representation())
    def left(self):
        return _Pixel(self.x()-1, self.y(), self.representation())
    def right(self):
        return _Pixel(self.x()+1, self.y(), self.representation())
    def left_up(self):
        return self.left().up()
    def left_down(self):
        return self.left().down()
    def right_up(self):
        return self.right().up()
    def right_down(self):
        return self.right().down()

    def draw(self, canvas):
        canvas.draw(self)