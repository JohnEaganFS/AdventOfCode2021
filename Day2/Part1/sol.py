import os

if __name__ == "__main__":
    filename = "Day2/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    dirs = [line.strip("\n") for line in lines]
    
    horizontal = 0
    depth = 0

    dirs = [(str.split()[0], int(str.split()[1])) for str in dirs]
    
    for (dir, num) in dirs:
        if dir == "forward":
            horizontal += num
        elif dir == "up":
            depth -= num
        else:
            depth += num
    
    ans = horizontal * depth
    print(ans) # 1451208
