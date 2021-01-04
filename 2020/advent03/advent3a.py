# https://adventofcode.com/2020/day/3
f1 = open("adventlist3.txt", "r")
mylist = f1.readlines()
print(mylist[0])
print(len(mylist[0][:len(mylist[0])-1]))
print(len(mylist[0].replace("\n", "")))
for i in range(0, len(mylist)):
    mylist[i] = mylist[i].replace("\n", "")
    for j in range(0, 7):
        mylist[i] = mylist[i] + mylist[i]

print (len(mylist))
print (len(mylist[0]))

counter11 = 0
for i in range(0, len(mylist)):
    if mylist[i][i] == "#":
        counter11 = counter11 + 1
print ("I am here 11 " + str(counter11))

counter13 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*3)] == "#":
        counter13 = counter13 + 1
print ("I am here 13 " + str(counter13))

counter15 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*5)] == "#":
        counter15 = counter15 + 1
print ("I am here 15 " + str(counter15))

counter17 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*7)] == "#":
        counter17 = counter17 + 1
print ("I am here 17 " + str(counter17))

counter21 = 0
for i in range(0, int(len(mylist)/2)+1):
    if mylist[i*2][i] == "#":
        counter21 = counter21 + 1
print ("I am here 21 " + str(counter21))

print ("multiple "+str(counter11 * counter13 * counter15 * counter17 * counter21))