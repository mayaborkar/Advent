# https://adventofcode.com/2021/day/4
def printBoard(board):
    newBoard = []
    for i in range(0, len(board)):
        if(i % 5 != 0):
            newBoard[i] = board[i]
        print(board[i])


f1 = open("adventinput4.txt", "r")
mylist = f1.readlines()
drawnNumbers = mylist[0].split("\n")

board1 = "14 33 79 61 44 85 60 38 13 48 51 34 11 19  7 21 30 73  6 76 41  4 65 18 91"
printBoard(board1)
print(board1)

