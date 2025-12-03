'''
Set total to 0

For each bank (each string of digits) in the list:

    Set best to -1

    For every position i in the bank:

        Let digit1 = digit at position i

            For every position j after i (so j = i+1 to end):

                Let digit2 = digit at position j

                Form the two-digit value: value = digit1 * 10 + digit2

            If value is greater than best, update best to value

    Add best to total
'''
f1 = open("2025/adventinput3", "r")

mylist = [line.strip() for line in f1 if line.strip()]


total = 0

for bank in mylist:
    best = -1

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            value = int(bank[i]) * 10 + int(bank[j])
            if value > best:
                best = value

    total += best

print(total)
