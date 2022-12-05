def isWin(opponent):
    if opponent == "A":
        return "Y"
    if opponent == "B":
        return "Z"
    if opponent == "C":
        return "X"


def isDraw(opponent):
    if opponent == "A":
        return "X"
    if opponent == "B":
        return "Y"
    if opponent == "C":
        return "Z"


def isLose(opponent):
    if opponent == "A":
        return "Z"
    if opponent == "B":
        return "X"
    if opponent == "C":
        return "Y"


f1 = open("adventinput2", "r")
mylist = f1.read().replace(' ', "").split("\n")

# auto-points 1-Rock, 2-Paper, 3-Scissors
# winning points 0-Lose, 3-Draw, 6-Win
# opponent: A-Rock, B-Paper, C-Scissors
# me: X-Rock, Y-Paper, Z-Scissors
# add to get the total
# X - lose, Y- draw, Z - win

sum = 0

print(mylist)

for i in range(0, len(mylist)):
    print(mylist[i])
    if mylist[i][1] == "Y":
        mylist[i] = mylist[i][0] + isDraw(mylist[i][0])
    elif mylist[i][1] == "Z":
        mylist[i] = mylist[i][0] + isWin(mylist[i][0])
    else:
        mylist[i] = mylist[i][0] + isLose(mylist[i][0])
    print(mylist[i])
    if isWin(mylist[i][0]) == mylist[i][1]:
        sum += 6
    elif isDraw(mylist[i][0]) == mylist[i][1]:
        sum += 3
    # lose sum += 0
    if mylist[i][1] == "X":
        sum += 1
    elif mylist[i][1] == "Y":
        sum += 2
    elif mylist[i][1] == "Z":
        sum += 3
print(mylist)
print(sum)
