# two compartments first 1/2 --> first compartment, second 1/2 second compartment
# lowercase 1-26 uppercase 27-52
# add priorities

f1 = open("adventinput3", "r")
mylist = f1.read().split("\n")
first = ""
last = ""
sum = 0

for i in range(0, len(mylist)):
    first = mylist[i][:len(mylist[i])//2]
    last = mylist[i][len(mylist[i])// 2:]
    # print(first)
    # print(last)
    com_str = ''.join(set(first).intersection(last))
    # print(com_str)
    if ord(com_str) >= 97:
        sum += ord(com_str) - 96
        # print(ord(com_str) - 96)
    elif ord(com_str) <= 90:
        sum += ord(com_str) - 38
        # print(ord(com_str) - 38)
    print(sum)

# going into both for loops