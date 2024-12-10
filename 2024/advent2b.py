import numpy as np

# Read and process the input file
with open("2024/adventinput2", "r") as f1:
    data = f1.read().strip().split('\n')

# Convert each report into a list of integers
mylist = []
for line in data:
    if line.strip():  # Ignore empty lines
        mylist.append(list(map(int, line.split())))

print("Processed Reports:", mylist)

def isSafe(sequence):
    """
    Checks if a sequence is inherently safe.
    A report is safe if:
      - The levels are either all increasing or all decreasing.
      - Any two adjacent levels differ by at least 1 and at most 3.
    """
    trend = None  # Determines if the sequence is increasing or decreasing
    
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]  # Elements are integers
        
        # Check if the difference is valid (between 1 and 3)
        if not (1 <= abs(diff) <= 3):
            return False

        # Establish the trend (increasing or decreasing) if not already set
        if trend is None:
            if diff > 0:
                trend = "increasing"
            elif diff < 0:
                trend = "decreasing"

        # Validate consistency with the trend
        if (trend == "increasing" and diff < 0) or (trend == "decreasing" and diff > 0):
            return False

    return True

def isSafeWithDamper(sequence):
    """
    Checks if a report is safe by either:
      - Being inherently safe.
      - Becoming safe after ignoring one "bad" level.
    """
    if isSafe(sequence):
        return True  # Already safe

    # Try removing each level to see if the sequence becomes safe
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i+1:]  # Remove the ith level
        if isSafe(modified_sequence):  # Check if the modified sequence is safe
            return True

    return False

# Count safe reports
safeReports = sum(isSafeWithDamper(report) for report in mylist)

print(f"Number of safe reports: {safeReports}")
