def parse_map(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def find_starting_position(grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return (i, j, cell)  # Return starting position and direction
    return None


def simulate_guard(grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    x, y, direction = find_starting_position(grid)
    visited = set()  # Track (x, y, direction) to detect loops
    rows, cols = len(grid), len(grid[0])

    while True:
        state = (x, y, direction)
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        # Check bounds
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            return False  # Guard leaves the map

        # Check for an obstacle
        if grid[nx][ny] == '#':
            direction = turn_right[direction]
        else:
            x, y = nx, ny


def find_loop_positions(grid):
    rows, cols = len(grid), len(grid[0])
    loop_positions = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != '.':  # Only consider empty positions
                continue

            # Skip starting position
            start_x, start_y, _ = find_starting_position(grid)
            if (x, y) == (start_x, start_y):
                continue

            # Temporarily place an obstruction
            grid[x][y] = '#'
            if simulate_guard(grid):
                loop_positions += 1
            grid[x][y] = '.'  # Remove the obstruction

    return loop_positions


# Example usage
file_path = "/Users/mayaborkar/Desktop/Advent/2024/adventinput6.txt"  # Replace with your file path
grid = parse_map(file_path)
result = find_loop_positions(grid)
print(result)  # Number of valid obstruction positions
