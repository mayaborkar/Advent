f1 = "adventinput8.txt"
# mylist = f1.read()
digitsOutput =[]

for x in open(f1):
    digits1, digits2 = x.strip().replace('\n','').split('|')
    digitsOutput.append(digits2.strip().split(' '))
print(digitsOutput)

oneCount = 0
fourCount = 0
sevenCount = 0
eightCount = 0

for i in range(0, len(digitsOutput)):
    for j in range(0, len(digitsOutput[i])):
        if len(digitsOutput[i][j]) == 2:
            oneCount += 1
        if len(digitsOutput[i][j]) == 4:
            fourCount += 1
        if len(digitsOutput[i][j]) == 3:
            sevenCount += 1
        if len(digitsOutput[i][j]) == 7:
            eightCount += 1

print(oneCount + fourCount + sevenCount + eightCount)
