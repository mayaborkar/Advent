f1 = open("adventinput8.txt", "r")
mylist = f1.read()


digits = mylist.replace('\n', '').split('|')
print(digits)