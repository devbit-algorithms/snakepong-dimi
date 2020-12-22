from direction import _Direction, _Direction_check_result, _check_direction

def test_check_direction_same():
    assert _check_direction(_Direction.UP, _Direction.UP) == _Direction_check_result.SAME
    assert _check_direction(_Direction.DOWN, _Direction.DOWN) == _Direction_check_result.SAME
    assert _check_direction(_Direction.LEFT, _Direction.LEFT) == _Direction_check_result.SAME
    assert _check_direction(_Direction.RIGHT, _Direction.RIGHT) == _Direction_check_result.SAME
    assert _check_direction(_Direction.LEFTUP, _Direction.LEFTUP) == _Direction_check_result.SAME
    assert _check_direction(_Direction.LEFTDOWN, _Direction.LEFTDOWN) == _Direction_check_result.SAME
    assert _check_direction(_Direction.RIGHTUP, _Direction.RIGHTUP) == _Direction_check_result.SAME
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.RIGHTDOWN) == _Direction_check_result.SAME

def test_check_direction_opposite():
    assert _check_direction(_Direction.LEFT, _Direction.RIGHT) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.RIGHT, _Direction.LEFT) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.UP, _Direction.DOWN) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.DOWN, _Direction.UP) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.LEFTUP, _Direction.RIGHTDOWN) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.LEFTUP) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.LEFTDOWN, _Direction.RIGHTUP) == _Direction_check_result.OPPOSITE
    assert _check_direction(_Direction.RIGHTUP, _Direction.LEFTDOWN) == _Direction_check_result.OPPOSITE

def test_check_direction_ok():
    assert _check_direction(_Direction.LEFT, _Direction.UP) == _Direction_check_result.OK
    assert _check_direction(_Direction.LEFT, _Direction.DOWN) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHT, _Direction.UP) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHT, _Direction.DOWN) == _Direction_check_result.OK
    assert _check_direction(_Direction.UP, _Direction.LEFT) == _Direction_check_result.OK
    assert _check_direction(_Direction.UP, _Direction.RIGHT) == _Direction_check_result.OK
    assert _check_direction(_Direction.DOWN, _Direction.LEFT) == _Direction_check_result.OK
    assert _check_direction(_Direction.DOWN, _Direction.RIGHT) == _Direction_check_result.OK
    assert _check_direction(_Direction.LEFTUP, _Direction.LEFTDOWN) == _Direction_check_result.OK
    assert _check_direction(_Direction.LEFTUP, _Direction.RIGHTUP) == _Direction_check_result.OK
    assert _check_direction(_Direction.LEFTDOWN, _Direction.LEFTUP) == _Direction_check_result.OK
    assert _check_direction(_Direction.LEFTDOWN, _Direction.RIGHTDOWN) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHTUP, _Direction.LEFTUP) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHTUP, _Direction.RIGHTDOWN) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.RIGHTUP) == _Direction_check_result.OK
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.LEFTDOWN) == _Direction_check_result.OK

def test_check_direction_invalid():
    assert _check_direction(_Direction.LEFT, _Direction.LEFTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFT, _Direction.LEFTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFT, _Direction.RIGHTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFT, _Direction.RIGHTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHT, _Direction.LEFTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHT, _Direction.LEFTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHT, _Direction.RIGHTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHT, _Direction.RIGHTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.UP, _Direction.LEFTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.UP, _Direction.LEFTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.UP, _Direction.RIGHTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.UP, _Direction.RIGHTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.DOWN, _Direction.LEFTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.DOWN, _Direction.LEFTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.DOWN, _Direction.RIGHTDOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.DOWN, _Direction.RIGHTUP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTUP, _Direction.LEFT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTUP, _Direction.RIGHT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTUP, _Direction.DOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTUP, _Direction.UP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTDOWN, _Direction.LEFT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTDOWN, _Direction.RIGHT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTDOWN, _Direction.DOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.LEFTDOWN, _Direction.UP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTUP, _Direction.LEFT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTUP, _Direction.RIGHT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTUP, _Direction.DOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTUP, _Direction.UP) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.LEFT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.RIGHT) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.DOWN) == _Direction_check_result.INVALID
    assert _check_direction(_Direction.RIGHTDOWN, _Direction.UP) == _Direction_check_result.INVALID


