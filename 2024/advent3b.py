import re

f1 = open("/Users/mayaborkar/Desktop/Advent/2024/adventinput3.txt", "r")
mylist = f1.read().split('\n')
print(mylist)

def calculate_mul_sum(corrupted_memory_list):
    # Regular expression to match valid mul, do, and don't instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"
    
    # Initialize state and total sum
    mul_enabled = True  # mul instructions start enabled
    total = 0

    # Process each corrupted memory string
    for corrupted_memory in corrupted_memory_list:
        # Split memory string into components
        components = re.split(r"(?<=\))", corrupted_memory)  # Split at closing parenthesis
        
        for component in components:
            # Check for do() or don't() instructions
            control_match = re.search(control_pattern, component)
            if control_match:
                if control_match.group() == "do()":
                    mul_enabled = True
                elif control_match.group() == "don't()":
                    mul_enabled = False
                continue
            
            # Check for valid mul instructions if enabled
            if mul_enabled:
                mul_match = re.search(mul_pattern, component)
                if mul_match:
                    x, y = map(int, mul_match.groups())  # Extract numbers and convert to integers
                    total += x * y  # Add the product to the total sum

    return total

# Example usage:
corrupted_memory_list = mylist

# Calculate the sum of all valid mul instructions
total_sum = calculate_mul_sum(corrupted_memory_list)
print("Total sum of valid mul instructions:", total_sum)
