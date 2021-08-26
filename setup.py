# DO NOT EDIT!!! built with `python _building/build_setup.py`
import setuptools
setuptools.setup(
    name="k3mime",
    packages=["k3mime"],
    version="0.1.0",
    license='MIT',
    description='This module provide some util methods to handle mime type.',
    long_description="# k3mime\n\n[![Action-CI](https://github.com/pykit3/k3mime/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3mime/actions/workflows/python-package.yml)\n[![Build Status](https://travis-ci.com/pykit3/k3mime.svg?branch=master)](https://travis-ci.com/pykit3/k3mime)\n[![Documentation Status](https://readthedocs.org/projects/k3mime/badge/?version=stable)](https://k3mime.readthedocs.io/en/stable/?badge=stable)\n[![Package](https://img.shields.io/pypi/pyversions/k3mime)](https://pypi.org/project/k3mime)\n\nThis module provide some util methods to handle mime type.\n\nk3mime is a component of [pykit3] project: a python3 toolkit set.\n\n\n#   Name\n\nk3mime\n\n#   Status\n\nThe library is considered production ready.\n\n\n\n\n# Install\n\n```\npip install k3mime\n```\n\n# Synopsis\n\n```python\n\nimport k3mime\n\nprint(k3mime.get_by_filename('file.json'))\n#  application/json\n\n\n```\n\n#   Author\n\nZhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n#   Copyright and License\n\nThe MIT License (MIT)\n\nCopyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n\n[pykit3]: https://github.com/pykit3",
    long_description_content_type="text/markdown",
    author='Zhang Yanpo',
    author_email='drdr.xp@gmail.com',
    url='https://github.com/pykit3/k3mime',
    keywords=['python', 'mime'],
    python_requires='>=3.0',

    install_requires=['k3ut<0.2,>=0.1.15'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ] + ['Programming Language :: Python :: 3'],
)
