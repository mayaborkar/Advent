f1 = open("adventinput2", "r")
mylist = f1.read().split('\n')

print(mylist)
total = 0

for i in range(0, len(mylist)):
    newlist = mylist[i].split("x")
    intNewList = map(int, newlist)
    newSort = sorted(intNewList)
    total += (2*newSort[0] + 2*newSort[1]) + (newSort[0] * newSort[1] * newSort[2])

print(total)
