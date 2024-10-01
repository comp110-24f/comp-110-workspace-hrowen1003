"""CQ4 Visualize Program"""

__author__ = "730722910"

from CQs.cq04.concatenation import (
    concat,
)  # import at start of file, just like defining functions within
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)  # don't need to print() this b/c get_coords prints already
