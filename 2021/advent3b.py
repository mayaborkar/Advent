# https://adventofcode.com/2021/day/3
f1 = open("adventinput3.txt", "r")
mylist = f1.readlines()

count1 = 0
count0 = 0

oxygenRating = ""
co2Rating = ""

for i in range(0, len(mylist[0])-1):

    count1 = 0
    count0 = 0
    for j in range(0, len(mylist)):
        # print (mylist[j][i])
        if(int(mylist[j][i]) == 1):
            count1 += 1
        else:
            count0 += 1

    
    if(count1 > count0 or count1 == count0):
        oxygenRating += "1"
        co2Rating += "0"
    else:
        oxygenRating += "0"
        co2Rating += "1"

print(int(oxygenRating, 2) * int(co2Rating, 2))


