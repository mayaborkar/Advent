f1 = open("adventinput1", "r")
mylist = f1.read().split('\n')

sets = []
gameid = []
for i in range(0, len(mylist)):
    sets.append(mylist[i].split(';'))
    gameid.append(mylist[i].split(':'))
