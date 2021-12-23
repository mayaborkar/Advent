def countIntersection(grid):
    count = 0
    for i in range(0, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 2:
                count += 1
    print count


def printGrid(grid):
    for x in grid:
        print(x)


f1 = open("adventinput5.txt", "r")
mylist = f1.readlines()

pairCoordinates = []
startingCoordinates = []
endingCoordinates = []
x1 = []
y1 = []
x2 = []
y2 = []

for i in range(0, len(mylist)):
    mylist[i] = mylist[i].replace('\n', '').replace(' ', '')
    pairCoordinates.append(mylist[i].split("->"))
    startingCoordinates.append(pairCoordinates[i][0].split(","))
    x1.append(int(startingCoordinates[i][0]))
    y1.append(int(startingCoordinates[i][1]))

    endingCoordinates.append(pairCoordinates[i][1].split(","))
    x2.append(int(endingCoordinates[i][0]))
    y2.append(int(endingCoordinates[i][1]))

maxX = max(max(x1), max(x2)) + 1
maxY = max(y1 + y2) + 1

grid = [[0] * maxX for i in range(maxY)]
# printGrid(grid)

for i in range(0, len(x1)):
    print(str(x1[i]), str(x2[i]), str(y1[i]), str(y2[i]))
    if x1[i] == x2[i]:
        for j in range(min(y1[i], y2[i]), max(y1[i], y2[i]) + 1):
            grid[j][x1[i]] += 1
    elif y1[i] == y2[i]:
        for k in range(min(x1[i], x2[i]), max(x1[i], x2[i]) + 1):
            grid[y1[i]][k] += 1
    # printGrid(grid)
print("\n")
# printGrid(grid)
countIntersection(grid)
