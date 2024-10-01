"""CQ4 Coordinates Program"""

__author__ = "730722910"


def get_coords(xs: str, ys: str) -> None:
    """Print xs and ys as coordinates"""
    index_x: int = 0
    index_y: int = 0
    while index_x < len(xs):
        while index_y < len(ys):
            print(
                "(" + xs[index_x] + "," + ys[index_y] + ")"
            )  # Need parentheses to be coords
            index_y += 1
        index_x += 1
        index_y = 0  # Don't forget to reset y back to 0


# didn't need a if __name__ = "__main__" for this file because there are no calls
