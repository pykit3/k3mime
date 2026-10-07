import json
import mimetypes
import os
import unittest

import k3ut

import k3mime

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

    def test_get_by_filename_uses_every_resource_entry(self):
        # Every suffix in the package data file maps to its entry there, before mimetypes is asked.
        path = os.path.join(os.path.dirname(k3mime.__file__), "thirdpart", "mimes.json")
        with open(path) as f:
            want = json.load(f)

        rst = {suffix: k3mime.get_by_filename("file." + suffix) for suffix in want}
        self.assertEqual(want, rst)

    def test_get_by_filename_ignores_suffix_case(self):
        # mimes.json has only lower-case suffixes.
        path = os.path.join(os.path.dirname(k3mime.__file__), "thirdpart", "mimes.json")
        with open(path) as f:
            want = json.load(f)

        rst = {suffix: k3mime.get_by_filename("file." + suffix.upper()) for suffix in want}
        self.assertEqual(want, rst)

    def test_get_by_filename_fallback(self):
        # mimes.json has no "py" entry, so the mimetypes module decides.
        want, _ = mimetypes.guess_type("file.py")
        self.assertIsNotNone(want)

        rst = k3mime.get_by_filename("file.py")
        self.assertEqual(want, rst)

        cases = (
            # A dot in a directory name is not a suffix.
            ("dir.json/file", "application/octet-stream"),
            ("dir/file.json", "application/json"),
        )

        for inp, expected in cases:
            rst = k3mime.get_by_filename(inp)
            self.assertEqual(expected, rst)
