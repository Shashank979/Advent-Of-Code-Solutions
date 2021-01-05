import sys 

def main():
    file1 = 'input_problem8.txt'
    input_file = open(file1).read().splitlines()
    list_changes = []
    for index, line in enumerate(input_file):
        if line.split(" ")[0] == "nop" or line.split(" ")[0] == "jmp":
            list_changes.append(index)
    #print(input_file)
    for num in list_changes:
        a, b = test_func(num, input_file.copy())
        if b == "caught":
            print(a)
            sys.exit()

def test_func(num, instructions):
    if instructions[num].split(" ")[0] == "nop":
        instructions[num] = "jmp" + " " + instructions[num].split(" ")[1]
    elif instructions[num].split(" ")[0] == "jmp":
        instructions[num] = "nop" + " " + instructions[num].split(" ")[1]
    acc = 0
    current_instruction = 0
    positions_visited = []
    while current_instruction not in positions_visited:
        positions_visited.append(current_instruction)
        try:
            instruction = instructions[current_instruction]
        except:
            return acc, "caught"
        ins = instruction.split(" ")
        if ins[0] == "nop":
            current_instruction += 1
        
        elif ins[0] == "acc":
            current_instruction += 1
            acc += int(ins[1])
        elif ins[0] == "jmp":
            current_instruction += int(ins[1])
    return acc, "failed"

main()