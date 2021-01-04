# https://adventofcode.com/2020/day/9
def comparing_lists(list1, list2):
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j] and i != j:
                print(list1[i])
                print(list2[j])
                return "Yes"
    return 'No'


# main
f1 = open("adventlist9.txt", "r")
encoding = f1.readlines()
for i in range(0, len(encoding)):
    encoding[i] = int(encoding[i].replace("\n", ''))
# replace 26
print (encoding)
for j in range(25, len(encoding)):
    diff_array = []
    for k in range(j - 25,j):
        diff_array.append(encoding[j] - encoding[k])
    print(encoding[j])
    print(encoding[j - 25:j])
    print(diff_array)
    if comparing_lists(diff_array, encoding[j - 25:j]) == "Yes":
        print("Found")
        del diff_array
    else:
        print("Not found")
        print(encoding[j])
        break
