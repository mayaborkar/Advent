f1 = open("2025/adventinput4", "r")
mylist = [line.strip() for line in f1 if line.strip()]

rows = len(mylist)
cols = len(mylist[0])


directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

accessible = 0

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
                accessible += 1

print(accessible)