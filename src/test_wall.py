from wall import Wall

def test_wall():
    wall = Wall(0, 1)
    assert wall.representation() == '#'
    assert wall.x() == 0
    assert wall.y() == 1