'''
Docstring for 2025.advent4b

Set totalRemoved to 0

Repeat:

    Create an empty list called removable

    Go through every position in the grid:

        If there is a roll of paper at this position:

            Count how many of the 8 surrounding positions
            also contain a roll of paper

            If the number of surrounding rolls is less than 4:
                Add this position to removable

    If removable is empty:
        Stop repeating

    For every position in removable:
        Remove the roll of paper at that position
        Increase totalRemoved by 1

Output totalRemoved

'''

f1 = open("2025/adventinput4", "r")
mylist = [list(line.strip()) for line in f1 if line.strip()]

rows = len(mylist)
cols = len(mylist[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

totalRemoved = 0

while True:
    toRemove = []

    for i in range(rows):
        for j in range(cols):
            if mylist[i][j] == '@':
                adjacent = 0

                for drow, dcol in directions:
                    nr = i + drow
                    nc = j + dcol

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if mylist[nr][nc] == '@':
                            adjacent += 1

                if adjacent < 4:
                    toRemove.append((i, j))

    if not toRemove:
        break

    for i, j in toRemove:
        mylist[i][j] = '.'
        totalRemoved += 1

print(totalRemoved)
