f1 = open("adventlist13sample.txt", "r")
bus = f1.readlines()
working_bus = []
for i in range(0, len(bus)):
    working_bus.append(bus[i].replace("\n", '').replace(",x", ''))
bus_number = working_bus[1].split(",")
bus_time = working_bus[0]
waiting_mins = []
for j in range(0, len(bus_number)):
    multiple = int(bus_time) % int(bus_number[j])
    waiting_mins.append(int(bus_number[j]) - multiple)
min_x = 0
for k in range(0, len(waiting_mins)):
    if waiting_mins[k] < waiting_mins[min_x]:
        min_x = k
print(min_x)
print(bus_number[min_x])
print(waiting_mins[min_x])
print(int(bus_number[min_x]) * int(waiting_mins[min_x]))
