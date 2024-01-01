def wordsToDigits(arr, i, j, num):
    if (arr[i][j:j + len(num)].__eq__(num)):
        return True
    return False


f1 = open("adventinput1", "r")
mylist = f1.read().split('\n')

digits = []
currentDigits = []
forward = True

for i in range(0, len(mylist)):
    print(mylist[i])
    currentDigits = []
    for j in range(0, len(mylist[i])):
        if mylist[i][j].isdigit() and forward:
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
