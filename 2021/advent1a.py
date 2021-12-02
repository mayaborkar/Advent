# https://adventofcode.com/2020/day/1
f1 = open("adventinput1.txt", "r")
mylist = f1.readlines()
# Did len(mylist)-1) to prevent the j for loop from going out of range
count = 0
for i in range(0, len(mylist)-1):

    if(int (mylist[i]) - int(mylist[i+1]) < 0):
        count += 1

print (count)