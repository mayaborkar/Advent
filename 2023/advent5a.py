def findLocation(arr, s1):
    if (arr[0][1] <= s1 and s1 < arr[0][1] + arr[0][2]):
        sx = s1 - arr[0][1] + arr[0][0]
    elif (arr[1][1] <= s1 and s1 < arr[1][1] + arr[1][2]):
        sx = s1 - arr[1][1] + arr[1][0]
    else:
        sx = s1
    return sx


f1 = open("adventinput5", "r")
mylist = f1.read().split('\n')
print(mylist)