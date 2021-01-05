'''
gotta clean it up a tad 
'''

class Computer:
    def __init__(self):
        self.memory = [int(x) for x in open('input_problem5.txt').read().split(",")]
        self.instruction_pointer = 0
        self.current_instruction = []
        self.halt = False 

    def run_instruction(self):
        first_instruction = self.memory[self.instruction_pointer]

        # opcode input 
        if first_instruction == 3:
            input_value = int(input("Enter Input: "))
            output_address = self.memory[self.instruction_pointer + 1]
            self.memory[output_address] = input_value
            self.instruction_pointer += 2

        # opcode output 
        elif int(str(first_instruction)[-1]) == 4:
            if len(str(first_instruction)) == 1:
                output_address = self.memory[self.instruction_pointer + 1]
                print(self.memory[output_address])
                self.instruction_pointer += 2
            elif len(str(first_instruction)) == 3:
                print(self.memory[self.instruction_pointer + 1])
                self.instruction_pointer += 2
            else: 
                print("ERROR IN OPCODE 4")
            # need to account for fact that it can be like 401 

        # opocode halt 
        elif first_instruction == 99:
            self.halt = True 

        # opcode addition
        elif int(str(first_instruction)[-1]) == 1:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            self.memory[value3] = value1 + value2
            self.instruction_pointer += 4

        # opcode multiplication 
        elif int(str(first_instruction)[-1]) == 2:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            self.memory[value3] = value1 * value2
            self.instruction_pointer += 4

    def get_values(self, instruction):
        # editing instruction so easy to read 
        for num in range(4 - len(instruction)):
            instruction.insert(0, 0)

        # getting value1
        # position mode 
        if instruction[-3] == 0:   
            address1 = self.memory[self.instruction_pointer + 1]
            value1 = self.memory[address1]
        # immediate mode
        elif instruction[-3] == 1:  
            value1 = self.memory[self.instruction_pointer + 1]
        else:
            print("ERROR")

        # getting value2
        # position mode 
        if instruction[-4] == 0:   
            address2 = self.memory[self.instruction_pointer + 2]
            value2 = self.memory[address2]
        # immediate mode
        elif instruction[-4] == 1:  
            value2 = self.memory[self.instruction_pointer + 2]
        else:
            print("ERROR")

        # returning both values 
        return value1, value2 

    def get_halt(self):
        return self.halt 

def main():
    intcode_computer = Computer()
    
    # running problem 5
    # do something like this: while computer_finished 
    while not intcode_computer.get_halt():
        intcode_computer.run_instruction()

main()