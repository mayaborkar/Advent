f1 = open("adventinput1", "r")
mylist = f1.read().split('\n')

# print (mylist[0].replace("one","1"))

# digits = []

currDigitsTens = []
currDigitOnes = []

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

for i in range(0, len(mylist)):
    # print(mylist[i])
    forward = True
    backward = True
    for j in range(0, len(mylist[i])):
        if mylist[i][j].isdigit() and forward:
            currDigitsTens.append(int(mylist[i][j]))
            forward = False
        else:
            if (mylist[i][j:j + 4] in numbers and forward):
                currDigitsTens.append(numbers.get(mylist[i][j:j + 4]))
                forward = False
            elif (mylist[i][j:j + 3] in numbers and forward):
                currDigitsTens.append(numbers.get(mylist[i][j:j + 3]))
                forward = False
            elif (mylist[i][j:j + 5] in numbers and forward):
                currDigitsTens.append(numbers.get(mylist[i][j:j + 5]))
                forward = False
        start = len(mylist[i]) - j
        if mylist[i][start-1:start].isdigit() and backward:
            currDigitOnes.append(int(mylist[i][start-1:start]))
            backward = False
        else:
            # print(mylist[i][start - 5:start])
            if (mylist[i][start-4:start] in numbers and backward):
                currDigitOnes.append(numbers.get(mylist[i][start-4:start]))
                backward = False
            elif (mylist[i][start-3:start] in numbers and backward):
                currDigitOnes.append(numbers.get(mylist[i][start-3:start]))
                backward = False
            elif (mylist[i][start-5:start] in numbers and backward):
                currDigitOnes.append(numbers.get(mylist[i][start-5:start]))
                backward = False



    # print(mylist[i])
print(currDigitsTens)
print(currDigitOnes)

total = (10 * sum(currDigitsTens)) + sum(currDigitOnes)

print(total)

# 54249