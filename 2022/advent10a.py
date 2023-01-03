f1 = open("adventtestinput10", "r")
mylist = f1.read().split()
print (mylist)
cycle = 0
x = 1
addxCount = 0
totalSum = 0
while(cycle < 240):
    cycle += 1
    print("cycle = ", cycle,x,mylist[cycle - 1], mylist[cycle])

    if cycle in (20, 60, 100, 140, 180, 220, 240):
        totalSum += x*cycle
        print("current total ", totalSum)

    if(mylist[cycle - 1] == "addx"):
        print("in here")
        # print("adding = " + str(mylist[cycle]))
        x += int(mylist[cycle])
        cycle += 1
        print("cycle = ", cycle, x, mylist[cycle - 1], mylist[cycle])

print("total sum = ", totalSum)
print(mylist)
'''
cycle=1, x=1, noop = mylist[0]
cycle=2, x=1, addx 3  = mylist[cycle-1], 
cycle=3, x=4, addx 3  = mylist[cycle]
cycle=4, x=4, addx -5 = mylist[cycle-1], 
cycle=5, x=-1,addx -5 = mylist[cycle]

noop --> x = 1 cycle = 1
addx 3 --> 1st iteration x = 1 cycle = 2, 2nd iteration x = 4 (3+1) cycle = 3
addx -5 --> 1st iteration x = 4 cycle = 4, 2nd iteration x = -1 (-5 + 4) cycle = 5
'''
# 420
# 1560 ( + 1140)
# 3360 ( + 1800)
# 6300 ( + 2940)
# 9180 ( + 2880)
