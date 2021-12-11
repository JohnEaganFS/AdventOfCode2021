import os
import time
import heapq

if __name__ == "__main__":
    filename = "Day6/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]
    #print(nums)

    fish = nums[0].split(',')
    fish = list(map(int, fish))
    
    days = 256

    spawnAmounts = dict()
    for f in fish:
        spawnAmounts[f] = fish.count(f)
    count = len(fish)
    currDay = 0

    start = time.perf_counter()
    while currDay < days:
        if currDay in spawnAmounts:
            spawn = spawnAmounts[currDay]
            temp = 0 if currDay+9 not in spawnAmounts else spawnAmounts[currDay+9]
            spawnAmounts[currDay+9] = temp + spawn
            temp = 0 if currDay+7 not in spawnAmounts else spawnAmounts[currDay+7]
            spawnAmounts[currDay+7] = temp + spawn
            count += spawn
        currDay += 1
    end = time.perf_counter()
    elapsed = end - start
    print("Time:", elapsed)
    ans = count
    print(ans) # 1604361182149