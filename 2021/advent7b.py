f1 = open("adventtestinput7b.txt", "r")
mylist = f1.read()

crabList = mylist.split(',')

# using for loop for each crab pos
print(crabList)
crabDistance = []
for i in range(0, len(crabList)):
    totalFuel = 0
    for j in range(0, len(crabList)):
        totalFuel += ((int(crabList[i]))/2) * (int(crabList[i]) + 1)
    crabDistance.append([crabList[i], totalFuel])

index = 0
leastFuel = crabDistance[0][1]
for i in range(0, len(crabDistance)):
    if crabDistance[i][1] < leastFuel:
        index = i
        leastFuel = crabDistance[i][1]
print(crabDistance[index])