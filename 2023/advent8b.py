'''
if the key of the last character is A start the process with it
continue til both are ending with Z
'''
def find_LCM(num1, num2):
    lcm = 0
    for i in range(max(num1, num2), 1 + (num1 * num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break
    return lcm


def ghost_Node(graph, ANode):
    steps(graph, ANode)


def steps(graph, ANode):
    stepCount = 0
    key = ANode
    newPos = []

    while (key[-1].__ne__('Z')):
        for i in range(0, len(instructions)):
            # print (graph[key])
            newPos = graph[key]
            if (instructions[i].__eq__('R')):
                key = newPos[1]
            else:
                key = newPos[0]
            stepCount += 1
            if key[-1] == 'Z':
                break
        if (key[-1].__eq__('Z')):
            return(stepCount)
            break


f1 = open("adventinput8", "r")
mylist = f1.read().split('\n')
# print(mylist)

instructions = mylist[0]
# print(instructions)
node = []
graph = {}


for i in range(2, len(mylist)):
    node.append(mylist[i].split(" = "))

for j in range(0, len(node)):
    # print(node[j][0], node[j][1])

    graph[node[j][0]] = node[j][1].replace("(", "").replace(")", "").replace(" ", "").split(",")


stepArr = []
ANodes = [node for node in graph.keys() if node[-1].__eq__('A')]
for k in range(0, len(ANodes)):
    stepArr.append(steps(graph, ANodes[k]))



# 3302684280
# 15746133679061
print(stepArr)