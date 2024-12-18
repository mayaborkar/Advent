f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput10.txt", "r")
mylist = f1.read().split('\n')
print(mylist)

def find_trailhead_scores(map_input):
    rows, cols = len(map_input), len(map_input[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Convert input into a 2D grid of integers
    grid = [[int(height) for height in row] for row in map_input]

    def is_valid(x, y):
        """Check if a position is within grid boundaries."""
        return 0 <= x < rows and 0 <= y < cols

    def bfs(start_x, start_y):
        """Perform BFS to find all reachable height-9 positions."""
        queue = [(start_x, start_y)]
        visited = set()
        reachable_nines = set()

        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # If current position is height 9, add to reachable set
            if grid[x][y] == 9:
                reachable_nines.add((x, y))
                continue  # Stop further exploration from height 9

            # Explore neighbors with height exactly +1
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    if grid[new_x][new_y] == grid[x][y] + 1:
                        queue.append((new_x, new_y))

        return len(reachable_nines)

    # Find all trailheads (height 0) and calculate scores
    total_score = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:  # Trailhead found
                total_score += bfs(i, j)

    return total_score


# Input in the specified format
topographic_map = mylist

# Calculate and print the result
result = find_trailhead_scores(topographic_map)
print("Sum of trailhead scores:", result)

