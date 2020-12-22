from pixel import _Pixel

def test_pixel_init():
    pixel = _Pixel(1,2, '.')
    assert pixel.x() == 1
    assert pixel.y() == 2
    assert pixel.representation() == '.'

def test_pixel_up():
    pixel = _Pixel(5, 5, '.')
    up = pixel.up()
    assert pixel.x() == up.x()
    assert pixel.y() == up.y()+1
    assert pixel.representation() == up.representation()

def test_pixel_down():
    pixel = _Pixel(5, 5, '.')
    down = pixel.down()
    assert pixel.x() == down.x()
    assert pixel.y() == down.y()-1
    assert pixel.representation() == down.representation()

def test_pixel_left():
    pixel = _Pixel(5, 5, '.')
    left = pixel.left()
    assert pixel.x() == left.x()+1
    assert pixel.y() == left.y()
    assert pixel.representation() == left.representation()

def test_pixel_right():
    pixel = _Pixel(5, 5, '.')
    right = pixel.right()
    assert pixel.x() == right.x()-1
    assert pixel.y() == right.y()
    assert pixel.representation() == right.representation()

def test_pixel_left_up():
    pixel = _Pixel(5, 5, '.')
    left_up = pixel.left_up()
    assert pixel.x() == left_up.x()+1
    assert pixel.y() == left_up.y()+1
    assert pixel.representation() == left_up.representation()

def test_pixel_left_down():
    pixel = _Pixel(5, 5, '.')
    left_down = pixel.left_down()
    assert pixel.x() == left_down.x()+1
    assert pixel.y() == left_down.y()-1
    assert pixel.representation() == left_down.representation()

def test_pixel_right_up():
    pixel = _Pixel(5, 5, '.')
    right_up = pixel.right_up()
    assert pixel.x() == right_up.x()-1
    assert pixel.y() == right_up.y()+1
    assert pixel.representation() == right_up.representation()

def test_pixel_right_down():
    pixel = _Pixel(5, 5, '.')
    right_down = pixel.right_down()
    assert pixel.x() == right_down.x()-1
    assert pixel.y() == right_down.y()-1
    assert pixel.representation() == right_down.representation()
