'''
if the key of the last character is A start the process with it
continue til both are ending with Z
'''
def ghost_Node(graph, ANode):
    steps(graph, ANode)


def steps(graph, ANode):
    stepCount = 0
    key = ANode[0]

    while (key[-1].__ne__('Z')):
        for i in range(0, len(instructions)):
            print(graph[key])
            newPos = graph[key]
            if (instructions[i].__eq__('R')):
                key = newPos[1]
            else:
                key = newPos[0]
            stepCount += 1
            if key[-1] == 'Z':
                break

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

ANodes = [node for node in graph.keys() if node[-1].__eq__('A')]
print(ANodes)

print(graph)
