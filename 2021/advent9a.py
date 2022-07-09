def isValid(i, j):
    if (len(mylist[0])) > i >= 0:
        return True
    if 0 <= j < (len(mylist)):
        return True
    else:
        return False


def adjacents(i, j):
    adjacent = []
    if isValid(i+1, j):
        adjacent.append(mylist[i + 1][j])
    if isValid(i, j + 1):
        adjacent.append(mylist[i][j + 1])


f1 = open("adventinput9.txt", "r")
mylist = f1.readlines()
