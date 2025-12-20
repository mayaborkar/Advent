f = open("2025/adventinput6", "r")
grid = [list(line.rstrip("\n")) for line in f if line.strip()]

maxLen = 0
for row in grid:
    if len(row) > maxLen:
        maxLen = len(row)

for row in grid:
    while len(row) < maxLen:
        row.append(' ')

total = 0
col = 0

while col < maxLen:
    empty = True
    for row in grid:
        if row[col] != ' ':
            empty = False
            break

    if empty:
        col += 1
        continue

    start = col
    while col < maxLen:
        empty = True
        for row in grid:
            if row[col] != ' ':
                empty = False
                break
        if empty:
            break
        col += 1
    end = col

    problem = []
    for row in grid:
        s = ""
        for i in range(start, end):
            s += row[i]
        if s.strip():
            problem.append(s.rstrip())

    operator = problem[-1]
    digRows = problem[:-1]

    num_cols = 0
    for r in digRows:
        if len(r) > num_cols:
            num_cols = len(r)

    padded = []
    for r in digRows:
        padded.append(r.ljust(num_cols))

    # Build numbers: column = number
    numbers = []
    for c in range(num_cols - 1, -1, -1):   # right → left
        num = ""
        for r in range(len(padded)):        # top → bottom
            if padded[r][c] != ' ':
                num += padded[r][c]
        if num != "":
            numbers.append(int(num))

    if operator == '+':
        value = 0
        for n in numbers:
            value += n
    else:
        value = 1
        for n in numbers:
            value *= n

    total += value

print(total)
