"""

    Module docstring

"""


__author__ = ""


def gamma_rate(data: list[str]) -> str:
    """ 

    >>> data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> gamma_rate(data)
    '10110'

    """
    result = ""
    for bits in zip(*data):
        one = sum(map(int, bits))  # the count of "1"
        zero = len(bits) - one
        result += "1" if one > zero else "0"
    return result

def epsilon_rate(gamma):
    """

    >>> epsilon_rate("10110")
    '01001'

    """
    return bin(~int(gamma, 2) & 0xf).replace("0b", "").zfill(len(gamma))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open("input", "r") as f:
        data = list(map(lambda s: s.strip(), f.readlines()))

    gamma = gamma_rate(data)
    epsilon = epsilon_rate(gamma)
    print(f"Power consumption is: {int(gamma, 2) * int(epsilon, 2)}")

