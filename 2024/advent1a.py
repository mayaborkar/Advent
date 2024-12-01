f1 = open("2024/adventinput1", "r")
# splits by line, then converts it into an integer
# finally converts the list to a tuple
mylist = [tuple(map(int, line.split())) for line in f1.readlines()]

#print(mylist)
mylistFirst = []
mylistSecond = []

for i in range(0, len(mylist)):
    mylistFirst.append(int(mylist[i][0]))
    mylistSecond.append(int(mylist[i][1]))

mylistFirst.sort()
mylistSecond.sort()
# print(mylistFirst)
#print(mylistSecond)
diffList = []
for j in range(0, len(mylistFirst)):
    diffList.append(abs(mylistFirst[j] - mylistSecond[j]))
#print(diffList)
print(sum(diffList))

# 454