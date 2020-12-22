import sys
import os
from game import Game

os.system('clear')
print("keys to move the snake:")
print("*********")
print("*   z   *")
print("* q s d *")
print("*********")
print("")
print("to stop the game, press space")
print("")
print("Press enter to start")
sys.stdin.readline()

game = Game()
while not game.is_over():
    char = sys.stdin.read(1) # reads one byte at a time, similar to getchar()
    if char == 'z':
        game.move_up()
    elif char == 's':
        game.move_down()
    elif char == 'q':
        game.move_left()
    elif char == 'd':
        game.move_right()
    elif char == ' ':
        print('Score = ' + str(game.score()))
        exit()
print('GAME OVER')
print('Score = ' + str(game.score()))
