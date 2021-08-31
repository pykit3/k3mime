"""
#   Table of Content

- [Name](#name)
- [Status](#status)
- [Synopsis](#synopsis)
- [Author](#author)
- [Copyright and License](#copyright-and-license)


#   Name

k3mime

#   Status

The library is considered production ready.

"""


__version__ = "0.1.2"
__name__ = "k3mime"

from .mime import (
    get_by_filename
)

__all__ = [
    'get_by_filename'
]

