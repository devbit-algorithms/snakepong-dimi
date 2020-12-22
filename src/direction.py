from enum import IntEnum

class _Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    LEFTUP = 4
    LEFTDOWN = 5
    RIGHTUP = 6
    RIGHTDOWN = 7


class _Direction_check_result(IntEnum):
    OK = 0
    SAME = 1
    OPPOSITE = 2
    INVALID = 3    


def _check_direction(direction1, direction2):
    if ((not (isinstance(direction1, _Direction) and isinstance(direction2, _Direction)))
    or (int(direction1)<4 and int(direction2)>3)
    or (int(direction2)<4 and int(direction1)>3)):
        return _Direction_check_result.INVALID

    if (direction1 == direction2):
        return _Direction_check_result.SAME

    elif ((direction1 == _Direction.LEFT and direction2 == _Direction.RIGHT)
    or (direction1 == _Direction.RIGHT and direction2 == _Direction.LEFT)
    or (direction1 == _Direction.UP and direction2 == _Direction.DOWN)
    or (direction1 == _Direction.DOWN and direction2 == _Direction.UP)
    or (direction1 == _Direction.LEFTUP and direction2 == _Direction.RIGHTDOWN)
    or (direction1 == _Direction.RIGHTDOWN and direction2 == _Direction.LEFTUP)
    or (direction1 == _Direction.LEFTDOWN and direction2 == _Direction.RIGHTUP)
    or (direction1 == _Direction.RIGHTUP and direction2 == _Direction.LEFTDOWN)
    ):
        return _Direction_check_result.OPPOSITE

    else:
        return _Direction_check_result.OK