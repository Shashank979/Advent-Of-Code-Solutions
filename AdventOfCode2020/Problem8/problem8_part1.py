def main():
    positions_visited = []
    file1 = 'input_problem8.txt'
    input_file = open(file1).read().splitlines()
    print(input_file)
    current_instruction = 0
    acc = 0 
    while current_instruction not in positions_visited:
        positions_visited.append(current_instruction)
        instruction = input_file[current_instruction]
        ins = instruction.split(" ")
        if ins[0] == "nop":
            current_instruction += 1
        
        elif ins[0] == "acc":
            current_instruction += 1
            acc += int(ins[1])
        elif ins[0] == "jmp":
            current_instruction += int(ins[1])
    print(acc)  

main()
