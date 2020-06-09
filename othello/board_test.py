from board import Board


def test_constructer():
    bd = Board(0)
    assert bd.size == 0
    bd = Board(2)
    assert bd.size == 2
    assert bd.occupy["black"] == []
    assert bd.occupy["white"] == []
    assert bd.occupy["empty"] == [(0, 0), (1, 0), (0, 1), (1, 1)]
    bd = Board(4)
    assert bd.size == 4
    assert bd.occupy["black"] == []
    assert bd.occupy["white"] == []
    assert bd.occupy["empty"] == [(0, 0), (1, 0), (2, 0), (3, 0),
                                  (0, 1), (1, 1), (2, 1), (3, 1),
                                  (0, 2), (1, 2), (2, 2), (3, 2),
                                  (0, 3), (1, 3), (2, 3), (3, 3)]


def test_initial_tile():
    bd = Board(2)
    bd.initial_tile()
    assert bd.occupy["black"] == [(0, 1), (1, 0)]
    assert bd.occupy["white"] == [(0, 0), (1, 1)]
    assert bd.occupy["empty"] == []
    bd = Board(4)
    bd.initial_tile()
    assert bd.size == 4
    assert bd.occupy["black"] == [(1, 2), (2, 1)]
    assert bd.occupy["white"] == [(1, 1), (2, 2)]
    assert bd.occupy["empty"] == [(0, 0), (1, 0), (2, 0), (3, 0),
                                  (0, 1), (3, 1),
                                  (0, 2), (3, 2),
                                  (0, 3), (1, 3), (2, 3), (3, 3)]


def test_is_empty():
    bd = Board(2)
    assert bd.is_empty() is False
    bd.initial_tile()
    assert bd.is_empty() is True


def test_put_tile():
    bd = Board(2)
    bd.put_tile("black", (0, 1))
    assert (0, 1) in bd.occupy["black"]
    assert (0, 1) not in bd.occupy["empty"]


def test_flip():
    bd = Board(4)
    bd.initial_tile()
    bd.put_tile("black", (0, 1))
    assert (1, 1) in bd.occupy["white"]
    bd.flip("black", (0, 1), "white")
    assert (1, 1) in bd.occupy["black"]


def test_check_who_wins():
    bd = Board(2)
    bd.put_tile("black", (0, 0))
    bd.put_tile("black", (0, 1))
    bd.put_tile("black", (1, 0))
    bd.put_tile("white", (1, 1))
    res = bd.check_who_wins()
    assert res == ["You win", 3, 1]


def test_is_legal():
    bd = Board(4)
    bd.initial_tile()
    assert bd.is_legal((0, 2), "black", "white") is False
    assert bd.is_legal((0, 1), "black", "white") is True
    assert bd.is_legal((1, 1), "black", "white") is False
    assert bd.is_legal((5, 4), "black", "white") is False
