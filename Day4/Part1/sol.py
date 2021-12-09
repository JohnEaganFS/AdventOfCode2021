import os
import numpy as np

def isWinner(board):
    for bd in [board]:
        #print(bd)
        for row in bd:
            if False not in [y for (x,y) in row]:
                return True
        cols = []
        for i in range(len(row)):
            col = []
            for j in range(len(bd)):
                col.append(bd[i][j])
            cols.append(col)
        for col in cols:
            if False not in [y for (x,y) in col]:
                return True
    return False

if __name__ == "__main__":
    filename = "Day4/Part1/test.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    nums = lines[0].strip("\n")
    #boards = [int(line.strip("\n")) for line in lines][1:]
    
    boards = []

    numBoards = (len(lines) - 1) // 6

    for i in range(numBoards):
        board = []
        for j in range(i*6+2, i*6+7, 1):
            line = lines[j].strip("\n")
            line = line.split()
            row = [(int(x), False) for x in line]
            board.append(row)
        boards.append(board)
    
    nums = [int(x) for x in nums.split(',')]
    
    for currNum in nums:
        newBoards = []
        for j, board in enumerate(boards):
            for i, row in enumerate(board):
                board[i] = [(num, False) if num != currNum else (num, True) for (num, x) in row]
            if isWinner(board):
                sumUnmarked = 0
                for row in board:
                    sumUnmarked += sum([x for (x,y) in row if y == False])
                ans = sumUnmarked * currNum
                print(ans)
            newBoards.append(board)
        boards = newBoards
        print("end")
        print(boards)