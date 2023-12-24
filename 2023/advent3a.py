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
            surroundingNums.append(input[c[0]-1][c[1] - 1])
        if (input[c[0]][ c[1] - 1] in '0123456789'):
            surroundingNums.append(input[c[0]][c[1] - 1])
        if (input[c[0] + 1][ c[1] - 1] in '0123456789'):
            surroundingNums.append(input[c[0] + 1][c[1] - 1])
        if (input[c[0] - 1][ c[1]] in '0123456789'):
            surroundingNums.append(input[c[0] - 1][c[1]])
        if (input[c[0] + 1][ c[1]] in '0123456789'):
            surroundingNums.append(input[c[0] + 1][c[1]])
        if (input[c[0] - 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(input[c[0] - 1][c[1] + 1])
        if (input[c[0]][ c[1] + 1] in '0123456789'):
            surroundingNums.append(input[c[0]][c[1] + 1])
        if (input[c[0] + 1][ c[1] + 1] in '0123456789'):
            surroundingNums.append(input[c[0] + 1][c[1] + 1])


        print(c[0], c[1])
    '''
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            try:
                print("here ", input[i][j], i, j)
                if(([i - 1, j - 1] or
                [i, j - 1] or
                [i + 1, j - 1] or
                [i - 1, j] or
                [i + 1,j] or
                [i - 1, j + 1] or
                [i, j + 1] or
                [i + 1, j + 1]) in special):
                    print("inside")
                    print(special)
                    if input[i][j] in '0123456789' :
                        surroundingNums.append(input[i][j])
                        print (surroundingNums)
            except:
                print("error ",NameError)
                continue
    '''
    return('Returning surrounding ', surroundingNums)







f1 = open("adventinput3", "r")
inputlist = f1.read().split('\n')
# print(inputlist)
# check if it is next to/diagonal to a viable symbol
# add all of the viable numbers *10^# the place that they are in

print(adjacent(inputlist))


