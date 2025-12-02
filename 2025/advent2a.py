f1 = open("2025/adventinput2", "r")

mylist = f1.read().strip()
ranges = mylist.split(",")

invalidId = []

for r in ranges:
    start, end = r.split("-")
    start = int(start)
    end = int(end)

    for idNum in range(start, end + 1):
        id = str(idNum)
        if (len(id) % 2) == 1:
            continue

        half = len(id) // 2
        if (id[:half] == id[half:]):
            invalidId.append(idNum)

print(sum(invalidId))