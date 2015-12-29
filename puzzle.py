# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from print import print_board
from cell_values import CELL_UNKNOWN, CELL_EMPTY, CELL_FILLED

BOARD_SIZE = 25


def init_row(board, y, row_str):
    assert len(row_str) == len(board[y])
    assert set(list(row_str)) <= set([CELL_UNKNOWN, CELL_EMPTY, CELL_FILLED])

    board[y] = row_str

    return board


def init_board(size):
    board = [ CELL_UNKNOWN * size for row in range(size)]

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


def get_possible_values(row , rules, x):
    rule_spaces = len(rules) - 1
    rule_unknowns = len(row) - sum(rules) - rule_spaces

    rule_parts = []



    possibles = set()

    if x < rule_unknowns:
        possibles.add(None)

def iterate_row(row, rules):
    row = list(row)
    rule_spaces = len(rules) - 1
    rule_unknowns = len(row) - sum(rules) - rule_spaces

    if rule_unknowns == 0:
        # no unknowns fit, fill in the whole row
        x = 0
        for set_length in rules:
            for set_x in range(set_length):
                row[x] = CELL_FILLED
                x += 1

            if x < len(row):
                # blanks
                row[x] = CELL_EMPTY
                x += 1
    else:
        for x, v in enumerate(row):
            if v is not None:
                # already known
                continue

            possible = get_possible_values(row, rules, x)

            if len(possible) == 1:
                row[x] = possible[0]

    row = ''.join(row)

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