def convertToSnafu(decimal):
    final = ""
    current = decimal
    while(current > 0):
        final += str(current % 5)
        current = current//5
    print(final)
    return final



f1 = open("adventinput25", "r")
inputlist = f1.readlines()
mylist = []
current = ""
total = 0
for i in range(0, len(inputlist)):
    number = 0
    currNum = 0
    current = inputlist[i].replace("\n", "")
    current = current[::-1]
    # print(current, current[::-1])
    for j in range(0, len(current)):
        if(current[j] == "-"):
            currNum = -1
        elif(current[j] == "="):
            currNum = -2
        else:
            currNum = int(current[j])
        number += (5**j) * currNum
    total += number
    print(current, number)
    # print(inputlist[i].replace("\n", ""))
print("converted" + str(convertToSnafu(31)))
# convert back to SNAFU
print(total)
print(inputlist)