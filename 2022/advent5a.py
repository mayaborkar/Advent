f1 = open("adventinput5", "r")

mylist = f1.read().replace("move", "").replace("from", "").replace("to", "").replace("\n", "").split(" ")
print(mylist)
'''
boxes = [][]
boxes[0][0] = "Z"
boxes[0][1] = "N"
boxes[0][2] = "D"
boxes[1][0] = "M"
boxes[1][1] = "C"
boxes[2][0] = "P"
'''


# move x (first number given) from i (2nd number given) to j (third number given)
'''
k = 0
x = mylist[k][0]
while(int(x) > 0):
    x = mylist[k]
    i = mylist[k][1]
    j = mylist[k][2]

    print("i = " + i)
    print("x = " + x)
    print("j = " + j)
'''
'''
    boxes[j].append(boxes[i][len(boxes[i])])
    boxes[i].pop()
     x -= 1
     '''
