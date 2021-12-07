def calculate_expression(my_expression):
    value = int(my_expression[0])
    for j in range(1, len(my_expression), 2):
        if my_expression[j] == "*":
            value = value * int(my_expression[j+1])
        elif current_expression[j] == "+":
            value = value + int(my_expression[j+1])
    return value


f1 = open("adventlist18.txt", "r")
homework = f1.read()
math_problems = homework.split("\n")
results = 0

for i in range(0, len(math_problems)):
    current_expression = math_problems[i].replace(" ", "").replace("(", "").replace(")", "")
    print(current_expression)
    results = results + calculate_expression(current_expression)
print(results)