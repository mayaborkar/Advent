# Advent 2021 Day 9
# on July 10th
def get_adjacent(i, j, mylist):
    adjacent = []
    if i != 0:
        adjacent.append(mylist[i-1][j])
    if i != len(mylist) - 1:
        adjacent.append(mylist[i+1][j])
    if j != 0:
        adjacent.append(mylist[i][j - 1])
    if j != (len(mylist[i]) - 1):
        adjacent.append(mylist[i][j+1])
    print("adjacent: " + str(adjacent))
    return adjacent


def get_height(i, j, adjacent, mylist):
    height = 0
    print("ax" + adjacent + "x")
    print("cx" + mylist[i][j] + "x")
    diff = int(adjacent) - int(mylist[i][j])
    print("difference: " + str(diff))
    if diff < 0:
        return 0
    elif diff > height:
        return height + 1


f1 = open("adventinput9.txt", "r")
mylist = f1.read().split('\n')
print (mylist)
risk = 0

for i in range(0, len(mylist)):
    for j in range(0, len(mylist[0])):
        # print(mylist[i][j])
        adjacent_list = sorted(get_adjacent(i, j, mylist))
        print(adjacent_list)
        if mylist[i][j] < adjacent_list[0]:
            risk += (int(mylist[i][j]) + 1)

print("risk: " + str(risk))
