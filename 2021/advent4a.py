# https://adventofcode.com/2021/day/4
def printBoard(board):
    for x in board:
        print("Printing next board... ")
        for y in x:
            print(y)


def isWin(board):
    # checking rows
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if int(board[i][j][0]) + int(board[i][j][1]) + int(board[i][j][2]) + int(board[i][j][3]) + int(board[i][j][4]) == -5:
                return True
    # checking columns

    for k in range(0, len(newGame)):
        for l in range(0, len(newGame[k])):
            if int(board[k][0][l]) + int(board[k][1][l]) + int(board[k][2][l]) + int(board[k][3][l]) + int(board[k][4][l]) == -5:
                return True
# take out null arrays (RESOLVED)
# if array starts with 1 digit number delete the null (RESOLVED)
# not printing last board (RESOLVED)

f1 = open("adventinput4.txt", "r")
mylist = f1.readlines()
drawnNumbers = mylist[0].replace("\n", "").split(",")

tempBoard = []
newGame = []
for i in range(2, len(mylist)):

    tempBoard.append(mylist[i].replace("\n", "").replace("  ", " ").split(" "))
    if len(tempBoard[len(tempBoard) - 1][0]) == 0:
        tempBoard[len(tempBoard) - 1].pop(0)

    if len(tempBoard) == 6:
        tempBoard.pop()
        newGame.append(tempBoard)
        tempBoard = []
# ------------------------

for numDrawn in drawnNumbers:
    for i in range(0, len(newGame)):
        for j in range(0, len(newGame[i])):
            for k in range(0, len(newGame[i][j])):
                # print (numDrawn)
                #print (newGame[i][j])
                if newGame[i][j][k] == numDrawn:
                    newGame[i][j][k] = -1
    isWin(newGame)
    if isWin == False:
        break
printBoard(newGame)



