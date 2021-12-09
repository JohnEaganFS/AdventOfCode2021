import os
import math

if __name__ == "__main__":
    filename = "Day1/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [int(line.strip("\n")) for line in lines]
    
    ans = 0
    threeSum = -math.inf
    for i in range(1, len(nums)-2):
        newThreeSum = nums[i] + nums[i+1] + nums[i+2]
        if newThreeSum > threeSum:
            ans += 1
        threeSum = newThreeSum
    print("Answer:", ans) # 1702