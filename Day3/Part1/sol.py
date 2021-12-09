import os

def binaryToDecimal(y):
    sum = 0
    for i in range(len(y)):
        sum += (2**(len(y) - i - 1)) * y[i]
    return sum

if __name__ == "__main__":
    filename = "Day3/Part1/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]

    digits = []
    for i in range(len(nums[0])):
        digits.append([int(num[i]) for num in nums])
    
    mostCommon = [max(set(lst), key=lst.count) for lst in digits]
    print(mostCommon)
    gamma = binaryToDecimal(mostCommon)
    print("Gamma Rate:", gamma)

    leastCommon = [0 if x == 1 else 1 for x in mostCommon]
    print(leastCommon)
    epsilon = binaryToDecimal(leastCommon)
    print("Epsilon Rate:", epsilon)

    ans = gamma * epsilon
    print("Energy Consumption:", ans) # 3885894