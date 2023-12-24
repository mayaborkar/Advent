def symbolArray(input):
    specialIndex = []
    notAllowed = "0123456789."
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if(input[i][j] not in notAllowed):
                specialIndex.append([i,j])


f1 = open("adventinput3", "r")
inputlist = f1.readlines()

# check if it is next to/diagonal to a viable symbol
# add all of the viable numbers *10^# the place that they are in

for i in range(0, len(inputlist)):
    for j in range(0, len(inputlist[i])):


