# https://adventofcode.com/2020/day/1
f1 = open("adventinput1.txt", "r")
mylist = f1.readlines()
# Did len(mylist)-1) to prevent the j for loop from going out of range
sum1 = 0
sum2 = 0
count = 0

for i in range(0, len(mylist)-3):
    sum1 = int(mylist[i]) + int(mylist[i+1]) + int(mylist[i+2])
    sum2 = int(mylist[i+1]) + int(mylist[i + 2]) + int(mylist[i+3])
    if(sum2 - sum1 > 0):
        count += 1

print (count)