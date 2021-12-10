import os

if __name__ == "__main__":
    filename = "Day6/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]
    print(nums)