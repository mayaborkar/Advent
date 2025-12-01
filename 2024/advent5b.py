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


def correct_update(update, rules):
    # Create a set of pages in the current update
    pages_in_update = set(update)

    # Filter rules to include only those relevant for the current update
    filtered_rules = [rule for rule in rules if rule[0] in pages_in_update and rule[1] in pages_in_update]

    # Use a topological sort to determine the correct order of pages
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and in-degree count
    for before, after in filtered_rules:
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0

    # Perform topological sort (Kahn's Algorithm)
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Ensure only pages in the update are included, preserving the original order
    sorted_update = [page for page in sorted_update if page in update]

    return sorted_update


def find_middle_sum_of_corrected_updates(rules, updates):
    total = 0

    for update in updates:
        if not is_update_valid(update, rules):
            # Correct the update
            corrected_update = correct_update(update, rules)

            # Find the middle page number
            middle_index = len(corrected_update) // 2
            total += corrected_update[middle_index]

    return total


# Example usage
file_path = "/Users/mayaborkar/Desktop/Advent/2024/adventinput5.txt"  # Replace with your file path
rules, updates = parse_input_simple(file_path)
result = find_middle_sum_of_corrected_updates(rules, updates)
print(result)
