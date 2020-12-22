from pixel import _Pixel

class Wall(_Pixel):
    def __init__(self, x, y):
        super().__init__(x, y, '#')