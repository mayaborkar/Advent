def readFiles(fileName, s1):
    f1 = open(fileName, "r")
    mylist = [cx.split(' ') for cx in f1.read().split('\n')]
    return findLocation(mylist, s1)


def findLocation(arr, s1):
    for c in arr:
        if (int(c[1]) <= int(s1) and int(s1) < int(c[1]) + int(c[2])):
            return (int(s1) - int(c[1]) + int(c[0]))
    return int(s1)


f1 = open("adventinput5", "r")
seedList = f1.read().split(" ")
#print(findLocation(mylist, 79))
print(seedList)
location = []
for i in range(0, len(seedList)):
    location.append(readFiles("htol",
        readFiles("ttoh",
        readFiles("ltot",
        readFiles("wtol",
        readFiles("ftow",
        readFiles("stof",
        readFiles("stos", seedList[i]))))))))

print(min(location))