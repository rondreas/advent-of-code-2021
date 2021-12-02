# Advent of Code: 2021

Trying to follow along for as long as possible. And keeping it all in one repo this year.

## Day 1

Figured I'd try use doctest to test out the examples, and get in the habit of using pythons new type annotation.

Likely not the most optimal solution for the first puzzle, using zip on two slices of the original list and using greater than comparision. But worked on both the example and main problem.

As for the second problem, the way I chose to iterate there caused me to run into off by one error when I got the range of indices I wanted to use to read the list. Added a debug print when running just the doctest and noticed it didn't read the last sum from the example problem.

## Day 2

After reading the instructions I figured this would be neat with python 3.10 new match, similar to the one from rust. So I downloaded a newer version of python and figured I'd attempt using dataclasses while I was at it. Worked the first class and method to solve the example without realizing I didn't even use the dataclass decorator. 

With the second problem I realized the first class wasn't maybe the best idea. Couldn't really see a way to reuse much besided the two previous attributes. But still opted for subclassing and overriding the move method from before.

Did a mistake in the code for the second problem at first, doing depth = aim * horizontal_position. Thankfully the docstest pointed out how crazy big the depth value ended up being.
