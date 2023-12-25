def symbolArray(input):
    specialIndex = []
    notAllowed = "0123456789."

    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            # print(input[i][j])
            if(input[i][j] not in notAllowed):
                specialIndex.append([i,j])

    return specialIndex


def adjacent(input):
    special = symbolArray(input)
    print ('Special ', special)
    print ('input ', input)
    surroundingNums = []

    for c in special:
        if (input[c[0] - 1][ c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
            # surroundingNums.append(input[c[0]-1][c[1] - 1])
        if (input[c[0]][c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "L"))
            # surroundingNums.append(input[c[0]][c[1] - 1])
        if (input[c[0] + 1][ c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
            # surroundingNums.append(input[c[0] + 1][c[1] - 1])
        if (input[c[0] - 1][ c[1]] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
            # surroundingNums.append(input[c[0] - 1][c[1]])
        if (input[c[0] + 1][ c[1]] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
            # surroundingNums.append(input[c[0] + 1][c[1]])
        if (input[c[0] - 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
           # surroundingNums.append(input[c[0] - 1][c[1] + 1])
        if (input[c[0]][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "R"))
            # surroundingNums.append(input[c[0]][c[1] + 1])
        if (input[c[0] + 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D"))
            # surroundingNums.append(input[c[0] + 1][c[1] + 1])


        print(c[0], c[1])
    return('Returning surrounding ', surroundingNums)



def wholeNum(line, position, side):
    print(line[:position])
    if side.__eq__("L"):
        index = line[:position].rfind('.')
        if(index == -1):
            index = 0
        return(line[index:position])
    elif side.__eq__("R"):
        index = line[position:].find('.')
        if(index == len(line)):
            index = len(line)
        return(line[position:index + 1])




f1 = open("adventinput3", "r")
inputlist = f1.read().split('\n')
# print(inputlist)
# check if it is next to/diagonal to a viable symbol
# add all of the viable numbers *10^# the place that they are in
print(wholeNum(inputlist[5], 7, "R"))

#print(adjacent(inputlist))


