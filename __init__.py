"""
k3mime is utility to .

Execute a shell script::

    import k3mime

    # execute a shell script

    returncode, out, err = pk3proc.shell_script('ls / | grep bin')
    print returncode
    print out
    # output:
    # > 0
    # > bin
    # > sbin

Run a command::

    # Unlike the above snippet, following statement does not start an sh process.
    returncode, out, err = pk3proc.command('ls', 'a*', cwd='/usr/local')

"""


__version__ = "0.1.0"
__name__ = "k3mime"

from .mime import (
    get_by_filename
)

__all__ = [
    'get_by_filename'
]

