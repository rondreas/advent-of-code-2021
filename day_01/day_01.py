# python 3.9.9
#-*- coding: utf-8 -*-

"""

"""


from typing import List


__author__ = "Andreas Rånman"


def count_increments(data: List[int]) -> int:
    """ count the number of times depth measurement increases from
    the previous reading.

    >>> data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> count_increments(data)
    7

    """
    return sum([a < b for a,b in zip(data[:-1], data[1:])])


def sliding_window(data: List[int], measurements: int) -> int:
    """ 
    >>> data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> sliding_window(data, 3)
    5

    """
    windows = []
    for index in range(len(data) - measurements + 1):
        window = sum(data[index:index+measurements])
        # used to debug my off by one error ...
        # print(f"{' + '.join(map(str, data[index:index+measurements]))} = {window}")
        windows.append(window)
    return count_increments(windows)


def main():
    """ Now solve the actual problem. """

    # Get the input
    with open("input", "r") as f:
        data = list(map(int, f.readlines()))

    # Part One
    # How many measurements are larger than the previous measurement?
    print(f"There were {count_increments(data)} increments")

    # Part Two
    # How many sums are larger than the previous sum?
    print(f"There were {sliding_window(data, 3)} incrementing sums")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
