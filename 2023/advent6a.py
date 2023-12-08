def currRecord(time, distance):
    count = 0
    for i in range(0, time):
        record = (time-i) * i
        if (record > distance):
            count += 1
    return count

print(currRecord(59,543) * currRecord(68, 1020) * currRecord(82, 1664) * currRecord(74, 1022))


