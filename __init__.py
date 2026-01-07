from importlib.metadata import version

__version__ = version("k3mime")

from .mime import get_by_filename

__all__ = [
    "get_by_filename",
]
