'''
Docstring for 2025.advent5b

Sort ranges by starting value
    This ensures overlapping ranges appear next to each other

Set totalFresh to 0

Set currentStart to the start of the first range
Set currentEnd to the end of the first range

For each remaining range (start, end) in ranges:

    If start is less than or equal to currentEnd + 1:
        This means the new range overlaps with or touches the current range,
        so both ranges represent the same continuous set of IDs

        Set currentEnd to the maximum of currentEnd and end
        This extends the current range to include all IDs from both ranges

    Else:
        This means the new range is completely separate from the current range,
        so the current range can be finalized

        Add (currentEnd − currentStart + 1) to totalFresh
        This counts how many unique IDs are covered by the finished range

        Set currentStart to start
        Set currentEnd to end
        This starts tracking a new range

Add (currentEnd − currentStart + 1) to totalFresh
    This accounts for the final range after the loop ends

Output totalFresh

'''
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
