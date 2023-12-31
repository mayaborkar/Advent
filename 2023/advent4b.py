f1 = open("adventinput4", "r")

mylist = [c1.split(': ') for c1 in [c.replace('\n', '') for c in f1.readlines()]]

match = []
for i in range (0,len(mylist)):
    current = [c2.split(' ') for c2 in mylist[i][1].split(' | ')]
    n = 0
    for j in current[0]:
        if j.__eq__(''):
            continue
        elif j in current[1]:
            n += 1
    match.append(n)

cards = []
for i in mylist:
    cards.append(1)


for i in range(0, len(cards)):
    for j in range(i, i+int(match[i-1])):
        if j <= len(cards):
            cards[j] += cards[i-1]
            print(i,j,cards)

print (cards)
total = 0
for i in cards:
    total += i
print(total)
# 5132675