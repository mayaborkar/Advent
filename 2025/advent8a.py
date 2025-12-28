import math
from collections import defaultdict

# Read input
points = []
with open("adventinput8", "r") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        points.append((x, y, z))

n = len(points)

# Union-Find (Disjoint Set Union)
parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# Compute all distances
pairs = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        dist = math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )
        pairs.append((dist, i, j))

# Sort by distance
pairs.sort()

# Connect the 1000 closest pairs
for k in range(1000):
    _, i, j = pairs[k]
    union(i, j)

# Count component sizes
components = defaultdict(int)
for i in range(n):
    components[find(i)] += 1

# Find the three largest
sizes = sorted(components.values(), reverse=True)
result = sizes[0] * sizes[1] * sizes[2]

print(result)
