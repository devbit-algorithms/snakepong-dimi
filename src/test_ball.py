from ball import Ball, _Direction

def test_ball_random_direction():
    ball = Ball(5, 5)
    direction = ball.direction()
    ball.random_direction()
    assert ball.direction() != direction

def test_ball_update_left_up():
    ball = Ball(5, 5, _Direction.LEFTUP)
    updated_ball = ball.update()
    assert updated_ball != ball
    assert updated_ball.x() == ball.x()-1
    assert updated_ball.y() == ball.y()-1

def test_ball_update_left_down():
    ball = Ball(5, 5, _Direction.LEFTDOWN)
    updated_ball = ball.update()
    assert updated_ball != ball
    assert updated_ball.x() == ball.x()-1
    assert updated_ball.y() == ball.y()+1

def test_ball_update_right_up():
    ball = Ball(5, 5, _Direction.RIGHTUP)
    updated_ball = ball.update()
    assert updated_ball != ball
    assert updated_ball.x() == ball.x()+1
    assert updated_ball.y() == ball.y()-1

def test_ball_update_right_down():
    ball = Ball(5, 5, _Direction.RIGHTDOWN)
    updated_ball = ball.update()
    assert updated_ball != ball
    assert updated_ball.x() == ball.x()+1
    assert updated_ball.y() == ball.y()+1