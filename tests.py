# -*- coding: utf-8 -*-

import unittest
import doctest
import puzzle
import iter


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(iter))
    tests.addTests(doctest.DocTestSuite(puzzle))
    return tests

if __name__ == "__main__":
    unittest.main()
