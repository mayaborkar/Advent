import numpy as np


f1 = open("2024/adventinput2", "r")
mylist = f1.read().split('\n')

print(mylist)

'''
make sure each are differing by at most 3/ at least 1
all should be increasing
'''

def is_safe(sequence):
    sequence = sequence.split(" ")
    trend = None
    for i in range(1, len(sequence)):
        diff = int(sequence[i]) - int(sequence[i-1])
        
        # check if difference is between 1 and 3
        if not (1 <= abs(diff) <= 3): 
            return False
        
        # see if the first numbers are increasing or decreasing
        if trend is None:  
            if diff > 0:
                trend = "increasing"
            elif diff < 0:
                trend = "decreasing"
        
        # Check if all the numbers are either increasing or decreasing
        if (trend == "increasing" and diff < 0) or (trend == "decreasing" and diff > 0):
            return False
    
    return True

# Count safe reports
safe_reports = sum(is_safe(report) for report in mylist)

print(safe_reports)
