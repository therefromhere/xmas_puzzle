# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals


def print_board(board):
    display = {
        False: '  ',
        True: "\u2588\u2588",
        None: '[]',
    }

    for row in board:
        row_letters = [display[c] for c in row]
        print(*row_letters, sep='')
