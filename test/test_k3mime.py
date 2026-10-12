import json
import mimetypes
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import venv

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
            # The bytes are gzip, whatever the archive inside holds.
            ("file.gz", "application/gzip"),
            ("archive.tar.gz", "application/gzip"),
            ("archive.tgz", "application/gzip"),
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
            ("dir.d/file.json", "application/json"),
            ("dir.v1/sub.v2/notes.txt", "text/plain"),
            ("dir.d/README", "application/octet-stream"),
            # A file without a suffix.
            ("README", "application/octet-stream"),
            ("dir/README", "application/octet-stream"),
            # A hidden file.
            (".bashrc", "application/octet-stream"),
            ("dir/.hidden.json", "application/json"),
            # Only the last of several suffixes counts.
            ("photo.jpeg.png", "image/png"),
            ("a.b.c.txt", "text/plain"),
        )

        for inp, expected in cases:
            rst = k3mime.get_by_filename(inp)
            self.assertEqual(expected, rst)

    def test_get_by_filename_from_wheel(self):
        # The other tests import k3mime from the checkout. This one installs a wheel into a new venv and imports
        # k3mime there, so it fails when the wheel leaves out thirdpart/mimes.json.
        src = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with tempfile.TemporaryDirectory() as tmp:
            # pip builds in the source tree, and a stale file in its build/ would get into the wheel.
            copy = os.path.join(tmp, "src")
            shutil.copytree(src, copy, ignore=shutil.ignore_patterns(".git", "build", "*.egg-info"))

            dist = os.path.join(tmp, "dist")
            subprocess.run([sys.executable, "-m", "pip", "wheel", "-q", "--no-deps", "-w", dist, copy], check=True)
            [name] = os.listdir(dist)
            wheel = os.path.join(dist, name)

            env = os.path.join(tmp, "env")
            venv.create(env)
            python = os.path.join(env, "bin", "python")
            subprocess.run([sys.executable, "-m", "pip", "--python", python, "install", "-q", wheel], check=True)

            code = "import k3mime; print(k3mime.get_by_filename('file.123'))"
            rst = subprocess.run([python, "-I", "-c", code], cwd=tmp, stdout=subprocess.PIPE, text=True, check=True)

        self.assertEqual("application/vnd.lotus-1-2-3\n", rst.stdout)
