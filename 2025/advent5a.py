ranges = []
ids = []

with open("2025/adventinput5", "r") as mylist:
    for line in mylist:
        item = line.strip()

        if not item:
            continue

        if "-" in item:
            ranges.append(item)
        else:
            ids.append(int(item))

count = 0

for idVal in ids:
    for r in ranges:
        start, end = r.split("-")
        start = int(start)
        end = int(end)

        if start <= idVal <= end:
            count += 1
            break

print(count)



