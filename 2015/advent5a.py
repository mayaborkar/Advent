import re

f1 = open("adventinput5", "r")
mylist = f1.read().split()
print(mylist)

vowels = ['a', 'e', 'i', 'o', 'u']

naughty = 0

for s in mylist:
    if re.match(r"\w*(ab|cd|pq|xy)\w*", s):
        naughty += 1
    elif re.match(r"\w*(\w)\1{1,}\w*", s) is None:
        naughty += 1
    elif len([c for c in s if c in vowels])<3:
        naughty += 1

print(len(mylist)-naughty)