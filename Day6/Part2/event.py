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
    #events = list(set([(f, fish.count(f)) for f in fish]))
    #heapq.heapify(events)
    count = len(fish)
    currDay = 0

    start = time.perf_counter()
    #print(events)
    while currDay < days:
        if currDay in spawnAmounts:
            spawn = spawnAmounts[currDay]
            if currDay+9 in spawnAmounts:
                spawnAmounts[currDay+9] += spawn
            else:
                spawnAmounts[currDay+9] = spawn
            if currDay+7 in spawnAmounts:
                spawnAmounts[currDay+7] += spawn
            else:
                spawnAmounts[currDay+7] = spawn
        #currDay, spawn = heapq.heappop(events)
        #heapq.heappush(events, (currDay+9, spawn))
        #heapq.heappush(events, (currDay+7, spawn))
            count += spawn
        currDay += 1
    end = time.perf_counter()
    elapsed = end - start
    print("Time:", elapsed)
    ans = count
    print(ans) # 1604361182149