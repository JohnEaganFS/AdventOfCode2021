import os

if __name__ == "__main__":
    filename = "Day7/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]
    nums = list(map(int, nums[0].split(',')))
    
    minPos = min(nums)
    maxPos = max(nums)

    fuelCosts = dict()
    for i in range(minPos, maxPos+1):
        sum = 0
        for crab in nums:
            sum += abs(crab - i)
        fuelCosts[i] = sum
    print(fuelCosts)
    ans = min(fuelCosts.values())
    print(ans) # 347449