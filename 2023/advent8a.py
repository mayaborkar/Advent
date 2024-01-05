f1 = open("adventinput8", "r")
mylist = f1.read().split('\n')
print(mylist)

instructions = mylist[0]
print(instructions)
node = []
graph = {}


for i in range(2, len(mylist)):
    node.append(mylist[i].split(" = "))

for j in range(0, len(node)):
    # print(node[j][0], node[j][1])

    graph[node[j][0]] = node[j][1].replace("(", "").replace(")", "").replace(" ", "").split(",")

print(graph)
stepCount = 0
key = 'AAA'
newPos = []

while(key.__ne__('ZZZ')):
    for i in range(0, len(instructions)):
        # print (graph[key])
        newPos = graph[key]
        if (instructions[i].__eq__('R')):
            key = newPos[1]
        else:
            key = newPos[0]
        stepCount += 1
        if key == 'ZZZ':
            break
    if (key.__eq__('ZZZ')):
        print(stepCount)
        break






'''
depending on the character in the left or right string pick 0 or 1
then store that value and search for if before the equal to sign
keep going again til you find the ZZZ

store as a key and value pair --> each key has 2 attributes R / L

datasets
1. how to initialize
2. how to add data to it
3. how to update a value
4. how to remove one value
4. how to delete everything from it

dictionary
1. dict = {
"key1": value1,
"key2": value2
}
2. get()
3. update()
4. pop()
5. del()
'''