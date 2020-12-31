f1 = open("adventlist8a.txt", "r")
gaming = f1.read()
instruction_set = []
instruction = []
instruction_set = gaming.split("\n")
for i in range(0, len(instruction_set)):
    instruction.append(instruction_set[i].split(" "))
# print(instruction)
accumulator = 0
instruction_index = 0
while instruction[instruction_index][0] != "RM":
    if instruction[instruction_index][0] == "acc":
        print(instruction[instruction_index][1])
        accumulator = accumulator + int(instruction[instruction_index][1])
        instruction[instruction_index][0] = "RM"
        instruction_index = instruction_index + 1
    elif instruction[instruction_index][0] == "nop":
        instruction[instruction_index][0] = "RM"
        instruction_index = instruction_index + 1
    elif instruction[instruction_index][0] == "jmp":
        instruction[instruction_index][0] = "RM"
        instruction_index = instruction_index + int(instruction[instruction_index][1])
print(accumulator)

