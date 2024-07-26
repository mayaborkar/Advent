def find_lowest_house(target):
    limit = target
    presents = [0] * (limit // 10 + 1)

    for elf in range(1, limit // 10 + 1):
        for house in range(elf, limit // 10 + 1, elf):
            presents[house] += elf * 10

#keeps track of the number of iterations
    for house_number, total_presents in enumerate(presents):
        if total_presents >= limit: 
            return house_number

    return None
 
# Puzzle input
target = 33100000
result = find_lowest_house(target)
print(f"The lowest house number to receive at least {target} presents is: {result}")
