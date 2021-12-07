"""

    Module docstring

"""

from typing import List

__author__ = ""


def gamma_rate(data: List[str]) -> str:
    """ Get the most common bit for each index in series strings representing bit patterns.

    >>> data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> gamma_rate(data)
    '10110'

    """
    result = ""
    for bits in zip(*data):
        one = sum(map(int, bits))  # the count of "1"
        zero = len(bits) - one  # the count of zeroes
        result += "1" if one >= zero else "0"
    return result


def epsilon_rate(gamma: str) -> str:
    """ Get the least common bit for each index in series of strings representing bit patterns.

    >>> epsilon_rate("10110")
    '01001'

    """
    i = int('0x' + 'f' * (len(gamma) // 4), 16)
    return bin(~int(gamma, 2) & i).replace("0b", "").zfill(len(gamma))


def oxygen_generator_rating(data: List[str]) -> int:
    """
    >>> data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> oxygen_generator_rating(data)
    23

    """

    size = len(data[0])
    for i in range(size):
        most_common_bits = gamma_rate(data)
        data = [x for x in data if x[i] == most_common_bits[i]]
        if len(data) == 1:
            break

    return int(data.pop(), 2)


def co2_generator_rating(data: List[str]) -> int:
    """
    >>> data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> co2_generator_rating(data)
    10

    """

    size = len(data[0])
    for i in range(size):
        least_common_bit = epsilon_rate(gamma_rate(data))
        data = [x for x in data if x[i] == least_common_bit[i]]
        if len(data) == 1:
            break

    return int(data.pop(), 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open("input", "r") as f:
        data = f.read().splitlines()

    gamma = gamma_rate(data)
    epsilon = epsilon_rate(gamma)
    print(f"Power consumption is: {int(gamma, 2) * int(epsilon, 2)}")

    oxygen_rating = oxygen_generator_rating(data)
    co2_rating = co2_generator_rating(data)
    print(f"Life support rating is: {oxygen_rating * co2_rating}")
