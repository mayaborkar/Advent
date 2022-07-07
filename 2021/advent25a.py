f1 = open("adventinput25.txt", "r")
mylist = f1.readlines()
moveArray = []
moves = []
for i in range(0, len(mylist)):
    moves = mylist[i].strip().split('\n')
    moveArray.append(moves)

stepCount = 0

validmove = True
for i in range(0, len(moveArray)):
    if moveArray[i] == ">" and moveArray[i + 1] != ".":
        validmove = False



print stepCount

