f1 = open("adventinput5", "r")

mylist = f1.read().replace("move", "").replace("from", "").replace("to", "").replace("\n", "").replace("  ", "").split()
print(mylist)

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

for i in range(0, len(mylist)):
    move = int(mylist[i][0])
    fromNumber = int(mylist[i][1]) - 1
    toNumber = int(mylist[i][2]) - 1

    print("move " + str(move))
    print("from " + str(fromNumber))
    print("to " + str(toNumber))

    for k in range(0, move):
        if(len(boxes[fromNumber]) == 0):
            print("empty box found")
            continue
        else:
            boxes[toNumber].append(boxes[fromNumber][-1])
            boxes[fromNumber].pop()


for j in range(0, len(boxes)):
    print(boxes[j][-1])





