def nextValue(input):
    arr = []
    for i in range(0, len(input) - 1):
        print("here")
        print(arr)
        arr.append(int(input[i + 1]) - int(input[i]))
    return(arr)


f1 = open("adventinput9", "r")
mylist = [cx.split(" ") for cx in f1.read().split("\n")]
print(mylist)
nextValue(mylist[0])
'''
find the differences between each of the values of the input array

'''