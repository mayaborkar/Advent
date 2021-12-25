f1 = open("adventinput7.txt", "r")
mylist = f1.read()

crabList = mylist.split(',')

# using for loop for each crab pos
print(crabList)
crabDistance = []
for i in range(0, len(crabList)):
    totalFuel = 0
    for j in range(0, len(crabList)):
        totalFuel += abs(int(crabList[i]) - int(crabList[j]))
    crabDistance.append([crabList[i], totalFuel])

index = 0
leastFuel = crabDistance[0][1]
for i in range(0, len(crabDistance)):
    if crabDistance[i][1] < leastFuel:
        index = i
        leastFuel = crabDistance[i][1]
print(crabDistance[index])

'''
# using average
sum = 0
for i in range(0, len(crabList)):
    sum += int(crabList[i])
average = sum/(len(crabList))

# fuel amount
fuelAmount = 0
for i in range(0, len(crabList)):
    fuelAmount += abs(int(crabList[i]) - average)
print(fuelAmount)
'''