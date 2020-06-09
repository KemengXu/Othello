from game_controller import GameController
from board import Board
from player import Player


def test_constructer():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(2)
    gc = GameController(p1, p2, bd)
    assert gc.p1.color == "black"
    assert gc.p2.color == "white"
    assert gc.bd.size == 2
    assert gc.p1_turn is True


"""
# to run this, need to comment out p1.display() in game_controller
def test_p1_move():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(4)
    bd.initial_tile()
    gc = GameController(p1, p2, bd)
    gc.p1_move((50, 180))
    assert len(gc.bd.occupy["empty"]) == 11
    assert (0, 1) in gc.bd.occupy["black"]
    assert (1, 1) in gc.bd.occupy["black"]  # flipped
    assert gc.p1_turn is False
    gc.p1_move((110, 170))    # click on a already_existed tile
    assert len(gc.bd.occupy["empty"]) == 11
    assert gc.p1_turn is False


# to run this, need to comment out p2.display() in game_controller
def test_p2_move():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(4)
    bd.initial_tile()
    gc = GameController(p1, p2, bd)
    gc.p1_move((50, 180))
    gc.p2_move()
    assert len(gc.bd.occupy["white"]) == 3
    assert len(gc.bd.occupy["black"]) == 3
"""
# check_res() concerns only with graphics


def test_check_p1():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(4)
    bd.initial_tile()
    gc = GameController(p1, p2, bd)
    assert gc.check_p1() is True
    bd = Board(2)
    bd.initial_tile()
    gc = GameController(p1, p2, bd)
    assert gc.check_p1() is False
