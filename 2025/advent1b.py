f1 = open("2025/adventinput1", "r")

mylist = [line.strip() for line in f1 if line.strip()]

position = 50
count = 0

for line in mylist:
    direction = line[0]
    distance = int(line[1:])

    if direction == 'R':
        step = 1
    else:
        step = -1

    for i in range(distance):
        position = (position + step) % 100

        if position == 0:
            count += 1

print(count)
