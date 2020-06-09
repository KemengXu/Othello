from player import Player
from game_controller import GameController
from board import Board
from helper import Helper

WIDTH = 400
HIGHT = 400
SIZE = 4
res = None
DELAY = 1024

p1 = Player("black")
p2 = Player("white")
bd = Board(SIZE)
bd.initial_tile()
gc = GameController(p1, p2, bd)
hp = Helper()


def setup():
    size(WIDTH, HIGHT)
    colorMode(RGB, 1)
    textAlign(CENTER)
    hp.set_bg_and_line(SIZE, WIDTH, HIGHT)
    bd.display(p1, p2)


def draw():
    global res
    if gc.check_p1() is False:
        gc.p1_turn = False  # bacause p1 has no legal move
    if res is not None:
        hp.record(res)
    else:
        res = hp.check_show_results(gc, WIDTH)
    if gc.p1_turn is False:
        delay(DELAY)
        gc.p2_move()
    gc.p1_turn = True  # it is set False after p2 makes a move


def mousePressed():
    hp.mouse_event(SIZE, p1, p2, gc, bd)
