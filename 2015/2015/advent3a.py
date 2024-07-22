f1 = open("adventinput3", "r")
mylist = f1.read()

history = [(0,0)]

for i in range(len(mylist)):
    last = history[-1]
    if mylist[i]=='v':
        history.append((last[0],last[1]-1))
    elif mylist[i]=='^':
        history.append((last[0],last[1]+1))
    elif mylist[i]=='>':
        history.append((last[0]+1,last[1]))
    elif mylist[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))