f1 = open("adventinput3", "r")
inputlist = f1.readlines()

for i in range(0, len(inputlist)):
    # check if it is next to/diagonal to a viable symbol
    # add all of the viable numbers *10^# the place that they are in