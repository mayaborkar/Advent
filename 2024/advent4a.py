f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput4.txt", "r")
mylist = f1.read().split('\n')
print(mylist)


def count_xmas_occurrences(grid):
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # The word to search for
    word = "XMAS"
    word_length = len(word)
    
    # Directions: (row step, col step)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]
    
    # Function to check if the word starts at a specific position in a specific direction
    def matches_from_position(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True
    
    # Count all occurrences
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if matches_from_position(r, c, dr, dc):
                    count += 1
                    
    return count

# Example word search grid
grid = mylist

# Convert the grid into a list of lists (optional step for clarity)
grid = [list(row) for row in grid]

# Count the occurrences of "XMAS"
result = count_xmas_occurrences(grid)
print("Total occurrences of XMAS:", result)
