"""

    Day 4

"""

class Board(object):
    """

    >>> values = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    >>> one = Board([22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19])
    >>> two = Board([3, 15, 0, 2, 22, 9, 18, 13, 17, 5, 19, 8, 7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12, 6])
    >>> three = Board([14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7])
    >>> boards = [one, two, three]
    >>> while not any(boards) and values:
    ...     value = values.pop(0)
    ...     Board.add(value)
    BINGO! The winner is board 3 with the score 4512

    """
    _num_boards = 0

    _called_numbers = set()
    _last_number = -1
    @classmethod
    def add(cls, number):
        cls._last_number = number
        cls._called_numbers.add(number)

    def __init__(self, cells: list[int, ...]):
        self.cells = cells

        # set this board id and increment the 
        Board._num_boards += 1
        self.id = Board._num_boards

    def row(self, i):
        return set(self.cells[ (i+1) * 5 - 5 : (i+1) * 5])

    def col(self, i):
        return set(self.cells[i:25:5])

    def score(self):
        return sum([x for x in self.cells if x not in Board._called_numbers]) * Board._last_number

    def __bool__(self):
        if len(Board._called_numbers) < 5:
            return False

        for i in range(5):
            row = self.row(i)
            col = self.row(i)

            if len(row & Board._called_numbers) == 5 or len(col & Board._called_numbers) == 5:
                print(f"BINGO! The winner is board {self.id} with the score {self.score()}")
                return True

        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open("input", "r") as f:
        values = [int(i) for i in f.readline().strip().split(",")]
        board_values = []

        # Get the values for the bingo boards
        lines = [
            line.replace(" ", ",")
                .strip()
                .split(",")
            for line in f.read().splitlines() if line
        ]

    numbers = []
    for line in lines:
        numbers += [int(i) for i in line if i]

    boards = []
    for i in numbers[::25]:
        boards.append(Board(numbers[i:i+25]))

    while not any(boards) and values:
        value = values.pop(0)
        Board.add(value)
