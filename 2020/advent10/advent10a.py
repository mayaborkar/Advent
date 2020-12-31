f1 = open("adventlist10a.txt", "r")
adapter = f1.readlines()
adapter_charge = []
for i in range(0, len(adapter)):
    adapter_charge.append(int(adapter[i].replace("\n", '')))
print(adapter_charge)
counter_1 = 0
counter_3 = 0
adapter_charge.sort()
print(adapter_charge)
for j in range(0, len(adapter_charge)-1):
    print(adapter_charge[j])
    print(adapter_charge[j+1])
    if abs(adapter_charge[j] - adapter_charge[j+1]) == 1:
        counter_1 = counter_1 + 1
    elif abs(adapter_charge[j] - adapter_charge[j+1]) == 3:
        counter_3 = counter_3 + 1
print(counter_1)
print(counter_3)
print((counter_3 + 1) * (counter_1+1))
