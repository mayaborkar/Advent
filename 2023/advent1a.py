def wordToNum(current):



f1 = open("adventinput1", "r")
mylist = f1.read().split('\n')

digits = []
currentDigits = []
for i in range(0, len(mylist)):
    currentDigits = []
    for j in range(0, len(mylist[i])):
        if mylist[i][j].isdigit():
            currentDigits.append(mylist[i][j])
    if (len(currentDigits) > 0):
        digits.append(currentDigits[0])
        digits.append(currentDigits[len(currentDigits) - 1])

    print(mylist[i])

total = 0
for k in range(0, len(digits)):
    if k % 2 == 0:
        total += 10 * int(digits[k])
    else:
        total += int(digits[k])

print(total)
print(digits)
