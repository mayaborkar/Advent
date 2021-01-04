# https://adventofcode.com/2020/day/3
f1 = open("adventlist3.txt", "r")
mylist = f1.readlines()
print(mylist[0])
print(len(mylist[0][:len(mylist[0])-1]))
# replacing \n to null
print(len(mylist[0].replace("\n", "")))
# removing \n from each line
for i in range(0, len(mylist)):
    mylist[i] = mylist[i].replace("\n", "")
    # duplicating the file 7 times so that the other for loops do not go out of range
    for j in range(0, 7):
        mylist[i] = mylist[i] + mylist[i]

print (len(mylist))
print (len(mylist[0]))

# checking if down 1 over 1 has a tree
# if it does increasing the counter by 1
counter11 = 0
for i in range(0, len(mylist)):
    if mylist[i][i] == "#":
        counter11 = counter11 + 1
print ("I am here 11 " + str(counter11))

# checking if down 1 over 3 has a tree
# if it does increasing the counter by 1
counter13 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*3)] == "#":
        counter13 = counter13 + 1
print ("I am here 13 " + str(counter13))

# checking if down 1 over 5 has a tree
# if it does increasing the counter by 1
counter15 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*5)] == "#":
        counter15 = counter15 + 1
print ("I am here 15 " + str(counter15))

# checking if down 1 over 7 has a tree
# if it does increasing the counter by 1
counter17 = 0
for i in range(0, len(mylist)):
    if mylist[i][(i*7)] == "#":
        counter17 = counter17 + 1
print ("I am here 17 " + str(counter17))

# checking if down 2 over 1 has a tree
# if it does increasing the counter by 1
counter21 = 0
for i in range(0, int(len(mylist)/2)+1):
    if mylist[i*2][i] == "#":
        counter21 = counter21 + 1
print ("I am here 21 " + str(counter21))

# multiplying all of the counters together
print ("multiple "+str(counter11 * counter13 * counter15 * counter17 * counter21))