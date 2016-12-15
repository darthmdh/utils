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


def gen_colour():
    pivots = (0x0, 0x5f, 0x87, 0xaf, 0xd7, 0xff)
    fakies = dict(zip(range(16), ["N/A"] * 16))
    palette = ["#{0:02x}{1:02x}{2:02x}".format(r,g,b) for r in pivots for g in pivots for b in pivots]
    palette = dict(zip(range(16, len(palette)+16), palette))
    greyscale = dict(zip(range(232, 256), ["#{0:02x}{0:02x}{0:02x}".format(g) for g in range(8, 248, 10)]))
    palette.update(greyscale)
    palette.update(fakies)
    assert len(palette) == 256
    for i, c in palette.iteritems():
        if i < 16:
            end = '\n' if (i + 1) % 8 == 0 else ''
        else:
            end = '\n' if i % 6 == 3 else ''
        yield ('\033[38;5;{0!s}m{0!s:>4} {1!s} \033[48;5;{0!s}mxxxxx\033[0m'.format(i, c), end)
            
for colour, end in gen_colour():
    print(colour, end=end)
