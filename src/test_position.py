from position import _Position

def test_position():
    position = _Position(1,2)
    assert position.x() == 1
    assert position.y() == 2