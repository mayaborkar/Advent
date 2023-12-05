
f1 = open("adventinput4", "r")
inputlist = f1.readlines()

cardArr = []
numbers = []

winning = []
yourNums = []
count = 0
total = 0

for i in range(0, len(inputlist)):
    cardArr.append(inputlist[i].replace("  ", " ").replace("\n", "").split(":"))
    numbers.append(cardArr[i][1].split("|"))
    print(numbers)
    for j in range(0, len(numbers)):
        winning = (numbers[0][j].split(" "))
        # print(winning)
        yourNums = (numbers[j][1].split(" "))

for k in range(0, len(yourNums)):
    if (yourNums == ''):
        continue
    if(yourNums[k] in winning):
        print(yourNums[k])
        count += 1

print(winning)
print(yourNums)
print(count)
total = 2**(count-2)
print(total)
