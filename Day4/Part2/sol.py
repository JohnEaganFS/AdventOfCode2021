import os
import numpy as np

def isWinner(board):
    cols = []
    for i in range(len(board)):
        cols.append([row[i] for row in board])
    for row in board:
        if 0 not in [y for (x,y) in row]:
            return True
    for col in cols:
        if 0 not in [y for (x,y) in col]:
            return True
    return False

def updateBoard(board, num):
    newBoard = []
    for row in board:
        newBoard.append([(num, 0) if num != currNum and x != 1 else (num, 1) for (num, x) in row])
    print(newBoard)
    return newBoard

if __name__ == "__main__":
    filename = "Day4/Part2/puzzle.txt"
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

    boards = np.asarray(boards)

    boardWinners = [0] * len(boards)
    print(boardWinners)
    #print(boards)
    ans = 0
    for currNum in nums:
        for i, board in enumerate(boards):
            board = updateBoard(board, currNum)
            boards[i] = board
            if boardWinners[i] != 1:
                if isWinner(board):
                    boardWinners[i] = 1
                    sumUnmarked = 0
                    for row in board:
                        sumUnmarked += sum([x for (x,y) in row if y == False])
                    ans = sumUnmarked * currNum
                    print(ans)
    #print(boards)
    print("Final:", ans) # 1920
    
    # for currNum in nums:
    #     newBoards = []
    #     for j, board in enumerate(boards):
    #         for i, row in enumerate(board):
    #             board[i] = [(num, False) if num != currNum else (num, True) for (num, x) in row]
    #         if isWinner(board):
    #             sumUnmarked = 0
    #             for row in board:
    #                 sumUnmarked += sum([x for (x,y) in row if y == False])
    #             ans = sumUnmarked * currNum
    #             print(ans)
    #         newBoards.append(board)
    #     boards = newBoards
    #     print("end")
    #     print(boards)