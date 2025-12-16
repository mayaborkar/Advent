f1 = open("2025/adventinput3", "r")
mylist = [line.strip() for line in f1 if line.strip()]

total = 0
batteries = 12 

for bank in mylist:
    stack = []
    remove = len(bank) - batteries

    for digit in bank:
        while stack and remove > 0 and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)

    stack = stack[:batteries]

    best = int("".join(stack))
    total += best

print(total)
