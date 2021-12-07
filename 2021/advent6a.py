# https://adventofcode.com/2021/day/3
f1 = open("adventinput6.txt", "r")
mylist = f1.readlines()

fishList = mylist[0].replace("\n", "").split(",")


count0 = fishList.count("0")
count1 = fishList.count("1")
count2 = fishList.count("2")
count3 = fishList.count("3")
count4 = fishList.count("4")
count5 = fishList.count("5")
count6 = fishList.count("6")
count7 = fishList.count("7")
count8 = fishList.count("8")


for i in range(0, 256):
    temp = count0
    count0 = count1
    count1 = count2
    count2 = count3
    count3 = count4
    count4 = count5
    count5 = count6
    count6 = count7 + temp
    count7 = count8
    count8 = temp

print(count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8)

# print(count3)
print(fishList)