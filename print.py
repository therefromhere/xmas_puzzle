# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from cell_values import CELL_UNKNOWN, CELL_EMPTY, CELL_FILLED


NEGATIVE = True

display = {
    CELL_EMPTY: '  ',
    CELL_FILLED: "\u2588\u2588",
    CELL_UNKNOWN: '[]',
}

if NEGATIVE:
    display[CELL_EMPTY], display[CELL_FILLED] = display[CELL_FILLED], display[CELL_EMPTY]


def print_board(board):
    for row in board:
        row_letters = [display[c] for c in row]
        print(*row_letters, sep='')
