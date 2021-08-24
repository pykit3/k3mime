import os
import unittest

import k3ut
import {{ name }}

dd = k3ut.dd

this_base = os.path.dirname(__file__)


class Test{{ nameBig }}(unittest.TestCase):

    foo_fn = '/tmp/foo'

    def _clean(self):

        # remove written file
        try:
            os.unlink(self.foo_fn)
        except EnvironmentError:
            pass

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    def test_procerror(self):
        pass
