# https://adventofcode.com/2020/day/6
f1 = open("adventlist6.txt", "r")
ticket = f1.read()
groups = ticket.split("\n\n")
# print(groups)
questions = []
for i in range(0, len(groups)):
    questions.append(groups[i].replace("\n", ''))
# print(questions)
# for j in range(0, questions[3]):
print(questions[0])
print(len(questions[0]))
number_questions = 0
for j in range(0, len(questions)):
    while questions[j]:
        questions[j] = questions[j][1:].replace(questions[j][0], '')
        number_questions = number_questions + 1
        print(questions[j])
print(number_questions)