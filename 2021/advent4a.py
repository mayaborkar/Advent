# https://adventofcode.com/2021/day/4
def printBoard(board):
    for x in board:
        print("Printing next board... ")
        for y in x:
            print(y)
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

printBoard(newGame)


