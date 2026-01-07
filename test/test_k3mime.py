import unittest

import k3mime
import k3ut

dd = k3ut.dd


class TestMime(unittest.TestCase):
    def test_get_by_filename(self):
        cases = (
            ("", "application/octet-stream"),
            ("123", "application/octet-stream"),
            ("file.123", "application/vnd.lotus-1-2-3"),
            ("file.123.not_exist_suffix_aa", "application/octet-stream"),
            ("file.json", "application/json"),
            ("file.not_exist_suffix_aa", "application/octet-stream"),
        )

        for inp, expected in cases:
            dd("inp, expected:", inp, " ", expected)
            rst = k3mime.get_by_filename(inp)

            dd("rst:", rst)

            self.assertEqual(expected, rst)
