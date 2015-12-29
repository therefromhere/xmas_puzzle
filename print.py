# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

NEGATIVE = True

display = {
    False: '  ',
    True: "\u2588\u2588",
    None: '[]',
}

if NEGATIVE:
    display[False], display[True] = display[True], display[False]

def print_board(board):


    for row in board:
        row_letters = [display[c] for c in row]
        print(*row_letters, sep='')
