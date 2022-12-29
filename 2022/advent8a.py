f1 = open("adventtestinput8", "r")
myinputlist = f1.readlines()
# look up, down, left, and right for each of the trees

mylist = [[]]
count = 0
for i in range(1, len(myinputlist) - 1):
    count += 2
    mylist.append(myinputlist[i].replace("\n", ""))

print(mylist)
count += 2 * len(mylist[0])
print(count)
'''
if (mylist[i][j] > mylist[i][j + 1]):
    if (mylist[i][j] > mylist[i][j - 1]):
        if (mylist[i][j] > mylist[i + 1][j]):
            if (mylist[i][j] > mylist[i - 1][j]):
                count += 1
'''