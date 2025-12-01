f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput10.txt", "r")
mylist = f1.read().split('\n')
print(mylist)

def find_trailhead_ratings(map_input):
    rows, cols = len(map_input), len(map_input[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Convert input into a 2D grid of integers
    grid = [[int(height) for height in row] for row in map_input]

    def is_valid(x, y):
        """Check if a position is within grid boundaries."""
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y):
        # Base case: if the current position is height 9, it's a valid trail end
        if grid[x][y] == 9:
            return 1

        # Recursive case: explore all valid neighbors
        return sum(
            dfs(x + dx, y + dy)
            for dx, dy in directions
                if is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == grid[x][y] + 1
        )


    # Find all trailheads (height 0) and calculate ratings
    total_rating = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:  # Trailhead found
                total_rating += dfs(i, j)

    return total_rating 


# Input in the specified format
topographic_map = mylist

# Calculate and print the result
result = find_trailhead_ratings(topographic_map)
print("Sum of trailhead ratings:", result)


#1289