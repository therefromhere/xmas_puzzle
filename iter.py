# -*- coding: utf-8 -*-

from __future__ import print_function
from itertools import permutations, product, ifilter


def rule_asc_len(number, buckets):
    """
    From http://math.stackexchange.com/a/28371
    :param number:
    :param buckets:
    :return:
    """
    a = [0 for i in range(number + 1)]
    k = 1
    a[0] = 0
    a[1] = number
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y and k < buckets - 1:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield tuple(a[:k + 1])


def partition_buckets_unique(number, buckets):
    """
    unique ways of partitioning number into buckets (independent of bucket position)

    >>> sorted(partition_buckets_unique(1, 3))
    [(1, 0, 0)]

    >>> sorted(partition_buckets_unique(2, 3))
    [(1, 1, 0), (2, 0, 0)]

    >>> sorted(partition_buckets_unique(5, 1))
    [(5,)]

    >>> sorted(partition_buckets_unique(0, 2))
    [(0, 0)]

    :param number:
    :param buckets:
    :return:
    """

    if number == 0:
        yield (0,) * buckets
        return

    for p in rule_asc_len(number, buckets):
        pad_len = buckets - len(p)
        if pad_len > 0:
            p = p + (0,) * pad_len

        yield p


def partition_buckets(number, buckets):
    """
    unique ways of partitioning number into buckets (dependent on bucket position)

    >>> sorted(partition_buckets(1, 3))
    [(0, 0, 1), (0, 1, 0), (1, 0, 0)]

    >>> sorted(partition_buckets(2, 3))
    [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)]

    >>> sorted(partition_buckets(5, 1))
    [(5,)]

    >>> sorted(partition_buckets(0, 2))
    [(0, 0)]

    :param number:
    :param buckets:
    :return: iterator of tuples of number splt into buckets
    """
    for part in partition_buckets_unique(number, buckets):
        # unique permutations of this partition
        # note that we don't need to compare with all history, since the rule_asc algorithm doesn't return duplicates,
        # just this partitition
        seen = set()

        for perm in permutations(part):
            if perm not in seen:
                yield perm

            seen.add(perm)


def partition_buckets_slow(number, buckets, minimum=0):
    """
    All possible ways of splitting number into buckets

    >>> list(partition_buckets_slow(1, 3))
    [(0, 0, 1), (0, 1, 0), (1, 0, 0)]

    >>> list(partition_buckets_slow(2, 3))
    [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)]

    >>> sorted(partition_buckets_slow(5, 1))
    [(5,)]

    >>> sorted(partition_buckets_slow(0, 2))
    [(0, 0)]

    :param number:
    :param buckets:
    :return: iterator of tuples of number splt into buckets
    """

    # this generates all values for all buckets and discards those with the wrong sum
    return ifilter(lambda x: sum(x) == number, product(xrange(number + 1), repeat=buckets))
