
from collections import Counter

f1 = open("2024/adventinput1", "r")
# splits by line, then converts it into an integer
# finally converts the list to a tuple
mylist = [tuple(map(int, line.split())) for line in f1.readlines()]

#print(mylist)
mylistFirst = []
mylistSecond = []

for i in range(0, len(mylist)):
    mylistFirst.append(int(mylist[i][0]))
    mylistSecond.append(int(mylist[i][1]))

# counter --> 
'''
Counter takes a list as input and creates a dictionary where:
Keys are the unique elements
Values are the counts (frequency) of those elements
'''
right_count = Counter(mylistFirst)

similarity_score = sum(num * right_count[num] for num in mylistSecond)

print(similarity_score)