f1 = open("adventinput1", "r")
mylist = f1.readlines()

caloriesArray = []
sum = 0
for i in range(0, len(mylist)):
    if mylist[i] == "\n":
        caloriesArray.append(sum)
        sum = 0
    else:
        sum += int(mylist[i])
caloriesArray.sort()
print(caloriesArray[len(caloriesArray) - 1] + caloriesArray[len(caloriesArray) - 2] + caloriesArray[len(caloriesArray) - 3])

