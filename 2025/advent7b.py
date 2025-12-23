# read the input
f = open("2025/adventinput7", "r")
grid = [list(line.rstrip("\n")) for line in f if line.strip()]

numRows = len(grid)
numCols = len(grid[0])

# find starting column
startCol = -1
for col in range(numCols):
    if grid[0][col] == 'S':
        startCol = col
        break

# maps column -> number of timelines at that column
activeTimelines = {startCol: 1}

# process each row
for row in range(1, numRows):
    nextTimelines = {}

    for col in activeTimelines:
        count = activeTimelines[col]

        if grid[row][col] == '^':
            # timeline splits
            if col - 1 >= 0:
                nextTimelines[col - 1] = nextTimelines.get(col - 1, 0) + count
            if col + 1 < numCols:
                nextTimelines[col + 1] = nextTimelines.get(col + 1, 0) + count
        else:
            # timeline continues straight
            nextTimelines[col] = nextTimelines.get(col, 0) + count

    activeTimelines = nextTimelines

    if len(activeTimelines) == 0:
        break

# total timelines is sum of all remaining paths
totalTimelines = 0
for count in activeTimelines.values():
    totalTimelines += count

print(totalTimelines)
