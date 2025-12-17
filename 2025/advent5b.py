ranges = []

with open("2025/adventinput5", "r") as mylist:
    for line in mylist:
        item = line.strip()

        if not item:
            continue

        if "-" in item:
            start, end = map(int, item.split("-"))
            ranges.append((start, end))

ranges.sort()

total = 0

current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        total += current_end - current_start + 1
        current_start, current_end = start, end

total += current_end - current_start + 1

print(total)
