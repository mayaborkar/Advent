def expand(blank, start, end):
    count = 0
    for c in blank:
        if (start <= c <= end or end <= c <= start):
            count += 1
    return count

f1 = open("adventinput11", "r")
mylist = f1.read().split("\n")
# print(mylist)

coordinates = []
xBlankArr = []

for i in range(0, len(mylist)):
    if ("#" not in mylist[i]):
        # print("here")
        xBlankArr.append(i)
    for j in range(0, len(mylist[i])):
        if (mylist[i][j].__eq__("#")):
            coordinates.append((i, j))

yBlankArr = []
for i in range(0, len(mylist)):
    switch = ''
    for j in range(0, len(mylist[i])):
        switch += mylist[j][i]
    if ("#" not in switch):
        yBlankArr.append(i)

totalDist = 0
distance = 0
for c in coordinates:
    distArr = []
    for c_other in coordinates:
        #print (c, '=', c_other)
        if(c != c_other ):
            distance = abs(c[0] - c_other[0]) + abs(c[1] - c_other[1])
            expandRow = expand(xBlankArr, c[0], c_other[0])
            expandCol = expand(yBlankArr, c[1], c_other[1])
            distance = distance + (1000000*expandRow) + (1000000*expandCol) - (expandRow+expandCol)
            totalDist += distance

print(xBlankArr)
print(yBlankArr)
print("total distance", totalDist/2)

# 339317600874
'''
distance(x1-x2 + y1-y2)
x,y of the * and the distances of each of the pairs
dictionary 1 is the key, then is the x,y and then do the distances
2 loops
iterate through the dict and iterate inside except for the existing row
pop the first distance, if 0 dont append the array

when calculating the distances --> look at the expansions
store x and y for the empty lines
and see how many empty points are between and *2 
find distance ex 4 --> 1 line is in between and subtract 1 and +2
two arrays of empty while traversing
'''