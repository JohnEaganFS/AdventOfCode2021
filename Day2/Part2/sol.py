import os

if __name__ == "__main__":
    filename = "Day2/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    dirs = [line.strip("\n") for line in lines]
    
    horizontal = 0
    depth = 0
    aim = 0

    dirs = [(str.split()[0], int(str.split()[1])) for str in dirs]
    
    for (dir, num) in dirs:
        if dir == "forward":
            horizontal += num
            depth += num * aim
        elif dir == "up":
            aim -= num
        else:
            aim += num
    
    ans = horizontal * depth
    print(ans) # 1620141160
