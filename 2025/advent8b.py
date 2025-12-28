import math

# Read input
points = []
with open("adventinput8", "r") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        points.append((x, y, z))

n = len(points)

# Union-Find
parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

# Compute all distances
edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        dist = math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )
        edges.append((dist, i, j))

edges.sort()

components = n

# Kruskal until fully connected
for _, i, j in edges:
    if union(i, j):
        components -= 1
        if components == 1:
            x1 = points[i][0]
            x2 = points[j][0]
            print(x1 * x2)
            break
