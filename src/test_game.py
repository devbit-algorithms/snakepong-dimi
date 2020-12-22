from game import Game

def test_game_init():
    game = Game(10,20)
    assert game.height() == 10+2
    assert game.width() == 20+2
    assert not game.is_over()
    assert game.score() == 0

def test_game_cut_itself__is_over():
    game = Game()
    game.move_up()
    game.move_right()
    game.move_down()
    game.move_left()
    game.move_up()
    assert game.is_over()