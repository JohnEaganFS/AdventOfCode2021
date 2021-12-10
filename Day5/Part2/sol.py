import os

if __name__ == "__main__":
    filename = "Day5/Part1/test.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip("\n") for line in lines]

    firstPoints = []
    secondPoints = []
    for line in lines:
        splitText = line.split()
        firstText = splitText[0]
        firstSplit = firstText.split(',')
        firstPoints.append((int(firstSplit[0]), int(firstSplit[1])))

        secondText = splitText[2]
        secondSplit = secondText.split(',')
        secondPoints.append((int(secondSplit[0]), int(secondSplit[1])))
    #print(firstPoints)
    #print(secondPoints)

    linePoints = list(zip(firstPoints, secondPoints))
    #print(linePoints)

    board = dict()

    for points in linePoints:
        p1 = points[0]
        p2 = points[1]
        
        x1, y1 = p1
        x2, y2 = p2
        
        if x1 == x2:
            yMin = min([y1, y2])
            yMax = max([y1, y2])
            for i in range(yMin, yMax + 1):
                if (x1, i) in board:
                    board[(x1, i)] += 1
                else:
                    board[(x1, i)] = 1
        elif y1 == y2: # y1 == y2
            xMin = min([x1, x2])
            xMax = max([x1, x2])
            for i in range(xMin, xMax + 1):
                if (i, y1) in board:
                    board[(i, y1)] += 1
                else:
                    board[(i, y1)] = 1
        else:
            curr = (x1, y1)
            end = (x2, y2)
            xDir = 1 if (x2 - x1) > 0 else -1
            yDir = 1 if (y2 - y1) > 0 else -1
            while (curr != (end[0] + xDir, end[1] + yDir)):
                if curr in board:
                    board[curr] += 1
                else:
                    board[curr] = 1
                curr = (curr[0] + xDir, curr[1] + yDir)
    
    #print(board)
    ans = sum([1 for val in board.values() if val >= 2])
    print(ans) # 22088