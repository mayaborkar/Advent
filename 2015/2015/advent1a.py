f1 = open("adventinput1", "r")
mylist = f1.read()

count = 0
for i in range(0, len(mylist)):
    if mylist[i] == "(":
        count += 1
    if mylist[i] == ")":
        count -= 1

print(count)
