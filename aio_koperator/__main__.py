import sys
from .server import cli

if __name__ == '__main__':
    # assume we're invoked via <pythong> -m ... - replace __main__.py in
    # argv0 with something sensible.
    cli(prog_name='%s -m %s' % (sys.executable, __package__))
