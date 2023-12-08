def currRecord(time, distance):
    count = 0
    for i in range(0, time):
        record = (time-i) * i
        if (record > distance):
            count += 1
    return count

print(currRecord(59688274, 543102016641022))