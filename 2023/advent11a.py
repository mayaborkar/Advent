def dist(currentCord, toCord):

    for c in toCord:
        distArr.append((currentCord[0] + toCord[0]) - (currentCord[1] - toCord[1]))

f1 = open("adventinput11", "r")
mylist = f1.read().split("\n")
# print(mylist)
galaxies = {}
coordinates = []
for i in range(0, len(mylist)):
    for j in range(0, len(mylist[i])):
        if (mylist[i][j].__eq__("#")):
            coordinates.append((i, j))

distArr = []
for c in coordinates:
    distArr = []
    for c_other in coordinates:
        #print (c, '=', c_other)
        if(abs(c[0] - c_other[0]) + abs(c[1] - c_other[1]).__ne__(0)):
            distArr.append(abs(c[0] - c_other[0]) + abs(c[1] - c_other[1]))
    galaxies[c] = min(distArr)

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