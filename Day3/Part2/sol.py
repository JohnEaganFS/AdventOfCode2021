import os

def binaryToDecimal(y):
    sum = 0
    for i in range(len(y)):
        sum += (2**(len(y) - i - 1)) * int(y[i])
    return sum

def mostCommon(digits):
    # print([lst.count(0) for lst in digits])
    # print([lst.count(1) for lst in digits])
    # print([max(set(lst), key=lst.count) for lst in digits])
    counts0 = [lst.count(0) for lst in digits]
    counts1 = [lst.count(1) for lst in digits]
    return [0 if ct0 > ct1 else 1 for (ct0, ct1) in zip(counts0, counts1)]
    #return [max(set(lst), key=lst.count) for lst in digits]

if __name__ == "__main__":
    filename = "Day3/Part2/puzzle.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = [line.strip("\n") for line in lines]

    digits = []
    for i in range(len(nums[0])):
        digits.append([int(num[i]) for num in nums])
    
    mostCom = mostCommon(digits)
    
    oxy = nums.copy() #strings
    oxyDigits = digits.copy()
    mostCom = mostCommon(oxyDigits)
    dig = 0
    while (len(oxy) > 1) and (dig <= len(oxy[0])):
        oxy = [x for x in oxy if int(x[dig]) == mostCom[dig]]
        oxyDigits = []
        for i in range(len(oxy[0])):
            oxyDigits.append([int(oxy[i]) for oxy in oxy])
        mostCom = mostCommon(oxyDigits)
        dig += 1
    print(oxy)
    oxyReading = binaryToDecimal(oxy[0])
    print("Oxygen Reading:", oxyReading)

    co2 = nums.copy()
    co2Digits = digits.copy()
    mostCom = mostCommon(co2Digits)
    dig = 0
    while (len(co2) > 1) and (dig < len(co2[0])):
        co2 = [x for x in co2 if int(x[dig]) != mostCom[dig]]
        co2Digits = []
        for i in range(len(co2[0])):
            co2Digits.append([int(co2[i]) for co2 in co2])
        mostCom = mostCommon(co2Digits)
        dig += 1
    print(co2)

    co2Reading = binaryToDecimal(co2[0])
    print("co2:", co2Reading)

    ans = oxyReading * co2Reading
    print(ans) # 4375225