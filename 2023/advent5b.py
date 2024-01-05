def readFiles(fileName, s1):
    f1 = open(fileName, "r")
    mylist = [cx.split(' ') for cx in f1.read().split('\n')]
    return findLocation(mylist, s1)


def findLocation(arr, s1):
    for c in arr:
        if (int(c[1]) <= int(s1) and int(s1) < int(c[1]) + int(c[2])):
            return (int(s1) - int(c[1]) + int(c[0]))
    return int(s1)


def overlap(range1, range2):
    # given two tuples see if their ranges intersect
    # should return a tuple
    start1, end1 = range1
    start2, end2 = range2

    # Check if ranges intersect
    if start1 <= end2 and start2 <= end1:
        # Calculate intersection
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)
        return (intersection_start, intersection_end)
    else:
        # No intersection
        return -1

def overlapList(range, mappings):




f1 = open("adventinput5", "r")
seedList = f1.read().split(" ")
#print(findLocation(mylist, 79))
print(seedList)
location = []
print(overlap((50, 60), (55, 70)))
'''
for i in range(0, len(seedList)):
    location.append(readFiles("htol",
        readFiles("ttoh",
        readFiles("ltot",
        readFiles("wtol",
        readFiles("ftow",
        readFiles("stof",
        readFiles("stos", seedList[i]))))))))
'''
# print(min(location))