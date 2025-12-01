def parse_map(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


def find_starting_position(grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return (i, j, cell)  # Return the starting position and direction
    return None


def simulate_guard(grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    # Find the starting position and direction
    x, y, current_direction = find_starting_position(grid)

    visited_positions = set()
    visited_positions.add((x, y))  # Add starting position to visited

    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate the next position
        dx, dy = directions[current_direction]
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            break  # Guard leaves the map

        # Check if there's an obstacle in front
        if grid[nx][ny] == '#':
            # Turn right
            current_direction = turn_right[current_direction]
        else:
            # Move forward
            x, y = nx, ny
            visited_positions.add((x, y))  # Mark the position as visited

    return visited_positions


# Example usage
file_path = "/Users/mayaborkar/Desktop/Advent/2024/adventinput6.txt"  # Replace with your file path
grid = parse_map(file_path)
visited_positions = simulate_guard(grid)
print(len(visited_positions))  # Number of distinct positions visited
