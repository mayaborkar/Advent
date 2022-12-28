# start at 0 go as long as u can (up to 4 characters) before finding a duplicate
# if the marker is found (4 characters in a row with no duplicate) --> return the index

f1 = open("adventinput6", "r")
myinputlist = f1.read()
print(myinputlist)
marker = ""
counter = 0
winCount = 0
for i in range(0, len(myinputlist)):
    winCount = 0
    marker = myinputlist[i:i+14]
    print("marker " + marker)
    for x in marker:
        counter = marker.count(x)
        print("count " + str(counter))
        if counter > 1:
            break
        elif (counter == 1):
            winCount += 1
            print("winCount " + str(winCount))
            # break
    if(winCount == 14):
        print(i + 14)
        break


