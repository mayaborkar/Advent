f1 = open("aventlist3.txt", "r")
mylist = f1.readlines()
totalcount = 0
validcount = 0
invalidcount = 0
for i in range(0, len(mylist)):
    startrange = int(mylist[i][:mylist[i].find("-")])
    endrange = int(mylist[i][mylist[i].find("-")+1:mylist[i].find(" ")])
    letter = mylist[i][mylist[i].find(" ")+1:mylist[i].find(":")]
    pwd = mylist[i][mylist[i].find(":")+2:]
    lettercount = int(pwd.count(letter))
    print(mylist[i])
    print(startrange)
    print(endrange)
    print(letter)
    print(pwd)
    print(lettercount)
    totalcount = totalcount + 1
#    if startrange <= lettercount and lettercount <= endrange:
    if lettercount >= startrange and lettercount <= endrange:
        validcount = validcount + 1
        print("password is valid")
    else:
        invalidcount = invalidcount + 1
        print("pwd is not valid")
print(validcount)
print(invalidcount)
print(totalcount)