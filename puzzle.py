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


def transpose_board(board):
    transposed_board = [[ board[x][y] for x in range(len(board[y]))  ] for y in range(len(board))]

    return transposed_board


def init_rules():
    row_rules = (
                    (7, 3, 1, 1, 7, ),
                 (1, 1, 2, 2, 1, 1, ),
           (1, 3, 1, 3, 1, 1, 3, 1, ),
           (1, 3, 1, 1, 6, 1, 3, 1, ),
           (1, 3, 1, 5, 2, 1, 3, 1, ),
                    (1, 1, 2, 1, 1, ),
              (7, 1, 1, 1, 1, 1, 7, ),
                             (3, 3, ),
        (1, 2, 3, 1, 1, 3, 1, 1, 2, ),
                 (1, 1, 3, 2, 1, 1, ),
                 (4, 1, 4, 2, 1, 2, ),
        # ...
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
    )

    col_rules = (
    )

    return row_rules, col_rules


def iterate_row(row, rules):
    return row


def iterate_board(board, row_rules, col_rules):

    for i, row in enumerate(board):
        #print(i, row)
        #print(row_rules[i])
        board[i] = iterate_row(row, row_rules[i])

    return board


if __name__ == "__main__":
    board = init_board(BOARD_SIZE)
    row_rules, col_rules = init_rules()

    #print_board(board)
    #print('------------')
    #board = transpose_board(board)
    #print_board(board)
    #print('------------')
    #board = transpose_board(board)
    #print_board(board)


    board = iterate_board(board, row_rules, col_rules)

    print_board(board)