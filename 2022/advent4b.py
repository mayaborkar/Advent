def contained(start1, end1, start2, end2):
    if ((start1 <= start2) and (end1 >= end2)) or ((start2 <= start1) and (end2 >= end1)) or ((start1 >= start2) and (start1 <= end2)) or ((end1 >= start2) and (end1 <= end2)):
        return 1
    return 0


f1 = open("adventinput4", "r")
inputlist = f1.readlines()
count = 0
for i in range(0, len(inputlist)):
    print(inputlist[i].replace('\n', ''))
    givenStart1 = int(inputlist[i].replace('\n', '').split(",")[0].split("-")[0])
    givenEnd1 = int(inputlist[i].replace('\n', '').split(",")[0].split("-")[1])
    givenStart2 = int(inputlist[i].replace('\n', '').split(",")[1].split("-")[0])
    givenEnd2 = int(inputlist[i].replace('\n', '').split(",")[1].split("-")[1])

    count += contained(givenStart1, givenEnd1, givenStart2, givenEnd2)

print(count)