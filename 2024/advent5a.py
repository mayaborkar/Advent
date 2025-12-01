def parse_input_simple(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')  # Split all lines into a list

    # Separate rules and updates
    divider_index = lines.index('')  # Find the blank line dividing rules and updates
    rules = [line.split('|') for line in lines[:divider_index] if line]
    updates = [line.split(',') for line in lines[divider_index + 1:] if line]

    # Convert all rules and updates to integers
    rules = [[int(x), int(y)] for x, y in rules]
    updates = [[int(x) for x in update] for update in updates]

    return rules, updates

def is_update_valid(update, rules):
    # Create a set of pages in the current update
    pages_in_update = set(update)

    # Filter rules to include only those relevant for the current update
    filtered_rules = [rule for rule in rules if rule[0] in pages_in_update and rule[1] in pages_in_update]

    # Validate order of pages in the update using the filtered rules
    for before, after in filtered_rules:
        if update.index(before) > update.index(after):
            return False  # Rule is violated
    return True

def find_middle_sum(rules, updates):
    total = 0

    for update in updates:
        if is_update_valid(update, rules):
            # Find the middle page number
            middle_index = len(update) // 2
            total += update[middle_index]

    return total

# Example usage
file_path = "/Users/mayaborkar/Desktop/Advent/2024/adventinput5.txt"  # Replace with your file path
rules, updates = parse_input_simple(file_path)
result = find_middle_sum(rules, updates)
print(result)
