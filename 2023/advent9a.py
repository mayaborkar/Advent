from math import comb


def term(x, i, n):
    # binomial theorem/ poly interpolation
    # thinking of it as a polynomial
    # value * (number of value choose index --> the coefficient of the term) ^
    # (number of values -1 - index --> alternates signs)
    return x * comb(n, i) * (-1) ** (n - 1 - i)


def polynomial(nums):
    n = len(nums)
    # summing all of the terms which gives you the bigger polynomial
    return sum(term(nums[i], i, n) for i in range(n))


f1 = open('adventinput9')
mylist = [[int(num) for num in line.strip().split()] for line in f1.readlines()]

expo_value = sum(polynomial(nums) for nums in mylist)

print(expo_value)
