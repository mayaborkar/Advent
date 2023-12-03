f1 = open("advent2input.txt", "r")
inputlist = f1.readlines()

gameId = [c.replace('\n', '').split(': ') for c in inputlist]

total = 0
red = 12
green = 13
blue = 14

for i in range (0,len(gameId)):
    redCount=0
    greenCount=0
    blueCount=0
    possible = True

    gameId[i][0] = int(gameId[i][0].replace('Game ', ''))
    gamearr1 = gameId[i][1].split(';')
    gamearr2 = [c.split(',') for c in gamearr1]

    for x in gamearr2:
        for c in x:
            if c.__contains__('blue'):
                # bx += int(c.replace("blue",""))
                if int(c.replace("blue","")) > blue:
                    possible=False
            elif c.__contains__('red'):
                # rx += int(c.replace("red",""))
                if int(c.replace("red","")) > red:
                    possible=False
            elif c.__contains__('green'):
                # gx += int(c.replace("green",""))
                if int(c.replace("green","")) > green:
                    possible=False
            if not possible:
                break
        if not possible:
            break
    if possible:
        total += gameId[i][0]
        print(gameId[i][0], gamearr2)
        print("adding to total ", total)
    else:
        print('Not possible ', gameId[i][0], gamearr2)

print(total)