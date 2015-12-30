# -*- coding: utf-8 -*-

from __future__ import print_function
from itertools import ifilter, product


def partition_buckets(number, buckets):
    """
    All possible ways of splitting number into buckets

    >>> list(partition_buckets(1, 3))
    [(0, 0, 1), (0, 1, 0), (1, 0, 0)]

    >>> list(partition_buckets(2, 3))
    [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)]

    :param number:
    :param buckets:
    :return: iterator of tuples of number splt into buckets
    """

    # this generates all values for all buckets and discards those with the wrong sum
    # TODO - optimise so that we only generate combinations with the right sum
    return ifilter(lambda x: sum(x) == number, product(xrange(number + 1), repeat=buckets))
