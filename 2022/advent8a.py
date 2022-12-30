def top(treeGrid, row, col):
    topArray = []
    for i in range(0, len(treeGrid)):
        topArray.append(treeGrid[i][col])
        if(i > row):
            break
    return topArray


def bottom(treeGrid, row, col):
    bottomArray = []
    for i in range(0, len(treeGrid)):
        bottomArray.append(treeGrid[i][col])
        if (i < row):
            break
    return bottomArray


f1 = open("adventtestinput8", "r")
myinputlist = f1.readlines()
# look up, down, left, and right for each of the trees
print(myinputlist)
mylist = []
treeGrid = []
count = 0
for i in range(0, len(myinputlist)):
    # count += 2
    mylist = [*myinputlist[i]]
    mylist.pop()
    treeGrid.append(mylist)
    # print(mylist)
print(treeGrid)
for row in range(1, len(treeGrid) - 1):
    for col in range(1, len(treeGrid[row]) - 1):
        currentTree = treeGrid[row][col]
        top = max(top(treeGrid, row, col))
        bottom = max(bottom(treeGrid, row, col))
        left = max(treeGrid[row][:col])
        right = max(treeGrid[row][col + 1:])
        if((currentTree > top) or (currentTree > bottom) or (currentTree > left) or (currentTree > right)):
            count += 1
print(count)

'''
    for j in range(1, len(mylist[i]) - 1):
        if (mylist[i][j] > mylist[i][j + 1]):
            if (mylist[i][j] > mylist[i][j]):
                if (mylist[i][j] > mylist[i + 1][j]):
                    if (mylist[i][j] > mylist[i - 1][j]):
                        count += 1

count += 2 * len(mylist[0])
print(count)
'''

