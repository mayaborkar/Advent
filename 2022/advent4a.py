mylist = open("adventinput4", "r").read().splitlines()


t = 0


for i in mylist:

    front, back = i.split(",")

    frontfront, frontfrontfront = [int(r) for r in front.split("-")]
    backback, backbackback = [int(r) for r in back.split("-")]


    if (frontfront <= backback and frontfrontfront >= backbackback ) or (backback<=frontfront and backbackback>=frontfrontfront):
        t+=1


print(t)