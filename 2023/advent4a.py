f1 = open("adventinput4", "r")
inputlist = f1.readlines()

cardArr = []
numbers = []

count = 0
total = 0

# print (inputlist)

for i in range(0, len(inputlist)):
    count = 0
    cardArr.append(inputlist[i].replace("  ", " ").replace("\n", "").split(":"))
    # print (cardArr)
    numbers = (cardArr[i][1].split(" | "))
    numbers1 = numbers[0].split(' ')
    numbers2 = numbers[1].split(' ')
    # print (numbers1)
    for k in numbers1:
        if (k == ''):
            continue
        if(k in numbers2):
            count += 1
            # print('match ', k, numbers)
    if (count > 0):
        total += 2**(count-1)


# print(count)
print(total)


#23384 --> too high