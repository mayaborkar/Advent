f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput3.txt", "r")
mylist = f1.read().split('\n')
print(mylist)

import re

def calculate_mul_sum(corrupted_memory_list):
    # Regular expression to match valid mul instructions
    # Format: "mul(X,Y)" where X and Y are any valid integers (of any length)
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Initialize total sum of results
    total = 0

    # Process each corrupted memory string in the list
    for corrupted_memory in corrupted_memory_list:
        # Find all valid mul instructions in the current string
        matches = re.findall(pattern, corrupted_memory)
        
        # Process each match
        for x, y in matches:
            result = int(x) * int(y)  # Convert numbers and multiply
            total += result           # Add to total sum
    
    return total
corrupted_memory_list = mylist

# Calculate the sum of all valid mul instructions
total_sum = calculate_mul_sum(corrupted_memory_list)
print("Total sum of valid mul instructions:", total_sum)
