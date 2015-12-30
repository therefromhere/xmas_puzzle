# -*- coding: utf-8 -*-

from __future__ import print_function
from print import print_board
from iter import partition_buckets
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
    transposed_board = [''.join([ board[x][y] for x in range(len(board[y])) ]) for y in range(len(board))]

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


def rules_runlen_to_str(rules):
    """
    Convert from run length of filled blocks to strings
    Note that we append an empty block onto all but the last block,
    since we know an empty block separates each filled run

    >>> rules_runlen_to_str((2, 1, 3))
    ['XX-', 'X-', 'XXX']

    >>> rules_runlen_to_str((2, ))
    ['XX']

    :param rules: sequence of ints
    :return: list of strings
    """

    rules_str = []

    for i, run_len in enumerate(rules):
        run = CELL_FILLED * run_len
        if i + 1 != len(rules):
            run += CELL_EMPTY

        rules_str.append(run)

    return rules_str


def generate_rule_combinations(rules, size):
    """
    Generator that returns all possible patterns matching "rules"

    >>> sorted(generate_rule_combinations((2,1,), 5))
    ['-XX-X', 'XX--X', 'XX-X-']

    >>> sorted(generate_rule_combinations((5,), 5))
    ['XXXXX']

    :param rules: tuple of run lengths of filled cells - all other cells are guaranteed empty, eg (7, 3, 1, 1, 7,)
    :param size: length of row
    :return:
    """
    assert sum(rules) <= size
    initial_rules_parts = rules_runlen_to_str(rules)

    # iterate through possible locations of empty space

    # there's guaranteed to be an empty space between the filled sequences, this is handled by rules_runlen_to_str
    fixed_spaces = len(rules) - 1

    movable_spaces = size - sum(rules) - fixed_spaces

    # the spaces could be in any of these gaps (hence this is the bucket count)
    number_gaps = len(rules) + 1

    for partition in partition_buckets(movable_spaces, number_gaps):
        # insert spaces into gaps
        rules_parts = list(initial_rules_parts)
        offset = 0
        for i, space_len in enumerate(partition):

            if space_len != 0:
                space = CELL_EMPTY * space_len
                rules_parts.insert(i + offset, space)
                # account for change in index due to previous inserts
                offset += 1

        yield ''.join(rules_parts)


def generate_row_candidates(row, rules):
    """
    Given row and rules, generates potential solutions

    eg: nothing known
    >>> sorted(generate_row_candidates('.....', (2, 1)))
    ['-XX-X', 'XX--X', 'XX-X-']

    >>> sorted(generate_row_candidates('....X', (2, 1)))
    ['-XX-X', 'XX--X']

    :param row: string
    :param rules: tuple
    :return:
    """

    for candidate in generate_rule_combinations(rules, len(row)):
        clash = False
        for cell_values in zip(row, candidate):
            if CELL_FILLED in cell_values and CELL_EMPTY in cell_values:
                # clash, this candidate doesn't fit
                clash = True
                break

        if not clash:
            yield candidate


def iterate_row(row, rules):

    cell_candidates = [ set() for i in range(len(row))]
    old_num_unknown = row.count(CELL_UNKNOWN)

    for candidate in generate_row_candidates(row, rules):
        num_unknown = 0
        for i, value in enumerate(candidate):
            cell_candidates[i].add(value)

            if len(cell_candidates[i]) > 1:
                num_unknown += 1

        if num_unknown == old_num_unknown:
            # we don't know any more than before
            return row

    return ''.join([CELL_UNKNOWN if len(c) > 1 else list(c)[0] for c in cell_candidates])


def iterate_board(board, row_rules, col_rules):

    iteration = 0
    complete_rows = 0
    while complete_rows < len(board):
        complete_rows = 0
        for i, row in enumerate(board):
            if CELL_UNKNOWN not in row:
                complete_rows += 1
                continue

            board[i] = iterate_row(row, row_rules[i])
            iteration += 1

            print_board(board, row_marker=i)
            print("-------------------------", iteration, complete_rows)


        board = transpose_board(board)

        for i, row in enumerate(board):
            if CELL_UNKNOWN not in row:
                continue

            board[i] = iterate_row(row, col_rules[i])

            board = transpose_board(board)
            iteration += 1

            print_board(board, col_marker=i)
            print("-------------------------", iteration, complete_rows)
            board = transpose_board(board)

        board = transpose_board(board)

    return board


if __name__ == "__main__":
    board = init_board(BOARD_SIZE)
    row_rules, col_rules = init_rules(BOARD_SIZE)

    board = iterate_board(board, row_rules, col_rules)

    print_board(board)