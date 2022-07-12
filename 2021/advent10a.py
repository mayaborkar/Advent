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


f1 = open("adventtestinput10.txt", "r")
mylist = f1.read().split('\n')
print (mylist)
openDels = ["<", "{", "[", "("]
valid = []
points = 0
for i in range(0, len(mylist) - 1):
    if mylist[i] in openDels:
        valid.append(mylist[i])
    if mylist[i] not in openDels:
        if mylist[i+1] == correspondingDel(mylist[i]):
            valid.pop()
        else:
            if valid[len(valid)] == "<":
                points += 25137
            if valid[len(valid)] == "{":
                points += 1197
            if valid[len(valid)] == "[":
                points += 57
            if valid[len(valid)] == "(":
                points += 3
print(points)

