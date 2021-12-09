import os

if __name__ == "__main__":
    filename = "Day1/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [int(line.strip("\n")) for line in lines]
    
    ans = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            ans += 1
    print("Answer:", ans) # 1665