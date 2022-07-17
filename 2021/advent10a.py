def correspondingDel(delimeter):
    if delimeter == "<":
        return ">"
    if delimeter == "{":
        return "}"
    if delimeter == "[":
        return "]"
    if delimeter == "(":
        return ")"
    return "not valid"


f1 = open("adventinput10.txt", "r")
mylist = f1.read().split('\n')
# print (mylist)
openDels = ["<", "{", "[", "("]
valid = []
points = 0
for i in range(0, len(mylist)):
    # print("current string: " + mylist[i])
    for j in range(0, len(mylist[i]) - 1):
        # print("current character: " + mylist[i][j])
        if mylist[i][j] in openDels:
            # print("current open character: " + mylist[i][j])
            valid.append(mylist[i][j])
        else:
            # print("current closed character: " + mylist[i][j])
            if mylist[i][j] == correspondingDel(valid[-1]):
                # print("found corresponding closed, now popping " + str(valid))
                valid.pop()
                # print("after popping: " + str(valid))
            else:
                # print("adding points\n")
                # print("wrong closed character: " + mylist[i][j])
                # print("previous characters: " + mylist[i][0:j])
                if mylist[i][j] == ">":
                    # print("adding 25137")
                    points += 25137
                if mylist[i][j] == "}":
                    # print("adding 1197")
                    points += 1197
                if mylist[i][j] == "]":
                    # print("adding 57")
                    points += 57
                if mylist[i][j] == ")":
                    # print("adding 3")
                    points += 3
                # print("printing partial points " + str(points))
                break
print(points)

