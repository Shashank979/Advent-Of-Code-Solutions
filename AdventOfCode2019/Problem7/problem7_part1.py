from itertools import permutations
file_name = 'input_problem7.txt'

class Computer:
    def __init__(self):
        self.memory = [int(x) for x in open(file_name).read().split(",")]
        self.instruction_pointer = 0
        self.current_instruction = []
        self.halt = False 
        self.output_value = 0 

        self.second_input = False
        self.input_value = None

    def run_instruction(self):
        #print(self.memory)
        first_instruction = self.memory[self.instruction_pointer]
        #print(first_instruction)

        # opcode input 
        if first_instruction == 3:
            output_address = self.memory[self.instruction_pointer + 1]
            # deciding whether to do phase setting or input value 
            if self.second_input:
                self.memory[output_address] = self.input_value
                #print("INPUT VALUE: ", self.input_value)
            else:
                self.memory[output_address] = self.phase_setting
            self.second_input = True 
            # setting instruction pointer 
            self.instruction_pointer += 2

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

    def set_inputs(self, phase_setting, input_value):
        self.phase_setting = phase_setting
        self.input_value = input_value

    def run_program(self):
        while not self.get_halt():
            self.run_instruction()

def main():
    list_amplifier_sequences = list(permutations([0,1,2,3,4], 5))
    thruster_signals = []
    #intcode_computer = Computer()
    for amp_sequence in list_amplifier_sequences:
        #print("---------------------------" + str(amp_sequence) + "---------------------------")
        intcode_computer = Computer()
        for index, phase_setting in enumerate(amp_sequence):
            #print("OUTPUT VALUE: ", intcode_computer.output_value)
            intcode_computer.set_inputs(phase_setting, intcode_computer.output_value)
            intcode_computer.run_program()
            # appending thruster signal if on last phase setting 
            if index == 4:
                thruster_signals.append(intcode_computer.output_value)
            # resetting computer 
            intcode_computer.reset_computer()
    max_thruster_signal = max(thruster_signals)
    return max_thruster_signal

print(main())