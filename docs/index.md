# k3mime

[![Action-CI](https://github.com/pykit3/k3mime/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3mime/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3mime/badge/?version=stable)](https://k3mime.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3mime)](https://pypi.org/project/k3mime)

MIME type detection by filename. Returns the correct MIME type based on file extension.

k3mime is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3mime
```

## Quick Start

```python
from k3mime import get_by_filename

# Get MIME type by filename
print(get_by_filename("document.pdf"))  # application/pdf
print(get_by_filename("image.png"))     # image/png
print(get_by_filename("video.mp4"))     # video/mp4
print(get_by_filename("data.json"))     # application/json

# Unknown extensions return application/octet-stream
print(get_by_filename("unknown.xyz"))   # application/octet-stream
```

## API Reference

::: k3mime

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
