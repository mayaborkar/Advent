f1 = open("2025/adventinput6", "r")
mylist = [list(line.rstrip("\n")) for line in f1 if line.strip()]

# making all of the rows the same length
maxLen = 0
for row in mylist:
    if len(row) > maxLen:
        maxLen = len(row)

for row in mylist:
    while len(row) < maxLen:
        row.append(' ')

total = 0
col = 0

while col < maxLen:
    allSpaces = True
    for row in mylist:
        if row[col] != ' ':
            allSpaces = False
            break

    if allSpaces:
        col += 1
        continue

    start = col
    while col < maxLen:
        allSpaces = True
        for row in mylist:
            if row[col] != ' ':
                allSpaces = False
                break
        if allSpaces:
            break
        col += 1

    end = col

# getting the problem vertically
    cleaned = []
    for row in mylist:
        piece = ""
        for i in range(start, end):
            piece += row[i]
        piece = piece.strip()
        if piece != "":
            cleaned.append(piece)

    operator = cleaned[-1]

    # Convert number rows
    numbers = []
    for value in cleaned[:-1]:
        numbers.append(int(value))

    # Solve
    if operator == '+':
        result = 0
        for n in numbers:
            result += n
    else:  # '*'
        result = 1
        for n in numbers:
            result *= n

    total += result

print(total)
