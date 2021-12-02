# Advent of Code: 2021

Trying to follow along for as long as possible. And keeping it all in one repo this year.

## Day 1

Figured I'd try use doctest to test out the examples, and get in the habit of using pythons new type annotation.

Likely not the most optimal solution for the first puzzle, using zip on two slices of the original list and using greater than comparision. But worked on both the example and main problem.

As for the second problem, the way I chose to iterate there caused me to run into off by one error when I got the range of indices I wanted to use to read the list. Added a debug print when running just the doctest and noticed it didn't read the last sum from the example problem.
