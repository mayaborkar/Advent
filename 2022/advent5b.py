f1 = open("adventinput5", "r")

myinputlist = f1.readlines()

'''
                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
 1   2   3   4   5   6   7   8   9 
'''
boxes = [["Z", "J", "N", "W", "P", "S"],
          ["G", "S", "T"],
          ["V", "Q", "R", "L", "H"],
          ["V", "S", "T", "D"],
          ["Q", "Z", "T", "D", "B", "M", "J"],
          ["M", "W", "T", "J", "D", "C", "Z", "L"],
          ["L", "P", "M", "W", "G", "T", "J"],
          ["N", "G", "M", "T", "B", "F", "Q", "H"],
          ["R", "D", "G", "C", "P", "B", "Q", "W"]]

# move x (first number given) from i (2nd number given) to j (third number given)
mylist = []
for i in range(0, len(myinputlist)):
    mylist.append(myinputlist[i].replace("\n", "").split())
    move = int(mylist[i][1])
    fromNumber = int(mylist[i][3]) - 1
    toNumber = int(mylist[i][5]) - 1

    print("move " + str(move))
    print("from " + str(fromNumber))
    print("to " + str(toNumber))


    for k in range(0, move):
        boxes[toNumber].append(boxes[fromNumber][-move + k])
        boxes[fromNumber].pop(-move + k)


outStr = ""
for j in range(0, len(boxes)):
    outStr += boxes[j][-1]
print(outStr)





