# python 3.10.0
#-*- coding: utf-8 -*-

"""

    Wanted to try the new Structural Pattern Matching

"""


from dataclasses import dataclass


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


if __name__ == '__main__':
    import doctest
    doctest.testmod()

