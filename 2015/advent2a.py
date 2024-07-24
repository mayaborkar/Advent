f1 = open("adventinput2", "r")
mylist = f1.read().split('\n')


total = 0
sum = 0

for i in range(0, len(mylist)):
    newlist = mylist[i].split("x")
    intNewList = map(int, newlist)
    newSort = sorted(intNewList)
    print(newSort)

    total += 2*(int(newSort[0]) * int(newSort[1]) + int(newSort[1]) * int(newSort[2]) + int(newSort[0]) * int(newSort[2])) + (int(newSort[0])*int(newSort[1]))

print(total)
