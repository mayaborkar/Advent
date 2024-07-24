import re

f1 = open("adventinput5", "r")
mylist = f1.read().split()
naughty = 0

for s in mylist:
    if re.match(r"\w*(\w\w)\w*\1\w*", s) is None:
        naughty += 1
    elif re.match(r"\w*(\w)[^\1]\1\w*", s) is None:
        naughty += 1

print(len(mylist)-naughty)