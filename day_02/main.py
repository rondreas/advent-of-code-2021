# python 3.10.0
#-*- coding: utf-8 -*-

"""

    Wanted to try the new Structural Pattern Matching

"""

__author__ = "Andreas Rånman"


class Submarine:
    horizontal_position: int = 0
    depth: int = 0

    def move(self, instruction: str):
        """ 
        >>> submarine = Submarine()
        >>> instructions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        >>> for instruction in instructions:
        ...     submarine.move(instruction)
        >>> submarine.horizontal_position
        15
        >>> submarine.depth
        10

        """
        direction, distance = instruction.split()
        match direction:
            case "forward":
                self.horizontal_position += int(distance)

            case "up":
                self.depth -= int(distance)

            case "down":
                self.depth += int(distance)

            case _:
                raise ValueError(f"Failed to parse instruction: {instruction}")

class CorrectSubmarine(Submarine):
    aim: int = 0

    def move(self, instruction: str):
        """
        >>> submarine = CorrectSubmarine()
        >>> instructions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        >>> for instruction in instructions:
        ...     submarine.move(instruction)
        >>> submarine.horizontal_position
        15
        >>> submarine.depth
        60
        """
        direction, distance = instruction.split()
        match direction:
            case "forward":
                self.horizontal_position += int(distance)
                self.depth += self.aim * int(distance)

            case "up":
                self.aim -= int(distance)

            case "down":
                self.aim += int(distance)

            case _:
                raise ValueError(f"Failed to parse instruction: {instruction}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open("input", "r") as f:
        instructions = f.readlines()

    submarine = Submarine()
    correct_submarine = CorrectSubmarine()

    for instruction in instructions:
        submarine.move(instruction)
        correct_submarine.move(instruction)

    # What do you get if you multiply your final horizontal position by your final depth?
    print(submarine.horizontal_position * submarine.depth)

    # What do you get if you multiply your final horizontal position by your final depth?
    print(correct_submarine.horizontal_position * correct_submarine.depth)
