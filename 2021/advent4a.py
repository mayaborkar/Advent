# https://adventofcode.com/2021/day/4
def printBoard(board):
    for x in board:
        print("Printing next board... ")
        for y in x:
            print(y)

def sumBoard(board, numDrawn):
    count = 0
    for x in board:
        for y in x:
            if y != -1:
                count += int(y)
    print  int(count) * int(numDrawn)


def isWin(board, numDrawn):
    # checking rows
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if int(board[i][j][0]) + int(board[i][j][1]) + int(board[i][j][2]) + int(board[i][j][3]) + int(board[i][j][4]) == -5:
                print("the winning board is: " + str(board[i]))
                sumBoard(board[i], numDrawn)
                return True
            if int(board[i][0][j]) + int(board[i][1][j]) + int(board[i][2][j]) + int(board[i][3][j]) + int(board[i][4][j]) == -5:
                print("the winning board is: " + str(board[i]))
                sumBoard(board[i], numDrawn)
                return True
    return False

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
    print ('Checking for '+str(numDrawn))
    for i in range(0, len(newGame)):
        for j in range(0, len(newGame[i])):
            for k in range(0, len(newGame[i][j])):
                # print (numDrawn)
                # print (newGame[i][j])
                if newGame[i][j][k] == numDrawn:
                    newGame[i][j][k] = -1
    if isWin(newGame, numDrawn) == True:
        print(numDrawn)
        break

# print(numDrawn * )
# printBoard(newGame)



