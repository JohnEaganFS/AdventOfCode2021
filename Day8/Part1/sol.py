import os

if __name__ == "__main__":
    filename = "Day8/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip("\n") for line in lines]

    outputs = []
    for line in lines:
        l = line.split('|')[1]
        outputs.append(l.split())
    
    ans = sum([sum([1 for x in output if len(x) in [2, 4, 3, 7]]) for output in outputs])
    print(ans) # 237