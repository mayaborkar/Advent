# https://adventofcode.com/2021/day/2
import re
f1 = open("adventinput2", "r")
mylist = f1.readlines()

horizontalPos = 0
depth = 0
aim = 0

for i in range(0, len(mylist)):
    direction = mylist[i].split()
    if(direction[0] == "forward"):
        horizontalPos += int(direction[1])
        depth += (aim * int(direction[1]))

    elif(direction[0] == "down"):
        aim += int(direction[1])

    elif(direction[0] == "up"):
        aim -= int(direction[1])

print(horizontalPos * depth)


'''
print(re.findall("^forward", mylist))
print(re.findall("[^\s]+", mylist))

direction = ""
moveAmount = 0

if(re.findall("^forward", mylist)):
    horizontalPos += int(re.findall("[^\s]+", mylist))
    
print(re.findall("^forward", mylist))
print(int(re.findall("[^\s]+", mylist)))

if(re.findall("^down", mylist)):
    depth += int(re.findall("[^\s]+", mylist))

if(re.findall("^up", mylist)):
    depth -= int(re.findall("[^\s]+", mylist))

print(horizontalPos * depth)
'''





