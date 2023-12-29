def dist(currentCord, toCord):
    distArr = []
    for c in toCord:
        # distArr.append((currentCord[0] + toCord[c][0]) - (currentCord[1] - toCord[c][1]))

f1 = open("adventinput11", "r")
mylist = f1.read().split("\n")
print(mylist)
galaxies = {}
coordinates = []
for i in range(0, len(mylist)):
    for j in range(0, len(mylist[i])):
        if (mylist[i][j].__eq__("#")):
            coordinates.append((i, j))

for c in coordinates:
    for c_other in coordinates:

        galaxies[c] = dist(c, c_other)


print(galaxies)
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