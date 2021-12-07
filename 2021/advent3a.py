# https://adventofcode.com/2021/day/3
f1 = open("adventinput3.txt", "r")
mylist = f1.readlines()

count1 = 0
count0 = 0

gammaRayString = ""
epsilonString = ""

for i in range(0, len(mylist[0])-1):

    count1 = 0
    count0 = 0
    for j in range(0, len(mylist)):
        # print (mylist[j][i])
        if(int(mylist[j][i]) == 1):
            count1 += 1
        else:
            count0 += 1

    if(count1 > count0):
        gammaRayString += "1"
        epsilonString += "0"
    else:
        gammaRayString += "0"
        epsilonString += "1"

print(int(gammaRayString, 2) * int(epsilonString, 2))
print(gammaRayString)
print(epsilonString)


