f1 = open("adventinput1", "r")
mylist = f1.read()

count = 0
i = 0

while count != -1:
    if mylist[i] == "(":
        count += 1
    if mylist[i] == ")":
        count -= 1
    i += 1
print(i)


