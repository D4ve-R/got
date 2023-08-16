#!/usr/bin/env python3
import sys
from cli import got

__all__ = ['got']

__version__ = '0.0.1'

if __name__ == '__main__':
    got(*sys.argv[1:])
