"""My file to play around with python"""


def sqrfinder(x: int) -> str:
    """Finds a close approximation to the square root of x"""
    g = x
    while ((g**2) - x) > 0.000000001:
        g = (g + x / g) / 2
        if ((g**2) - x) <= 0.000000001:
            break
    return f"The square root of x is approx. {g}"


def testing(param1: float) -> float:
    return param1 * 3


print(testing(param1=2))
