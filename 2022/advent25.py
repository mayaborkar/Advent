f1 = open("adventtestinput25", "r")
inputlist = f1.readlines()
mylist = []
for i in range(0, len(inputlist)):
    mylist.append(inputlist[i].replace("=", "-2").replace("-", "-1").split())
total = 0



print(mylist)