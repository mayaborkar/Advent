def find_lowest_house(target):
    limit = target // 11  # A rough estimate to limit the search space
    presents = [0] * (limit + 1)

    for elf in range(1, limit + 1):
        houses_visited = 0
        for house in range(elf, limit + 1, elf):
            if houses_visited < 50:
                presents[house] += elf * 11
                houses_visited += 1
            else:
                break

    for house_number, total_presents in enumerate(presents):
        if total_presents >= target:
            return house_number

    return None

# Puzzle input
target = 33100000
result = find_lowest_house(target)
print("The lowest house number to receive at least {target} presents is: {result}")
