import os
import time

if __name__ == "__main__":
    filename = "Day6/Part1/test.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]
    #print(nums)

    fish = nums[0].split(',')
    fish = list(map(int, fish))
    
    days = 256

    start = time.perf_counter()
    for i in range(days):
        temp = []
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                temp.append(8)
            else:
                fish[i] -= 1
        fish += temp
    end = time.perf_counter()
    elapsed = end - start
    print("Time:", elapsed)
    ans = len(fish)
    print(ans) # 352872