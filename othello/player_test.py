from player import Player
from board import Board


def test_constructer():
    p = Player("black")
    p.color = "black"


def test_check_next_step():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(4)
    bd.put_tile("black", (0, 0))
    bd.put_tile("black", (2, 0))
    bd.put_tile("white", (0, 1))
    bd.put_tile("white", (1, 1))
    assert p1.check_next_step(bd, "white") == (0, 2)  # next step for black
    bd.put_tile("black", (0, 2))
    bd.flip("black", (0, 2), "white")
    bd.put_tile("white", (1, 0))
    assert p2.check_next_step(bd, "black") == (3, 0)


def test_is_at_edge():
    p = Player("black")
    bd = Board(4)
    assert p.is_at_edge((3, 2), 4) is True
    assert p.is_at_edge((2, 2), 4) is False


def test_check_legal_move_exist():
    p1 = Player("black")
    p2 = Player("white")
    bd = Board(4)
    bd.put_tile("black", (0, 0))
    bd.put_tile("black", (2, 0))
    bd.put_tile("white", (0, 1))
    bd.put_tile("white", (1, 1))
    assert p1.check_legal_move_exist(bd, "white") is True
    bd.put_tile("black", (0, 2))
    bd.flip("black", (0, 2), "white")
    assert p2.check_legal_move_exist(bd, "black") is False
    bd.put_tile("white", (0, 3))
    assert p2.check_legal_move_exist(bd, "black") is False
