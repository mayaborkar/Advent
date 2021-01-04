# https://adventofcode.com/2020/day/1
# for day 1 part b
f1 = open("adventlist2.txt", "r")
mylist = f1.readlines()
# Did len(mylist)-1) to prevent the j for loop from going out of range
for i in range(0, len(mylist)-1):
    for j in range(i+1, len(mylist)):
        # if x+y+z does not equal 2020 the for loop continues and the index value increments by 1
        for k in range(j+1, len(mylist)):
            stx = mylist[i]
            # first number
            x = int(stx[0:len(stx)-1])
            stx = mylist[j]
            # second number
            y = int(stx[0:len(stx)-1])
            stx = mylist[k]
            # third number
            z = int(stx[0:len(stx)-1])
            # finding the product
            if x + y + z == 2020:
                print('x = '+str(x)+' y = '+str(y)+' z='+str(z)+' product xyz = '+str(x * y * z))
