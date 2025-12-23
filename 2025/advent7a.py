# read the input
f = open("2025/adventinput7", "r")
grid = [list(line.rstrip("\n")) for line in f if line.strip()]

numRows = len(grid)
numCols = len(grid[0])

# find starting column S (always in the first row)
startCol = -1
for col in range(numCols):
    if grid[0][col] == 'S':
        startCol = col
        break

activeBeams = {startCol}
splitCount = 0

# process each row below S
for row in range(1, numRows):
    nextBeams = set()

    for col in activeBeams:
        if grid[row][col] == '^':
            splitCount += 1

            if col - 1 >= 0:
                nextBeams.add(col - 1)
            if col + 1 < numCols:
                nextBeams.add(col + 1)
        else:
            nextBeams.add(col)

    activeBeams = nextBeams

    # stop if no beams remain
    if len(activeBeams) == 0:
        break

print(splitCount)
