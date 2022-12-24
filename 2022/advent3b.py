f1 = open("adventinput3", "r")
mylist = f1.read().split("\n")

sum = 0
first = ""
middle = ""
last = ""
for i in range(0, len(mylist) - 2):
    first = mylist[i]
    middle = mylist[i+1]
    last = mylist[i+2]
    print(first)
    print(middle)
    print(last)
    com_str = ''.join(set(first).intersection(last).intersection(middle))
    if ord(com_str) >= 97:
        sum += ord(com_str) - 96
        # print(ord(com_str) - 96)
    elif ord(com_str) <= 90:
        sum += ord(com_str) - 38
        # print(ord(com_str) - 38)
    i += 3
    print(com_str)
    print(sum)

