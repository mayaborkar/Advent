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
    startEnd = []

    for c in special:
        if (input[c[0] - 1][ c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
            # surroundingNums.append(input[c[0]-1][c[1] - 1])
        if (input[c[0]][c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "L", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "L", startEnd)[1])
            # surroundingNums.append(input[c[0]][c[1] - 1])
        if (input[c[0] + 1][ c[1] - 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
            # surroundingNums.append(input[c[0] + 1][c[1] - 1])
        if (input[c[0] - 1][ c[1]] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
            # surroundingNums.append(input[c[0] - 1][c[1]])
        if (input[c[0] + 1][ c[1]] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
            # surroundingNums.append(input[c[0] + 1][c[1]])
        if (input[c[0] - 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd[0]))
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
           # surroundingNums.append(input[c[0] - 1][c[1] + 1])
        if (input[c[0]][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "R", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "R", startEnd)[1])
            # surroundingNums.append(input[c[0]][c[1] + 1])
        if (input[c[0] + 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(wholeNum(input[c[0]], c[1], "D", startEnd)[0])
            startEnd.append(wholeNum(input[c[0]], c[1], "D", startEnd)[1])
            # surroundingNums.append(input[c[0] + 1][c[1] + 1])


        print(c[0], c[1])
    return('Returning surrounding ', surroundingNums)



def wholeNum(line, position, side, startEndArr):
    print(line[:position])
    if side.__eq__("L"):
        index = line[:position].rfind('.')
        if(index == -1):
            index = 0
        if [index, position] not in startEndArr:
            startEndArr.append([index, position])
            return(line[index:position], startEndArr)
    elif side.__eq__("R"):
        index = line[position:].find('.')
        print(index)
        if(index == -1):
            index = len(line)
        if [position + 1, position + index] not in startEndArr:
            startEndArr.append([position + 1, position + index])
            return(line[position + 1: position + index], startEndArr)

    elif side.__eq__("D"):
        indexl = line[position:].find('.')
        indexr = line[:position].rfind('.')
        if(indexl == -1):
            indexl = 0
        if(indexr == -1):
            indexr = len(line)
        if [indexl, position + indexr] not in startEndArr:
            startEndArr.append([indexl, position + indexr])
            return(line[indexl:position + indexr], startEndArr)





f1 = open("adventinput3", "r")
inputlist = f1.read().split('\n')
# print(inputlist)
# check if it is next to/diagonal to a viable symbol
# add all of the viable numbers *10^# the place that they are in
# print(wholeNum(inputlist[5], 6, "R"))

print(sum(adjacent(inputlist)))
#print(adjacent(inputlist))
