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


def init_rules(size):
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
           (1, 1, 1, 1, 1, 4, 1, 3, ),
                 (2, 1, 1, 1, 2, 5, ),
                 (3, 2, 2, 6, 3, 1, ),
                 (1, 9, 1, 1, 2, 1, ),
                 (2, 1, 2, 2, 3, 1, ),
              (3, 1, 1, 1, 1, 5, 1, ),
                       (1, 2, 2, 5, ),
              (7, 1, 2, 1, 1, 1, 3, ),
              (1, 1, 2, 1, 2, 2, 1, ),
                 (1, 3, 1, 4, 5, 1, ),
                 (1, 3, 1, 3, 10,2, ),
                 (1, 3, 1, 1, 6, 6, ),
                 (1, 1, 2, 1, 1, 2, ),
                    (7, 2, 1, 2, 5, ),
    )

    col_rules = (
                    (7, 2, 1, 1, 7, ),
                 (1, 1, 2, 2, 1, 1, ),
        (1, 3, 1, 3, 1, 3, 1, 3, 1, ),
           (1, 3, 1, 1, 5, 1, 3, 1, ),
           (1, 3, 1, 1, 4, 1, 3, 1, ),
                 (1, 1, 1, 2, 1, 1, ),
              (7, 1, 1, 1, 1, 1, 7, ),
                          (1, 1, 3, ),
              (2, 1, 2, 1, 8, 2, 1, ),
           (2, 2, 1, 2, 1, 1, 1, 2, ),
                    (1, 7, 3, 2, 1, ),
           (1, 2, 3, 1, 1, 1, 1, 1, ),
                    (4, 1, 1, 2, 6, ),
              (3, 3, 1, 1, 1, 3, 1, ),
                    (1, 2, 5, 2, 2, ),
        (2, 2, 1, 1, 1, 1, 1, 2, 1, ),
              (1, 3, 3, 2, 1, 8, 1, ),
                          (6, 2, 1, ),
                 (7, 1, 4, 1, 1, 3, ),
                    (1, 1, 1, 1, 4, ),
                 (1, 3, 1, 3, 7, 1, ),
        (1, 3, 1, 1, 1, 2, 1, 1, 4, ),
                 (1, 3, 1, 4, 3, 3, ),
              (1, 1, 2, 2, 2, 6, 1, ),
                 (7, 1, 3, 2, 1, 1, ),
    )

    assert len(row_rules) == size
    assert len(col_rules) == size

    for row in row_rules:
        assert sum(row) <= size

    for row in col_rules:
        assert sum(row) <= size

    return row_rules, col_rules


def iterate_row(row, rules):

    rule_spaces = len(rules) - 1
    rule_unknowns = len(row) - sum(rules) - rule_spaces

    if rule_unknowns == 0:
        # no unknowns fit, fill in the whole row
        x = 0
        for set_length in rules:
            for set_x in range(set_length):
                row[x] = True
                x += 1

            if x < len(row):
                # blanks
                row[x] = False
                x += 1

    return row


def iterate_board(board, row_rules, col_rules):

    for i, row in enumerate(board):
        board[i] = iterate_row(row, row_rules[i])

    board = transpose_board(board)

    for i, row in enumerate(board):
        board[i] = iterate_row(row, col_rules[i])

    board = transpose_board(board)

    return board


if __name__ == "__main__":
    board = init_board(BOARD_SIZE)
    row_rules, col_rules = init_rules(BOARD_SIZE)

    #print_board(board)
    #print('------------')
    #board = transpose_board(board)
    #print_board(board)
    #print('------------')
    #board = transpose_board(board)
    #print_board(board)


    board = iterate_board(board, row_rules, col_rules)

    print_board(board)