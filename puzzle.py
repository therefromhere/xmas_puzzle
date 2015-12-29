# -*- coding: utf-8 -*-

from __future__ import print_function
from print import print_board

BOARD_SIZE = 25


def init_row(board, y, row_str):
    assert len(row_str) == len(board[y])

    decode = {
        '.': None,
        'X': True,
    }

    board[y] = [ decode[cell] for cell in row_str ]

    return board


def init_board(size):
    board = [[ None for col in range(size) ] for row in range(size)]

    board = init_row(board, 3,  '...XX.......XX.......X...')
    board = init_row(board, 8,  '......XX..X...XX..X......')
    board = init_row(board, 16, '......X....X....X...X....')
    board = init_row(board, 21, '...XX....XX....X....XX...')

    return board


if __name__ == "__main__":
    board = init_board(BOARD_SIZE)

    print_board(board)