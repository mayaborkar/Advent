f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput4.txt", "r")
mylist = f1.read().split('\n')
print(mylist)

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check for "MAS" or "SAM"
    def is_mas_or_sam(sequence):
        return sequence == "MAS" or sequence == "SAM"

    # Iterate through the grid, treating each cell as the center of an X-MAS
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Check top-left to bottom-right diagonal
            diag1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]

            # Check bottom-left to top-right diagonal
            diag2 = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

            # If both diagonals form "MAS" or "SAM", it's an X-MAS
            if is_mas_or_sam(diag1) and is_mas_or_sam(diag2):
                count += 1

    return count

# Example grid
word_search = mylist

# Count X-MAS patterns in the grid
result = count_xmas(word_search)
print("Number of X-MAS patterns:", result)
