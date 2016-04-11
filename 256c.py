#!/usr/bin/env python

# Generate a 256 colour palette on the terminal.
# Colour numbers are good for Vim cterm= values with t_Co=256
# Copyright (c) 2016 Matthew Hawkins.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import print_function

def gen_colour(c):
    return '\033[38;5;{0!s}m{0!s:>4} \033[48;5;{0!s}mxxxxx\033[0m'.format(c)

print('## Normal ASCII terminal colours ##\n')
for c in range(16):
    print(gen_colour(c), end='')
    if (c + 1) % 8 == 0: print('\n')

print('## Extended ASCII terminal colour range ##\n')
for r in range(6):
    for g in range(6):
        for b in range(6):
            c = 16 + (r * 36) + (g * 6) + b
            print(gen_colour(c), end='')
            if (c + 3) % 6 == 0: print('\n')

print('## Final Grayscale patch\n')
for c in range(232,256):
    print(gen_colour(c), end='')
    if (c + 1) % 8 == 0: print('\n')
