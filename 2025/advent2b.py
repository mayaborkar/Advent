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
        length = len(id)

        for size in range(1, length // 2 + 1): # check for all possible segment sizes
            if length % size == 0:
                seg = id[:size]
                if seg * (length // size) == id:
                    invalidId.append(idNum)
                    break

print(sum(invalidId))
