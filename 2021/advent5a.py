f1 = open("adventinput5.txt", "r")
mylist = f1.readlines()

firstCoordinates = []
secondCoordinates = []

for i in range(0, len(mylist)):
    mylist[i] = mylist[i].replace('\n', '')
    firstCoordinates = mylist[i][0].split(',')
    secondCoordinates = mylist[i][1].split(',')
print(mylist)


