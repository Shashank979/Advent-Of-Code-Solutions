from itertools import permutations
file_name = 'input_problem7.txt'
'''
CLEAN THIS SHIT UP
'''
class Computer:
    def __init__(self, phase_setting):
        self.memory = [int(x) for x in open(file_name).read().split(",")]
        self.instruction_pointer = 0
        self.current_instruction = []
        self.halt = False 
        self.output_value = 0 
        self.phase_setting = phase_setting
        self.final_loop = False 

        self.input_value = None
        self.input_counter = 0 

    def run_instruction(self):
        first_instruction = self.memory[self.instruction_pointer]
        #print(first_instruction)
        # opcode input 
        if first_instruction == 3:
            output_address = self.memory[self.instruction_pointer + 1]
            # deciding whether to do phase setting or input value 
            if self.input_counter == 0:
                self.memory[output_address] = self.phase_setting
                self.input_counter += 1
                # setting instruction pointer 
                self.instruction_pointer += 2
            elif self.input_counter == 1:
                self.memory[output_address] = self.input_value
                self.input_counter += 1
                # setting instruction pointer 
                self.instruction_pointer += 2
            else:
                self.halt = True 
                self.input_counter = 1
    

        # opcode output 
        elif int(str(first_instruction)[-1]) == 4:
            # position ? 
            if len(str(first_instruction)) == 1:
                output_address = self.memory[self.instruction_pointer + 1]
                #print(self.memory[output_address])
                self.output_value = self.memory[output_address]
                self.instruction_pointer += 2
            # immediate ? 
            elif len(str(first_instruction)) == 3:
                #print(self.memory[self.instruction_pointer + 1])
                self.output_value = self.memory[self.instruction_pointer + 1]
                self.instruction_pointer += 2
            # error 
            else: 
                print("ERROR IN OPCODE 4")

        # opocode halt 
        elif first_instruction == 99:
            self.halt = True 
            self.final_loop = True 
            # testing 
            #print(self.memory)

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

        # opcode 5 
        elif int(str(first_instruction)[-1]) == 5:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            #print("Value1: ", value1)
            #print("Value2: ", value2)
            if value1 != 0:
                self.instruction_pointer = value2
            else:
                self.instruction_pointer += 3

        # opcode 6
        elif int(str(first_instruction)[-1]) == 6:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            if value1 == 0:
                self.instruction_pointer = value2
            else:
                self.instruction_pointer += 3

        # opcode 7
        elif int(str(first_instruction)[-1]) == 7:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            if value1 < value2: 
                self.memory[value3] = 1
            else:
                self.memory[value3] = 0
            self.instruction_pointer += 4

        # opcode 8
        elif int(str(first_instruction)[-1]) == 8:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            if value1 == value2: 
                self.memory[value3] = 1
            else:
                self.memory[value3] = 0
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

    def reset_computer(self):
        self.memory = [int(x) for x in open(file_name).read().split(",")]
        self.instruction_pointer = 0
        self.current_instruction = []
        self.halt = False 
        self.second_input = False
        self.input_value = None

    def set_input(self, input_value):
        self.input_value = input_value

    def run_program(self):
        while not self.get_halt():
            self.run_instruction()
        self.halt = False 

def main():
    list_amplifier_sequences = list(permutations(range(5, 10), 5))
    
    thruster_signals = []
    for amp_sequence in list_amplifier_sequences:
        amp_computers = [Computer(x) for x in amp_sequence] 
        first_one = True 
        while not amp_computers[4].final_loop:
            for index, amp in enumerate(amp_computers):
                # running the program 
                if first_one:
                    input_value = 0
                    first_one = False 
                else:
                    if index == 0:
                        input_value = amp_computers[4].output_value
                    else:
                        input_value = amp_computers[index - 1].output_value 
                amp.set_input(input_value)
                amp.run_program()

                # final loop processing 
                if index == 4 and amp.final_loop:
                    thruster_signals.append(amp.output_value)

    # returning max signal 
    max_thruster_signal = max(thruster_signals)
    return max_thruster_signal

print(main())