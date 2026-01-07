import doctest

import k3mime


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(k3mime))
    return tests
