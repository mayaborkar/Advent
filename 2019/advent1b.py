f1 = open("adventinput1", "r")
mylist = f1.read().split("\n")
totalFuel = 0
for i in range(0, len(mylist)):
    totalFuel += (int(mylist[i])//3) - 2
print(totalFuel)