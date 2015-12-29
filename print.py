# -*- coding: utf-8 -*-

from __future__ import print_function


def print_board(board):
    display = {
        False: ' ',
        True: '#',
        None: '?',
    }

    for row in board:
        row_letters = [display[c] for c in row]
        print(*row_letters)
