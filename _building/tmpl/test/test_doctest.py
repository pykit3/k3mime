import doctest

import {{ name }}


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite({{ name }}))
    return tests
