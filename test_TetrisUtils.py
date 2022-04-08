import TetrisUtils

board1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]]

board2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]]

board3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 6, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 6, 0, 0, 1, 0, 4, 4, 4],
          [1, 1, 1, 0, 6, 0, 0, 1, 0, 4, 0, 0]]

"""
NB: Tetris Utils counts row and column with the constants GRID_ROW/COL_ROUND so we must
change it by len(board) and len(board[0]) respectively when we need to launch the test
methods, otherwise we have an index error.
"""


def test_get_hollow_column_count():
    assert TetrisUtils.get_hollow_column_count(board1) == 1
    assert TetrisUtils.get_hollow_column_count(board2) == 4
    assert TetrisUtils.get_hollow_column_count(board3) == 4


def test_get_row_transition():
    assert TetrisUtils.get_row_transition(board1) == 9
    assert TetrisUtils.get_row_transition(board2) == 14
    assert TetrisUtils.get_row_transition(board3) == 18


def test_get_row_transition_from_top():
    assert TetrisUtils.get_row_transition_from_top(board1) == 9
    assert TetrisUtils.get_row_transition_from_top(board2) == 14
    assert TetrisUtils.get_row_transition_from_top(board3) == 18


def test_get_col_transition():
    assert TetrisUtils.get_col_transition(board1) == 7
    assert TetrisUtils.get_col_transition(board2) == 14
    assert TetrisUtils.get_col_transition(board3) == 16


def test_get_pit_count():
    assert TetrisUtils.get_pit_count(board1) == 6
    assert TetrisUtils.get_pit_count(board2) == 2
    assert TetrisUtils.get_pit_count(board3) == 2
